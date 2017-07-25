from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from matplotlib import pylab as pt

class RownaniaKwadratowe(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self)

        self.interfejs()

    def interfejs(self):
        etyk1 = QLabel("f(x) = ", self)
        etyk2 = QLabel("x^2 + ", self)
        etyk3 = QLabel("x + ", self)

        self.wsp_a = QLineEdit()
        self.wsp_b = QLineEdit()
        self.wsp_c = QLineEdit()
        self.wzor = QLineEdit()

        self.poka_wyk = QPushButton("Pokaż &wykres!")
        self.poka_fun = QPushButton("Pokaż &funkcję!")

        uklad = QGridLayout()
        uklad.addWidget(etyk1, 0, 0)
        uklad.addWidget(self.wsp_a, 0, 1)
        uklad.addWidget(etyk2, 0, 2)
        uklad.addWidget(self.wsp_b, 0, 3)
        uklad.addWidget(etyk3, 0, 4)
        uklad.addWidget(self.wsp_c, 0, 5)
        uklad.addWidget(self.poka_fun, 1, 0, 1, 6)
        uklad.addWidget(self.poka_wyk, 2, 0, 1, 6)
        uklad.addWidget(self.wzor, 3, 0, 1, 6)

        self.setLayout(uklad)

        self.poka_wyk.clicked.connect(self.rysuj)
        self.poka_fun.clicked.connect(self.funkcja)

        self.resize(300, 100)
        self.setWindowTitle("Vincent")

        self.show()

    def funkcja(self):
        wypis = "{}x + {}x^2 + {}".format(self.wsp_a.text(), self.wsp_b.text(), self.wsp_c.text())
        self.wzor.setText(str(wypis))

    def rysuj(self):
        x_tab = []
        y_tab = []
        xmin = -10
        xmax = 10
        ymin = -10
        ymax = 10
        skok = 1

        while xmin <= xmax:
            y = float(self.wsp_a.text()) * xmin ** 2 + float(self.wsp_b.text()) * xmin + float(self.wsp_c.text())
            x_tab.append(xmin)
            y_tab.append(y)
            xmin += skok
        pt.plot(x_tab, y_tab)
        pt.grid()
        pt.show()


    def Koniec(self):
        self.close()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = RownaniaKwadratowe()
    sys.exit(app.exec_())