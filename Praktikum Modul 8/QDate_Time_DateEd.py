import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## contoh program implementasi QDateEdit, QTimeEdit dan QDateTimeEdit
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        ## membuat ukuran dan memposisikan form
        self.resize(400, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QDateTimeEdit')


        ## bagian isi utama
        # date edit
        self.dateLabel = QLabel('Tanggal')  # label tanggal
        self.dateEdit = QDateEdit()         # deklarasi DateEdit
        self.dateEdit.setDisplayFormat('dddd dd/MM/yyyy')   # set display DateEdit
        self.dateEdit.setDate(QDate.currentDate())

        # time edit
        self.timeLabel = QLabel('Waktu')
        self.timeEdit = QTimeEdit()                 # deklarasi TimeEdit
        self.timeEdit.setDisplayFormat('hh:mm')     # set display TimeEdit
        self.timeEdit.setTime(QTime.currentTime())

        # date time edit
        self.dateTimeLabel = QLabel('Tanggal dan Waktu')
        self.dateTimeEdit = QDateTimeEdit()         # deklarasi DateTimeEdit
        self.dateTimeEdit.setDisplayFormat('dddd dd/MM/yyyyhh:mm')      # set DateTimeEdit
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        self.okButton = QPushButton('&OK')      # deklarasi button OK

        ## merapikan widget
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.okButton)
        layout = QGridLayout()
        layout.addWidget(self.dateLabel, 0, 0)
        layout.addWidget(self.dateEdit, 0, 1)
        layout.addWidget(self.timeLabel, 1, 0)
        layout.addWidget(self.timeEdit, 1, 1)
        layout.addWidget(self.dateTimeLabel, 2, 0)
        layout.addWidget(self.dateTimeEdit, 2, 1)
        layout.addLayout(hbox, 3, 0, 1, 2)
        self.setLayout(layout)
        self.okButton.clicked.connect(self.okButtonClick)

    ## fungsi ini adalah lanjutan dari button OK
    ## yang berfungsi untuk menampilkan informasi yang dipilih pada form utama
    def okButtonClick(self):
        QMessageBox.information(self, 'Informasi',
        'Date: ' + self.dateEdit.date().toString() +
        '\n' + 'Time: ' + self.timeEdit.time().toString() + '\n' +'Datetime: ' +
        self.dateTimeEdit.dateTime().toString() + '\n')

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
