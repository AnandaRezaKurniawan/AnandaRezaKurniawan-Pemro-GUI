from PyQt5.QtWidgets import QWidget, QPushButton

class OtherForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        # mengatur ukuran form dan posisi
        self.resize(400, 300)
        self.move(500, 300)
        self.setWindowTitle("Form lainnya")

        # membuat button tutup
        self.button = QPushButton('TUTUP')
        self.button.move(150,150)
        self.button.setParent(self)

        self.button.clicked.connect(self.buttonClicked)

    # mendefinisikan fungsi buttonClicked, dimana disini di close
    def buttonClicked(self):
        self.close()
