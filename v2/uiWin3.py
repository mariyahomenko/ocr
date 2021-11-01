from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window3(object):
    def setupUi(self, Window3):
        Window3.setObjectName("Window3")

        Window3.setFixedSize(360, 170)

        Window3.setStyleSheet("QMainWindow { \n"
                              "background: #674e4d\n"
                              "}\n"
                              "QPushButton {\n"
                              "background: #4e3938;\n"
                              "color: #d06814;\n"
                              "border: 1px solid #420c12;\n"
                              "border-radius: 3px\n"
                              "}\n"
                              "QPushButton:hover {\n"
                              "background: #941f02;\n"
                              "border: 1px solid #112d60;\n"
                              "color: #112d60\n"
                              "}\n"
                              "QPushButton:pressed {\n"
                              "background: #420c12;\n"
                              "border: 1px solid #112d60;\n"
                              "color: #d06814\n"
                              "}")

        self.centralwidget = QtWidgets.QWidget(Window3)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Yandex-UI-Icons-Private")
        font.setPointSize(12)

        self.conditionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.conditionsButton.setGeometry(QtCore.QRect(20, 30, 321, 27))
        self.conditionsButton.setFont(font)
        self.conditionsButton.setObjectName("conditionsButton")

        self.modeButton = QtWidgets.QPushButton(self.centralwidget)
        self.modeButton.setGeometry(QtCore.QRect(20, 70, 321, 27))
        self.modeButton.setFont(font)
        self.modeButton.setObjectName("modeButton")

        self.langButton = QtWidgets.QPushButton(self.centralwidget)
        self.langButton.setGeometry(QtCore.QRect(20, 110, 321, 27))
        self.langButton.setFont(font)
        self.langButton.setObjectName("langButton")

        Window3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window3)
        self.statusbar.setObjectName("statusbar")
        Window3.setStatusBar(self.statusbar)

        self.retranslateUi(Window3)
        QtCore.QMetaObject.connectSlotsByName(Window3)

    def retranslateUi(self, Window3):
        _translate = QtCore.QCoreApplication.translate
        Window3.setWindowTitle(_translate("Window3", "MainWindow"))
        self.conditionsButton.setText(_translate("Window3", "Условия для распознавания"))
        self.modeButton.setText(_translate("Window3", "Настройки чтения экрана"))
        self.langButton.setText(_translate("Window3", "Настройка видео"))
