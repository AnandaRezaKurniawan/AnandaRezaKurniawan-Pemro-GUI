from PyQt5.QtWidgets import (QDialog, QGridLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton)


class EntryForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(320, 280)
        self.setWindowTitle('Tambah/Ubah Kontak')

        self.okButton = QPushButton('OK')
        self.cancelButton = QPushButton('Batal')

        hbox = QHBoxLayout()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)

        self.label1 = QLabel("Nim :")
        self.nim = QLineEdit()
        self.label2 = QLabel("Nama :")
        self.nama = QLineEdit()
        self.label3 = QLabel("Jurusan :")
        self.jurusan = QLineEdit()
        self.label4 = QLabel("No.Telp :")
        self.telp = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.nim, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.nama, 1, 1)
        layout.addWidget(self.label3, 2, 0)
        layout.addWidget(self.jurusan, 2, 1)
        layout.addWidget(self.label4, 4, 0)
        layout.addWidget(self.telp, 4, 1)
        layout.addLayout(hbox, 5, 1)
        self.setLayout(layout)

        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)