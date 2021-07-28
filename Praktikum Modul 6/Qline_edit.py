import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## belajar QLineEdit, QLabel dan QPushButton
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    # fungsi ui nya
    def setupUi(self):
        self.resize(400, 200)
        self.move(300, 300)
        self.setWindowTitle('Demo QLabel, QLineEdit, dan QPushButton')

        ## label BIlangan Pertama, Kedua, dan hasil Perhitungan berada dalam
        ## vertical layout
        # membuat label Bilangan Pertama
        # dan membuat line editnya sekalian
        self.label1 = QLabel()
        self.label1.setText('Bilangan pertama')
        self.numberEdit1 = QLineEdit()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.numberEdit1)

        # membuat label Bilangan Kedua
        # dan membuat line editnya sekalian
        self.label2 = QLabel()
        self.label2.setText('Bilangan kedua')
        self.numberEdit2 = QLineEdit()
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.numberEdit2)

        # membuat label Hasil Perhitungan
        # dan membuat line editnya sekalian
        self.label3 = QLabel()
        self.label3.setText('Hasil Perhitungan')
        self.resultEdit = QLineEdit()
        self.resultEdit.setReadOnly(True)
        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.label3)
        vbox3.addWidget(self.resultEdit)
        vbox4 = QVBoxLayout()
        vbox4.addLayout(vbox1)
        vbox4.addLayout(vbox2)
        vbox4.addLayout(vbox3)
        vbox4.addStretch()

        ## Push buttom tambah, kurang, kali dan bagi berada dalam
        ## vertical layout
        self.addButton = QPushButton('Tambah')
        self.substractButton = QPushButton('Kurang')
        self.mulButton = QPushButton('Kali')
        self.divButton = QPushButton('Bagi')
        vbox5 = QVBoxLayout()
        vbox5.addWidget(self.addButton)
        vbox5.addWidget(self.substractButton)
        vbox5.addWidget(self.mulButton)
        vbox5.addWidget(self.divButton)
        vbox5.addStretch()
        layout = QHBoxLayout()
        layout.addLayout(vbox4)

        # membuat garis vertical untuk pembatas
        verticalLine = QFrame();
        verticalLine.setFrameShape(QFrame.VLine)
        verticalLine.setFrameShadow(QFrame.Sunken)
        layout.addWidget(verticalLine)
        layout.addLayout(vbox5)
        self.setLayout(layout)

        # setting dari tiap button ke fungsinya masing-masing
        self.addButton.clicked.connect(self.addButtonClick)
        self.substractButton.clicked.connect(self.substractButtonClick)
        self.mulButton.clicked.connect(self.mulButtonClick)
        self.divButton.clicked.connect(self.divButtonClick)

    # fungsi untuk melakukan perhitungan
    def calculate(self, operator):
        a = float(self.numberEdit1.text())
        b = float(self.numberEdit2.text())
        if operator == '+':
            c = a + b
        elif operator == '-':
            c = a - b
        elif operator == '*':
            c = a * b
        else:
            c = a / b
        # setText() berdasarkan variabel c (hasil)
        self.resultEdit.setText(str(c))

    ## fungsi-fungsi buttonClick diarahkan ke sini
    ## dan nanti akan menuju ke fungsi calculate
    def addButtonClick(self):
        self.calculate('+')
    def substractButtonClick(self):
        self.calculate('-')
    def mulButtonClick(self):
        self.calculate('*')
    def divButtonClick(self):
        self.calculate('/')


# untuk menjalankan program
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
