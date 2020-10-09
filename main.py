from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
import sys
from app.Model import *
from app.yt_downloader import MyApp
import app.test_rc

if __name__ == '__main__':
    model=Model()
    app = QtWidgets.QApplication(sys.argv)
    form = MyApp(model)
    model.dir=os.path.dirname(os.path.abspath(__file__))
    model.config=model.dir+'/config.txt'
    form.setWindowIcon(QtGui.QIcon(model.dir+'/assets/icon.png'))
    form.setWindowTitle("Youtube-Downloader")
    form.show()
    app.exec_()