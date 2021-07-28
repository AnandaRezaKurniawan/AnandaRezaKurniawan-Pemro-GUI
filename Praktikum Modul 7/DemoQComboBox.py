import sys

from PyQt5.QtWidgets import *
## contoh program combo box

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        # membuat ukuran widget
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QComboBox')
        # membuat combo box sebanyak 10 item
        self.combo = QComboBox()
        for i in range(1, 11):
            self.combo.addItem('Item ke-%d' % i)
        # button ambil teks
        self.getTextButton = QPushButton('Ambil Teks')
        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.getTextButton)
        layout.addStretch()
        self.setLayout(layout)
        self.getTextButton.clicked.connect(self.getTextButtonClick)


    ## fungsi jika tombol getText diclick akan membukan messageBox dan menampilkan
    # informasi yang dipilih
    def getTextButtonClick(self):
        QMessageBox.information(self, 'Informasi',
                                'Anda memilih: ' + self.combo.currentText())


if __name__ == '__main__':    a = QApplication(sys.argv)
form = MainForm()
form.show()
a.exec_()
