# contoh signal and slot
# dan membuat full dari qtdesigner

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 208)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 40, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nameEdit = QtWidgets.QLineEdit(Form)
        self.nameEdit.setGeometry(QtCore.QRect(80, 90, 241, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 140, 239, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hallo = QtWidgets.QPushButton(self.layoutWidget)
        self.hallo.setObjectName("hallo")
        self.horizontalLayout.addWidget(self.hallo)
        self.clear = QtWidgets.QPushButton(self.layoutWidget)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.exit = QtWidgets.QPushButton(self.layoutWidget)
        self.exit.setObjectName("exit")
        self.horizontalLayout.addWidget(self.exit)

        self.retranslateUi(Form)
        self.clear.clicked.connect(self.nameEdit.clear)
        self.exit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Masukkan Nama Anda :"))
        self.hallo.setText(_translate("Form", "Halo"))
        self.clear.setText(_translate("Form", "Clear"))
        self.exit.setText(_translate("Form", "Keluar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
