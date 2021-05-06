# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nama2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from GUI2 import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class DemoQtDesainer(QDialog):
        def __init__(self,parent = None):
            QDialog. __init__(self,parent)
            self.ui = Ui_Form()
            self.ui.setupUi(self)
            self.ui.hallo.clicked.connect(self.halloClicked)

        def halloClicked(self):
            QMessageBox.information(self, 'Demo Qt Designer','Hallo %s, apa kabar?' % self.ui.nameEdit.text())


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(505, 332)
        self.MasukanNamaAnda = QtWidgets.QLabel(Form)
        self.MasukanNamaAnda.setGeometry(QtCore.QRect(170, 70, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MasukanNamaAnda.setFont(font)
        self.MasukanNamaAnda.setObjectName("MasukanNamaAnda")
        self.namaEdit = QtWidgets.QLineEdit(Form)
        self.namaEdit.setGeometry(QtCore.QRect(120, 110, 291, 20))
        self.namaEdit.setObjectName("namaEdit")
        self.Hallo = QtWidgets.QPushButton(Form)
        self.Hallo.setGeometry(QtCore.QRect(170, 160, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Hallo.setFont(font)
        self.Hallo.setObjectName("Hallo")
        self.Keluar = QtWidgets.QPushButton(Form)
        self.Keluar.setGeometry(QtCore.QRect(230, 200, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Keluar.setFont(font)
        self.Keluar.setObjectName("Keluar")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(290, 160, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MasukanNamaAnda.setText(_translate("Form", "MASUKAN NAMA ANDA :"))
        self.Hallo.setText(_translate("Form", "Hallo"))
        self.Keluar.setText(_translate("Form", "Exit"))
        self.clear.setText(_translate("Form", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

