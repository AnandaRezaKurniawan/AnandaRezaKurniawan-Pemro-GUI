import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# contoh penerapan dialog versi model dan non-model
class DialogForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        # mengatur ukuran dan posisi
        self.resize(300, 100)
        self.move(320, 280)
        # menentukan nama windownya
        self.setWindowTitle('Dialog')
        # membuat label
        self.label = QLabel('')
        # membuat button
        self.closeButton = QPushButton('Tutup')
        # merapikan item
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.closeButton)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(hbox)
        self.setLayout(layout)
        # menghubungkan button close dengan fungsinya
        self.closeButton.clicked.connect(self.close)

# kelas form utama
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        # setting ukuran dan posisi
        self.resize(350, 100)
        self.move(300, 300)
        # menentukan judul window
        self.setWindowTitle('Demo QDialog.setModal()')
        # membuat label dan lineEdit
        self.label = QLabel('Tuliskan teks pada kotak di bawah ' + 'ketika dialog ditampilkan.')
        self.lineEdit = QLineEdit()
        # membuat button dengan untuk modal dan non-modal
        self.showModalDialogButton = QPushButton('Modal')
        self.showModelessDialogButton = QPushButton('Non-Modal')
        # set layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.showModalDialogButton)
        hbox.addWidget(self.showModelessDialogButton)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addLayout(hbox)
        self.setLayout(layout)
        # menghubungkan button dengan fungsinya
        self.showModalDialogButton.clicked.connect(self.showModalDialogButtonClick)
        self.showModelessDialogButton.clicked.connect(self.showModelessDialogButtonClick)

    # menampilkan dialog secara modal
    # mainform ga bisa di klik atau diakses sebelum dialog ini ditutup
    def showModalDialogButtonClick(self):
        self.form = DialogForm()
        self.form.label.setText('Dialog bersifat modal')
        self.form.setModal(True)
        self.form.show()

    # menampilkan dialog secara non-modal
    # mainform bisa diakses tanpa harus close dialog ini
    def showModelessDialogButtonClick(self):
        self.form = DialogForm()
        self.form.label.setText('Dialog bersifat nonmodal (modeless)')
        self.form.setModal(False)
        self.form.show()

if __name__ == '__main__':
     a = QApplication(sys.argv)
     form = MainForm()
     form.show()
     a.exec_()
