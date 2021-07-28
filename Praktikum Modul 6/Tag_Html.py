import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication

# membuat kelas untuk applikasinya
class TextForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
        # mengatur ukuran dari widgetnya
		self.resize(400, 200)
		self.move(300, 300)
		self.setWindowTitle('Demo Tag HTML')

        # contoh membuat teks dengan tag html dan diberi warna merah
        # html nya head jadi tulisannya besar
		self.label1 = QLabel('<h1>Hello <font color=red>Afandi</font></h1>')
		self.label1.move(10, 10)
		self.label1.setParent(self)

        # berikut contoh tag html dengan cara miring, underline, dan tebal
		self.label2 = QLabel('''Teks ini dibuat dengan tag HTML. Teks dapat dijadikan <b>Tebal</b>
			<i>miring</i>, dan <u>Bergaris Bawah</i>''')
		self.label2.setWordWrap(True)
		self.label2.move(10,50)
		self.label2.setParent(self)


# tes untuk run saya jadikan dalam satu file
if __name__ == '__main__':
	a = QApplication(sys.argv)

	form = TextForm()
	form.show()
	a.exec_()
