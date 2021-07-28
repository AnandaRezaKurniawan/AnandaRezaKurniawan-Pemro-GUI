import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## Belajar QTextEdit
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    # fungsi yang berisikan ui nya
    def setupUi(self):
        # membuat formnya terlebih dulu
        self.resize(400, 200)
        self.move(300, 300)
        self.setWindowTitle('Demo QTextEdit')

        ## kontennya di rapikan dengan vertical box tiap bagiannya
        ## bagian Label, TextEdit dan LineEdit
        self.label1 = QLabel()      # membuat label baru
        self.label1.setText('No. HP')       # label diberi teks No.HP
        self.phoneEdit = QLineEdit()        # membuat LineEdit
        vbox1 = QVBoxLayout()
        # memasukkan label1 dan phoneEdit pada vertical box (vbox1)
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.phoneEdit)

        self.label2 = QLabel()      # membuat label baru
        self.label2.setText('Pesan')        # label diberi teks Pesan
        self.messageEdit = QTextEdit()      # membuat TextEdit
        vbox2 = QVBoxLayout()
        # memasukkan label2 dan messageEdit pada vbox 2
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.messageEdit)
        # menggabungkan vbox1 dan vbox2
        vbox3 = QVBoxLayout()
        vbox3.addLayout(vbox1)
        vbox3.addLayout(vbox2)

        ## Bagian Button
        # membuat 2 button baru
        self.sendButton = QPushButton('&Kirim SMS')
        self.cancelButton = QPushButton('&Batal')
        # dirapikan dengan horizontal box
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.sendButton)
        hbox.addWidget(self.cancelButton)
        layout = QVBoxLayout()
        layout.addLayout(vbox3)
        # membuat horizontal line untuk membatasi button dengan bagian Text
        horizontalLine = QFrame()
        horizontalLine.setFrameShape(QFrame.HLine)
        horizontalLine.setFrameShadow(QFrame.Sunken)
        layout.addWidget(horizontalLine)
        layout.addLayout(hbox)
        self.setLayout(layout)


# untuk menjalankan program
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
