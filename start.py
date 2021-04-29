from PyQt5 import QtCore, QtWidgets, QtSql
from PyQt5.QtWidgets import QApplication, QAction, QFileDialog, QInputDialog, QTableWidget, QTableWidgetItem, \
    QPushButton
import sys
import service
from search_file import find


# self.pushButton_5.clicked.connect(self.button_clicked(text="goods"))
# self.pushButton_4.clicked.connect(self.button_clicked(text="units"))
# self.pushButton_3.clicked.connect(self.button_clicked(text="categories"))
# self.pushButton_2.clicked.connect(self.button_clicked(text="positions"))
# self.pushButton_7.clicked.connect(self.button_clicked(text="employees"))
# self.pushButton_6.clicked.connect(self.button_clicked(text="vendors"))

class ExampleApp(QtWidgets.QMainWindow, service.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.global_word = ""
        self.pushButton.clicked.connect(self.show_dialog)
        self.pushButton_5.clicked.connect(self.button_clicked_5)
        self.pushButton_4.clicked.connect(self.button_clicked_4)
        self.pushButton_3.clicked.connect(self.button_clicked_3)
        self.pushButton_2.clicked.connect(self.button_clicked_2)
        self.pushButton_7.clicked.connect(self.button_clicked_6)
        self.pushButton_6.clicked.connect(self.button_clicked_7)

    def button_clicked_5(self):
        self.global_word = self.pushButton_5.text()

    def button_clicked_4(self):
        self.global_word = self.pushButton_4.text()

    def button_clicked_3(self):
        self.global_word = self.pushButton_3.text()

    def button_clicked_2(self):
        self.global_word = self.pushButton_2.text()

    def button_clicked_6(self):
        self.global_word = self.pushButton_6.text()

    def button_clicked_7(self):
        self.global_word = self.pushButton_7.text()

    def show_dialog(self):
        f_name = QFileDialog.getOpenFileName(self, 'Open file', "/home")[0]
        f_name = f_name.split("/")[-1]
        finds = find(f_name)
        self.textEdit.setText(finds)
        conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        conn.setDatabaseName(finds)
        if conn.open():
            query_table = QtWidgets.QTableView(self.horizontalLayoutWidget)
            query_table.setObjectName("tableView")
            self.horizontalLayout.addWidget(query_table)
            query_model = QtSql.QSqlQueryModel(parent=query_table)
            query_model.setQuery(f'select * from {self.global_word}')
            query_table.setModel(query_model)


        else:
            # Выводим текст ошибки
            print(conn.lastError().text())


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
