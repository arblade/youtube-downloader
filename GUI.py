# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 346)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setAccessibleName("")
        self.lineEdit.setAccessibleDescription("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setIconSize(QtCore.QSize(10, 10))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.lineEdit_link = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_link.setObjectName("lineEdit_link")
        self.gridLayout.addWidget(self.lineEdit_link, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.state = QtWidgets.QLabel(self.centralWidget)
        self.state.setWordWrap(True)
        self.state.setObjectName("state")
        self.verticalLayout.addWidget(self.state)
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 807, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.browseSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/name/icon_little.png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Link</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Directory "))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Path of download, default if empty"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.lineEdit_link.setPlaceholderText(_translate("MainWindow", "Link of the video or playlist"))
        self.checkBox.setText(_translate("MainWindow", "playlist in separate folder"))
        self.state.setText(_translate("MainWindow", "<html><head/><body><p>State : None</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
import test_rc
