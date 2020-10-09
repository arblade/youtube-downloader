from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
import sys
from app.Model import *
from app.yt_downloader import MyApp

if __name__ == '__main__':
    model=Model()
    app = QtWidgets.QApplication(sys.argv)
    form = MyApp()
    form.setWindowIcon(QtGui.QIcon(model.folder+'/icon.png'))
    form.setWindowTitle("Youtube-Downloader")
    form.show()
    app.exec_()