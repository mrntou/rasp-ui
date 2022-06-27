from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer, QTime, Qt
import sys
from datetime import datetime
import random


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('gui.ui', self) # Load the .ui file
        self.show() # Show the GUI

        timer = QTimer(self)
        timer.timeout.connect(self.displayHour)
        timer.timeout.connect(self.displaySec)
        timer.timeout.connect(self.displayDate)


        timer.start(1000)

        self.closeBtn.clicked.connect(sys.exit)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.showMaximized()
        self.showFullScreen()

        self.colors =[
            "#c0392b","#9b59b6","#8e44ad","#2980b9","#2874a6","#DFFF00",
            "#6495ED","#CCCCFF","#ff0077","#79486b","#fa7f93","#66c8b0",
            "#d2d1d0","#ffd966","#FFFFFF","#78ae00","#b12547","#2596be"
        ]


        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)


    def displayHour(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString("hh:mm")

        self.hour.setText(displayText)

    def displaySec(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString("ss")

        self.sec.setText(displayText)
        self.sec.setStyleSheet(f"color:{random.choice(self.colors)}")

    def displayDate(self):
        today = datetime.today().strftime("%A")
        self.day.setText(today)




app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()