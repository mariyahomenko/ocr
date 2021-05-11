from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1034, 383)
        Dialog.setMaximumSize(QtCore.QSize(1034, 383))
        Dialog.setStyleSheet("QDialog {\n"
                             "background-color: #64a15f;\n"
                             "color: #f5f5f5;\n"
                             "}\n"
                             "QLabel {\n"
                             "color: #f5f5f5;\n"
                             "background-color: #64a15f;\n"
                             "}"
                             "QCheckBox {\n"
                             "color: #5d64a1;\n"
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
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(12)

  #      self.line = QtWidgets.QFrame(Dialog)
  #      self.line.setGeometry(QtCore.QRect(20, 30, 241, 331))
  #      self.line.setStyleSheet("border-width: 2px;\n"
  #                              "border-style: dotted;\n"
  #                              "border-color: #c6c6c6;")
  #      self.line.setFrameShape(QtWidgets.QFrame.HLine)
  #      self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
  #      self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(170, 270, 81, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(420, 270, 81, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

  #      self.line_4 = QtWidgets.QFrame(Dialog)
  #      self.line_4.setGeometry(QtCore.QRect(270, 30, 241, 331))
  #      self.line_4.setStyleSheet("border-width: 2px;\n"
  #                                "border-style: dotted;\n"
  #                                "border-color: #c6c6c6;")
  #      self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
  #      self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
  #      self.line_4.setObjectName("line_4")

        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(670, 270, 81, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

   #     self.line_6 = QtWidgets.QFrame(Dialog)
   #     self.line_6.setGeometry(QtCore.QRect(520, 30, 241, 331))
   #     self.line_6.setStyleSheet("border-width: 2px;\n"
   #                               "border-style: dotted;\n"
   #                               "border-color: #c6c6c6;")
   #     self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
   #     self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
   #     self.line_6.setObjectName("line_6")

        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(920, 270, 81, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

    #    self.line_8 = QtWidgets.QFrame(Dialog)
    #    self.line_8.setGeometry(QtCore.QRect(770, 30, 241, 331))
    #    self.line_8.setStyleSheet("border-width: 2px;\n"
    #                              "border-style: dotted;\n"
    #                              "border-color: #c6c6c6;")
    #    self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
    #    self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
    #    self.line_8.setObjectName("line_8")


        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(235, 90, 20, 20))
        self.checkBox.setObjectName('checkBox')

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(235, 120, 20, 20))
        self.checkBox_2.setObjectName('checkBox_2')

        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(235, 150, 20, 20))
        self.checkBox_3.setObjectName('checkBox_3')

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(235, 180, 20, 20))
        self.checkBox_4.setObjectName('checkBox_4')

        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(235, 210, 20, 20))
        self.checkBox_5.setObjectName('checkBox_5')

        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(235, 240, 20, 20))
        self.checkBox_6.setObjectName('checkBox_6')

        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(485, 90, 20, 20))
        self.checkBox_7.setObjectName('checkBox_7')

        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(485, 120, 20, 20))
        self.checkBox_8.setObjectName('checkBox_8')

        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(485, 150, 20, 20))
        self.checkBox_9.setObjectName('checkBox_7')

        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(485, 180, 20, 20))
        self.checkBox_10.setObjectName('checkBox_10')

        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(485, 210, 20, 20))
        self.checkBox_11.setObjectName('checkBox_11')

        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setGeometry(QtCore.QRect(485, 240, 20, 20))
        self.checkBox_12.setObjectName('checkBox_12')

        self.checkBox_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_13.setGeometry(QtCore.QRect(735, 240, 20, 20))
        self.checkBox_13.setObjectName('checkBox_13')

        self.checkBox_14 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_14.setGeometry(QtCore.QRect(735, 210, 20, 20))
        self.checkBox_14.setObjectName('checkBox_14')

        self.checkBox_15 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_15.setGeometry(QtCore.QRect(735, 180, 20, 20))
        self.checkBox_15.setObjectName('checkBox_15')

        self.checkBox_16 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_16.setGeometry(QtCore.QRect(735, 150, 20, 20))
        self.checkBox_16.setObjectName('checkBox_16')

        self.checkBox_17 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_17.setGeometry(QtCore.QRect(735, 120, 20, 20))
        self.checkBox_17.setObjectName('checkBox_17')

        self.checkBox_18 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_18.setGeometry(QtCore.QRect(735, 90, 20, 20))
        self.checkBox_18.setObjectName('checkBox_18')

        self.checkBox_19 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_19.setGeometry(QtCore.QRect(985, 240, 20, 20))
        self.checkBox_19.setObjectName('checkBox_19')

        self.checkBox_20 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_20.setGeometry(QtCore.QRect(985, 210, 20, 20))
        self.checkBox_20.setObjectName('checkBox_20')

        self.checkBox_21 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_21.setGeometry(QtCore.QRect(985, 180, 20, 20))
        self.checkBox_21.setObjectName('checkBox_21')

        self.checkBox_22 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_22.setGeometry(QtCore.QRect(985, 150, 20, 20))
        self.checkBox_22.setObjectName('checkBox_22')

        self.checkBox_23 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_23.setGeometry(QtCore.QRect(985, 120, 20, 20))
        self.checkBox_23.setObjectName('checkBox_23')

        self.checkBox_24 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_24.setGeometry(QtCore.QRect(985, 90, 20, 20))
        self.checkBox_24.setObjectName('checkBox_24')

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(165, 90, 61, 20))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 90, 61, 20))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 120, 61, 20))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(165, 120, 61, 20))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 150, 61, 20))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(165, 150, 61, 20))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 180, 61, 20))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 210, 61, 20))
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(100, 240, 61, 20))
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(165, 180, 61, 20))
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.lineEdit_11 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(165, 210, 61, 20))
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")

        self.lineEdit_12 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(165, 240, 61, 20))
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")

        self.lineEdit_13 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_13.setGeometry(QtCore.QRect(100, 280, 61, 20))
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")

        self.lineEdit_14 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_14.setGeometry(QtCore.QRect(100, 310, 61, 20))
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")

        self.lineEdit_15 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_15.setGeometry(QtCore.QRect(350, 90, 61, 20))
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName("lineEdit_15")

        self.lineEdit_16 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_16.setGeometry(QtCore.QRect(350, 280, 61, 20))
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setObjectName("lineEdit_16")

        self.lineEdit_17 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_17.setGeometry(QtCore.QRect(415, 210, 61, 20))
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setObjectName("lineEdit_17")

        self.lineEdit_18 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_18.setGeometry(QtCore.QRect(350, 150, 61, 20))
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setObjectName("lineEdit_18")

        self.lineEdit_19 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_19.setGeometry(QtCore.QRect(350, 310, 61, 20))
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setObjectName("lineEdit_19")

        self.lineEdit_20 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_20.setGeometry(QtCore.QRect(415, 150, 61, 20))
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setObjectName("lineEdit_20")

        self.lineEdit_21 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_21.setGeometry(QtCore.QRect(350, 180, 61, 20))
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setObjectName("lineEdit_21")

        self.lineEdit_22 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_22.setGeometry(QtCore.QRect(415, 90, 61, 20))
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setObjectName("lineEdit_22")

        self.lineEdit_23 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_23.setGeometry(QtCore.QRect(415, 120, 61, 20))
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setObjectName("lineEdit_23")

        self.lineEdit_24 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_24.setGeometry(QtCore.QRect(350, 210, 61, 20))
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setObjectName("lineEdit_24")

        self.lineEdit_25 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_25.setGeometry(QtCore.QRect(350, 240, 61, 20))
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setObjectName("lineEdit_25")

        self.lineEdit_26 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_26.setGeometry(QtCore.QRect(415, 180, 61, 20))
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setObjectName("lineEdit_26")

        self.lineEdit_27 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_27.setGeometry(QtCore.QRect(415, 240, 61, 20))
        self.lineEdit_27.setFont(font)
        self.lineEdit_27.setObjectName("lineEdit_27")

        self.lineEdit_28 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_28.setGeometry(QtCore.QRect(350, 120, 61, 20))
        self.lineEdit_28.setFont(font)
        self.lineEdit_28.setObjectName("lineEdit_28")

        self.lineEdit_29 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_29.setGeometry(QtCore.QRect(600, 90, 61, 20))
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setObjectName("lineEdit_29")

        self.lineEdit_30 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_30.setGeometry(QtCore.QRect(600, 280, 61, 20))
        self.lineEdit_30.setFont(font)
        self.lineEdit_30.setObjectName("lineEdit_30")

        self.lineEdit_31 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_31.setGeometry(QtCore.QRect(665, 210, 61, 20))
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setObjectName("lineEdit_31")

        self.lineEdit_32 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_32.setGeometry(QtCore.QRect(600, 150, 61, 20))
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setObjectName("lineEdit_32")

        self.lineEdit_33 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_33.setGeometry(QtCore.QRect(600, 310, 61, 20))
        self.lineEdit_33.setFont(font)
        self.lineEdit_33.setObjectName("lineEdit_33")

        self.lineEdit_34 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_34.setGeometry(QtCore.QRect(665, 150, 61, 20))
        self.lineEdit_34.setFont(font)
        self.lineEdit_34.setObjectName("lineEdit_34")

        self.lineEdit_35 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_35.setGeometry(QtCore.QRect(600, 180, 61, 20))
        self.lineEdit_35.setFont(font)
        self.lineEdit_35.setObjectName("lineEdit_35")

        self.lineEdit_36 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_36.setGeometry(QtCore.QRect(665, 90, 61, 20))
        self.lineEdit_36.setFont(font)
        self.lineEdit_36.setObjectName("lineEdit_36")

        self.lineEdit_37 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_37.setGeometry(QtCore.QRect(665, 120, 61, 20))
        self.lineEdit_37.setFont(font)
        self.lineEdit_37.setObjectName("lineEdit_37")

        self.lineEdit_38 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_38.setGeometry(QtCore.QRect(600, 210, 61, 20))
        self.lineEdit_38.setFont(font)
        self.lineEdit_38.setObjectName("lineEdit_38")

        self.lineEdit_39 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_39.setGeometry(QtCore.QRect(600, 240, 61, 20))
        self.lineEdit_39.setFont(font)
        self.lineEdit_39.setObjectName("lineEdit_39")

        self.lineEdit_40 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_40.setGeometry(QtCore.QRect(665, 180, 61, 20))
        self.lineEdit_40.setFont(font)
        self.lineEdit_40.setObjectName("lineEdit_40")

        self.lineEdit_41 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_41.setGeometry(QtCore.QRect(665, 240, 61, 20))
        self.lineEdit_41.setFont(font)
        self.lineEdit_41.setObjectName("lineEdit_41")

        self.lineEdit_42 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_42.setGeometry(QtCore.QRect(600, 120, 61, 20))
        self.lineEdit_42.setFont(font)
        self.lineEdit_42.setObjectName("lineEdit_42")

        self.lineEdit_43 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_43.setGeometry(QtCore.QRect(850, 90, 61, 20))
        self.lineEdit_43.setFont(font)
        self.lineEdit_43.setObjectName("lineEdit_43")

        self.lineEdit_44 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_44.setGeometry(QtCore.QRect(850, 280, 61, 20))
        self.lineEdit_44.setFont(font)
        self.lineEdit_44.setObjectName("lineEdit_44")

        self.lineEdit_45 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_45.setGeometry(QtCore.QRect(915, 210, 61, 20))
        self.lineEdit_45.setFont(font)
        self.lineEdit_45.setObjectName("lineEdit_45")

        self.lineEdit_46 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_46.setGeometry(QtCore.QRect(850, 150, 61, 20))
        self.lineEdit_46.setFont(font)
        self.lineEdit_46.setObjectName("lineEdit_46")

        self.lineEdit_47 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_47.setGeometry(QtCore.QRect(850, 310, 61, 20))
        self.lineEdit_47.setFont(font)
        self.lineEdit_47.setObjectName("lineEdit_47")

        self.lineEdit_48 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_48.setGeometry(QtCore.QRect(915, 150, 61, 20))
        self.lineEdit_48.setFont(font)
        self.lineEdit_48.setObjectName("lineEdit_48")

        self.lineEdit_49 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_49.setGeometry(QtCore.QRect(850, 180, 61, 20))
        self.lineEdit_49.setFont(font)
        self.lineEdit_49.setObjectName("lineEdit_49")

        self.lineEdit_50 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_50.setGeometry(QtCore.QRect(915, 90, 61, 20))
        self.lineEdit_50.setFont(font)
        self.lineEdit_50.setObjectName("lineEdit_50")

        self.lineEdit_51 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_51.setGeometry(QtCore.QRect(915, 120, 61, 20))
        self.lineEdit_51.setFont(font)
        self.lineEdit_51.setObjectName("lineEdit_51")

        self.lineEdit_52 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_52.setGeometry(QtCore.QRect(850, 210, 61, 20))
        self.lineEdit_52.setFont(font)
        self.lineEdit_52.setObjectName("lineEdit_52")

        self.lineEdit_53 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_53.setGeometry(QtCore.QRect(850, 240, 61, 20))
        self.lineEdit_53.setFont(font)
        self.lineEdit_53.setObjectName("lineEdit_53")

        self.lineEdit_54 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_54.setGeometry(QtCore.QRect(915, 180, 61, 20))
        self.lineEdit_54.setFont(font)
        self.lineEdit_54.setObjectName("lineEdit_54")

        self.lineEdit_55 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_55.setGeometry(QtCore.QRect(915, 240, 61, 20))
        self.lineEdit_55.setFont(font)
        self.lineEdit_55.setObjectName("lineEdit_55")

        self.lineEdit_56 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_56.setGeometry(QtCore.QRect(850, 120, 61, 20))
        self.lineEdit_56.setFont(font)
        self.lineEdit_56.setObjectName("lineEdit_56")

        self.pushButton_400 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_400.setGeometry(QtCore.QRect(924, 290, 71, 40))
        self.pushButton_400.setObjectName("pushButton_400")
        self.pushButton_400.setFont(font)
        self.pushButton_400.setIconSize(QSize(40, 40))
        self.pushButton_400.setStyleSheet("QPushButton {\n"
                                          "background: #d6ffd4;\n"
                                          "border: 1px solid #7f3a19;\n"
                                          "border-radius: 20px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: #ffff52;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "background: #e1ffdc;\n"
                                          "}")

        self.pushButton_300 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_300.setGeometry(QtCore.QRect(674, 290, 71, 40))
        self.pushButton_300.setObjectName("pushButton_300")
        self.pushButton_300.setFont(font)
        self.pushButton_300.setIconSize(QSize(40, 40))
        self.pushButton_300.setStyleSheet("QPushButton {\n"
                                          "background: #d6ffd4;\n"
                                          "border: 1px solid #7f3a19;\n"
                                          "border-radius: 20px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: #ffff52;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "background: #e1ffdc;\n"
                                          "}")

        self.pushButton_200 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_200.setGeometry(QtCore.QRect(424, 290, 71, 40))
        self.pushButton_200.setObjectName("pushButton_200")
        self.pushButton_200.setFont(font)
        self.pushButton_200.setIconSize(QSize(40, 40))
        self.pushButton_200.setStyleSheet("QPushButton {\n"
                                          "background: #d6ffd4;\n"
                                          "border: 1px solid #7f3a19;\n"
                                          "border-radius: 20px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: #ffff52;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "background: #e1ffdc;\n"
                                          "}")

        self.pushButton_100 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_100.setGeometry(QtCore.QRect(174, 290, 71, 40))
        self.pushButton_100.setObjectName("pushButton_100")
        self.pushButton_100.setFont(font)
        self.pushButton_100.setIconSize(QSize(40,40))
        self.pushButton_100.setStyleSheet("QPushButton {\n"
                                          "background: #d6ffd4;\n"
                                          "border: 1px solid #7f3a19;\n"
                                          "border-radius: 20px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "background: #ffff52;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "background: #e1ffdc;\n"
                                          "}")

        self.pushButton_1000 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1000.setGeometry(QtCore.QRect(985, 350, 40, 25))
        self.pushButton_1000.setObjectName("pushButton_1000")
        self.pushButton_1000.setFont(font)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 150, 19))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(125, 60, 10, 19))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 60, 10, 19))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 53, 19))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 53, 19))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 150, 53, 19))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 180, 53, 19))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 210, 53, 19))
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 240, 53, 19))
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(30, 280, 58, 19))
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(30, 310, 58, 19))
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(280, 90, 53, 19))
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(280, 10, 150, 19))
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(280, 210, 53, 19))
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")

        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(280, 150, 53, 19))
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(280, 120, 53, 19))
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(375, 60, 28, 19))
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(280, 180, 53, 19))
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")

        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(280, 280, 58, 19))
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")

        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(280, 310, 58, 19))
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")

        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(280, 240, 53, 19))
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")

        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(440, 58, 26, 21))
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")

        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(530, 90, 53, 19))
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")

        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(530, 10, 150, 19))
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")

        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(530, 210, 53, 19))
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")

        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(530, 150, 53, 19))
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")

        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(530, 120, 53, 19))
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")

        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(625, 60, 28, 19))
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")

        self.label_29 = QtWidgets.QLabel(Dialog)
        self.label_29.setGeometry(QtCore.QRect(530, 180, 53, 19))
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")

        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(530, 280, 58, 19))
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")

        self.label_31 = QtWidgets.QLabel(Dialog)
        self.label_31.setGeometry(QtCore.QRect(530, 310, 58, 19))
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")

        self.label_32 = QtWidgets.QLabel(Dialog)
        self.label_32.setGeometry(QtCore.QRect(530, 240, 53, 19))
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")

        self.label_33 = QtWidgets.QLabel(Dialog)
        self.label_33.setGeometry(QtCore.QRect(690, 60, 26, 19))
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")

        self.label_34 = QtWidgets.QLabel(Dialog)
        self.label_34.setGeometry(QtCore.QRect(780, 90, 53, 19))
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")

        self.label_35 = QtWidgets.QLabel(Dialog)
        self.label_35.setGeometry(QtCore.QRect(780, 10, 150, 19))
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")

        self.label_36 = QtWidgets.QLabel(Dialog)
        self.label_36.setGeometry(QtCore.QRect(780, 210, 53, 19))
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")

        self.label_37 = QtWidgets.QLabel(Dialog)
        self.label_37.setGeometry(QtCore.QRect(780, 150, 53, 19))
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")

        self.label_38 = QtWidgets.QLabel(Dialog)
        self.label_38.setGeometry(QtCore.QRect(780, 120, 53, 19))
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")

        self.label_39 = QtWidgets.QLabel(Dialog)
        self.label_39.setGeometry(QtCore.QRect(875, 60, 28, 19))
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")

        self.label_40 = QtWidgets.QLabel(Dialog)
        self.label_40.setGeometry(QtCore.QRect(780, 180, 53, 19))
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")

        self.label_41 = QtWidgets.QLabel(Dialog)
        self.label_41.setGeometry(QtCore.QRect(780, 280, 58, 19))
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")

        self.label_42 = QtWidgets.QLabel(Dialog)
        self.label_42.setGeometry(QtCore.QRect(780, 310, 58, 19))
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")

        self.label_43 = QtWidgets.QLabel(Dialog)
        self.label_43.setGeometry(QtCore.QRect(780, 240, 53, 19))
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")

        self.label_44 = QtWidgets.QLabel(Dialog)
        self.label_44.setGeometry(QtCore.QRect(940, 60, 26, 19))
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Map"))
        self.label.setText(_translate("Dialog", "I"))
        self.label_2.setText(_translate("Dialog", "Y"))
        self.label_3.setText(_translate("Dialog", "X"))
        self.label_4.setText(_translate("Dialog", "1"))
        self.lineEdit.setText(_translate("Dialog", "0"))
        self.lineEdit_2.setText(_translate("Dialog", "0"))
        self.label_5.setText(_translate("Dialog", "2"))
        self.label_6.setText(_translate("Dialog", "3"))
        self.label_7.setText(_translate("Dialog", "4"))
        self.label_8.setText(_translate("Dialog", "5"))
        self.label_9.setText(_translate("Dialog", "6"))
        self.lineEdit_3.setText(_translate("Dialog", "0"))
        self.lineEdit_4.setText(_translate("Dialog", "0"))
        self.lineEdit_5.setText(_translate("Dialog", "0"))
        self.lineEdit_6.setText(_translate("Dialog", "0"))
        self.lineEdit_7.setText(_translate("Dialog", "0"))
        self.lineEdit_8.setText(_translate("Dialog", "0"))
        self.lineEdit_9.setText(_translate("Dialog", "0"))
        self.lineEdit_10.setText(_translate("Dialog", "0"))
        self.lineEdit_11.setText(_translate("Dialog", "0"))
        self.lineEdit_12.setText(_translate("Dialog", "0"))
        self.label_10.setText(_translate("Dialog", "W"))
        self.label_11.setText(_translate("Dialog", "H"))
        self.lineEdit_13.setText(_translate("Dialog", "0"))
        self.lineEdit_14.setText(_translate("Dialog", "0"))
        self.lineEdit_15.setText(_translate("Dialog", "0"))
        self.label_12.setText(_translate("Dialog", "1"))
        self.lineEdit_16.setText(_translate("Dialog", "0"))
        self.label_13.setText(_translate("Dialog", "II"))
        self.label_14.setText(_translate("Dialog", "5"))
        self.lineEdit_17.setText(_translate("Dialog", "0"))
        self.label_15.setText(_translate("Dialog", "3"))
        self.label_16.setText(_translate("Dialog", "2"))
        self.lineEdit_18.setText(_translate("Dialog", "0"))
        self.lineEdit_19.setText(_translate("Dialog", "0"))
        self.lineEdit_20.setText(_translate("Dialog", "0"))
        self.lineEdit_21.setText(_translate("Dialog", "0"))
        self.label_17.setText(_translate("Dialog", "Y"))
        self.label_18.setText(_translate("Dialog", "4"))
        self.lineEdit_22.setText(_translate("Dialog", "0"))
        self.lineEdit_23.setText(_translate("Dialog", "0"))
        self.lineEdit_24.setText(_translate("Dialog", "0"))
        self.lineEdit_25.setText(_translate("Dialog", "0"))
        self.lineEdit_26.setText(_translate("Dialog", "0"))
        self.lineEdit_27.setText(_translate("Dialog", "0"))
        self.label_19.setText(_translate("Dialog", "W"))
        self.lineEdit_28.setText(_translate("Dialog", "0"))
        self.label_20.setText(_translate("Dialog", "H"))
        self.label_21.setText(_translate("Dialog", "6"))
        self.label_22.setText(_translate("Dialog", "X"))
        self.lineEdit_29.setText(_translate("Dialog", "0"))
        self.label_23.setText(_translate("Dialog", "1"))
        self.lineEdit_30.setText(_translate("Dialog", "0"))
        self.label_24.setText(_translate("Dialog", "III"))
        self.label_25.setText(_translate("Dialog", "5"))
        self.lineEdit_31.setText(_translate("Dialog", "0"))
        self.label_26.setText(_translate("Dialog", "3"))
        self.label_27.setText(_translate("Dialog", "2"))
        self.lineEdit_32.setText(_translate("Dialog", "0"))
        self.lineEdit_33.setText(_translate("Dialog", "0"))
        self.lineEdit_34.setText(_translate("Dialog", "0"))
        self.lineEdit_35.setText(_translate("Dialog", "0"))
        self.label_28.setText(_translate("Dialog", "Y"))
        self.label_29.setText(_translate("Dialog", "4"))
        self.lineEdit_36.setText(_translate("Dialog", "0"))
        self.lineEdit_37.setText(_translate("Dialog", "0"))
        self.lineEdit_38.setText(_translate("Dialog", "0"))
        self.lineEdit_39.setText(_translate("Dialog", "0"))
        self.lineEdit_40.setText(_translate("Dialog", "0"))
        self.lineEdit_41.setText(_translate("Dialog", "0"))
        self.label_30.setText(_translate("Dialog", "W"))
        self.lineEdit_42.setText(_translate("Dialog", "0"))
        self.label_31.setText(_translate("Dialog", "H"))
        self.label_32.setText(_translate("Dialog", "6"))
        self.label_33.setText(_translate("Dialog", "X"))
        self.lineEdit_43.setText(_translate("Dialog", "0"))
        self.label_34.setText(_translate("Dialog", "1"))
        self.lineEdit_44.setText(_translate("Dialog", "0"))
        self.label_35.setText(_translate("Dialog", "IV"))
        self.label_36.setText(_translate("Dialog", "5"))
        self.lineEdit_45.setText(_translate("Dialog", "0"))
        self.label_37.setText(_translate("Dialog", "3"))
        self.label_38.setText(_translate("Dialog", "2"))
        self.lineEdit_46.setText(_translate("Dialog", "0"))
        self.lineEdit_47.setText(_translate("Dialog", "0"))
        self.lineEdit_48.setText(_translate("Dialog", "0"))
        self.lineEdit_49.setText(_translate("Dialog", "0"))
        self.label_39.setText(_translate("Dialog", "Y"))
        self.label_40.setText(_translate("Dialog", "4"))
        self.lineEdit_50.setText(_translate("Dialog", "0"))
        self.lineEdit_51.setText(_translate("Dialog", "0"))
        self.lineEdit_52.setText(_translate("Dialog", "0"))
        self.lineEdit_53.setText(_translate("Dialog", "0"))
        self.lineEdit_54.setText(_translate("Dialog", "0"))
        self.lineEdit_55.setText(_translate("Dialog", "0"))
        self.label_41.setText(_translate("Dialog", "W"))
        self.lineEdit_56.setText(_translate("Dialog", "0"))
        self.label_42.setText(_translate("Dialog", "H"))
        self.label_43.setText(_translate("Dialog", "6"))
        self.label_44.setText(_translate("Dialog", "X"))
        self.pushButton_1000.setText(_translate("Dialog", "ok"))
