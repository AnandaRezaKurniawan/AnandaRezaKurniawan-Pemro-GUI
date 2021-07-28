import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from EntryForm import *

# studi kasus phoneBook dengan menggunakan database
# ini merupakan kelas utamanya
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loadData()
    def setupUi(self):
        # menentukan ukuran dan posisi form
        self.resize(350, 300)
        self.move(300, 300)
        # menentukan judul form
        self.setWindowTitle('Phonebook Manager')
        # membuat tabel
        self.table = QTableWidget()
        # membuat button
        self.addButton = QPushButton('Tambah')
        self.editButton = QPushButton('Ubah')
        self.deleteButton = QPushButton('Hapus')
        # merapikan button
        hbox = QHBoxLayout()
        hbox.addWidget(self.addButton)
        hbox.addWidget(self.editButton)
        hbox.addWidget(self.deleteButton)
        hbox.addStretch()
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(hbox)
        self.setLayout(layout)
        # menghubungkan button ke tiap fungsinya
        self.addButton.clicked.connect(self.addButtonClick)
        self.editButton.clicked.connect(self.editButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)
    # untuk mengambil data dari database
    def loadData(self):
        self.table.clear()
        self.table.setRowCount(self.getRowCount())
        # set jumlah kolom
        self.table.setColumnCount(3)
        # set nama kolom
        columnHeaders = ['ID', 'Nama', 'No. HP']
        self.table.setHorizontalHeaderLabels(columnHeaders)
        query = QSqlQuery()
        ID, NAMA, NOHP = range(3)
        row = 0
        query.exec_('SELECT * FROM phonebook')

        # menampilkan data pada tabel
        while query.next():
            for i in range(3):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.table.setItem(row, i, item)
            row += 1

        item = QTableWidgetItem()
        item.setText(str(self.getRowCount()))
        self.table.setItem(6, 0, item)
    # digunakan untuk menghitung jumlah baris
    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM phonebook')
        query.next()
        rowCount = query.value(0)
        return rowCount
    # fungsi unutk menambahkan data baru pada tabel
    def addButtonClick(self):
        self.entryForm = EntryForm()
        self.mode = 0       # mode tambah, seperti dalam kelas EntryForm
        if self.entryForm.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1
            query = QSqlQuery()

            # memasukkan data yang sudah diketikkan pada lineEdit ke dalam database
            query.exec_("INSERT INTO phonebook (id, nama, nohp) VALUES (%d, '%s', '%s')" %
                        (id, self.entryForm.nameLineEdit.text(), self.entryForm.phoneLineEdit.text()))
            self.loadData()
    # fungsi untuk mengedit data pada tabel
    def editButtonClick(self):
        self.entryForm = EntryForm()
        self.mode = 1       # mode edit, seperti dalam kelas EntryForm
        # mengambil data yang ada pada row yang sedang dipilih
        self.entryForm.nameLineEdit.setText(self.table.item(self.table.currentRow(), 1).text())
        self.entryForm.phoneLineEdit.setText(self.table.item(self.table.currentRow(), 2).text())
        # melakukan perubahan data seperti cara menambahkan data
        if self.entryForm.exec_() == QDialog.Accepted:
            id = int(self.table.item(self.table.currentRow(),0).text())
            query = QSqlQuery()
            query.exec_('''UPDATE phonebook SET nama = '%s', nohp = '%s' WHERE id = %d ''' %
                        (self.entryForm.nameLineEdit.text(), self.entryForm.phoneLineEdit.text(), id))
            self.loadData()
    # digunakan untuk menghapus data yang dipilih
    def deleteButtonClick(self):
        id = int(self.table.item(self.table.currentRow(),0).text())
        query = QSqlQuery()
        query.exec_('DELETE FROM phonebook WHERE id = %d' % id)
        self.loadData()
if __name__ == '__main__':
    a = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('testdb')
    if not db.open():
        print('ERROR: ' + db.lastError().text())
        sys.exit(1)
    form = MainForm()
    form.show()
    a.exec_()
