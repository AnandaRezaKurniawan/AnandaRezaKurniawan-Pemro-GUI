import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## contoh menggunakan QListWidget
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        ## ukuran widget nya
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Demo QListWidget')
        self.label = QLabel('&Elemen baru')
        self.itemEdit = QLineEdit()
        self.label.setBuddy(self.itemEdit)
        self.addItemButton = QPushButton('Tambah')
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.itemEdit)
        hbox1.addWidget(self.addItemButton)
        hbox1.addStretch()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label)
        vbox1.addLayout(hbox1)

        # membuat list pertama
        self.list1 = QListWidget()

        ## membuat pushButton penunjuk
        self.moveRightButton = QPushButton('>')
        self.moveRightAllButton = QPushButton('>>')
        self.moveLeftButton = QPushButton('<')
        self.moveLeftAllButton = QPushButton('<<')
        ## merapikan pushButton penunjuk
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.moveRightButton)
        vbox2.addWidget(self.moveRightAllButton)
        vbox2.addWidget(self.moveLeftButton)
        vbox2.addWidget(self.moveLeftAllButton)
        vbox2.addStretch()

        ## membuat list kedua
        self.list2 = QListWidget()
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.list1)
        hbox2.addLayout(vbox2)
        hbox2.addWidget(self.list2)
        layout = QVBoxLayout()
        layout.addLayout(vbox1)
        layout.addLayout(hbox2)
        self.setLayout(layout)

        ## menghubungkan tombol ke fungsi masing2
        self.addItemButton.clicked.connect(self.addItemButtonClick)
        self.moveRightButton.clicked.connect(self.moveRightButtonClick)
        self.moveRightAllButton.clicked.connect(self.moveRightAllButtonClick)
        self.moveLeftButton.clicked.connect(self.moveLeftButtonClick)
        self.moveLeftAllButton.clicked.connect(self.moveLeftAllButtonClick)

    # digunakan untuk menambahkan data ke dalam list baru
    def addItemButtonClick(self):
        if len(self.itemEdit.text()) == 0: return
        item = self.itemEdit.text()
        self.list1.addItem(item)
        self.itemEdit.clear()
        self.itemEdit.setFocus()

    # berguna untuk memindahkan data yang dipilih ke list kanan
    def moveRightButtonClick(self):
        if self.list1.currentRow() < 0: return
        self.list2.addItem(self.list1.currentItem().text())
        self.list1.takeItem(self.list1.currentRow())

    # digunakan untuk memindahkan semua data di list kiri ke list kanan (masih belum jadi)
    def moveRightAllButtonClick(self):
        for index in range(self.list1.count()):
            self.list2.addItem(self.list1.item(index).text())
            self.list1.clear()

    # berguna untuk memindahkan data yang dipilih ke list kiri
    def moveLeftButtonClick(self):
        if self.list2.currentRow() < 0: return
        self.list1.addItem(self.list2.currentItem().text())
        self.list2.takeItem(self.list2.currentRow())

    # digunakan untuk memindahkan semua data di list kanan ke list kiri (masih belum jadi)
    def moveLeftAllButtonClick(self):
        for index in range(self.list2.count()):
            self.list1.addItem(self.list2.item(index).text())
            self.list2.clear()

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
