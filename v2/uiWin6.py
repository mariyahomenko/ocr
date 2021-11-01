from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window6(object):
    def setupUi(self, Window6):
        Window6.setObjectName("Window6")

        Window6.setFixedSize(360, 241)

        Window6.setStyleSheet("QMainWindow { \n"
                              "background: #674e4d\n"
                              "}\n"
                              "QTabWidget:pane {\n"
                              "background: #674e4d;\n"
                              "border-top: 1px solid #420c12;\n"
                              "\n"
                              "}\n"
                              "QTabBar:tab{\n"
                              "color: #d06814;\n"
                              "background: #4e3938;\n"
                              "border: 1px solid #420c12;\n"
                              "padding: 3px;\n"
                              "}\n"
                              "QTabBar:tab:selected{\n"
                              "background: #941f02;\n"
                              "border: 1px solid #112d60;\n"
                              "color: #112d60\n"
                              "}\n"
                              "QTextEdit {\n"
                              "color: #f1e2e0;\n"
                              "background: #674e4d;\n"
                              "}\n"
                              "")

        self.centralwidget = QtWidgets.QWidget(Window6)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Yandex-UI-Icons-Private")
        font.setPointSize(12)

        self.TabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(10, 10, 341, 211))
        self.TabWidget.setFont(font)
        self.TabWidget.setStyleSheet("")
        self.TabWidget.setObjectName("TabWidget")

        self.modeTab = QtWidgets.QWidget()
        self.modeTab.setObjectName("modeTab")

        self.modeTextEdit = QtWidgets.QTextEdit(self.modeTab)
        self.modeTextEdit.setGeometry(QtCore.QRect(10, 10, 321, 171))
        self.modeTextEdit.setFont(font)
        self.modeTextEdit.setObjectName("modeTextEdit")

        self.TabWidget.addTab(self.modeTab, "")

        self.langTab = QtWidgets.QWidget()
        self.langTab.setObjectName("langTab")

        self.langTextEdit = QtWidgets.QTextEdit(self.langTab)
        self.langTextEdit.setGeometry(QtCore.QRect(10, 10, 321, 171))
        self.langTextEdit.setFont(font)
        self.langTextEdit.setObjectName("langTextEdit")

        self.TabWidget.addTab(self.langTab, "")

        self.layoutTab = QtWidgets.QWidget()
        self.layoutTab.setObjectName("layoutTab")

        self.layoutTextEdit = QtWidgets.QTextEdit(self.layoutTab)
        self.layoutTextEdit.setGeometry(QtCore.QRect(10, 10, 321, 171))
        self.layoutTextEdit.setFont(font)
        self.layoutTextEdit.setObjectName("layoutTextEdit")

        self.TabWidget.addTab(self.layoutTab, "")

        self.filterTab = QtWidgets.QWidget()
        self.filterTab.setObjectName("filterTab")

        self.filterTextEdit = QtWidgets.QTextEdit(self.filterTab)
        self.filterTextEdit.setGeometry(QtCore.QRect(10, 10, 321, 171))
        self.filterTextEdit.setFont(font)
        self.filterTextEdit.setObjectName("filterTextEdit")

        self.TabWidget.addTab(self.filterTab, "")

        Window6.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window6)
        self.statusbar.setObjectName("statusbar")
        Window6.setStatusBar(self.statusbar)

        self.retranslateUi(Window6)
        self.TabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Window6)

    def retranslateUi(self, Window6):
        _translate = QtCore.QCoreApplication.translate
        Window6.setWindowTitle(_translate("Window6", "MainWindow"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.modeTab), _translate("Window6", " Режим "))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.langTab), _translate("Window6", " Язык "))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.layoutTab), _translate("Window6", " Разметка "))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.filterTab), _translate("Window6", " Фильтрация "))
