import sys

from IPython.external.qt_for_kernel import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MyTable(QWidget):
    def __init__(
            self,
            name="",
            room="",
            class_type="",
            time="",
            tip="",
            bg="#FAFDD6"):
        super().__init__()
        self.setGeometry(0, 0, 40, 30)
        self.setFocusPolicy(Qt.NoFocus)
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setStyleSheet("QWidget{background:" + bg + ";}")

        self.class_name = QLabel(name)
        self.class_name.setFont(QFont("Arial", 7, QFont.Bold))
        self.class_name.setStyleSheet("QLabel{color:#B20600;}")
        self.class_name.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.classroom = QLabel(room)
        self.classroom.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.classroom.setFont(QFont("Roman times", 7, QFont.Bold))
        self.classroom.setStyleSheet("QLabel{color:#00FFC6;}")

        self.class_type = QLabel(class_type)
        self.class_type.setFont(QFont("Arial", 7, QFont.Bold))
        self.class_type.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.class_type.setStyleSheet("QLabel{color:#FF5F00;}")

        self.class_time = QLabel(time)
        self.class_time.setFont(QFont("Roman times", 7, QFont.Bold))
        self.class_time.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.class_time.setStyleSheet("QLabel{color:#A2B38B;}")

        self.grid.addWidget(self.class_name, 0, 0, 1, 1)
        self.grid.addWidget(self.classroom, 0, 1, 1, 1)
        self.grid.addWidget(self.class_type, 1, 0, 1, 1)
        self.grid.addWidget(self.class_time, 1, 1, 1, 1)
        self.setToolTip(tip)

    def resizeEvent(self, event):
        print(self.width())


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ex = MyTable("ММИПиУ", "302-3K", "test", "9:00-10:30", "no", "skyblue")
    ex.show()
    print(ex.geometry())
    sys.exit(app.exec_())
