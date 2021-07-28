from PyQt5.QtWidgets import (QDialog, QGridLayout,QHBoxLayout, QLabel, QLineEdit, QPushButton)

# kelas lanjutan contoh database phonobook
# form pada kelas ini akan berjalan ketika user
# berusahan untuk menambahkan atau mengedit item
class EntryForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        # set ukuran dan posisi form
        self.resize(300, 100)
        self.move(320, 280)
        # menentukan nama window nya
        self.setWindowTitle('Tambah/Ubah Kontak')
        self.mode = -1 # 0: mode tambah, 1: mode ubah
        # membuat button ok dan batal
        self.okButton = QPushButton('OK')
        self.cancelButton = QPushButton('Batal')
        # merapikan button
        hbox = QHBoxLayout()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        # membuat label dan lineEdit
        self.label1 = QLabel("Nama Lengkap:")
        self.nameLineEdit = QLineEdit()
        self.label2 = QLabel("Nomor HP:")
        self.phoneLineEdit = QLineEdit()
        # ini jika user memilih untuk menambah item
        # data pada lineEdit akan hilang
        if self.mode == 0:
            self.nameLineEdit.clear()
            self.phoneLineEdit.clear()
        # merapikan layout item form
        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.nameLineEdit, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.phoneLineEdit, 1, 1)
        layout.addLayout(hbox, 2, 1)
        self.setLayout(layout)
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
