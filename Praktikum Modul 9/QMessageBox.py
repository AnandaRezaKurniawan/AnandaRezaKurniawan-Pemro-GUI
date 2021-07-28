import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## contoh implementasi message box
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        # setting ukuran dan posisi form
        self.resize(450, 100)
        self.move(300, 300)
        # menentukan judul window
        self.setWindowTitle('Demo QMessageBox')
        # membuat button-button
        self.aboutButton = QPushButton('About')
        self.criticalButton = QPushButton('Critical')
        self.informationButton = QPushButton('Information')
        self.questionButton = QPushButton('Question')
        self.warningButton = QPushButton('Warning')
        # merapihkan secara horizontal
        layout = QHBoxLayout()
        layout.addWidget(self.aboutButton)
        layout.addWidget(self.criticalButton)
        layout.addWidget(self.informationButton)
        layout.addWidget(self.questionButton)
        layout.addWidget(self.warningButton)
        self.setLayout(layout)
        # menghubungkan button pada tiap fungsinya
        self.aboutButton.clicked.connect(self.aboutButtonClick)
        self.criticalButton.clicked.connect(self.criticalButtonClick)
        self.informationButton.clicked.connect(self.informationButtonClick)
        self.questionButton.clicked.connect(self.questionButtonClick)
        self.warningButton.clicked.connect(self.warningButtonClick)

    # about nanti munculin message yang bentukan about, deskripsi dan tombol oke
    def aboutButtonClick(self):
        QMessageBox.about(self, 'Tentang Program', 'Video Recorder\n' + 'Versi 1.0.0\n' + 'Hak cipta (C) 2016 PyQt Lover Team')
    # ini buat misal ada kesalahan dalam suatu proses
    def criticalButtonClick(self):
        QMessageBox.critical(self, 'Kesalahan', 'File settings.conf tidak ditemukan.')
    # ini buat nampilin info, mirip about tapi ada ikon I dan suaranya
    def informationButtonClick(self):
        QMessageBox.information(self, 'Informasi','Proses upload file ke server telah berhasil dilakukan.')
    # ini untuk dipakai jika memerlukan suatu konfirmasi
    def questionButtonClick(self):
        fileName = 'settings.conf'
        response = QMessageBox.question(self, 'Konfirmasi', 'Anda yakin akan menghapus file %s?' % fileName)
        if response == QMessageBox.Yes:
            QMessageBox.about(self, 'Respon','Anda memilih tombol Yes')
        else:
            QMessageBox.about(self, 'Respon', 'Anda memilih tombol No')
    # untuk peringatan konfirmasi, biasanya dipakai di saat penting
    def warningButtonClick(self):
        QMessageBox.warning(self, 'Peringatan', 'Operasi ini akan menghapus semua data di dalam disk Anda!')
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
