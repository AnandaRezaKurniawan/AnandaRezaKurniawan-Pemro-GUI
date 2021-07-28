import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## implementasi contoh QTree
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        ## setting ukuran dan posisi
        self.resize(700, 300)
        self.move(300, 300)
        self.setWindowTitle('Demo QTreeWidget')

        ## konten dari form
        self.tree = QTreeWidget()               # membuat tree
        self.tree.setColumnCount(3)             # deklarasi kolom tree

        # deklarasi variabel dengan datanya untuk header kolom
        columnHeaders = ['Judul Buku', 'Penulis', 'Penerbit']
        self.tree.setHeaderLabels(columnHeaders)    # set variabel menjadi header
        parent1 = self.addTopLevel('Python')        # deklarasi parent 1 dengan nama python

        ## isi data dari parent 1
        self.addChild(parent1, 'Python 3 Object Oriented Programming',
            'Dusty Phillips', 'PACKT Publishing')
        self.addChild(parent1, 'Numerical Python', 'Robert Johansson', 'Apress')
        self.addChild(parent1, 'A Primer Scientific Programming with Python',
            'Hans Peter Langtangen', 'Springer')

        ## sama seperti parent 1 prosesnya
        parent2 = self.addTopLevel('Ruby')
        self.addChild(parent2, 'Beginning Ruby', 'Peter Cooper', 'Apress')
        self.addChild(parent2, 'Ruby Under a Microscope', 'Pat Shaughnessy',
            'No Starch Press')

        self.lineEdit = QLineEdit()         # membuat line edit
        # merapihkan widget
        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)
        self.tree.itemClicked.connect(self.treeItemClick)

    ## tujuannya nanti akan muncul nama dari judul ke line edit
    def treeItemClick(self):
        item = self.tree.currentItem()
        self.lineEdit.setText(item.text(0))
    # mengatur vategory sebagai root nya
    def addTopLevel(self, category):
        item = QTreeWidgetItem()
        item.setText(0, category)
        self.tree.addTopLevelItem(item)
        return item
    # menambahkan item sebagai child
    def addChild(self, parent, title, author, publisher):
        item = QTreeWidgetItem(parent)
        item.setText(0, title)
        item.setText(1, author)
        item.setText(2, publisher)
        parent.addChild(item)
        return item

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
