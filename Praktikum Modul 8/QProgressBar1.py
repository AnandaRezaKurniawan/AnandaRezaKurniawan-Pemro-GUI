import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## contoh penggunaan progress bar
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        ## mengatur ukuran dan posisi form/widget
        self.resize(400, 400)
        self.move(300, 300)
        self.setWindowTitle('Demo QProgressBar')

        ## bagian isi dari form/widget
        self.label1 = QLabel('Bilangan Ganjil')
        self.list1 = QListWidget()                  # membuat list
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.list1)
        self.label2 = QLabel('Bilangan Genap')
        self.list2 = QListWidget()                  # membuat list
        # merapikan widget
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.list2)
        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)
        self.progress = QProgressBar()              # membuat progres bar
        self.progress.setMinimum(0)                 # menetapkan minimum/awal progres bar
        self.progress.setMaximum(10000)             # menetapkan maximum progres bar
        self.progress.setValue(0)
        self.startButton = QPushButton('Mulai...')  # membuat button mulai
        layout = QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.progress)
        layout.addWidget(self.startButton)
        self.setLayout(layout)
        # menghubungkan button ke fungsinya
        self.startButton.clicked.connect(self.startButtonClick)

    ## nantinya bilangan akan dipisah dimana kiri bilangan ganjil dan kanan bilangan genap
    def startButtonClick(self):
        self.progress.setValue(0)
        for i in range(0,1000):
            QApplication.processEvents()
            if i % 2 == 1:
                self.list1.addItem(str(i))
            else:
                self.list2.addItem(str(i))
                self.progress.setValue(self.progress.value()+1)

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
