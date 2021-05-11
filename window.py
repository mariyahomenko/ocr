from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(390, 477)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "background-color: #3b5f38;\n"
                                 "}\n"
                                 "QLabel {\n"
                                 "color: #d6ffd4;\n"
                                 "}\n"
                                 "QTextEdit {\n"
                                 "background-color: #64a15f;\n"
                                 "color: #f5f5f5;\n"
                                 "}\n"
                                 "QCheckBox {\n"
                                 "color: #d6ffd4;\n"
                                 " }\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "background: #d6ffd4;\n"
                                 "border: 1px solid #7f3a19;\n"
                                 "border-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "background: #ffff52;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "background: #e1ffdc;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 10, 351, 71))
        self.line.setStyleSheet("border-width: 2px;\n"
                                "border-style: dotted;\n"
                                "border-color: #c6c6c6;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 46, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 331, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.pushButton_100 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_100.setGeometry(QtCore.QRect(260, 430, 112, 27))
        self.pushButton_100.setObjectName("pushButton_100")
        self.pushButton_100.setFont(font)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout.addWidget(self.checkBox_6)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 100, 351, 311))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(20, 430, 112, 27))
        self.pushButton_55 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_55.setGeometry(QtCore.QRect(170, 430, 56, 27))
        self.pushButton_555 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_555.setFont(font)
        self.pushButton_555.setObjectName("pushButton_555")
        self.pushButton_555.setGeometry(QtCore.QRect(170, 430, 56, 27))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 395, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timer = QtCore.QTimer()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Win"))
        self.label.setText(_translate("MainWindow", "Areas"))
        self.checkBox.setText(_translate("MainWindow", "1"))
        self.checkBox_2.setText(_translate("MainWindow", "2"))
        self.checkBox_3.setText(_translate("MainWindow", "3"))
        self.checkBox_4.setText(_translate("MainWindow", "4"))
        self.checkBox_5.setText(_translate("MainWindow", "5"))
        self.checkBox_6.setText(_translate("MainWindow", "6"))
        self.pushButton.setText(_translate("MainWindow", "Map"))
        self.pushButton_55.setText(_translate("MainWindow", "Start"))
        self.pushButton_555.setText(_translate("MainWindow", "Stop"))
        self.pushButton_100.setText(_translate("MainWindow", "Data"))
