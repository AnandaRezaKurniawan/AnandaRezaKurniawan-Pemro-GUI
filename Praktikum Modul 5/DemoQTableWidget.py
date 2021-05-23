import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(700, 300)
        self.move(300, 300)
        self.setWindowTitle('Demo QTableWidget')
        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        columnHeaders = ['Judul Buku', 'Penulis', 'Penerbit']
        self.table.setHorizontalHeaderLabels(columnHeaders)
        self.addRow(0, ['Python 3 Object Oriented Programming', 'Dusty Phillips', 'PACKT Publishing'])
        self.addRow(1, ['Numerical Python', 'Robert Johansson', 'Apress'])
        self.addRow(2, ['A Primer Scientific Programming with Python', 'Hans Peter Langtangen', 'Springer'])
        self.addRow(3, ['Beginning Ruby', 'Peter Cooper', 'Apress'])
        self.addRow(4, ['Ruby Under a Microscope', 'Pat Shaughnessy', 'No Starch Press'])
        self.lineEdit = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)
        self.table.itemClicked.connect(self.tableItemClick)
    def tableItemClick(self):
        item = self.table.currentItem()
        self.lineEdit.setText(item.text() + ' [baris: %d, kolom: %d]' % (self.table.currentRow(),
        self.table.currentColumn()))
    def addRow(self, row, itemLabels=[]):
        for i in range(0,3):
            item = QTableWidgetItem()
            item.setText(itemLabels[i])
            self.table.setItem(row, i, item)
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()