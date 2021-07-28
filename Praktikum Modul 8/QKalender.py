import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## program untuk contoh implementasi QCalendar
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(400, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QCalendarWidget')

        ## bagian isi dari aplikasi
        self.calendar = QCalendarWidget()           # deklarasi QCalendar
        self.calendar.setGridVisible(True)          # menampilkan grid/batas tanggal calendar
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)
        self.shortNamesCheck = QCheckBox('Nama hari pendek')    # deklarasi checkbox nama hari versi pendek
        self.dateEdit = QDateEdit()             # menambahkan DateEdit
        self.dateEdit.setDisplayFormat('dd/MM/yyyy')
        self.dateEdit.setDate(QDate.currentDate())

        # deklarasi button tentukan dan ambil tanggal
        self.setButton = QPushButton('Tentukan Tanggal')
        self.getButton = QPushButton('Ambil Tanggal')

        # bagian untuk merapihkan widget
        hbox = QHBoxLayout()
        hbox.addWidget(self.dateEdit)
        hbox.addWidget(self.setButton)
        hbox.addWidget(self.getButton)
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.shortNamesCheck)
        layout.addLayout(hbox)
        self.setLayout(layout)

        # untuk menghubungkan button ke fungsi masing-masing
        self.shortNamesCheck.clicked.connect(self.shortNamesCheckClick)
        self.setButton.clicked.connect(self.setButtonClick)
        self.getButton.clicked.connect(self.getButtonClick)

    ## berfungsi untuk mengubah nama hari jadi singkat
    def shortNamesCheckClick(self):
        if self.shortNamesCheck.isChecked():
            self.calendar.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        else:
            self.calendar.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)

    ## mengembalikan posisi tanggal ke tanggal yang di pilih di date edit
    def setButtonClick(self):
        self.calendar.setSelectedDate(self.dateEdit.date())

    ## mengambil informasi tanggal yang sedang di pilih
    def getButtonClick(self):
        QMessageBox.information(self, 'Informasi','Tanggal aktif: ' +
                                self.calendar.selectedDate().toString())

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
