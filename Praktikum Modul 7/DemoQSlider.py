import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## contoh menggunakan slider
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        ## menentukan ukuran widget
        self.resize(400, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QSlider dan QLCDNumber')

        ## membuat slider dan ukuran/setting nya
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(-1)
        self.slider.setMaximum(101)
        self.slider.setValue(45)
        self.lcd = QLCDNumber()     # membuat lcd untuk nanti memperjelas nilai slider
        self.lcd.setDigitCount(3)
        self.lcd.display(45)

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.lcd)
        self.setLayout(layout)
        self.slider.sliderMoved.connect(self.sliderMoved)

    ## menghubungkan slider dengan lcd
    def sliderMoved(self):
        self.lcd.display(str(self.slider.value()))


if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
