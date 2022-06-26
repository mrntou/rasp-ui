from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer, QTime, Qt
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('gui.ui', self) # Load the .ui file
        self.show() # Show the GUI

        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)


    def displayTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString("hh:mm:ss")
        print(currentTime)

        self.label.setText(displayText)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()