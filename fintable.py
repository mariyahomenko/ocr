from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogII(object):
    def setupUi(self, DialogII):
        DialogII.setObjectName("DialogII")
        DialogII.resize(1000, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogII.sizePolicy().hasHeightForWidth())
        DialogII.setSizePolicy(sizePolicy)
        DialogII.setMaximumSize(QtCore.QSize(1000, 600))
        DialogII.setStyleSheet("QDialog {\n"
                                "background-color: #64a15f;\n"
                                "}\n"
                                "\n"
                                "QTableWidget{\n"
                                "background-color: #f5f5f5;\n"
                                "}\n"
                                "\n"
                                "QLabel {\n"
                                "color: #f5f5f5;\n"
                                " }\n"
                                "\n"
                                "QPushButton {\n"
                                "background: #d4e7ff;\n"
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

        self.centralwidget = QtWidgets.QWidget(DialogII)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(12)

        self.pushButton_100 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_100.setGeometry(QtCore.QRect(900, 561, 75, 30))
        self.pushButton_100.setObjectName("pushButton_100")
        self.pushButton_100.setFont(font)
        self.pushButton_100.setStyleSheet("QPushButton {\n"
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

        self.pushButton_800 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_800.setGeometry(QtCore.QRect(20, 561, 75, 30))
        self.pushButton_800.setObjectName("pushButton_800")
        self.pushButton_800.setFont(font)
        self.pushButton_800.setStyleSheet("QPushButton {\n"
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

        self.tableWidget = QtWidgets.QTableWidget(DialogII)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 961, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(43)
        self.tableWidget.setRowCount(26)
        item = QtWidgets.QTableWidgetItem()

        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


        self.tableWidget.setSpan(0, 0, 1, 3)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('I'.center(55)))
        self.tableWidget.item(0, 0).setBackground(QtGui.QColor(254, 151, 146))

        # 1
        self.tableWidget.setSpan(0, 3, 1, 2)
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 3).setBackground(QtGui.QColor(255, 231, 230))
        # 2
        self.tableWidget.setSpan(0, 5, 1, 2)
        self.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 5).setBackground(QtGui.QColor(255, 243, 242))
        # 3
        self.tableWidget.setSpan(0, 7, 1, 2)
        self.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 7).setBackground(QtGui.QColor(255, 231, 230))
        # 4
        self.tableWidget.setSpan(0, 9, 1, 2)
        self.tableWidget.setItem(0, 9, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 9).setBackground(QtGui.QColor(255, 243, 242))
        # 5
        self.tableWidget.setSpan(0, 11, 1, 2)
        self.tableWidget.setItem(0, 11, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 11).setBackground(QtGui.QColor(255, 231, 230))
        # 6
        self.tableWidget.setSpan(0, 13, 1, 2)
        self.tableWidget.setItem(0, 13, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 13).setBackground(QtGui.QColor(255, 243, 242))
        # 7
        self.tableWidget.setSpan(0, 15, 1, 2)
        self.tableWidget.setItem(0, 15, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 15).setBackground(QtGui.QColor(255, 231, 230))
        # 8
        self.tableWidget.setSpan(0, 17, 1, 2)
        self.tableWidget.setItem(0, 17, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 17).setBackground(QtGui.QColor(255, 243, 242))
        # 9
        self.tableWidget.setSpan(0, 19, 1, 2)
        self.tableWidget.setItem(0, 19, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 19).setBackground(QtGui.QColor(255, 231, 230))
        # 10
        self.tableWidget.setSpan(0, 21, 1, 2)
        self.tableWidget.setItem(0, 21, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 21).setBackground(QtGui.QColor(255, 243, 242))
        # 11
        self.tableWidget.setSpan(0, 23, 1, 2)
        self.tableWidget.setItem(0, 23, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 23).setBackground(QtGui.QColor(255, 231, 230))
        # 12
        self.tableWidget.setSpan(0, 25, 1, 2)
        self.tableWidget.setItem(0, 25, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 25).setBackground(QtGui.QColor(255, 243, 242))
        # 13
        self.tableWidget.setSpan(0, 27, 1, 2)
        self.tableWidget.setItem(0, 27, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 27).setBackground(QtGui.QColor(255, 231, 230))
        # 14
        self.tableWidget.setSpan(0, 29, 1, 2)
        self.tableWidget.setItem(0, 29, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 29).setBackground(QtGui.QColor(255, 243, 242))
        # 15
        self.tableWidget.setSpan(0, 31, 1, 2)
        self.tableWidget.setItem(0, 31, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 31).setBackground(QtGui.QColor(255, 231, 230))
        # 16
        self.tableWidget.setSpan(0, 33, 1, 2)
        self.tableWidget.setItem(0, 33, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 33).setBackground(QtGui.QColor(255, 243, 242))
        # 17
        self.tableWidget.setSpan(0, 35, 1, 2)
        self.tableWidget.setItem(0, 35, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 35).setBackground(QtGui.QColor(255, 231, 230))
        # 18
        self.tableWidget.setSpan(0, 37, 1, 2)
        self.tableWidget.setItem(0, 37, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 37).setBackground(QtGui.QColor(255, 243, 242))
        # 19
        self.tableWidget.setSpan(0, 39, 1, 2)
        self.tableWidget.setItem(0, 39, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 39).setBackground(QtGui.QColor(255, 231, 230))
        # 20
        self.tableWidget.setSpan(0, 41, 1, 2)
        self.tableWidget.setItem(0, 41, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(0, 41).setBackground(QtGui.QColor(255, 243, 242))



        self.tableWidget.setSpan(1, 0, 1, 2)
        self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem('II'.center(34)))
        self.tableWidget.item(1, 0).setBackground(QtGui.QColor(174, 200, 255))

        # 1
        self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(2, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 2
        self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(3, 0).setBackground(QtGui.QColor(242, 247, 255))
        # 3
        self.tableWidget.setItem(4, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(4, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 4
        self.tableWidget.setItem(5, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(5, 0).setBackground(QtGui.QColor(242, 247, 255))
        # 5
        self.tableWidget.setItem(6, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(6, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 6
        self.tableWidget.setItem(7, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(7, 0).setBackground(QtGui.QColor(242, 247, 255))
        # 7
        self.tableWidget.setItem(8, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(8, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 8
        self.tableWidget.setItem(9, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(9, 0).setBackground(QtGui.QColor(242, 247, 255))
        # 9
        self.tableWidget.setItem(10, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(10, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 10
        self.tableWidget.setItem(11, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(11, 0).setBackground(QtGui.QColor(242, 247, 255))
        # 11
        self.tableWidget.setItem(12, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(12, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 12
        self.tableWidget.setItem(13, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(13, 0).setBackground(QtGui.QColor(242, 247, 255))
        # 13
        self.tableWidget.setItem(14, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(14, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 14
        self.tableWidget.setItem(15, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(15, 0).setBackground(QtGui.QColor(242, 247, 255))
        # 15
        self.tableWidget.setItem(16, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(16, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 16
        self.tableWidget.setItem(17, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(17, 0).setBackground(QtGui.QColor(242, 247, 255))
        # 17
        self.tableWidget.setItem(18, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(18, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 18
        self.tableWidget.setItem(19, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(19, 0).setBackground(QtGui.QColor(242, 247, 255))
        # 19
        self.tableWidget.setItem(20, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(20, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 20
        self.tableWidget.setItem(21, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(21, 0).setBackground(QtGui.QColor(242, 247, 255))
        # 21
        self.tableWidget.setItem(22, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(22, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 22
        self.tableWidget.setItem(23, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(23, 0).setBackground(QtGui.QColor(242, 247, 255))
        # 23
        self.tableWidget.setItem(24, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(24, 0).setBackground(QtGui.QColor(230, 238, 255))
        # 24
        self.tableWidget.setItem(25, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(25, 0).setBackground(QtGui.QColor(242, 247, 255))



        self.tableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem('III'.center(15)))
        self.tableWidget.item(1, 2).setBackground(QtGui.QColor(252, 240, 203))

        # 1
        self.tableWidget.setItem(2, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(2, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 2
        self.tableWidget.setItem(3, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(3, 2).setBackground(QtGui.QColor(254, 252, 243))
        # 3
        self.tableWidget.setItem(4, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(4, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 4
        self.tableWidget.setItem(5, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(5, 2).setBackground(QtGui.QColor(254, 252, 243))
        # 5
        self.tableWidget.setItem(6, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(6, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 6
        self.tableWidget.setItem(7, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(7, 2).setBackground(QtGui.QColor(254, 252, 243))
        # 7
        self.tableWidget.setItem(8, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(8, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 8
        self.tableWidget.setItem(9, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(9, 2).setBackground(QtGui.QColor(254, 252, 243))
        # 9
        self.tableWidget.setItem(10, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(10, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 10
        self.tableWidget.setItem(11, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(11, 2).setBackground(QtGui.QColor(254, 252, 243))
        # 11
        self.tableWidget.setItem(12, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(12, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 12
        self.tableWidget.setItem(13, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(13, 2).setBackground(QtGui.QColor(254, 252, 243))
        # 13
        self.tableWidget.setItem(14, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(14, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 14
        self.tableWidget.setItem(15, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(15, 2).setBackground(QtGui.QColor(254, 252, 243))
        # 15
        self.tableWidget.setItem(16, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(16, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 16
        self.tableWidget.setItem(17, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(17, 2).setBackground(QtGui.QColor(254, 252, 243))
        # 17
        self.tableWidget.setItem(18, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(18, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 18
        self.tableWidget.setItem(19, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(19, 2).setBackground(QtGui.QColor(254, 252, 243))
        # 19
        self.tableWidget.setItem(20, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(20, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 20
        self.tableWidget.setItem(21, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(21, 2).setBackground(QtGui.QColor(254, 252, 243))
        # 21
        self.tableWidget.setItem(22, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(22, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 22
        self.tableWidget.setItem(23, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(23, 2).setBackground(QtGui.QColor(254, 252, 243))
        # 23
        self.tableWidget.setItem(24, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(24, 2).setBackground(QtGui.QColor(253, 247, 227))
        # 24
        self.tableWidget.setItem(25, 2, QtWidgets.QTableWidgetItem())
        self.tableWidget.item(25, 2).setBackground(QtGui.QColor(254, 252, 243))

        self.tableWidget.setSpan(1, 3, 1, 41)
        self.tableWidget.setItem(1, 3, QtWidgets.QTableWidgetItem('Start/Period'.center(1000)))
        self.tableWidget.item(1, 3).setBackground(QtGui.QColor(229, 229, 229))

        self.tableWidget.setSpan(2, 0, 1, 2)
        self.tableWidget.setSpan(3, 0, 1, 2)
        self.tableWidget.setSpan(4, 0, 1, 2)
        self.tableWidget.setSpan(5, 0, 1, 2)
        self.tableWidget.setSpan(6, 0, 1, 2)
        self.tableWidget.setSpan(7, 0, 1, 2)
        self.tableWidget.setSpan(8, 0, 1, 2)
        self.tableWidget.setSpan(9, 0, 1, 2)
        self.tableWidget.setSpan(10, 0, 1, 2)
        self.tableWidget.setSpan(11, 0, 1, 2)
        self.tableWidget.setSpan(12, 0, 1, 2)
        self.tableWidget.setSpan(13, 0, 1, 2)
        self.tableWidget.setSpan(14, 0, 1, 2)
        self.tableWidget.setSpan(15, 0, 1, 2)
        self.tableWidget.setSpan(16, 0, 1, 2)
        self.tableWidget.setSpan(17, 0, 1, 2)
        self.tableWidget.setSpan(18, 0, 1, 2)
        self.tableWidget.setSpan(19, 0, 1, 2)
        self.tableWidget.setSpan(20, 0, 1, 2)
        self.tableWidget.setSpan(21, 0, 1, 2)
        self.tableWidget.setSpan(22, 0, 1, 2)
        self.tableWidget.setSpan(23, 0, 1, 2)
        self.tableWidget.setSpan(24, 0, 1, 2)
        self.tableWidget.setSpan(25, 0, 1, 2)

        x = 25
        while x != 1:
            if x%2 == 0:
                self.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 3).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 4, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 4).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 5, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 5).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 6, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 6).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 7, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 7).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 8, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 8).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 9, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 9).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 10, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 10).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 11, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 11).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 12, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 12).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 13, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 13).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 14, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 14).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 15, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 15).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 16, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 16).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 17, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 17).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 18, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 18).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 19, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 19).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 20, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 20).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 21, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 21).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 22, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 22).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 23, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 23).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 24, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 24).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 25, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 25).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 26, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 26).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 27, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 27).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 28, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 28).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 29, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 29).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 30, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 30).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 31, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 31).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 32, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 32).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 33, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 33).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 34, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 34).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 35, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 35).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 36, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 36).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 37, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 37).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 38, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 38).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 39, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 39).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 40, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 40).setBackground(QtGui.QColor(255, 231, 230))
                self.tableWidget.setItem(x, 41, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 41).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 42, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 42).setBackground(QtGui.QColor(255, 243, 242))

            elif x%2 == 1:
                self.tableWidget.setItem(x, 3, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 3).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 4, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 4).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 5, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 5).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 6, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 6).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 7, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 7).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 8, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 8).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 9, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 9).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 10, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 10).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 11, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 11).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 12, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 12).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 13, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 13).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 14, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 14).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 15, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 15).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 16, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 16).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 17, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 17).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 18, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 18).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 19, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 19).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 20, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 20).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 21, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 21).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 22, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 22).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 23, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 23).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 24, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 24).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 25, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 25).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 26, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 26).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 27, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 27).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 28, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 28).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 29, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 29).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 30, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 30).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 31, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 31).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 32, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 32).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 33, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 33).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 34, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 34).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 35, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 35).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 36, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 36).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 37, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 37).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 38, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 38).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 39, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 39).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 40, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 40).setBackground(QtGui.QColor(255, 243, 242))
                self.tableWidget.setItem(x, 41, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 41).setBackground(QtGui.QColor(255, 249, 249))
                self.tableWidget.setItem(x, 42, QtWidgets.QTableWidgetItem())
                self.tableWidget.item(x, 42).setBackground(QtGui.QColor(255, 249, 249))

            x = x - 1

        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)

        self.retranslateUi(DialogII)
        QtCore.QMetaObject.connectSlotsByName(DialogII)

    def retranslateUi(self, DialogII):
        _translate = QtCore.QCoreApplication.translate
        DialogII.setWindowTitle(_translate("DialogII", "Data"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_100.setText(_translate("Dialog", "Save"))
        self.pushButton_800.setText(_translate("Dialog", "Period"))
