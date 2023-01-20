from other.UDKClass import UDKList
from other.ParseClass import Parsing
from forms.MainForm.MainClass import MainWindowClass
from PyQt5.QtWidgets import QApplication


URL_TEMPLATE = "https://www.teacode.com/online/udc/index.html"


def main():
    import sys
    headers = ["Код УДК", "Описание", "Число кодов", "Ссылка на следующий"]
    file_name = "file_name.json"
    broken_links_file = "add_info/broken_links.txt"
    all_links = "add_info/all_links.txt"
    udk_ins = UDKList()
    parser = Parsing()

    udk_ins.load_from_file(file_name)
    udk_ins.structurize_loaded_data()
    
    app = QApplication(sys.argv)
    MainWindow = MainWindowClass(headers, udk_ins.get_udk_list())
    MainWindow.show()
    sys.exit(app.exec_())

    # parser.get_all_pages(udk_ins.udk_list, URL_TEMPLATE)
    # parser.save_broken_links(broken_links_file)
    # parser.save_all_links(all_links)
    # udk_ins.set_codes_amount()
    
    # udk_ins.save_to_file(file_name)
    # udk_ins.print_udk()
    # udk_ins.udk_list.clear()
    # udk_ins.print_udk()


if __name__ == "__main__":
    main()