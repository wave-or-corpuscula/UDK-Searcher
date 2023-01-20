import json

class UDK:

    def __init__(self, udk_code: str, description: str, codes_amount: int, next_reference: str):
        self.codes_on_page = int()
        self.udk_code = udk_code
        self.description = description
        self.codes_amount = codes_amount
        self.next_reference = next_reference
        self.udk_sublist = []

    def __str__(self):
        return f"{self.udk_code}, {self.description}, {self.codes_amount} | {self.next_reference} | {self.codes_on_page};"


class UDKList:

    def __init__(self):
        self.udk_list = []
        self.data = []
        self.start_index = 0

    def set_codes_amount_private(self, sublist):
        for item in sublist:
            item.codes_on_page = len(sublist)
        for item in sublist:
            if item.next_reference is not None:
                self.set_codes_amount_private(item.udk_sublist)
    
    def set_codes_amount(self):
        self.set_codes_amount_private(self.udk_list)

    def print_udk(self):
        self.print_udk_private(self.udk_list)

    def print_udk_private(self, sublist: list):
        for item in sublist:
            print(item)
        for item in sublist:
            if item.next_reference is not None:
                self.print_udk_private(item.udk_sublist)

    def get_data_private(self, sublist: list):
        for item in sublist:
            self.data.append(
                    {
                        "Код УДК": item.udk_code,
                        "Описание": item.description,
                        "Число кодов": item.codes_amount,
                        "Ссылка на следующий": item.next_reference,
                        "Число кодов на текущей странице": item.codes_on_page
                    }
                )
        for item in sublist:
            if item.next_reference is not None:
                self.get_data_private(item.udk_sublist)

    def get_data(self):
        self.get_data_private(self.udk_list)
        return self.data

    def get_udk_list(self):
        return self.udk_list
    
    def save_to_file(self, file_name: str):
        with open(file_name, "w") as file:
            json.dump(self.get_data(), file)
            print(f"Data have saved to {file_name} file!")

    def load_from_file(self, file_name: str):
        with open(file_name, "r") as file:
            self.data = json.load(file)
            print(len(self.data))
            print(f"Data have loaded from {file_name} file!")

    def structurize_loaded_data(self):
        self.start_index = 0
        self.structurize_loaded_data_private(self.udk_list)

    def structurize_loaded_data_private(self, sublist: list):
        try:
            end_index = self.data[self.start_index]["Число кодов на текущей странице"] + self.start_index
        except IndexError:
            return
        for i in range(self.start_index, end_index):
            self.start_index += 1
            sublist.append(UDK(udk_code=self.data[i]["Код УДК"],
                            description=self.data[i]["Описание"],
                            codes_amount=self.data[i]["Число кодов"],
                            next_reference=self.data[i]["Ссылка на следующий"]))
        for item in sublist:
            if item.next_reference is not None:
                self.structurize_loaded_data_private(item.udk_sublist)
