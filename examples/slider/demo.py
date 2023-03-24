# coding:utf-8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QSlider

from qfluentwidgets import HollowHandleStyle, Slider


class Demo1(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(300, 150)
        self.setStyleSheet("Demo1{background: rgb(184, 106, 106)}")

        # customize style
        style = {
            "sub-page.color": QColor(70, 23, 180)
        }
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setStyle(HollowHandleStyle(style))

        # need adjust height
        self.slider.resize(200, 28)
        self.slider.move(50, 61)


class Demo2(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(300, 150)

        self.slider = Slider(Qt.Horizontal, self)
        self.slider.setFixedWidth(200)
        self.slider.move(50, 61)

        self.setStyleSheet('Demo2{background: white}')


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w1 = Demo1()
    w1.show()
    w2 = Demo2()
    w2.show()
    sys.exit(app.exec_())
