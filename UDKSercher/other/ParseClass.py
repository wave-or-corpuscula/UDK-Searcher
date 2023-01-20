import requests
from bs4 import BeautifulSoup as bs 
from .UDKClass import UDK
from .functions import delete_to_first_char, is_udk_index
from .ErrorClass import CustomErrors


class Parsing:

    def __init__(self):
        self.parse_depth = None
        self.depth_count = 0
        self.codes_amount = 0
        self.broken_links = []
        self.all_links = []

    def get_page(self, udk_list: list, CUR_URL: str):
        self.all_links.append(CUR_URL)
        r = requests.get(CUR_URL)
        if r.status_code != 200:
            raise CustomErrors(f"Problems in access to site! << {CUR_URL} >>, status_code: {r.status_code}")
        soup = bs(r.text, "lxml")
        try:
            table = soup.find("table").find("table").find_all("tr")
        except Exception:
            raise CustomErrors("Fucking broken site!!!")

        for tag in table:
            td = tag.find_all("td")

            try:
                next_reference = td[0].find("a")
                if next_reference is not None:
                    next_reference = next_reference.get("href")
                
                udk_code = td[0].find("font").text
                if not is_udk_index(udk_code):
                    raise Exception
                description = str(td[1].string).replace('\n', '').replace('\r', '')
                codes_amount = td[2].text
                udk_list.append(UDK(udk_code, description, codes_amount, next_reference))
            except Exception:
                continue    

    def get_all_pages(self, udk_sublist: list, cur_url: str, parse_depth : int = None):
        if parse_depth is not None:
            if parse_depth == 0:
                raise CustomErrors("Too deep!")
        print(cur_url)
        try:
            self.get_page(udk_sublist, cur_url)
        except CustomErrors as e:
            self.broken_links.append(e.get_message())
            print(e.get_message())
            return

        for item in udk_sublist:
            if item.next_reference is not None:
                try:
                    if parse_depth is not None:
                        self.get_all_pages(item.udk_sublist, delete_to_first_char(cur_url, "/") + 
                        delete_to_first_char(item.next_reference, "/", del_border=True, from_end=False), parse_depth - 1)    
                    else:
                        self.get_all_pages(item.udk_sublist, delete_to_first_char(cur_url, "/") + 
                        delete_to_first_char(item.next_reference, "/", del_border=True, from_end=False))
                except CustomErrors as e:
                    continue

    def save_all_links(self, file_name: str):
        with open(file_name, "w") as file:
            file.write(f"Total links amount: {len(self.all_links)}\n")
            file.write("\n".join(self.all_links))

    def save_broken_links(self, file_name: str):
        if len(self.broken_links) == 0:
            print("No broken links!!!)))")
            return
        with open(file_name, "w") as file:
            file.write("\n".join(self.broken_links))
            print("There are few broken links!!!(((")
