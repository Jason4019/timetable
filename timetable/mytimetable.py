import sys
import os
from IPython.external.qt_for_kernel import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from table import MyTable
import day
import requests


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'table'
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 720
        self.currentweek = self.get_current_week()
        self.displayweek = self.currentweek
        self.initUI()
        self.center()


    def init_data(self):
        try:
            ans1 = os.system("table.py")
            ans2 = os.system("myclass.py")
        except Exception as e:
            print(e)
        print(ans1, ans2)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        # Add box layout, add table to box layout and add box layout to widget
        self.grid.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.grid.addWidget(self.button1, 1, 0, 1, 1)
        self.grid.addWidget(self.button2, 1, 1, 1, 1)
        # Show widget
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ["周一", "周二", "周三", "周四", "周五", "周六", "周日"])
        self.tableWidget.setVerticalHeaderLabels(
            [
                "09:00-10:20",
                "10:35-11:55",
                "12:25-13:45",
                "14:00-15:20",
                "15:50-17:10",
                "17:25-18:45",
                "19:00-20:20",
                "20:35-21:55"])
        self.tableWidget.setStyleSheet(
            "QHeaderView::section{background:skyblue;color:black;}"
            "QTableView QTableCornerButton::section {background:skyblue;color:black;}"
            "QTableWidget{background:#FAFDD6;}")

        self.mytable(self.displayweek)
        self.button1 = QPushButton("上周")
        self.button1.clicked.connect(self.before)
        self.button2 = QPushButton("下周")
        self.button2.clicked.connect(self.after)


    def before(self, event):
        self.tableWidget.clearContents()
        if int(self.displayweek) - 1 == 0:
            self.displayweek = "4"
        else:
            self.displayweek = str(int(self.displayweek) - 1)
        self.mytable(self.displayweek)
        print(self.displayweek)

    def after(self, event):
        self.tableWidget.clearContents()
        if int(self.displayweek) + 1 == 5:
            self.displayweek = "1"
        else:
            self.displayweek = str(int(self.displayweek) + 1)
        self.mytable(self.displayweek)
        print(self.displayweek)

    def mytable(self, weeknumber):
        dataset = day.weektable(weeknumber)
        for i in range(8):
            for j in range(7):
                name = dataset[i][j].get("subject").replace(" ", "")
                room = dataset[i][j].get("auditory").replace(" ", "").replace("а", "a").replace("к", "K")
                class_type = dataset[i][j].get("lessonType").replace(" ", "")
                time = dataset[i][j].get("lessonTime").replace(" ", "")
                tip = dataset[i][j].get("subjectFullName").replace(" ", "")
                self.tableWidget.setCellWidget(
                    i, j, MyTable(name, room, class_type, time, tip))

    def get_current_week(self):
        url2 = "https://iis.bsuir.by/api/v1/schedule/current-week"
        res2 = requests.get(url2)
        currentweek = res2.text
        res2.close()
        return currentweek


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
