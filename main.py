from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer, QTime, Qt
import sys
from datetime import datetime


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


    def displayHour(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString("hh:mm")

        self.hour.setText(displayText)

    def displaySec(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString("ss")

        self.sec.setText(displayText)

    def displayDate(self):
        today = datetime.today().strftime("%A")
        self.day.setText(today)




app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()