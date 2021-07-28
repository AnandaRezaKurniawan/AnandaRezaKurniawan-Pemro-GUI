import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## contoh implementasi qdialog versi 2
# untuk kelas form jika dipencet tambah
class AddForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        # set ukuran dan posisi
        self.resize(350, 130)
        self.move(320, 280)
        # menentukan nama window
        self.setWindowTitle('Tambah Data')
        # membuat label dan lineEdit
        self.label1 = QLabel('Bahasa Pemrograman')
        self.languageEdit = QLineEdit()
        self.label2 = QLabel('Nama Pencipta')
        self.nameEdit = QLineEdit()
        # merapikan label dan lineEdit secara grid
        grid = QGridLayout()
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.languageEdit, 0, 1)
        grid.addWidget(self.label2, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)
        # membuat button ok dan batal
        self.okButton = QPushButton('OK')
        self.cancelButton = QPushButton('Batal')
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(hbox)
        self.setLayout(layout)
        # menghubungkan button sesuai dengan fungsinya
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)

# ini untuk kelas utamanaya
class MainForm(QWidget):
    lastRecordNumber = -1
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        # mengatur ukuran dan posisi
        self.resize(450, 300)
        self.move(300, 300)
        # menentukan nama windownya
        self.setWindowTitle('Demo QDialog.accept() dan QDialog.reject()')
        # membuat table pada kelas utaman
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(0)         # set baris awal sebagai 0
        self.setColumnAndHeaders()              # fungsi set kolom headers
        # membuat 3 button pada kelas utama sbagai berikut
        self.addButton = QPushButton('Tambah')
        self.deleteButton = QPushButton('Hapus')
        self.exitButton = QPushButton('Keluar')
        # merapikan layout secara vertical
        vbox = QVBoxLayout()
        vbox.addWidget(self.addButton)
        vbox.addWidget(self.deleteButton)
        vbox.addStretch()
        vbox.addWidget(self.exitButton)
        layout = QHBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addLayout(vbox)
        self.setLayout(layout)
        # menghubungkan button dengan masing-masing fungsinya
        self.addButton.clicked.connect(self.addButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)
        self.exitButton.clicked.connect(self.exitButtonClick)

    # isi fungsi setColumnHeaders diatas
    # membuat 2 kolom dengan judul sebagai berikut
    def setColumnAndHeaders(self):
        self.tableWidget.setColumnCount(2)
        columnHeaders = ['Bahasa Pemrograman', 'Nama Pencipta']
        self.tableWidget.setHorizontalHeaderLabels(columnHeaders)

    # menambahkan baris
    def addRow(self, row, itemLabels=[]):
        for i in range(2):
            item = QTableWidgetItem()
            item.setText(itemLabels[i])
            self.tableWidget.setItem(row, i, item)
    # menambah baris dan membuka dari kelas dialog diatas
    def addButtonClick(self):
        if MainForm.lastRecordNumber == self.tableWidget.rowCount()-1:
            self.tableWidget.setRowCount(
            self.tableWidget.rowCount()+1)
            form = AddForm()
        if form.exec_() == QDialog.Accepted:
            MainForm.lastRecordNumber += 1
            language = form.languageEdit.text()
            name = form.nameEdit.text()
            data = [language, name]
            self.addRow(MainForm.lastRecordNumber, data)
    # menghapus baris pada tabel, cuma masih agak error
    def deleteButtonClick(self):
        tableData = []
        for i in range(0, self.tableWidget.rowCount()):
            language = self.tableWidget.item(i, 0).text()
            name = self.tableWidget.item(i, 1).text()
            tableData.append([language, name])
            row = self.tableWidget.currentRow()
            del tableData[row]
            MainForm.lastRecordNumber -= 1
            self.tableWidget.clear()
            self.setColumnAndHeaders()
            self.tableWidget.setRowCount(len(tableData))
            for i in range(0, len(tableData)):
                data = tableData[i]
                self.addRow(i, data)
    # keluar / close
    def exitButtonClick(self):
        self.close()

if __name__ == '__main__':
     a = QApplication(sys.argv)
     form = MainForm()
     form.show()
     a.exec_()
