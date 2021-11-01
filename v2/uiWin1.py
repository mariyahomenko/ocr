from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")

        MainWindow.setFixedSize(351, 363)

        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "background: qlineargradient"
                                 "(spread:pad, x1:0, y1:0, x2:1, y2:1,"
                                 "stop:0 rgba(196, 42, 3, 255),"
                                 "stop:1 rgba(66, 12, 18, 255))\n"
                                 "}\n"
                                 "QLabel {\n"
                                 "border:1px solid #420c12;\n"
                                 "color: #d06814\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "background: qlineargradient"
                                 "(spread:pad, x1:0, y1:0, x2:1, y2:1,"
                                 "stop:0 rgba(119, 22, 32, 255),"
                                 "stop:1 rgba(140, 30, 2, 255));\n"
                                 "border: 1px solid qlineargradient"
                                 "(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                 "stop:0 rgba(196, 42, 3, 255), "
                                 "stop:1 rgba(66, 12, 18, 255));\n"
                                 "color: #d06814;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "background: #c42a03;\n"
                                 "border: 1px solid qlineargradient"
                                 "(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                 "stop:0 rgba(196, 42, 3, 255), "
                                 "stop:1 rgba(66, 12, 18, 255));\n"
                                 "color: #112d60\n"
                                 "}\n"
                                 "QPushButton:pressed {\n"
                                 "background: #420c12;\n"
                                 "border: 1px solid #112d60;\n"
                                 "color: #d06814\n"
                                 "}\n"
                                 "QToolButton {\n"
                                 "background: qlineargradient"
                                 "(spread:pad, x1:0, y1:0, x2:1, y2:1,"
                                 "stop:0 rgba(119, 22, 32, 255),"
                                 "stop:1 rgba(140, 30, 2, 255));\n"
                                 "border: 1px solid qlineargradient"
                                 "(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                 "stop:0 rgba(196, 42, 3, 255), "
                                 "stop:1 rgba(66, 12, 18, 255));\n"
                                 "color: #d06814\n"
                                 "}\n"
                                 "QToolButton:hover {\n"
                                 "background: #c42a03;\n"
                                 "border: 1px solid qlineargradient"
                                 "(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                 "stop:0 rgba(196, 42, 3, 255), "
                                 "stop:1 rgba(66, 12, 18, 255));\n"
                                 "color: #112d60\n"
                                 "}\n"
                                 "QToolButton:pressed {\n"
                                 "background: #420c12;\n"
                                 "border: 1px solid #112d60;\n"
                                 "color: #d06814\n"
                                 "}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Yandex-UI-Icons-Private")
        font.setPointSize(12)

        self.mapButton = QtWidgets.QPushButton(self.centralwidget)
        self.mapButton.setGeometry(QtCore.QRect(20, 310, 91, 22))
        self.mapButton.setFont(font)
        self.mapButton.setObjectName("mapButton")

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(130, 310, 91, 22))
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")

        self.dataButton = QtWidgets.QPushButton(self.centralwidget)
        self.dataButton.setGeometry(QtCore.QRect(240, 310, 91, 22))
        self.dataButton.setFont(font)
        self.dataButton.setObjectName("dataButton")

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(20, 10, 21, 19))
        self.toolButton.setObjectName("toolButton")

        font.setBold(True)
        font.setWeight(75)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 311, 161))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mapButton.setText(_translate("MainWindow", "Map"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.dataButton.setText(_translate("MainWindow", "Data"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Добрый день"))
