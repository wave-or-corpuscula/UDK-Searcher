from .MainFormClass import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget
# from other.UDKClass import UDK
from PyQt5.QtGui import QColor


class MainWindowClass(QMainWindow, Ui_MainWindow):
    
    def __init__(self, headers: list, udk_list=None):
        super(MainWindowClass, self).__init__()
        self.setupUi(self)
        self.udkTw.setColumnCount(len(headers))
        self.udkTw.setHorizontalHeaderLabels(headers)
        self.udk_list = udk_list
        self.current_udk_list = udk_list
        self.udk_stack = []

        if udk_list is not None:
            self.set_udk_table(udk_list)

        self.udkTw.cellClicked.connect(self.cell_clicked)
        self.backBut.clicked.connect(self.back_in_udk_tree)

        self.udkTw.setColumnHidden(2, True)
        self.udkTw.setColumnHidden(3, True)

    def get_current_udk_list(self):
        if len(self.udk_stack) == 0:
            return self.udk_list
        return self.udk_stack[0].udk_sublist

    # def print_current_page(self):
    #     if len(self.current_udk_list) == 0:
    #         print("Nothing to print(((")
    #     for item in self.current_udk_list:
    #         print(item)
    
    def cell_clicked(self, row: int, column: int):
        clicked_udk = self.current_udk_list[row]
        if clicked_udk.next_reference is not None:
            self.current_udk_list = clicked_udk.udk_sublist
            self.udk_stack.insert(0, clicked_udk)
            self.set_udk_table(self.current_udk_list)

    def back_in_udk_tree(self):
        try:
            self.udk_stack.pop(0)
            self.current_udk_list = self.get_current_udk_list()
            self.set_udk_table(self.current_udk_list)
        except IndexError:
            pass

    def set_udk_table(self, udk_list: list):
        self.udkTw.setRowCount(len(udk_list))
        for i in range(len(udk_list)):
            code_item = QTableWidgetItem(udk_list[i].udk_code)
            if udk_list[i].next_reference is not None:
                code_item.setForeground(QColor(0, 0, 255))
            self.udkTw.setItem(i, 0, code_item)
            description_text = udk_list[i].description
            if description_text == "None":
                description_text = ""
            self.udkTw.setItem(i, 1, QTableWidgetItem(description_text))
            self.udkTw.setItem(i, 2, QTableWidgetItem(udk_list[i].codes_amount))
            self.udkTw.setItem(i, 3, QTableWidgetItem(udk_list[i].next_reference))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindowClass()
    MainWindow.show()
    sys.exit(app.exec_())
