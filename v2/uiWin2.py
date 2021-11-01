from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window2(object):
    def setupUi(self, Window2):

        Window2.setObjectName("Window2")

        Window2.setFixedSize(351, 363)

        Window2.setStyleSheet("QMainWindow {\n"
                              "background: qlineargradient"
                              "(spread:pad, x1:0, y1:0, x2:1, y2:1,"
                              "stop:0 rgba(196, 42, 3, 255), "
                              "stop:1 rgba(66, 12, 18, 255))\n"
                              "}\n"
                              "QLabel {\n"
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
                              "QLineEdit {\n"
                              "background: #7c1908;\n"
                              "color: #d06814;\n"
                              "border: 1px solid #721507\n"
                              "}")

        self.centralwidget = QtWidgets.QWidget(Window2)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Yandex-UI-Icons-Private")
        font.setPointSize(12)

        self.labelTop = QtWidgets.QLabel(self.centralwidget)
        self.labelTop.setGeometry(QtCore.QRect(60, 50, 50, 13))
        self.labelTop.setFont(font)
        self.labelTop.setObjectName("labelTop")

        self.labelLeft = QtWidgets.QLabel(self.centralwidget)
        self.labelLeft.setGeometry(QtCore.QRect(200, 50, 50, 13))
        self.labelLeft.setFont(font)
        self.labelLeft.setObjectName("labelLeft")

        self.labelWidt = QtWidgets.QLabel(self.centralwidget)
        self.labelWidt.setGeometry(QtCore.QRect(60, 170, 50, 13))
        self.labelWidt.setFont(font)
        self.labelWidt.setObjectName("labelWidt")

        self.labelHeight = QtWidgets.QLabel(self.centralwidget)
        self.labelHeight.setGeometry(QtCore.QRect(200, 170, 50, 13))
        self.labelHeight.setFont(font)
        self.labelHeight.setObjectName("labelHeight")

        self.lineEditTop = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTop.setGeometry(QtCore.QRect(60, 80, 91, 24))
        self.lineEditTop.setFont(font)
        self.lineEditTop.setObjectName("lineEditTop")

        self.lineEditLeft = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLeft.setGeometry(QtCore.QRect(200, 80, 91, 24))
        self.lineEditLeft.setFont(font)
        self.lineEditLeft.setObjectName("lineEditLeft")

        self.lineEditWidt = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWidt.setGeometry(QtCore.QRect(60, 200, 91, 24))
        self.lineEditWidt.setFont(font)
        self.lineEditWidt.setObjectName("lineEditWidt")

        self.lineEditHeight = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditHeight.setGeometry(QtCore.QRect(200, 200, 91, 24))
        self.lineEditHeight.setFont(font)
        self.lineEditHeight.setObjectName("lineEditHeight")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(155, 280, 41, 31))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        Window2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window2)
        self.statusbar.setObjectName("statusbar")
        Window2.setStatusBar(self.statusbar)

        self.retranslateUi(Window2)
        QtCore.QMetaObject.connectSlotsByName(Window2)

    def retranslateUi(self, Window2):
        _translate = QtCore.QCoreApplication.translate
        Window2.setWindowTitle(_translate("Window2", "MainWindow"))
        self.labelTop.setText(_translate("Window2", "Top"))
        self.labelLeft.setText(_translate("Window2", "Left"))
        self.labelWidt.setText(_translate("Window2", "Widt"))
        self.labelHeight.setText(_translate("Window2", "Height"))
        self.pushButton.setText(_translate("Window2", "x"))
