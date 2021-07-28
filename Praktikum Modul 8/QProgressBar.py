import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

## contoh penggunaan progres bar
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        ## mengatur ukuran dan posisi form
        self.setGeometry(300, 300, 280, 150)
        self.setWindowTitle('Demo QProgressBar')
        self.show()

        ## mengatur posisi dan ukuran progress bar
        self.pbar = QProgressBar(self)              # membuat progres bar
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)       # membuat button start
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()      # mendeklarasikan timer
        self.step = 0

        layout = QHBoxLayout()
        layout.addWidget(self.pbar)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    ## mengatur agar berhenti saat mencapai 100
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Selesai')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    ## mengatur tampilan tombol sesuai keadaan progress bar
    ## juga untuk menghentikan progressbar (pause)
    def doAction(self, e):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    sys.exit(app.exec_())
