import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
# import dari file other_form.py
from  Other_Form import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        # mengatur ukuran dan posisi form
        self.resize(400,300)
        self.move(100,300)
        self.setWindowTitle('Buka Tutup Beda Form')

        self.button = QPushButton('Tampilkan form lain')
        self.button1 = QPushButton('TUTUP')
        self.button.move(150,130)
        self.button1.move(310,260)
        self.button.setParent(self)
        self.button1.setParent(self)

        self.button.clicked.connect(self.buttonClicked)
        self.button1.clicked.connect(self.buttonClicked1)

    # mendefinisikan fungsi buttonClicked, dimana disini menampilkan OtherForm
    # dari file Other_Form.py
    def buttonClicked(self):
        self.form = OtherForm()
        self.form.show()

    # mendefinisikan fungsi buttonClicked1, dimana disini di close
    def buttonClicked1(self):
        self.close()


# tes untuk run saya jadikan dalam satu file
if __name__ == '__main__':
	a = QApplication(sys.argv)

	form = MainForm()
	form.show()
	a.exec_()
