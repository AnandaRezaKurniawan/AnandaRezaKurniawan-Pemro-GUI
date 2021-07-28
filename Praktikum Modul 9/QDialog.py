import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## contoh program penerapan dialog pyqt5
# ini merupakan kelas unutk dialog ke dua
class DialogForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        # menentukan ukuran dan posisi widget
        self.resize(300, 100)
        self.move(320, 280)

        # mengganti judul window menjadi Dialog
        self.setWindowTitle('Dialog')
        # membuat label form untuk dialog ke dua ini
        self.label = QLabel('Form Kedua (Dialog)')
        # kemudian membuat 2 button pada dialog kedua ini
        self.okButton = QPushButton('OK')
        self.cancelButton = QPushButton('Batal')
        # merapihkan layout item
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(hbox)
        self.setLayout(layout)
        # menghubungkan button ke fungsinya
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)

# ini unutk kelas atau widget utamanya
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        # setting ukuran dan posisi
        self.resize(350, 100)
        self.move(300, 300)
        # set nama window
        self.setWindowTitle('Demo QDialog.accept() dan QDialog.reject()')
        # membuat label pada form utama ini
        self.label = QLabel('Form Utama')
        # membuat button untuk menampilkan dialog dari kelas dialog
        self.showDialogButton = QPushButton('Tampilkan Dialog')
        # merapikan layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.showDialogButton)
        self.setLayout(layout)
        # menghubungkan ke fungsinya.
        self.showDialogButton.clicked.connect(self.showDialogButtonClick)

    # fungsi jika button tampilkan di klik
    def showDialogButtonClick(self):
        form = DialogForm()
        ## menjalankan dialog sekaligus menentukan jika salah satu tombol dklik
        # akan memunculkan message box yang mana
        if form.exec_() == QDialog.Accepted:
            QMessageBox.information(self, 'Informasi', 'Anda memilih tombol OK')
        else: # QDialog.Rejected
            QMessageBox.information(self, 'Informasi', 'Anda memilih tombol Batal')
if __name__ == '__main__':
     a = QApplication(sys.argv)
     form = MainForm()
     form.show()
     a.exec_()
