from PyQt5 import QtGui, QtWidgets, QtCore
from dialog import Ui_Dialog
from window import Ui_MainWindow
from fintable import Ui_DialogII

import sys
import os
from xlsxwriter.workbook import Workbook

from ctypes import windll, Structure, c_long, byref
import cv2
import mss
import numpy as np
from decimal import Decimal

import pytesseract
from fuzzywuzzy import fuzz

from win32api import GetSystemMetrics
import keyboard
import ctypes
import threading

import datetime
import re

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
uimap = Ui_Dialog()
uimap.setupUi(Dialog)

DialogII = QtWidgets.QDialog()
uitable = Ui_DialogII()
uitable.setupUi(DialogII)

MainWindow = QtWidgets.QMainWindow()
uiwin = Ui_MainWindow()
uiwin.setupUi(MainWindow)


try:
    with open('settings.txt') as file:
        s = file.readlines()

        a_y1 = s[0]
        uimap.lineEdit_2.setText(a_y1)
        a_x1 = s[1]
        uimap.lineEdit.setText(a_x1)
        a_y2 = s[2]
        uimap.lineEdit_3.setText(a_y2)
        a_x2 = s[3]
        uimap.lineEdit_4.setText(a_x2)
        a_y3 = s[4]
        uimap.lineEdit_5.setText(a_y3)
        a_x3 = s[5]
        uimap.lineEdit_6.setText(a_x3)
        a_y4 = s[6]
        uimap.lineEdit_7.setText(a_y4)
        a_x4 = s[7]
        uimap.lineEdit_10.setText(a_x4)
        a_y5 = s[8]
        uimap.lineEdit_8.setText(a_y5)
        a_x5 = s[9]
        uimap.lineEdit_11.setText(a_x5)
        a_y6 = s[10]
        uimap.lineEdit_9.setText(a_y6)
        a_x6 = s[11]
        uimap.lineEdit_12.setText(a_x6)

        b_y1 = s[12]
        uimap.lineEdit_15.setText(b_y1)
        b_x1 = s[13]
        uimap.lineEdit_22.setText(b_x1)
        b_y2 = s[14]
        uimap.lineEdit_28.setText(b_y2)
        b_x2 = s[15]
        uimap.lineEdit_23.setText(b_x2)
        b_y3 = s[16]
        uimap.lineEdit_18.setText(b_y3)
        b_x3 = s[17]
        uimap.lineEdit_20.setText(b_x3)
        b_y4 = s[18]
        uimap.lineEdit_21.setText(b_y4)
        b_x4 = s[19]
        uimap.lineEdit_26.setText(b_x4)
        b_y5 = s[20]
        uimap.lineEdit_24.setText(b_y5)
        b_x5 = s[21]
        uimap.lineEdit_17.setText(b_x5)
        b_y6 = s[22]
        uimap.lineEdit_25.setText(b_y6)
        b_x6 = s[23]
        uimap.lineEdit_27.setText(b_x6)

        c_y1 = s[24]
        uimap.lineEdit_29.setText(c_y1)
        c_x1 = s[25]
        uimap.lineEdit_36.setText(c_x1)
        c_y2 = s[26]
        uimap.lineEdit_42.setText(c_y2)
        c_x2 = s[27]
        uimap.lineEdit_37.setText(c_x2)
        c_y3 = s[28]
        uimap.lineEdit_32.setText(c_y3)
        c_x3 = s[29]
        uimap.lineEdit_34.setText(c_x3)
        c_y4 = s[30]
        uimap.lineEdit_35.setText(c_y4)
        c_x4 = s[31]
        uimap.lineEdit_40.setText(c_x4)
        c_y5 = s[32]
        uimap.lineEdit_38.setText(c_y5)
        c_x5 = s[33]
        uimap.lineEdit_31.setText(c_x5)
        c_y6 = s[34]
        uimap.lineEdit_39.setText(c_y6)
        c_x6 = s[35]
        uimap.lineEdit_41.setText(c_x6)

        d_y1 = s[36]
        uimap.lineEdit_43.setText(d_y1)
        d_x1 = s[37]
        uimap.lineEdit_50.setText(d_x1)
        d_y2 = s[38]
        uimap.lineEdit_56.setText(d_y2)
        d_x2 = s[39]
        uimap.lineEdit_51.setText(d_x2)
        d_y3 = s[40]
        uimap.lineEdit_46.setText(d_y3)
        d_x3 = s[41]
        uimap.lineEdit_48.setText(d_x3)
        d_y4 = s[42]
        uimap.lineEdit_49.setText(d_y4)
        d_x4 = s[43]
        uimap.lineEdit_54.setText(d_x4)
        d_y5 = s[44]
        uimap.lineEdit_52.setText(d_y5)
        d_x5 = s[45]
        uimap.lineEdit_45.setText(d_x5)
        d_y6 = s[46]
        uimap.lineEdit_53.setText(d_y6)
        d_x6 = s[47]
        uimap.lineEdit_55.setText(d_x6)

        w1 = s[48]
        uimap.lineEdit_13.setText(w1)
        h1 = s[49]
        uimap.lineEdit_14.setText(h1)

        w2 = s[50]
        uimap.lineEdit_16.setText(w2)
        h2 = s[51]
        uimap.lineEdit_19.setText(h2)

        w3 = s[52]
        uimap.lineEdit_30.setText(w3)
        h3 = s[53]
        uimap.lineEdit_33.setText(h3)

        w4 = s[54]
        uimap.lineEdit_44.setText(w4)
        h4 = s[55]
        uimap.lineEdit_47.setText(h4)

    file.close()
except:
    uiwin.textEdit.setText('Failed to restore settings. Check "settings.txt".')


MainWindow.show()

def buttons():
    uiwin.pushButton.setEnabled(False)
    uimap.pushButton_100.setEnabled(False)
    uimap.pushButton_200.setEnabled(False)
    uimap.pushButton_300.setEnabled(False)
    uimap.pushButton_400.setEnabled(False)
    uiwin.pushButton_55.setEnabled(False)
    uiwin.pushButton_555.hide()

buttons()



# Глобальные переменные
#-------------------------------------------------------------------------
class globals():
    WIN_TABLES = 0

    MON_Y = 0
    MON_X = 0

    W = 400
    H = 200

    RUN = True

    flag = 0
#-------------------------------------------------------------------------



# Открытие диалогового окна с координатами
#-------------------------------------------------------------------------
def show_table_map():
    DialogII.hide()
    uimap.checkBox.setChecked(False)
    uimap.checkBox_2.setChecked(False)
    uimap.checkBox_3.setChecked(False)
    uimap.checkBox_4.setChecked(False)
    uimap.checkBox_5.setChecked(False)
    uimap.checkBox_6.setChecked(False)
    uimap.checkBox_7.setChecked(False)
    uimap.checkBox_8.setChecked(False)
    uimap.checkBox_9.setChecked(False)
    uimap.checkBox_10.setChecked(False)
    uimap.checkBox_11.setChecked(False)
    uimap.checkBox_12.setChecked(False)
    uimap.checkBox_13.setChecked(False)
    uimap.checkBox_14.setChecked(False)
    uimap.checkBox_15.setChecked(False)
    uimap.checkBox_16.setChecked(False)
    uimap.checkBox_17.setChecked(False)
    uimap.checkBox_18.setChecked(False)
    uimap.checkBox_19.setChecked(False)
    uimap.checkBox_10.setChecked(False)
    uimap.checkBox_21.setChecked(False)
    uimap.checkBox_22.setChecked(False)
    uimap.checkBox_23.setChecked(False)
    uimap.checkBox_24.setChecked(False)
    Dialog.show()
#-------------------------------------------------------------------------



# Открытие диалогового окна с таблицей
#-------------------------------------------------------------------------
def show_table():
    Dialog.hide()
    DialogII.show()
#-------------------------------------------------------------------------



# QCheckBox элементы раздела Areas
#-------------------------------------------------------------------------
def t_or_f_checktables():
    x_1 = uiwin.checkBox.isChecked()
    x_2 = uiwin.checkBox_2.isChecked()
    x_3 = uiwin.checkBox_3.isChecked()
    x_4 = uiwin.checkBox_4.isChecked()
    x_5 = uiwin.checkBox_5.isChecked()
    x_6 = uiwin.checkBox_6.isChecked()

    if x_1 is True:
        checkbox_tables(1)
        globals.WIN_TABLES = 1
        uiwin.pushButton_55.setEnabled(True)
    elif x_2 is True:
        checkbox_tables(2)
        globals.WIN_TABLES = 2
        uiwin.pushButton_55.setEnabled(True)
    elif x_3 is True:
        checkbox_tables(3)
        globals.WIN_TABLES = 3
        uiwin.pushButton_55.setEnabled(True)
    elif x_4 is True:
        checkbox_tables(4)
        globals.WIN_TABLES = 4
        uiwin.pushButton_55.setEnabled(True)
    elif x_5 is True:
        checkbox_tables(5)
        globals.WIN_TABLES = 5
        uiwin.pushButton_55.setEnabled(True)
    elif x_6 is True:
        checkbox_tables(6)
        globals.WIN_TABLES = 6
        uiwin.pushButton_55.setEnabled(True)
    else:
        uiwin.checkBox.setEnabled(True)
        uiwin.checkBox_2.setEnabled(True)
        uiwin.checkBox_3.setEnabled(True)
        uiwin.checkBox_4.setEnabled(True)
        uiwin.checkBox_5.setEnabled(True)
        uiwin.checkBox_6.setEnabled(True)
        globals.WIN_TABLES = 0
        not_enabled_map()
        uiwin.pushButton.setEnabled(False)
        uiwin.textEdit.clear()
        uiwin.pushButton_55.setEnabled(False)


def checkbox_tables(num):
    if num == 1:
        uiwin.checkBox_2.setEnabled(False)
        uiwin.checkBox_3.setEnabled(False)
        uiwin.checkBox_4.setEnabled(False)
        uiwin.checkBox_5.setEnabled(False)
        uiwin.checkBox_6.setEnabled(False)

        enabled_map_1()
        uiwin.pushButton.setEnabled(True)

    elif num == 2:
        uiwin.checkBox.setEnabled(False)
        uiwin.checkBox_3.setEnabled(False)
        uiwin.checkBox_4.setEnabled(False)
        uiwin.checkBox_5.setEnabled(False)
        uiwin.checkBox_6.setEnabled(False)

        enabled_map_2()
        uiwin.pushButton.setEnabled(True)

    elif num == 3:
        uiwin.checkBox.setEnabled(False)
        uiwin.checkBox_2.setEnabled(False)
        uiwin.checkBox_4.setEnabled(False)
        uiwin.checkBox_5.setEnabled(False)
        uiwin.checkBox_6.setEnabled(False)

        enabled_map_3()
        uiwin.pushButton.setEnabled(True)

    elif num == 4:
        uiwin.checkBox.setEnabled(False)
        uiwin.checkBox_2.setEnabled(False)
        uiwin.checkBox_3.setEnabled(False)
        uiwin.checkBox_5.setEnabled(False)
        uiwin.checkBox_6.setEnabled(False)

        enabled_map_4()
        uiwin.pushButton.setEnabled(True)

    elif num == 5:
        uiwin.checkBox.setEnabled(False)
        uiwin.checkBox_2.setEnabled(False)
        uiwin.checkBox_3.setEnabled(False)
        uiwin.checkBox_4.setEnabled(False)
        uiwin.checkBox_6.setEnabled(False)

        enabled_map_5()
        uiwin.pushButton.setEnabled(True)

    elif num == 6:
        uiwin.checkBox.setEnabled(False)
        uiwin.checkBox_2.setEnabled(False)
        uiwin.checkBox_3.setEnabled(False)
        uiwin.checkBox_4.setEnabled(False)
        uiwin.checkBox_5.setEnabled(False)

        not_enabled_map()
        uiwin.pushButton.setEnabled(True)


def not_enabled_map():
    uimap.label_5.show()
    uimap.label_6.show()
    uimap.label_7.show()
    uimap.label_8.show()
    uimap.label_9.show()
    uimap.lineEdit_3.show()
    uimap.lineEdit_4.show()
    uimap.lineEdit_5.show()
    uimap.lineEdit_6.show()
    uimap.lineEdit_7.show()
    uimap.lineEdit_10.show()
    uimap.lineEdit_8.show()
    uimap.lineEdit_11.show()
    uimap.lineEdit_9.show()
    uimap.lineEdit_12.show()

    uimap.label_16.show()
    uimap.label_15.show()
    uimap.label_18.show()
    uimap.label_14.show()
    uimap.label_21.show()
    uimap.lineEdit_28.show()
    uimap.lineEdit_23.show()
    uimap.lineEdit_18.show()
    uimap.lineEdit_20.show()
    uimap.lineEdit_21.show()
    uimap.lineEdit_26.show()
    uimap.lineEdit_24.show()
    uimap.lineEdit_17.show()
    uimap.lineEdit_25.show()
    uimap.lineEdit_27.show()

    uimap.label_27.show()
    uimap.label_26.show()
    uimap.label_29.show()
    uimap.label_25.show()
    uimap.label_32.show()
    uimap.lineEdit_42.show()
    uimap.lineEdit_37.show()
    uimap.lineEdit_32.show()
    uimap.lineEdit_35.show()
    uimap.lineEdit_38.show()
    uimap.lineEdit_31.show()
    uimap.lineEdit_39.show()
    uimap.lineEdit_41.show()
    uimap.lineEdit_40.show()
    uimap.lineEdit_34.show()

    uimap.label_38.show()
    uimap.label_37.show()
    uimap.label_40.show()
    uimap.label_36.show()
    uimap.label_43.show()
    uimap.lineEdit_56.show()
    uimap.lineEdit_51.show()
    uimap.lineEdit_46.show()
    uimap.lineEdit_48.show()
    uimap.lineEdit_49.show()
    uimap.lineEdit_54.show()
    uimap.lineEdit_52.show()
    uimap.lineEdit_45.show()
    uimap.lineEdit_53.show()
    uimap.lineEdit_55.show()

    uimap.checkBox_2.show()
    uimap.checkBox_3.show()
    uimap.checkBox_4.show()
    uimap.checkBox_5.show()
    uimap.checkBox_6.show()

    uimap.checkBox_8.show()
    uimap.checkBox_9.show()
    uimap.checkBox_10.show()
    uimap.checkBox_11.show()
    uimap.checkBox_12.show()

    uimap.checkBox_13.show()
    uimap.checkBox_14.show()
    uimap.checkBox_15.show()
    uimap.checkBox_16.show()
    uimap.checkBox_17.show()

    uimap.checkBox_19.show()
    uimap.checkBox_20.show()
    uimap.checkBox_21.show()
    uimap.checkBox_22.show()
    uimap.checkBox_23.show()

def enabled_map_1():
    uimap.label_5.hide()
    uimap.label_6.hide()
    uimap.label_7.hide()
    uimap.label_8.hide()
    uimap.label_9.hide()
    uimap.lineEdit_3.hide()
    uimap.lineEdit_4.hide()
    uimap.lineEdit_5.hide()
    uimap.lineEdit_6.hide()
    uimap.lineEdit_7.hide()
    uimap.lineEdit_10.hide()
    uimap.lineEdit_8.hide()
    uimap.lineEdit_11.hide()
    uimap.lineEdit_9.hide()
    uimap.lineEdit_12.hide()

    uimap.label_16.hide()
    uimap.label_15.hide()
    uimap.label_18.hide()
    uimap.label_14.hide()
    uimap.label_21.hide()
    uimap.lineEdit_28.hide()
    uimap.lineEdit_23.hide()
    uimap.lineEdit_18.hide()
    uimap.lineEdit_20.hide()
    uimap.lineEdit_21.hide()
    uimap.lineEdit_26.hide()
    uimap.lineEdit_24.hide()
    uimap.lineEdit_17.hide()
    uimap.lineEdit_25.hide()
    uimap.lineEdit_27.hide()

    uimap.label_27.hide()
    uimap.label_26.hide()
    uimap.label_29.hide()
    uimap.label_25.hide()
    uimap.label_32.hide()
    uimap.lineEdit_42.hide()
    uimap.lineEdit_37.hide()
    uimap.lineEdit_32.hide()
    uimap.lineEdit_35.hide()
    uimap.lineEdit_38.hide()
    uimap.lineEdit_31.hide()
    uimap.lineEdit_39.hide()
    uimap.lineEdit_41.hide()
    uimap.lineEdit_40.hide()
    uimap.lineEdit_34.hide()

    uimap.label_38.hide()
    uimap.label_37.hide()
    uimap.label_40.hide()
    uimap.label_36.hide()
    uimap.label_43.hide()
    uimap.lineEdit_56.hide()
    uimap.lineEdit_51.hide()
    uimap.lineEdit_46.hide()
    uimap.lineEdit_48.hide()
    uimap.lineEdit_49.hide()
    uimap.lineEdit_54.hide()
    uimap.lineEdit_52.hide()
    uimap.lineEdit_45.hide()
    uimap.lineEdit_53.hide()
    uimap.lineEdit_55.hide()

    uimap.checkBox_2.hide()
    uimap.checkBox_3.hide()
    uimap.checkBox_4.hide()
    uimap.checkBox_5.hide()
    uimap.checkBox_6.hide()

    uimap.checkBox_8.hide()
    uimap.checkBox_9.hide()
    uimap.checkBox_10.hide()
    uimap.checkBox_11.hide()
    uimap.checkBox_12.hide()

    uimap.checkBox_13.hide()
    uimap.checkBox_14.hide()
    uimap.checkBox_15.hide()
    uimap.checkBox_16.hide()
    uimap.checkBox_17.hide()

    uimap.checkBox_19.hide()
    uimap.checkBox_20.hide()
    uimap.checkBox_21.hide()
    uimap.checkBox_22.hide()
    uimap.checkBox_23.hide()


def enabled_map_2():
    uimap.label_6.hide()
    uimap.label_7.hide()
    uimap.label_8.hide()
    uimap.label_9.hide()
    uimap.lineEdit_5.hide()
    uimap.lineEdit_6.hide()
    uimap.lineEdit_7.hide()
    uimap.lineEdit_10.hide()
    uimap.lineEdit_8.hide()
    uimap.lineEdit_11.hide()
    uimap.lineEdit_9.hide()
    uimap.lineEdit_12.hide()

    uimap.label_15.hide()
    uimap.label_18.hide()
    uimap.label_14.hide()
    uimap.label_21.hide()
    uimap.lineEdit_18.hide()
    uimap.lineEdit_20.hide()
    uimap.lineEdit_21.hide()
    uimap.lineEdit_26.hide()
    uimap.lineEdit_24.hide()
    uimap.lineEdit_17.hide()
    uimap.lineEdit_25.hide()
    uimap.lineEdit_27.hide()

    uimap.label_26.hide()
    uimap.label_29.hide()
    uimap.label_25.hide()
    uimap.label_32.hide()
    uimap.lineEdit_32.hide()
    uimap.lineEdit_35.hide()
    uimap.lineEdit_38.hide()
    uimap.lineEdit_31.hide()
    uimap.lineEdit_39.hide()
    uimap.lineEdit_41.hide()
    uimap.lineEdit_40.hide()
    uimap.lineEdit_34.hide()

    uimap.label_37.hide()
    uimap.label_40.hide()
    uimap.label_36.hide()
    uimap.label_43.hide()
    uimap.lineEdit_46.hide()
    uimap.lineEdit_48.hide()
    uimap.lineEdit_49.hide()
    uimap.lineEdit_54.hide()
    uimap.lineEdit_52.hide()
    uimap.lineEdit_45.hide()
    uimap.lineEdit_53.hide()
    uimap.lineEdit_55.hide()

    uimap.checkBox_3.hide()
    uimap.checkBox_4.hide()
    uimap.checkBox_5.hide()
    uimap.checkBox_6.hide()

    uimap.checkBox_9.hide()
    uimap.checkBox_10.hide()
    uimap.checkBox_11.hide()
    uimap.checkBox_12.hide()

    uimap.checkBox_13.hide()
    uimap.checkBox_14.hide()
    uimap.checkBox_15.hide()
    uimap.checkBox_16.hide()

    uimap.checkBox_19.hide()
    uimap.checkBox_20.hide()
    uimap.checkBox_21.hide()
    uimap.checkBox_22.hide()

def enabled_map_3():
    uimap.label_7.hide()
    uimap.label_8.hide()
    uimap.label_9.hide()
    uimap.lineEdit_7.hide()
    uimap.lineEdit_10.hide()
    uimap.lineEdit_8.hide()
    uimap.lineEdit_11.hide()
    uimap.lineEdit_9.hide()
    uimap.lineEdit_12.hide()

    uimap.label_18.hide()
    uimap.label_14.hide()
    uimap.label_21.hide()
    uimap.lineEdit_21.hide()
    uimap.lineEdit_26.hide()
    uimap.lineEdit_24.hide()
    uimap.lineEdit_17.hide()
    uimap.lineEdit_25.hide()
    uimap.lineEdit_27.hide()

    uimap.label_29.hide()
    uimap.label_25.hide()
    uimap.label_32.hide()
    uimap.lineEdit_35.hide()
    uimap.lineEdit_38.hide()
    uimap.lineEdit_31.hide()
    uimap.lineEdit_39.hide()
    uimap.lineEdit_41.hide()
    uimap.lineEdit_40.hide()

    uimap.label_40.hide()
    uimap.label_36.hide()
    uimap.label_43.hide()
    uimap.lineEdit_49.hide()
    uimap.lineEdit_54.hide()
    uimap.lineEdit_52.hide()
    uimap.lineEdit_45.hide()
    uimap.lineEdit_53.hide()
    uimap.lineEdit_55.hide()

    uimap.checkBox_4.hide()
    uimap.checkBox_5.hide()
    uimap.checkBox_6.hide()

    uimap.checkBox_10.hide()
    uimap.checkBox_11.hide()
    uimap.checkBox_12.hide()

    uimap.checkBox_13.hide()
    uimap.checkBox_14.hide()
    uimap.checkBox_15.hide()

    uimap.checkBox_19.hide()
    uimap.checkBox_20.hide()
    uimap.checkBox_21.hide()

def enabled_map_4():
    uimap.label_8.hide()
    uimap.label_9.hide()
    uimap.lineEdit_8.hide()
    uimap.lineEdit_11.hide()
    uimap.lineEdit_9.hide()
    uimap.lineEdit_12.hide()

    uimap.label_14.hide()
    uimap.label_21.hide()
    uimap.lineEdit_24.hide()
    uimap.lineEdit_17.hide()
    uimap.lineEdit_25.hide()
    uimap.lineEdit_27.hide()

    uimap.label_25.hide()
    uimap.label_32.hide()
    uimap.lineEdit_38.hide()
    uimap.lineEdit_31.hide()
    uimap.lineEdit_39.hide()
    uimap.lineEdit_41.hide()

    uimap.label_36.hide()
    uimap.label_43.hide()
    uimap.lineEdit_52.hide()
    uimap.lineEdit_45.hide()
    uimap.lineEdit_53.hide()
    uimap.lineEdit_55.hide()

    uimap.checkBox_5.hide()
    uimap.checkBox_6.hide()

    uimap.checkBox_11.hide()
    uimap.checkBox_12.hide()

    uimap.checkBox_13.hide()
    uimap.checkBox_14.hide()

    uimap.checkBox_19.hide()
    uimap.checkBox_20.hide()

def enabled_map_5():
    uimap.label_9.hide()
    uimap.lineEdit_9.hide()
    uimap.lineEdit_12.hide()

    uimap.label_21.hide()
    uimap.lineEdit_25.hide()
    uimap.lineEdit_27.hide()

    uimap.label_32.hide()
    uimap.lineEdit_39.hide()
    uimap.lineEdit_41.hide()

    uimap.label_43.hide()
    uimap.lineEdit_53.hide()
    uimap.lineEdit_55.hide()

    uimap.checkBox_6.hide()
    uimap.checkBox_12.hide()
    uimap.checkBox_13.hide()
    uimap.checkBox_19.hide()
#-------------------------------------------------------------------------



# Чекбоксы диалогового окна
#-------------------------------------------------------------------------
def witch_checkbox():
    x_1 = uimap.checkBox.isChecked()
    x_2 = uimap.checkBox_2.isChecked()
    x_3 = uimap.checkBox_3.isChecked()
    x_4 = uimap.checkBox_4.isChecked()
    x_5 = uimap.checkBox_5.isChecked()
    x_6 = uimap.checkBox_6.isChecked()
    x_7 = uimap.checkBox_7.isChecked()
    x_8 = uimap.checkBox_8.isChecked()
    x_9 = uimap.checkBox_9.isChecked()
    x_10 = uimap.checkBox_10.isChecked()
    x_11 = uimap.checkBox_11.isChecked()
    x_12 = uimap.checkBox_12.isChecked()
    x_13 = uimap.checkBox_13.isChecked()
    x_14 = uimap.checkBox_14.isChecked()
    x_15 = uimap.checkBox_15.isChecked()
    x_16 = uimap.checkBox_16.isChecked()
    x_17 = uimap.checkBox_17.isChecked()
    x_18 = uimap.checkBox_18.isChecked()
    x_19 = uimap.checkBox_19.isChecked()
    x_20 = uimap.checkBox_20.isChecked()
    x_21 = uimap.checkBox_21.isChecked()
    x_22 = uimap.checkBox_22.isChecked()
    x_23 = uimap.checkBox_23.isChecked()
    x_24 = uimap.checkBox_24.isChecked()

    if x_1 is True:
        yx_acc_t1()
    elif x_2 is True:
        yx_acc_t2()
    elif x_3 is True:
        yx_acc_t3()
    elif x_4 is True:
        yx_acc_t4()
    elif x_5 is True:
        yx_acc_t5()
    elif x_6 is True:
        yx_acc_t6()
    elif x_7 is True:
        yx_tablename_t1()
    elif x_8 is True:
        yx_tablename_t2()
    elif x_9 is True:
        yx_tablename_t3()
    elif x_10 is True:
        yx_tablename_t4()
    elif x_11 is True:
        yx_tablename_t5()
    elif x_12 is True:
        yx_tablename_t6()
    elif x_13 is True:
        yx_table_n_t6()
    elif x_14 is True:
        yx_table_n_t5()
    elif x_15 is True:
        yx_table_n_t4()
    elif x_16 is True:
        yx_table_n_t3()
    elif x_17 is True:
        yx_table_n_t2()
    elif x_18 is True:
        yx_table_n_t1()
    elif x_19 is True:
        yx_cards_t6()
    elif x_20 is True:
        yx_cards_t5()
    elif x_21 is True:
        yx_cards_t4()
    elif x_22 is True:
        yx_cards_t3()
    elif x_23 is True:
        yx_cards_t2()
    elif x_24 is True:
        yx_cards_t1()


def allcheckboxesaretrue():
    uimap.checkBox.setEnabled(True)
    uimap.checkBox_2.setEnabled(True)
    uimap.checkBox_3.setEnabled(True)
    uimap.checkBox_4.setEnabled(True)
    uimap.checkBox_5.setEnabled(True)
    uimap.checkBox_6.setEnabled(True)
    uimap.checkBox_7.setEnabled(True)
    uimap.checkBox_8.setEnabled(True)
    uimap.checkBox_9.setEnabled(True)
    uimap.checkBox_10.setEnabled(True)
    uimap.checkBox_11.setEnabled(True)
    uimap.checkBox_12.setEnabled(True)
    uimap.checkBox_13.setEnabled(True)
    uimap.checkBox_14.setEnabled(True)
    uimap.checkBox_15.setEnabled(True)
    uimap.checkBox_16.setEnabled(True)
    uimap.checkBox_17.setEnabled(True)
    uimap.checkBox_18.setEnabled(True)
    uimap.checkBox_19.setEnabled(True)
    uimap.checkBox_20.setEnabled(True)
    uimap.checkBox_21.setEnabled(True)
    uimap.checkBox_22.setEnabled(True)
    uimap.checkBox_23.setEnabled(True)
    uimap.checkBox_24.setEnabled(True)


def yx_acc_t1():
    x = uimap.checkBox.isChecked()
    uimap.pushButton_100.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(True)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_2.setText(str(globals.MON_Y))
        uimap.lineEdit.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))
    else:
        uimap.pushButton_100.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_2.setText(str(globals.MON_Y))
        uimap.lineEdit.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))


def yx_acc_t2():
    x = uimap.checkBox_2.isChecked()
    uimap.pushButton_100.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(True)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_3.setText(str(globals.MON_Y))
        uimap.lineEdit_4.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))
    else:
        uimap.pushButton_100.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_3.setText(str(globals.MON_Y))
        uimap.lineEdit_4.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))


def yx_acc_t3():
    x = uimap.checkBox_3.isChecked()
    uimap.pushButton_100.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(True)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_5.setText(str(globals.MON_Y))
        uimap.lineEdit_6.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))
    else:
        uimap.pushButton_100.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_5.setText(str(globals.MON_Y))
        uimap.lineEdit_6.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))


def yx_acc_t4():
    x = uimap.checkBox_4.isChecked()
    uimap.pushButton_100.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(True)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_7.setText(str(globals.MON_Y))
        uimap.lineEdit_10.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))
    else:
        uimap.pushButton_100.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_7.setText(str(globals.MON_Y))
        uimap.lineEdit_10.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))


def yx_acc_t5():
    x = uimap.checkBox_5.isChecked()
    uimap.pushButton_100.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(True)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_8.setText(str(globals.MON_Y))
        uimap.lineEdit_11.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))
    else:
        uimap.pushButton_100.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_8.setText(str(globals.MON_Y))
        uimap.lineEdit_11.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))


def yx_acc_t6():
    x = uimap.checkBox_6.isChecked()
    uimap.pushButton_100.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(True)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_9.setText(str(globals.MON_Y))
        uimap.lineEdit_12.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))
    else:
        uimap.pushButton_100.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_9.setText(str(globals.MON_Y))
        uimap.lineEdit_12.setText(str(globals.MON_X))
        uimap.lineEdit_13.setText(str(globals.W))
        uimap.lineEdit_14.setText(str(globals.H))


def yx_tablename_t1():
    x = uimap.checkBox_7.isChecked()
    uimap.pushButton_200.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(True)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_15.setText(str(globals.MON_Y))
        uimap.lineEdit_22.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))
    else:
        uimap.pushButton_200.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_15.setText(str(globals.MON_Y))
        uimap.lineEdit_22.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))


def yx_tablename_t2():
    x = uimap.checkBox_8.isChecked()
    uimap.pushButton_200.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(True)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_28.setText(str(globals.MON_Y))
        uimap.lineEdit_23.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))
    else:
        uimap.pushButton_200.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_28.setText(str(globals.MON_Y))
        uimap.lineEdit_23.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))


def yx_tablename_t3():
    x = uimap.checkBox_9.isChecked()
    uimap.pushButton_200.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(True)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_18.setText(str(globals.MON_Y))
        uimap.lineEdit_20.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))
    else:
        uimap.pushButton_200.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_18.setText(str(globals.MON_Y))
        uimap.lineEdit_20.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))


def yx_tablename_t4():
    x = uimap.checkBox_10.isChecked()
    uimap.pushButton_200.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(True)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_21.setText(str(globals.MON_Y))
        uimap.lineEdit_26.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))
    else:
        uimap.pushButton_200.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_21.setText(str(globals.MON_Y))
        uimap.lineEdit_26.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))


def yx_tablename_t5():
    x = uimap.checkBox_11.isChecked()
    uimap.pushButton_200.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(True)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_24.setText(str(globals.MON_Y))
        uimap.lineEdit_17.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))
    else:
        uimap.pushButton_200.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_24.setText(str(globals.MON_Y))
        uimap.lineEdit_17.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))


def yx_tablename_t6():
    x = uimap.checkBox_12.isChecked()
    uimap.pushButton_200.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(True)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_25.setText(str(globals.MON_Y))
        uimap.lineEdit_27.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))
    else:
        uimap.pushButton_200.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_25.setText(str(globals.MON_Y))
        uimap.lineEdit_27.setText(str(globals.MON_X))
        uimap.lineEdit_16.setText(str(globals.W))
        uimap.lineEdit_19.setText(str(globals.H))


def yx_table_n_t6():
    x = uimap.checkBox_13.isChecked()
    uimap.pushButton_300.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(True)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_39.setText(str(globals.MON_Y))
        uimap.lineEdit_41.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))
    else:
        uimap.pushButton_300.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_39.setText(str(globals.MON_Y))
        uimap.lineEdit_41.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))


def yx_table_n_t5():
    x = uimap.checkBox_14.isChecked()
    uimap.pushButton_300.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(True)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_38.setText(str(globals.MON_Y))
        uimap.lineEdit_31.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))
    else:
        uimap.pushButton_300.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_38.setText(str(globals.MON_Y))
        uimap.lineEdit_31.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))


def yx_table_n_t4():
    x = uimap.checkBox_15.isChecked()
    uimap.pushButton_300.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(True)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_35.setText(str(globals.MON_Y))
        uimap.lineEdit_40.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))
    else:
        uimap.pushButton_300.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_35.setText(str(globals.MON_Y))
        uimap.lineEdit_40.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))


def yx_table_n_t3():
    x = uimap.checkBox_16.isChecked()
    uimap.pushButton_300.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(True)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_32.setText(str(globals.MON_Y))
        uimap.lineEdit_34.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))
    else:
        uimap.pushButton_300.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_32.setText(str(globals.MON_Y))
        uimap.lineEdit_34.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))


def yx_table_n_t2():
    x = uimap.checkBox_17.isChecked()
    uimap.pushButton_300.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(True)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_42.setText(str(globals.MON_Y))
        uimap.lineEdit_37.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))
    else:
        uimap.pushButton_300.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_42.setText(str(globals.MON_Y))
        uimap.lineEdit_37.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))


def yx_table_n_t1():
    x = uimap.checkBox_18.isChecked()
    uimap.pushButton_300.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(True)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_29.setText(str(globals.MON_Y))
        uimap.lineEdit_36.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))
    else:
        uimap.pushButton_300.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_29.setText(str(globals.MON_Y))
        uimap.lineEdit_36.setText(str(globals.MON_X))
        uimap.lineEdit_30.setText(str(globals.W))
        uimap.lineEdit_33.setText(str(globals.H))


def yx_cards_t6():
    x = uimap.checkBox_19.isChecked()
    uimap.pushButton_400.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(True)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_53.setText(str(globals.MON_Y))
        uimap.lineEdit_55.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))
    else:
        uimap.pushButton_400.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_53.setText(str(globals.MON_Y))
        uimap.lineEdit_55.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))


def yx_cards_t5():
    x = uimap.checkBox_20.isChecked()
    uimap.pushButton_400.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(True)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_52.setText(str(globals.MON_Y))
        uimap.lineEdit_45.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))
    else:
        uimap.pushButton_400.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_52.setText(str(globals.MON_Y))
        uimap.lineEdit_45.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))


def yx_cards_t4():
    x = uimap.checkBox_21.isChecked()
    uimap.pushButton_400.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(True)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_49.setText(str(globals.MON_Y))
        uimap.lineEdit_54.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))
    else:
        uimap.pushButton_400.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_49.setText(str(globals.MON_Y))
        uimap.lineEdit_54.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))


def yx_cards_t3():
    x = uimap.checkBox_22.isChecked()
    uimap.pushButton_400.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(True)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_46.setText(str(globals.MON_Y))
        uimap.lineEdit_48.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))
    else:
        uimap.pushButton_400.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_46.setText(str(globals.MON_Y))
        uimap.lineEdit_48.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))


def yx_cards_t2():
    x = uimap.checkBox_23.isChecked()
    uimap.pushButton_400.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(True)
        uimap.checkBox_24.setEnabled(False)
        uimap.lineEdit_56.setText(str(globals.MON_Y))
        uimap.lineEdit_51.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))
    else:
        uimap.pushButton_400.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_56.setText(str(globals.MON_Y))
        uimap.lineEdit_51.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))


def yx_cards_t1():
    x = uimap.checkBox_24.isChecked()
    uimap.pushButton_400.setEnabled(True)
    if x is True:
        uimap.checkBox.setEnabled(False)
        uimap.checkBox_2.setEnabled(False)
        uimap.checkBox_3.setEnabled(False)
        uimap.checkBox_4.setEnabled(False)
        uimap.checkBox_5.setEnabled(False)
        uimap.checkBox_6.setEnabled(False)
        uimap.checkBox_7.setEnabled(False)
        uimap.checkBox_8.setEnabled(False)
        uimap.checkBox_9.setEnabled(False)
        uimap.checkBox_10.setEnabled(False)
        uimap.checkBox_11.setEnabled(False)
        uimap.checkBox_12.setEnabled(False)
        uimap.checkBox_13.setEnabled(False)
        uimap.checkBox_14.setEnabled(False)
        uimap.checkBox_15.setEnabled(False)
        uimap.checkBox_16.setEnabled(False)
        uimap.checkBox_17.setEnabled(False)
        uimap.checkBox_18.setEnabled(False)
        uimap.checkBox_19.setEnabled(False)
        uimap.checkBox_20.setEnabled(False)
        uimap.checkBox_21.setEnabled(False)
        uimap.checkBox_22.setEnabled(False)
        uimap.checkBox_23.setEnabled(False)
        uimap.checkBox_24.setEnabled(True)
        uimap.lineEdit_43.setText(str(globals.MON_Y))
        uimap.lineEdit_50.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))
    else:
        uimap.pushButton_400.setEnabled(False)
        allcheckboxesaretrue()
        uimap.lineEdit_43.setText(str(globals.MON_Y))
        uimap.lineEdit_50.setText(str(globals.MON_X))
        uimap.lineEdit_44.setText(str(globals.W))
        uimap.lineEdit_47.setText(str(globals.H))
#-------------------------------------------------------------------------



# Шрина и высота
#-------------------------------------------------------------------------
def acc_name():
    globals.W = int(uimap.lineEdit_13.text())
    globals.H = int(uimap.lineEdit_14.text())


def table_name():
    globals.W = int(uimap.lineEdit_16.text())
    globals.H = int(uimap.lineEdit_19.text())


def n_table():
    globals.W = int(uimap.lineEdit_30.text())
    globals.H = int(uimap.lineEdit_33.text())


def cards():
    globals.W = int(uimap.lineEdit_44.text())
    globals.H = int(uimap.lineEdit_47.text())
#-------------------------------------------------------------------------



#  Координаты
#-------------------------------------------------------------------------
class POINT(Structure):
    _fields_ = [('x', c_long), ('y', c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {'x': pt.x, 'y': pt.y}

title = 'Q'
sct = mss.mss()

def video():
    Dialog.hide()

    while True:
        try:
            cur = queryMousePosition()
            th = Decimal(globals.H) / Decimal(2)
            lw = Decimal(globals.W) / Decimal(2)
            mon = {'top': cur['y'] - th, 'left': cur['x'] - lw, 'width': globals.W, 'height': globals.H}
            img = np.asarray(sct.grab(mon))

            cv2.imshow(title, img)

            globals.MON_Y = cur['y'] - th
            globals.MON_X = cur['x'] - lw

            if cv2.waitKey(1) & keyboard.is_pressed('q'):
                break
        except:
            break

    cv2.destroyAllWindows()
    Dialog.show()
    witch_checkbox()
#-------------------------------------------------------------------------



#-------------------------------------------------------------------------
def how_many_tables():
    if globals.WIN_TABLES == 1:
        reading_1()
    elif globals.WIN_TABLES == 2:
        reading_2()
    elif globals.WIN_TABLES == 3:
        reading_3()
    elif globals.WIN_TABLES == 4:
        reading_4()
    elif globals.WIN_TABLES == 5:
        reading_5()
    elif globals.WIN_TABLES == 6:
        reading_6()
#-------------------------------------------------------------------------



# OCR
#-------------------------------------------------------------------------
def reading_1():
    x = 2
    y = 1
    z = 1

    Width = GetSystemMetrics(0)
    Height = GetSystemMetrics(1)

    filename = 'Image1.png'

    while globals.RUN:
        try:
            if x == 20:
                break
            if y == 24:
                break
            if z == 24:
                break
            if keyboard.is_pressed('q'):
                break

            mon = {'top': 0, 'left': 0, 'width': Width, 'height': Height}
            screen = np.asarray(sct.grab(mon))
            cv2.imwrite(filename, screen)
            img = cv2.imread('Image1.png')

            t_1 = int(uimap.lineEdit_2.text())
            l_1 = int(uimap.lineEdit.text())
            w_1 = l_1 + int(uimap.lineEdit_13.text())
            h_1 = t_1 + int(uimap.lineEdit_14.text())

            if l_1 < 0:
                l_1 = 0
            if t_1 < 0:
                t_1 = 0
            if w_1 > Width:
                w_1 = Width
            if h_1 > Height:
                h_1 = Height
            t_2 = int(uimap.lineEdit_15.text())
            l_2 = int(uimap.lineEdit_22.text())
            w_2 = l_2 + int(uimap.lineEdit_16.text())
            h_2 = t_2 + int(uimap.lineEdit_19.text())
            if l_2 < 0:
                l_2 = 0
            if t_2 < 0:
                t_2 = 0
            if w_2 > Width:
                w_2 = Width
            if h_2 > Height:
                h_2 = Height
            t_3 = int(uimap.lineEdit_29.text())
            l_3 = int(uimap.lineEdit_36.text())
            w_3 = l_3 + int(uimap.lineEdit_30.text())
            h_3 = t_3 + int(uimap.lineEdit_33.text())
            if l_3 < 0:
                l_3 = 0
            if t_3 < 0:
                t_3 = 0
            if w_3 > Width:
                w_3 = Width
            if h_3 > Height:
                h_3 = Height
            t_4 = int(uimap.lineEdit_43.text())
            l_4 = int(uimap.lineEdit_50.text())
            w_4 = l_4 + int(uimap.lineEdit_44.text())
            h_4 = t_4 + int(uimap.lineEdit_47.text())
            if l_4 < 0:
                l_4 = 0
            if t_4 < 0:
                t_4 = 0
            if w_4 > Width:
                w_4 = Width
            if h_4 > Height:
                h_4 = Height

            acct1 = img[t_1 : h_1, l_1 : w_1]
            tnt1 = img[t_2 : h_2, l_2 : w_2]
            ntt1 = img[t_3 : h_3, l_3 : w_3]
            ct1 = img[t_4 : h_4, l_4 : w_4]

            try:
                text_1 = pytesseract.image_to_string(acct1, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_1 = reg.sub('', text_1)
                text_1 = text_1[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_1 not in a:
                    if fuzz.ratio(text_1, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_1))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_2 = pytesseract.image_to_string(tnt1, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_2 = reg.sub('', text_2)
                text_2 = text_2[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_2 not in a:
                    if fuzz.ratio(text_2, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_2))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_3 = pytesseract.image_to_string(ntt1, lang = 'chi_sim')
                reg2 = re.compile('[^0-9]')
                text_3 = reg2.sub('', text_3)
                text_3 = text_3[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_3 not in a:
                    z += 1
                    color = uitable.tableWidget.item(z, 2).background()
                    uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_3))
                    uitable.tableWidget.item(z, 2).setBackground(color)
                    autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_4 = pytesseract.image_to_string(ct1)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_4 = reg.sub('', text_4)
                text_4 = text_4[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'w')
                f.write(text_4)
                f.close()
            except:
                continue

            os.remove('Image1.png')
        except:
            break


def reading_2():
    x = 2
    y = 1
    z = 1

    Width = GetSystemMetrics(0)
    Height = GetSystemMetrics(1)

    filename = 'Image1.png'

    while globals.RUN:
        try:
            if x == 20:
                break
            if y == 24:
                break
            if z == 24:
                break
            if keyboard.wait('q'):
                break

            mon = {'top': 0, 'left': 0, 'width': Width, 'height': Height}
            screen = np.asarray(sct.grab(mon))
            cv2.imwrite(filename, screen)
            img = cv2.imread('Image1.png')

            t_1 = int(uimap.lineEdit_2.text())
            l_1 = int(uimap.lineEdit.text())
            w_1 = l_1 + int(uimap.lineEdit_13.text())
            h_1 = t_1 + int(uimap.lineEdit_14.text())
            if l_1 < 0:
                l_1 = 0
            elif t_1 < 0:
                t_1 = 0
            elif w_1 > Width:
                w_1 = Width
            elif h_1 > Height:
                h_1 = Height
            t_2 = int(uimap.lineEdit_15.text())
            l_2 = int(uimap.lineEdit_22.text())
            w_2 = l_2 + int(uimap.lineEdit_16.text())
            h_2 = t_2 + int(uimap.lineEdit_19.text())
            if l_2 < 0:
                l_2 = 0
            elif t_2 < 0:
                t_2 = 0
            elif w_2 > Width:
                w_2 = Width
            elif h_2 > Height:
                h_2 = Height
            t_3 = int(uimap.lineEdit_29.text())
            l_3 = int(uimap.lineEdit_36.text())
            w_3 = l_3 + int(uimap.lineEdit_30.text())
            h_3 = t_3 + int(uimap.lineEdit_33.text())
            if l_3 < 0:
                l_3 = 0
            elif t_3 < 0:
                t_3 = 0
            elif w_3 > Width:
                w_3 = Width
            elif h_3 > Height:
                h_3 = Height
            t_4 = int(uimap.lineEdit_43.text())
            l_4 = int(uimap.lineEdit_50.text())
            w_4 = l_4 + int(uimap.lineEdit_44.text())
            h_4 = t_4 + int(uimap.lineEdit_47.text())
            if l_4 < 0:
                l_4 = 0
            elif t_4 < 0:
                t_4 = 0
            elif w_4 > Width:
                w_4 = Width
            elif h_4 > Height:
                h_4 = Height

            t_5 = int(uimap.lineEdit_3.text())
            l_5 = int(uimap.lineEdit_4.text())
            w_5 = l_5 + int(uimap.lineEdit_13.text())
            h_5 = t_5 + int(uimap.lineEdit_14.text())
            if l_5 < 0:
                l_5 = 0
            elif t_5 < 0:
                t_5 = 0
            elif w_5 > Width:
                w_5 = Width
            elif h_5 > Height:
                h_5 = Height
            t_6 = int(uimap.lineEdit_28.text())
            l_6 = int(uimap.lineEdit_23.text())
            w_6 = l_6 + int(uimap.lineEdit_16.text())
            h_6 = t_6 + int(uimap.lineEdit_19.text())
            if l_6 < 0:
                l_6 = 0
            elif t_6 < 0:
                t_6 = 0
            elif w_6 > Width:
                w_6 = Width
            elif h_6 > Height:
                h_6 = Height
            t_7 = int(uimap.lineEdit_42.text())
            l_7 = int(uimap.lineEdit_37.text())
            w_7 = l_7 + int(uimap.lineEdit_30.text())
            h_7 = t_7 + int(uimap.lineEdit_33.text())
            if l_7 < 0:
                l_7 = 0
            elif t_7 < 0:
                t_7 = 0
            elif w_7 > Width:
                w_7 = Width
            elif h_7 > Height:
                h_7 = Height
            t_8 = int(uimap.lineEdit_56.text())
            l_8 = int(uimap.lineEdit_51.text())
            w_8 = l_8 + int(uimap.lineEdit_44.text())
            h_8 = t_8 + int(uimap.lineEdit_47.text())
            if l_8 < 0:
                l_8 = 0
            elif t_8 < 0:
                t_8 = 0
            elif w_8 > Width:
                w_8 = Width
            elif h_8 > Height:
                h_8 = Height

            acct1 = img[t_1: h_1, l_1: w_1]
            tnt1 = img[t_2: h_2, l_2: w_2]
            ntt1 = img[t_3: h_3, l_3: w_3]
            ct1 = img[t_4: h_4, l_4: w_4]

            acct2 = img[t_5: h_5, l_5: w_5]
            tnt2 = img[t_6: h_6, l_6: w_6]
            ntt2 = img[t_7: h_7, l_7: w_7]
            ct2 = img[t_8: h_8, l_8: w_8]

            try:
                text_1 = pytesseract.image_to_string(acct1, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_1 = reg.sub('', text_1)
                text_1 = text_1[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_1 not in a:
                    if fuzz.ratio(text_1, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_1))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_2 = pytesseract.image_to_string(tnt1, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_2 = reg.sub('', text_2)
                text_2 = text_2[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_2 not in a:
                    if fuzz.ratio(text_2, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_2))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_3 = pytesseract.image_to_string(ntt1, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_3 = reg.sub('', text_3)
                text_3 = text_3[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_3 not in a:
                    if fuzz.ratio(text_3, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_3))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_4 = pytesseract.image_to_string(ct1)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_4 = reg.sub('', text_4)
                text_4 = text_4[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'w')
                txt = text_4
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_5 = pytesseract.image_to_string(acct2, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_5 = reg.sub('', text_5)
                text_5 = text_5[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_5 not in a:
                    if fuzz.ratio(text_5, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_5))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue

            try:
                text_6 = pytesseract.image_to_string(tnt2, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_6 = reg.sub('', text_6)
                text_6 = text_6[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_6 not in a:
                    if fuzz.ratio(text_6, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_6))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue

            try:
                text_7 = pytesseract.image_to_string(ntt2, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_7 = reg.sub('', text_7)
                text_7 = text_7[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_7 not in a:
                    if fuzz.ratio(text_7, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_7))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue

            try:
                text_8 = pytesseract.image_to_string(ct2)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_8 = reg.sub('', text_8)
                text_8 = text_8[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt =text_8
                f.write(txt)
                f.close()
            except:
                continue

            os.remove('Image1.png')
        except:
            break

def reading_3():
    x = 2
    y = 1
    z = 1

    Width = GetSystemMetrics(0)
    Height = GetSystemMetrics(1)

    filename = 'Image1.png'

    while globals.RUN:
        try:
            if x == 20:
                break
            if y == 24:
                break
            if z == 24:
                break
            if keyboard.is_pressed('q'):
                break

            mon = {'top': 0, 'left': 0, 'width': Width, 'height': Height}
            screen = np.asarray(sct.grab(mon))
            cv2.imwrite(filename, screen)
            img = cv2.imread('Image1.png')

            t_1 = int(uimap.lineEdit_2.text())
            l_1 = int(uimap.lineEdit.text())
            w_1 = l_1 + int(uimap.lineEdit_13.text())
            h_1 = t_1 + int(uimap.lineEdit_14.text())
            if l_1 < 0:
                l_1 = 0
            elif t_1 < 0:
                t_1 = 0
            elif w_1 > Width:
                w_1 = Width
            elif h_1 > Height:
                h_1 = Height
            t_2 = int(uimap.lineEdit_15.text())
            l_2 = int(uimap.lineEdit_22.text())
            w_2 = l_2 + int(uimap.lineEdit_16.text())
            h_2 = t_2 + int(uimap.lineEdit_19.text())
            if l_2 < 0:
                l_2 = 0
            elif t_2 < 0:
                t_2 = 0
            elif w_2 > Width:
                w_2 = Width
            elif h_2 > Height:
                h_2 = Height
            t_3 = int(uimap.lineEdit_29.text())
            l_3 = int(uimap.lineEdit_36.text())
            w_3 = l_3 + int(uimap.lineEdit_30.text())
            h_3 = t_3 + int(uimap.lineEdit_33.text())
            if l_3 < 0:
                l_3 = 0
            elif t_3 < 0:
                t_3 = 0
            elif w_3 > Width:
                w_3 = Width
            elif h_3 > Height:
                h_3 = Height
            t_4 = int(uimap.lineEdit_43.text())
            l_4 = int(uimap.lineEdit_50.text())
            w_4 = l_4 + int(uimap.lineEdit_44.text())
            h_4 = t_4 + int(uimap.lineEdit_47.text())
            if l_4 < 0:
                l_4 = 0
            elif t_4 < 0:
                t_4 = 0
            elif w_4 > Width:
                w_4 = Width
            elif h_4 > Height:
                h_4 = Height

            t_5 = int(uimap.lineEdit_3.text())
            l_5 = int(uimap.lineEdit_4.text())
            w_5 = l_5 + int(uimap.lineEdit_13.text())
            h_5 = t_5 + int(uimap.lineEdit_14.text())
            if l_5 < 0:
                l_5 = 0
            elif t_5 < 0:
                t_5 = 0
            elif w_5 > Width:
                w_5 = Width
            elif h_5 > Height:
                h_5 = Height
            t_6 = int(uimap.lineEdit_28.text())
            l_6 = int(uimap.lineEdit_23.text())
            w_6 = l_6 + int(uimap.lineEdit_16.text())
            h_6 = t_6 + int(uimap.lineEdit_19.text())
            if l_6 < 0:
                l_6 = 0
            elif t_6 < 0:
                t_6 = 0
            elif w_6 > Width:
                w_6 = Width
            elif h_6 > Height:
                h_6 = Height
            t_7 = int(uimap.lineEdit_42.text())
            l_7 = int(uimap.lineEdit_37.text())
            w_7 = l_7 + int(uimap.lineEdit_30.text())
            h_7 = t_7 + int(uimap.lineEdit_33.text())
            if l_7 < 0:
                l_7 = 0
            elif t_7 < 0:
                t_7 = 0
            elif w_7 > Width:
                w_7 = Width
            elif h_7 > Height:
                h_7 = Height
            t_8 = int(uimap.lineEdit_56.text())
            l_8 = int(uimap.lineEdit_51.text())
            w_8 = l_8 + int(uimap.lineEdit_44.text())
            h_8 = t_8 + int(uimap.lineEdit_47.text())
            if l_8 < 0:
                l_8 = 0
            elif t_8 < 0:
                t_8 = 0
            elif w_8 > Width:
                w_8 = Width
            elif h_8 > Height:
                h_8 = Height

            t_9 = int(uimap.lineEdit_5.text())
            l_9 = int(uimap.lineEdit_6.text())
            w_9 = l_9 + int(uimap.lineEdit_13.text())
            h_9 = t_9 + int(uimap.lineEdit_14.text())
            if l_9 < 0:
                l_9 = 0
            elif t_9 < 0:
                t_9 = 0
            elif w_9 > Width:
                w_9 = Width
            elif h_9 > Height:
                h_9 = Height
            t_10 = int(uimap.lineEdit_18.text())
            l_10 = int(uimap.lineEdit_20.text())
            w_10 = l_10 + int(uimap.lineEdit_16.text())
            h_10 = t_10 + int(uimap.lineEdit_19.text())
            if l_10 < 0:
                l_10 = 0
            elif t_10 < 0:
                t_10 = 0
            elif w_10 > Width:
                w_10 = Width
            elif h_10 > Height:
                h_10 = Height
            t_11 = int(uimap.lineEdit_32.text())
            l_11 = int(uimap.lineEdit_34.text())
            w_11 = l_11 + int(uimap.lineEdit_30.text())
            h_11 = t_11 + int(uimap.lineEdit_33.text())
            if l_11 < 0:
                l_11 = 0
            elif t_11 < 0:
                t_11 = 0
            elif w_11 > Width:
                w_11 = Width
            elif h_11 > Height:
                h_11 = Height
            t_12 = int(uimap.lineEdit_46.text())
            l_12 = int(uimap.lineEdit_48.text())
            w_12 = l_12 + int(uimap.lineEdit_44.text())
            h_12 = t_12 + int(uimap.lineEdit_47.text())
            if l_12 < 0:
                l_12 = 0
            elif t_12 < 0:
                t_12 = 0
            elif w_12 > Width:
                w_12 = Width
            elif h_12 > Height:
                h_12 = Height

            acct1 = img[t_1: h_1, l_1: w_1]
            tnt1 = img[t_2: h_2, l_2: w_2]
            ntt1 = img[t_3: h_3, l_3: w_3]
            ct1 = img[t_4: h_4, l_4: w_4]

            acct2 = img[t_5: h_5, l_5: w_5]
            tnt2 = img[t_6: h_6, l_6: w_6]
            ntt2 = img[t_7: h_7, l_7: w_7]
            ct2 = img[t_8: h_8, l_8: w_8]

            acct3 = img[t_9: h_9, l_9: w_9]
            tnt3 = img[t_10: h_10, l_10: w_10]
            ntt3 = img[t_11: h_11, l_11: w_11]
            ct3 = img[t_12: h_12, l_12: w_12]

            try:
                text_1 = pytesseract.image_to_string(acct1, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_1 = reg.sub('', text_1)
                text_1 = text_1[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_1 not in a:
                    if fuzz.ratio(text_1, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_1))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_2 = pytesseract.image_to_string(tnt1, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_2 = reg.sub('', text_2)
                text_2 = text_2[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_2 not in a:
                    if fuzz.ratio(text_2, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_2))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_3 = pytesseract.image_to_string(ntt1, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_3 = reg.sub('', text_3)
                text_3 = text_3[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_3 not in a:
                    if fuzz.ratio(text_3, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_3))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_4 = pytesseract.image_to_string(ct1)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_4 = reg.sub('', text_4)
                text_4 = text_4[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'w')
                txt = text_4
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_5 = pytesseract.image_to_string(acct2, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_5 = reg.sub('', text_5)
                text_5 = text_5[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_5 not in a:
                    if fuzz.ratio(text_5, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_5))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue

            try:
                text_6 = pytesseract.image_to_string(tnt2, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_6 = reg.sub('', text_6)
                text_6 = text_6[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_6 not in a:
                    if fuzz.ratio(text_6, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_6))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_7 = pytesseract.image_to_string(ntt2, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_7 = reg.sub('', text_7)
                text_7 = text_7[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_7 not in a:
                    if fuzz.ratio(text_7, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_7))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_8 = pytesseract.image_to_string(ct2)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_8 = reg.sub('', text_8)
                text_8 = text_8[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_8
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_9 = pytesseract.image_to_string(acct3, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_9 = reg.sub('', text_9)
                text_9 = text_9[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_9 not in a:
                    if fuzz.ratio(text_9, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_9))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_10 = pytesseract.image_to_string(tnt3, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_10 = reg.sub('', text_10)
                text_10 = text_10[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_10 not in a:
                    if fuzz.ratio(text_10, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_10))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_11 = pytesseract.image_to_string(ntt3, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_11 = reg.sub('', text_11)
                text_11 = text_11[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_11 not in a:
                    if fuzz.ratio(text_11, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_11))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_12 = pytesseract.image_to_string(ct3)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_12 = reg.sub('', text_12)
                text_12 = text_12[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_12
                f.write(txt)
                f.close()
            except:
                continue

            os.remove('Image1.png')
        except:
            break


def reading_4():
    x = 2
    y = 1
    z = 1

    Width = GetSystemMetrics(0)
    Height = GetSystemMetrics(1)

    filename = 'Image1.png'

    while globals.RUN:
        try:
            if x == 20:
                break
            if y == 24:
                break
            if z == 24:
                break
            if keyboard.is_pressed('q'):
                break

            mon = {'top': 0, 'left': 0, 'width': Width, 'height': Height}
            screen = np.asarray(sct.grab(mon))
            cv2.imwrite(filename, screen)
            img = cv2.imread('Image1.png')

            t_1 = int(uimap.lineEdit_2.text())
            l_1 = int(uimap.lineEdit.text())
            w_1 = l_1 + int(uimap.lineEdit_13.text())
            h_1 = t_1 + int(uimap.lineEdit_14.text())
            if l_1 < 0:
                l_1 = 0
            elif t_1 < 0:
                t_1 = 0
            elif w_1 > Width:
                w_1 = Width
            elif h_1 > Height:
                h_1 = Height
            t_2 = int(uimap.lineEdit_15.text())
            l_2 = int(uimap.lineEdit_22.text())
            w_2 = l_2 + int(uimap.lineEdit_16.text())
            h_2 = t_2 + int(uimap.lineEdit_19.text())
            if l_2 < 0:
                l_2 = 0
            elif t_2 < 0:
                t_2 = 0
            elif w_2 > Width:
                w_2 = Width
            elif h_2 > Height:
                h_2 = Height
            t_3 = int(uimap.lineEdit_29.text())
            l_3 = int(uimap.lineEdit_36.text())
            w_3 = l_3 + int(uimap.lineEdit_30.text())
            h_3 = t_3 + int(uimap.lineEdit_33.text())
            if l_3 < 0:
                l_3 = 0
            elif t_3 < 0:
                t_3 = 0
            elif w_3 > Width:
                w_3 = Width
            elif h_3 > Height:
                h_3 = Height
            t_4 = int(uimap.lineEdit_43.text())
            l_4 = int(uimap.lineEdit_50.text())
            w_4 = l_4 + int(uimap.lineEdit_44.text())
            h_4 = t_4 + int(uimap.lineEdit_47.text())
            if l_4 < 0:
                l_4 = 0
            elif t_4 < 0:
                t_4 = 0
            elif w_4 > Width:
                w_4 = Width
            elif h_4 > Height:
                h_4 = Height

            t_5 = int(uimap.lineEdit_3.text())
            l_5 = int(uimap.lineEdit_4.text())
            w_5 = l_5 + int(uimap.lineEdit_13.text())
            h_5 = t_5 + int(uimap.lineEdit_14.text())
            if l_5 < 0:
                l_5 = 0
            elif t_5 < 0:
                t_5 = 0
            elif w_5 > Width:
                w_5 = Width
            elif h_5 > Height:
                h_5 = Height
            t_6 = int(uimap.lineEdit_28.text())
            l_6 = int(uimap.lineEdit_23.text())
            w_6 = l_6 + int(uimap.lineEdit_16.text())
            h_6 = t_6 + int(uimap.lineEdit_19.text())
            if l_6 < 0:
                l_6 = 0
            elif t_6 < 0:
                t_6 = 0
            elif w_6 > Width:
                w_6 = Width
            elif h_6 > Height:
                h_6 = Height
            t_7 = int(uimap.lineEdit_42.text())
            l_7 = int(uimap.lineEdit_37.text())
            w_7 = l_7 + int(uimap.lineEdit_30.text())
            h_7 = t_7 + int(uimap.lineEdit_33.text())
            if l_7 < 0:
                l_7 = 0
            elif t_7 < 0:
                t_7 = 0
            elif w_7 > Width:
                w_7 = Width
            elif h_7 > Height:
                h_7 = Height
            t_8 = int(uimap.lineEdit_56.text())
            l_8 = int(uimap.lineEdit_51.text())
            w_8 = l_8 + int(uimap.lineEdit_44.text())
            h_8 = t_8 + int(uimap.lineEdit_47.text())
            if l_8 < 0:
                l_8 = 0
            elif t_8 < 0:
                t_8 = 0
            elif w_8 > Width:
                w_8 = Width
            elif h_8 > Height:
                h_8 = Height

            t_9 = int(uimap.lineEdit_5.text())
            l_9 = int(uimap.lineEdit_6.text())
            w_9 = l_9 + int(uimap.lineEdit_13.text())
            h_9 = t_9 + int(uimap.lineEdit_14.text())
            if l_9 < 0:
                l_9 = 0
            elif t_9 < 0:
                t_9 = 0
            elif w_9 > Width:
                w_9 = Width
            elif h_9 > Height:
                h_9 = Height
            t_10 = int(uimap.lineEdit_18.text())
            l_10 = int(uimap.lineEdit_20.text())
            w_10 = l_10 + int(uimap.lineEdit_16.text())
            h_10 = t_10 + int(uimap.lineEdit_19.text())
            if l_10 < 0:
                l_10 = 0
            elif t_10 < 0:
                t_10 = 0
            elif w_10 > Width:
                w_10 = Width
            elif h_10 > Height:
                h_10 = Height
            t_11 = int(uimap.lineEdit_32.text())
            l_11 = int(uimap.lineEdit_34.text())
            w_11 = l_11 + int(uimap.lineEdit_30.text())
            h_11 = t_11 + int(uimap.lineEdit_33.text())
            if l_11 < 0:
                l_11 = 0
            elif t_11 < 0:
                t_11 = 0
            elif w_11 > Width:
                w_11 = Width
            elif h_11 > Height:
                h_11 = Height
            t_12 = int(uimap.lineEdit_46.text())
            l_12 = int(uimap.lineEdit_48.text())
            w_12 = l_12 + int(uimap.lineEdit_44.text())
            h_12 = t_12 + int(uimap.lineEdit_47.text())
            if l_12 < 0:
                l_12 = 0
            elif t_12 < 0:
                t_12 = 0
            elif w_12 > Width:
                w_12 = Width
            elif h_12 > Height:
                h_12 = Height

            t_13 = int(uimap.lineEdit_7.text())
            l_13 = int(uimap.lineEdit_10.text())
            w_13 = l_13 + int(uimap.lineEdit_13.text())
            h_13 = t_13 + int(uimap.lineEdit_14.text())
            if l_13 < 0:
                l_13 = 0
            elif t_13 < 0:
                t_13 = 0
            elif w_13 > Width:
                w_13 = Width
            elif h_13 > Height:
                h_13 = Height
            t_14 = int(uimap.lineEdit_21.text())
            l_14 = int(uimap.lineEdit_26.text())
            w_14 = l_14 + int(uimap.lineEdit_16.text())
            h_14 = t_14 + int(uimap.lineEdit_19.text())
            if l_14 < 0:
                l_14 = 0
            elif t_14 < 0:
                t_14 = 0
            elif w_14 > Width:
                w_14 = Width
            elif h_14 > Height:
                h_14 = Height
            t_15 = int(uimap.lineEdit_35.text())
            l_15 = int(uimap.lineEdit_40.text())
            w_15 = l_15 + int(uimap.lineEdit_30.text())
            h_15 = t_15 + int(uimap.lineEdit_33.text())
            if l_15 < 0:
                l_15 = 0
            elif t_15 < 0:
                t_15 = 0
            elif w_15 > Width:
                w_15 = Width
            elif h_15 > Height:
                h_15 = Height
            t_16 = int(uimap.lineEdit_49.text())
            l_16 = int(uimap.lineEdit_54.text())
            w_16 = l_16 + int(uimap.lineEdit_44.text())
            h_16 = t_16 + int(uimap.lineEdit_47.text())
            if l_16 < 0:
                l_16 = 0
            elif t_16 < 0:
                t_16 = 0
            elif w_16 > Width:
                w_16 = Width
            elif h_16 > Height:
                h_16 = Height

            acct1 = img[t_1: h_1, l_1: w_1]
            tnt1 = img[t_2: h_2, l_2: w_2]
            ntt1 = img[t_3: h_3, l_3: w_3]
            ct1 = img[t_4: h_4, l_4: w_4]

            acct2 = img[t_5: h_5, l_5: w_5]
            tnt2 = img[t_6: h_6, l_6: w_6]
            ntt2 = img[t_7: h_7, l_7: w_7]
            ct2 = img[t_8: h_8, l_8: w_8]

            acct3 = img[t_9: h_9, l_9: w_9]
            tnt3 = img[t_10: h_10, l_10: w_10]
            ntt3 = img[t_11: h_11, l_11: w_11]
            ct3 = img[t_12: h_12, l_12: w_12]

            acct4 = img[t_13: h_13, l_13: w_13]
            tnt4 = img[t_14: h_14, l_14: w_14]
            ntt4 = img[t_15: h_15, l_15: w_15]
            ct4 = img[t_16: h_16, l_16: w_16]

            try:
                text_1 = pytesseract.image_to_string(acct1, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_1 = reg.sub('', text_1)
                text_1 = text_1[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_1 not in a:
                    if fuzz.ratio(text_1, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_1))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_2 = pytesseract.image_to_string(tnt1, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_2 = reg.sub('', text_2)
                text_2 = text_2[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_2 not in a:
                    if fuzz.ratio(text_2, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_2))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_3 = pytesseract.image_to_string(ntt1, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_3 = reg.sub('', text_3)
                text_3 = text_3[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_3 not in a:
                    if fuzz.ratio(text_3, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_3))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_4 = pytesseract.image_to_string(ct1)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_4 = reg.sub('', text_4)
                text_4 = text_4[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'w')
                txt = text_4
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_5 = pytesseract.image_to_string(acct2, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_5 = reg.sub('', text_5)
                text_5 = text_5[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_5 not in a:
                    if fuzz.ratio(text_5, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_5))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue

            try:
                text_6 = pytesseract.image_to_string(tnt2, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_6 = reg.sub('', text_6)
                text_6 = text_6[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_6 not in a:
                    if fuzz.ratio(text_6, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_6))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_7 = pytesseract.image_to_string(ntt2, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_7 = reg.sub('', text_7)
                text_7 = text_7[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_7 not in a:
                    if fuzz.ratio(text_7, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_7))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_8 = pytesseract.image_to_string(ct2)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_8 = reg.sub('', text_8)
                text_8 = text_8[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_8
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_9 = pytesseract.image_to_string(acct3, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_9 = reg.sub('', text_9)
                text_9 = text_9[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_9 not in a:
                    if fuzz.ratio(text_9, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_9))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_10 = pytesseract.image_to_string(tnt3, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_10 = reg.sub('', text_10)
                text_10 = text_10[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_10 not in a:
                    if fuzz.ratio(text_10, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_10))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_11 = pytesseract.image_to_string(ntt3, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_11 = reg.sub('', text_11)
                text_11 = text_11[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_11 not in a:
                    if fuzz.ratio(text_11, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_11))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_12 = pytesseract.image_to_string(ct3)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_12 = reg.sub('', text_12)
                text_12 = text_12[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_12
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_13 = pytesseract.image_to_string(acct4, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_13 = reg.sub('', text_13)
                text_13 = text_13[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_13 not in a:
                    if fuzz.ratio(text_13, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_13))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_14 = pytesseract.image_to_string(tnt4, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_14 = reg.sub('', text_14)
                text_14 = text_14[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_14 not in a:
                    if fuzz.ratio(text_14, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_14))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_15 = pytesseract.image_to_string(ntt4, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_15 = reg.sub('', text_15)
                text_15 = text_15[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_15 not in a:
                    if fuzz.ratio(text_15, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_15))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_16 = pytesseract.image_to_string(ct4)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_16 = reg.sub('', text_16)
                text_16 = text_16[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_16
                f.write(txt)
                f.close()
            except:
                continue

            os.remove('Image1.png')
        except:
            break


def reading_5():
    x = 2
    y = 1
    z = 1

    Width = GetSystemMetrics(0)
    Height = GetSystemMetrics(1)

    filename = 'Image1.png'

    while globals.RUN:
        try:
            if x == 20:
                break
            if y == 24:
                break
            if z == 24:
                break
            if keyboard.is_pressed('q'):
                break

            mon = {'top': 0, 'left': 0, 'width': Width, 'height': Height}
            screen = np.asarray(sct.grab(mon))
            cv2.imwrite(filename, screen)
            img = cv2.imread('Image1.png')

            t_1 = int(uimap.lineEdit_2.text())
            l_1 = int(uimap.lineEdit.text())
            w_1 = l_1 + int(uimap.lineEdit_13.text())
            h_1 = t_1 + int(uimap.lineEdit_14.text())
            if l_1 < 0:
                l_1 = 0
            elif t_1 < 0:
                t_1 = 0
            elif w_1 > Width:
                w_1 = Width
            elif h_1 > Height:
                h_1 = Height
            t_2 = int(uimap.lineEdit_15.text())
            l_2 = int(uimap.lineEdit_22.text())
            w_2 = l_2 + int(uimap.lineEdit_16.text())
            h_2 = t_2 + int(uimap.lineEdit_19.text())
            if l_2 < 0:
                l_2 = 0
            elif t_2 < 0:
                t_2 = 0
            elif w_2 > Width:
                w_2 = Width
            elif h_2 > Height:
                h_2 = Height
            t_3 = int(uimap.lineEdit_29.text())
            l_3 = int(uimap.lineEdit_36.text())
            w_3 = l_3 + int(uimap.lineEdit_30.text())
            h_3 = t_3 + int(uimap.lineEdit_33.text())
            if l_3 < 0:
                l_3 = 0
            elif t_3 < 0:
                t_3 = 0
            elif w_3 > Width:
                w_3 = Width
            elif h_3 > Height:
                h_3 = Height
            t_4 = int(uimap.lineEdit_43.text())
            l_4 = int(uimap.lineEdit_50.text())
            w_4 = l_4 + int(uimap.lineEdit_44.text())
            h_4 = t_4 + int(uimap.lineEdit_47.text())
            if l_4 < 0:
                l_4 = 0
            elif t_4 < 0:
                t_4 = 0
            elif w_4 > Width:
                w_4 = Width
            elif h_4 > Height:
                h_4 = Height

            t_5 = int(uimap.lineEdit_3.text())
            l_5 = int(uimap.lineEdit_4.text())
            w_5 = l_5 + int(uimap.lineEdit_13.text())
            h_5 = t_5 + int(uimap.lineEdit_14.text())
            if l_5 < 0:
                l_5 = 0
            elif t_5 < 0:
                t_5 = 0
            elif w_5 > Width:
                w_5 = Width
            elif h_5 > Height:
                h_5 = Height
            t_6 = int(uimap.lineEdit_28.text())
            l_6 = int(uimap.lineEdit_23.text())
            w_6 = l_6 + int(uimap.lineEdit_16.text())
            h_6 = t_6 + int(uimap.lineEdit_19.text())
            if l_6 < 0:
                l_6 = 0
            elif t_6 < 0:
                t_6 = 0
            elif w_6 > Width:
                w_6 = Width
            elif h_6 > Height:
                h_6 = Height
            t_7 = int(uimap.lineEdit_42.text())
            l_7 = int(uimap.lineEdit_37.text())
            w_7 = l_7 + int(uimap.lineEdit_30.text())
            h_7 = t_7 + int(uimap.lineEdit_33.text())
            if l_7 < 0:
                l_7 = 0
            elif t_7 < 0:
                t_7 = 0
            elif w_7 > Width:
                w_7 = Width
            elif h_7 > Height:
                h_7 = Height
            t_8 = int(uimap.lineEdit_56.text())
            l_8 = int(uimap.lineEdit_51.text())
            w_8 = l_8 + int(uimap.lineEdit_44.text())
            h_8 = t_8 + int(uimap.lineEdit_47.text())
            if l_8 < 0:
                l_8 = 0
            elif t_8 < 0:
                t_8 = 0
            elif w_8 > Width:
                w_8 = Width
            elif h_8 > Height:
                h_8 = Height

            t_9 = int(uimap.lineEdit_5.text())
            l_9 = int(uimap.lineEdit_6.text())
            w_9 = l_9 + int(uimap.lineEdit_13.text())
            h_9 = t_9 + int(uimap.lineEdit_14.text())
            if l_9 < 0:
                l_9 = 0
            elif t_9 < 0:
                t_9 = 0
            elif w_9 > Width:
                w_9 = Width
            elif h_9 > Height:
                h_9 = Height
            t_10 = int(uimap.lineEdit_18.text())
            l_10 = int(uimap.lineEdit_20.text())
            w_10 = l_10 + int(uimap.lineEdit_16.text())
            h_10 = t_10 + int(uimap.lineEdit_19.text())
            if l_10 < 0:
                l_10 = 0
            elif t_10 < 0:
                t_10 = 0
            elif w_10 > Width:
                w_10 = Width
            elif h_10 > Height:
                h_10 = Height
            t_11 = int(uimap.lineEdit_32.text())
            l_11 = int(uimap.lineEdit_34.text())
            w_11 = l_11 + int(uimap.lineEdit_30.text())
            h_11 = t_11 + int(uimap.lineEdit_33.text())
            if l_11 < 0:
                l_11 = 0
            elif t_11 < 0:
                t_11 = 0
            elif w_11 > Width:
                w_11 = Width
            elif h_11 > Height:
                h_11 = Height
            t_12 = int(uimap.lineEdit_46.text())
            l_12 = int(uimap.lineEdit_48.text())
            w_12 = l_12 + int(uimap.lineEdit_44.text())
            h_12 = t_12 + int(uimap.lineEdit_47.text())
            if l_12 < 0:
                l_12 = 0
            elif t_12 < 0:
                t_12 = 0
            elif w_12 > Width:
                w_12 = Width
            elif h_12 > Height:
                h_12 = Height

            t_13 = int(uimap.lineEdit_7.text())
            l_13 = int(uimap.lineEdit_10.text())
            w_13 = l_13 + int(uimap.lineEdit_13.text())
            h_13 = t_13 + int(uimap.lineEdit_14.text())
            if l_13 < 0:
                l_13 = 0
            elif t_13 < 0:
                t_13 = 0
            elif w_13 > Width:
                w_13 = Width
            elif h_13 > Height:
                h_13 = Height
            t_14 = int(uimap.lineEdit_21.text())
            l_14 = int(uimap.lineEdit_26.text())
            w_14 = l_14 + int(uimap.lineEdit_16.text())
            h_14 = t_14 + int(uimap.lineEdit_19.text())
            if l_14 < 0:
                l_14 = 0
            elif t_14 < 0:
                t_14 = 0
            elif w_14 > Width:
                w_14 = Width
            elif h_14 > Height:
                h_14 = Height
            t_15 = int(uimap.lineEdit_35.text())
            l_15 = int(uimap.lineEdit_40.text())
            w_15 = l_15 + int(uimap.lineEdit_30.text())
            h_15 = t_15 + int(uimap.lineEdit_33.text())
            if l_15 < 0:
                l_15 = 0
            elif t_15 < 0:
                t_15 = 0
            elif w_15 > Width:
                w_15 = Width
            elif h_15 > Height:
                h_15 = Height
            t_16 = int(uimap.lineEdit_49.text())
            l_16 = int(uimap.lineEdit_54.text())
            w_16 = l_16 + int(uimap.lineEdit_44.text())
            h_16 = t_16 + int(uimap.lineEdit_47.text())
            if l_16 < 0:
                l_16 = 0
            elif t_16 < 0:
                t_16 = 0
            elif w_16 > Width:
                w_16 = Width
            elif h_16 > Height:
                h_16 = Height

            t_17 = int(uimap.lineEdit_8.text())
            l_17 = int(uimap.lineEdit_11.text())
            w_17 = l_17 + int(uimap.lineEdit_13.text())
            h_17 = t_17 + int(uimap.lineEdit_14.text())
            if l_17 < 0:
                l_17 = 0
            elif t_17 < 0:
                t_17 = 0
            elif w_17 > Width:
                w_17 = Width
            elif h_17 > Height:
                h_17 = Height
            t_18 = int(uimap.lineEdit_24.text())
            l_18 = int(uimap.lineEdit_17.text())
            w_18 = l_18 + int(uimap.lineEdit_16.text())
            h_18 = t_18 + int(uimap.lineEdit_19.text())
            if l_18 < 0:
                l_18 = 0
            elif t_18 < 0:
                t_18 = 0
            elif w_18 > Width:
                w_18 = Width
            elif h_18 > Height:
                h_18 = Height
            t_19 = int(uimap.lineEdit_38.text())
            l_19 = int(uimap.lineEdit_31.text())
            w_19 = l_19 + int(uimap.lineEdit_30.text())
            h_19 = t_19 + int(uimap.lineEdit_33.text())
            if l_19 < 0:
                l_19 = 0
            elif t_19 < 0:
                t_19 = 0
            elif w_19 > Width:
                w_19 = Width
            elif h_19 > Height:
                h_19 = Height
            t_20 = int(uimap.lineEdit_52.text())
            l_20 = int(uimap.lineEdit_45.text())
            w_20 = l_20 + int(uimap.lineEdit_44.text())
            h_20 = t_20 + int(uimap.lineEdit_47.text())
            if l_20 < 0:
                l_20 = 0
            elif t_20 < 0:
                t_20 = 0
            elif w_20 > Width:
                w_20 = Width
            elif h_20 > Height:
                h_20 = Height

            acct1 = img[t_1: h_1, l_1: w_1]
            tnt1 = img[t_2: h_2, l_2: w_2]
            ntt1 = img[t_3: h_3, l_3: w_3]
            ct1 = img[t_4: h_4, l_4: w_4]

            acct2 = img[t_5: h_5, l_5: w_5]
            tnt2 = img[t_6: h_6, l_6: w_6]
            ntt2 = img[t_7: h_7, l_7: w_7]
            ct2 = img[t_8: h_8, l_8: w_8]

            acct3 = img[t_9: h_9, l_9: w_9]
            tnt3 = img[t_10: h_10, l_10: w_10]
            ntt3 = img[t_11: h_11, l_11: w_11]
            ct3 = img[t_12: h_12, l_12: w_12]

            acct4 = img[t_13: h_13, l_13: w_13]
            tnt4 = img[t_14: h_14, l_14: w_14]
            ntt4 = img[t_15: h_15, l_15: w_15]
            ct4 = img[t_16: h_16, l_16: w_16]

            acct5 = img[t_17: h_17, l_17: w_17]
            tnt5 = img[t_18: h_18, l_18: w_18]
            ntt5 = img[t_19: h_19, l_19: w_19]
            ct5 = img[t_20: h_20, l_20: w_20]

            try:
                text_1 = pytesseract.image_to_string(acct1, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_1 = reg.sub('', text_1)
                text_1 = text_1[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_1 not in a:
                    if fuzz.ratio(text_1, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_1))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_2 = pytesseract.image_to_string(tnt1, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_2 = reg.sub('', text_2)
                text_2 = text_2[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_2 not in a:
                    if fuzz.ratio(text_2, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_2))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_3 = pytesseract.image_to_string(ntt1, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_3 = reg.sub('', text_3)
                text_3 = text_3[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_3 not in a:
                    if fuzz.ratio(text_3, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_3))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_4 = pytesseract.image_to_string(ct1)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_4 = reg.sub('', text_4)
                text_4 = text_4[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'w')
                txt = text_4
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_5 = pytesseract.image_to_string(acct2, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_5 = reg.sub('', text_5)
                text_5 = text_5[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_5 not in a:
                    if fuzz.ratio(text_5, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_5))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue

            try:
                text_6 = pytesseract.image_to_string(tnt2, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_6 = reg.sub('', text_6)
                text_6 = text_6[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_6 not in a:
                    if fuzz.ratio(text_6, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_6))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_7 = pytesseract.image_to_string(ntt2, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_7 = reg.sub('', text_7)
                text_7 = text_7[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_7 not in a:
                    if fuzz.ratio(text_7, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_7))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_8 = pytesseract.image_to_string(ct2)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_8 = reg.sub('', text_8)
                text_8 = text_8[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_8
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_9 = pytesseract.image_to_string(acct3, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_9 = reg.sub('', text_9)
                text_9 = text_9[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_9 not in a:
                    if fuzz.ratio(text_9, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_9))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_10 = pytesseract.image_to_string(tnt3, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_10 = reg.sub('', text_10)
                text_10 = text_10[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_10 not in a:
                    if fuzz.ratio(text_10, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_10))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_11 = pytesseract.image_to_string(ntt3, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_11 = reg.sub('', text_11)
                text_11 = text_11[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_11 not in a:
                    if fuzz.ratio(text_11, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_11))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_12 = pytesseract.image_to_string(ct3)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_12 = reg.sub('', text_12)
                text_12 = text_12[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_12
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_13 = pytesseract.image_to_string(acct4, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_13 = reg.sub('', text_13)
                text_13 = text_13[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_13 not in a:
                    if fuzz.ratio(text_13, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_13))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_14 = pytesseract.image_to_string(tnt4, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_14 = reg.sub('', text_14)
                text_14 = text_14[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_14 not in a:
                    if fuzz.ratio(text_14, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_14))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_15 = pytesseract.image_to_string(ntt4, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_15 = reg.sub('', text_15)
                text_15 = text_15[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_15 not in a:
                    if fuzz.ratio(text_15, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_15))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_16 = pytesseract.image_to_string(ct4)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_16 = reg.sub('', text_16)
                text_16 = text_16[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_16
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_17 = pytesseract.image_to_string(acct5, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_17 = reg.sub('', text_17)
                text_17 = text_17[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_17 not in a:
                    if fuzz.ratio(text_17, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_17))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_18 = pytesseract.image_to_string(tnt5, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_18 = reg.sub('', text_18)
                text_18 = text_18[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_18 not in a:
                    if fuzz.ratio(text_18, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_18))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_19 = pytesseract.image_to_string(ntt5, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_19 = reg.sub('', text_19)
                text_19 = text_19[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_19 not in a:
                    if fuzz.ratio(text_19, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_19))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_20 = pytesseract.image_to_string(ct5)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_20 = reg.sub('', text_20)
                text_20 = text_20[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_20
                f.write(txt)
                f.close()
            except:
                continue

            os.remove('Image1.png')
        except:
            break


def reading_6():
    x = 2
    y = 1
    z = 1

    Width = GetSystemMetrics(0)
    Height = GetSystemMetrics(1)

    filename = 'Image1.png'

    while globals.RUN:
        try:
            if x == 20:
                break
            if y == 24:
                break
            if z == 24:
                break
            if keyboard.is_pressed('q'):
                break

            mon = {'top': 0, 'left': 0, 'width': Width, 'height': Height}
            screen = np.asarray(sct.grab(mon))
            cv2.imwrite(filename, screen)
            img = cv2.imread('Image1.png')

            t_1 = int(uimap.lineEdit_2.text())
            l_1 = int(uimap.lineEdit.text())
            w_1 = l_1 + int(uimap.lineEdit_13.text())
            h_1 = t_1 + int(uimap.lineEdit_14.text())
            if l_1 < 0:
                l_1 = 0
            elif t_1 < 0:
                t_1 = 0
            elif w_1 > Width:
                w_1 = Width
            elif h_1 > Height:
                h_1 = Height
            t_2 = int(uimap.lineEdit_15.text())
            l_2 = int(uimap.lineEdit_22.text())
            w_2 = l_2 + int(uimap.lineEdit_16.text())
            h_2 = t_2 + int(uimap.lineEdit_19.text())
            if l_2 < 0:
                l_2 = 0
            elif t_2 < 0:
                t_2 = 0
            elif w_2 > Width:
                w_2 = Width
            elif h_2 > Height:
                h_2 = Height
            t_3 = int(uimap.lineEdit_29.text())
            l_3 = int(uimap.lineEdit_36.text())
            w_3 = l_3 + int(uimap.lineEdit_30.text())
            h_3 = t_3 + int(uimap.lineEdit_33.text())
            if l_3 < 0:
                l_3 = 0
            elif t_3 < 0:
                t_3 = 0
            elif w_3 > Width:
                w_3 = Width
            elif h_3 > Height:
                h_3 = Height
            t_4 = int(uimap.lineEdit_43.text())
            l_4 = int(uimap.lineEdit_50.text())
            w_4 = l_4 + int(uimap.lineEdit_44.text())
            h_4 = t_4 + int(uimap.lineEdit_47.text())
            if l_4 < 0:
                l_4 = 0
            elif t_4 < 0:
                t_4 = 0
            elif w_4 > Width:
                w_4 = Width
            elif h_4 > Height:
                h_4 = Height

            t_5 = int(uimap.lineEdit_3.text())
            l_5 = int(uimap.lineEdit_4.text())
            w_5 = l_5 + int(uimap.lineEdit_13.text())
            h_5 = t_5 + int(uimap.lineEdit_14.text())
            if l_5 < 0:
                l_5 = 0
            elif t_5 < 0:
                t_5 = 0
            elif w_5 > Width:
                w_5 = Width
            elif h_5 > Height:
                h_5 = Height
            t_6 = int(uimap.lineEdit_28.text())
            l_6 = int(uimap.lineEdit_23.text())
            w_6 = l_6 + int(uimap.lineEdit_16.text())
            h_6 = t_6 + int(uimap.lineEdit_19.text())
            if l_6 < 0:
                l_6 = 0
            elif t_6 < 0:
                t_6 = 0
            elif w_6 > Width:
                w_6 = Width
            elif h_6 > Height:
                h_6 = Height
            t_7 = int(uimap.lineEdit_42.text())
            l_7 = int(uimap.lineEdit_37.text())
            w_7 = l_7 + int(uimap.lineEdit_30.text())
            h_7 = t_7 + int(uimap.lineEdit_33.text())
            if l_7 < 0:
                l_7 = 0
            elif t_7 < 0:
                t_7 = 0
            elif w_7 > Width:
                w_7 = Width
            elif h_7 > Height:
                h_7 = Height
            t_8 = int(uimap.lineEdit_56.text())
            l_8 = int(uimap.lineEdit_51.text())
            w_8 = l_8 + int(uimap.lineEdit_44.text())
            h_8 = t_8 + int(uimap.lineEdit_47.text())
            if l_8 < 0:
                l_8 = 0
            elif t_8 < 0:
                t_8 = 0
            elif w_8 > Width:
                w_8 = Width
            elif h_8 > Height:
                h_8 = Height

            t_9 = int(uimap.lineEdit_5.text())
            l_9 = int(uimap.lineEdit_6.text())
            w_9 = l_9 + int(uimap.lineEdit_13.text())
            h_9 = t_9 + int(uimap.lineEdit_14.text())
            if l_9 < 0:
                l_9 = 0
            elif t_9 < 0:
                t_9 = 0
            elif w_9 > Width:
                w_9 = Width
            elif h_9 > Height:
                h_9 = Height
            t_10 = int(uimap.lineEdit_18.text())
            l_10 = int(uimap.lineEdit_20.text())
            w_10 = l_10 + int(uimap.lineEdit_16.text())
            h_10 = t_10 + int(uimap.lineEdit_19.text())
            if l_10 < 0:
                l_10 = 0
            elif t_10 < 0:
                t_10 = 0
            elif w_10 > Width:
                w_10 = Width
            elif h_10 > Height:
                h_10 = Height
            t_11 = int(uimap.lineEdit_32.text())
            l_11 = int(uimap.lineEdit_34.text())
            w_11 = l_11 + int(uimap.lineEdit_30.text())
            h_11 = t_11 + int(uimap.lineEdit_33.text())
            if l_11 < 0:
                l_11 = 0
            elif t_11 < 0:
                t_11 = 0
            elif w_11 > Width:
                w_11 = Width
            elif h_11 > Height:
                h_11 = Height
            t_12 = int(uimap.lineEdit_46.text())
            l_12 = int(uimap.lineEdit_48.text())
            w_12 = l_12 + int(uimap.lineEdit_44.text())
            h_12 = t_12 + int(uimap.lineEdit_47.text())
            if l_12 < 0:
                l_12 = 0
            elif t_12 < 0:
                t_12 = 0
            elif w_12 > Width:
                w_12 = Width
            elif h_12 > Height:
                h_12 = Height

            t_13 = int(uimap.lineEdit_7.text())
            l_13 = int(uimap.lineEdit_10.text())
            w_13 = l_13 + int(uimap.lineEdit_13.text())
            h_13 = t_13 + int(uimap.lineEdit_14.text())
            if l_13 < 0:
                l_13 = 0
            elif t_13 < 0:
                t_13 = 0
            elif w_13 > Width:
                w_13 = Width
            elif h_13 > Height:
                h_13 = Height
            t_14 = int(uimap.lineEdit_21.text())
            l_14 = int(uimap.lineEdit_26.text())
            w_14 = l_14 + int(uimap.lineEdit_16.text())
            h_14 = t_14 + int(uimap.lineEdit_19.text())
            if l_14 < 0:
                l_14 = 0
            elif t_14 < 0:
                t_14 = 0
            elif w_14 > Width:
                w_14 = Width
            elif h_14 > Height:
                h_14 = Height
            t_15 = int(uimap.lineEdit_35.text())
            l_15 = int(uimap.lineEdit_40.text())
            w_15 = l_15 + int(uimap.lineEdit_30.text())
            h_15 = t_15 + int(uimap.lineEdit_33.text())
            if l_15 < 0:
                l_15 = 0
            elif t_15 < 0:
                t_15 = 0
            elif w_15 > Width:
                w_15 = Width
            elif h_15 > Height:
                h_15 = Height
            t_16 = int(uimap.lineEdit_49.text())
            l_16 = int(uimap.lineEdit_54.text())
            w_16 = l_16 + int(uimap.lineEdit_44.text())
            h_16 = t_16 + int(uimap.lineEdit_47.text())
            if l_16 < 0:
                l_16 = 0
            elif t_16 < 0:
                t_16 = 0
            elif w_16 > Width:
                w_16 = Width
            elif h_16 > Height:
                h_16 = Height

            t_17 = int(uimap.lineEdit_8.text())
            l_17 = int(uimap.lineEdit_11.text())
            w_17 = l_17 + int(uimap.lineEdit_13.text())
            h_17 = t_17 + int(uimap.lineEdit_14.text())
            if l_17 < 0:
                l_17 = 0
            elif t_17 < 0:
                t_17 = 0
            elif w_17 > Width:
                w_17 = Width
            elif h_17 > Height:
                h_17 = Height
            t_18 = int(uimap.lineEdit_24.text())
            l_18 = int(uimap.lineEdit_17.text())
            w_18 = l_18 + int(uimap.lineEdit_16.text())
            h_18 = t_18 + int(uimap.lineEdit_19.text())
            if l_18 < 0:
                l_18 = 0
            elif t_18 < 0:
                t_18 = 0
            elif w_18 > Width:
                w_18 = Width
            elif h_18 > Height:
                h_18 = Height
            t_19 = int(uimap.lineEdit_38.text())
            l_19 = int(uimap.lineEdit_31.text())
            w_19 = l_19 + int(uimap.lineEdit_30.text())
            h_19 = t_19 + int(uimap.lineEdit_33.text())
            if l_19 < 0:
                l_19 = 0
            elif t_19 < 0:
                t_19 = 0
            elif w_19 > Width:
                w_19 = Width
            elif h_19 > Height:
                h_19 = Height
            t_20 = int(uimap.lineEdit_52.text())
            l_20 = int(uimap.lineEdit_45.text())
            w_20 = l_20 + int(uimap.lineEdit_44.text())
            h_20 = t_20 + int(uimap.lineEdit_47.text())
            if l_20 < 0:
                l_20 = 0
            elif t_20 < 0:
                t_20 = 0
            elif w_20 > Width:
                w_20 = Width
            elif h_20 > Height:
                h_20 = Height

            t_21 = int(uimap.lineEdit_9.text())
            l_21 = int(uimap.lineEdit_12.text())
            w_21 = l_21 + int(uimap.lineEdit_13.text())
            h_21 = t_21 + int(uimap.lineEdit_14.text())
            if l_21 < 0:
                l_21 = 0
            elif t_21 < 0:
                t_21 = 0
            elif w_21 > Width:
                w_21 = Width
            elif h_21 > Height:
                h_21 = Height
            t_22 = int(uimap.lineEdit_25.text())
            l_22 = int(uimap.lineEdit_27.text())
            w_22 = l_22 + int(uimap.lineEdit_16.text())
            h_22 = t_22 + int(uimap.lineEdit_19.text())
            if l_22 < 0:
                l_22 = 0
            elif t_22 < 0:
                t_22 = 0
            elif w_22 > Width:
                w_22 = Width
            elif h_22 > Height:
                h_22 = Height
            t_23 = int(uimap.lineEdit_39.text())
            l_23 = int(uimap.lineEdit_41.text())
            w_23 = l_23 + int(uimap.lineEdit_30.text())
            h_23 = t_23 + int(uimap.lineEdit_33.text())
            if l_23 < 0:
                l_23 = 0
            elif t_23 < 0:
                t_23 = 0
            elif w_23 > Width:
                w_23 = Width
            elif h_23 > Height:
                h_23 = Height
            t_24 = int(uimap.lineEdit_53.text())
            l_24 = int(uimap.lineEdit_55.text())
            w_24 = l_24 + int(uimap.lineEdit_44.text())
            h_24 = t_24 + int(uimap.lineEdit_47.text())
            if l_24 < 0:
                l_24 = 0
            elif t_24 < 0:
                t_24 = 0
            elif w_24 > Width:
                w_24 = Width
            elif h_24 > Height:
                h_24 = Height

            acct1 = img[t_1: h_1, l_1: w_1]
            tnt1 = img[t_2: h_2, l_2: w_2]
            ntt1 = img[t_3: h_3, l_3: w_3]
            ct1 = img[t_4: h_4, l_4: w_4]

            acct2 = img[t_5: h_5, l_5: w_5]
            tnt2 = img[t_6: h_6, l_6: w_6]
            ntt2 = img[t_7: h_7, l_7: w_7]
            ct2 = img[t_8: h_8, l_8: w_8]

            acct3 = img[t_9: h_9, l_9: w_9]
            tnt3 = img[t_10: h_10, l_10: w_10]
            ntt3 = img[t_11: h_11, l_11: w_11]
            ct3 = img[t_12: h_12, l_12: w_12]

            acct4 = img[t_13: h_13, l_13: w_13]
            tnt4 = img[t_14: h_14, l_14: w_14]
            ntt4 = img[t_15: h_15, l_15: w_15]
            ct4 = img[t_16: h_16, l_16: w_16]

            acct5 = img[t_17: h_17, l_17: w_17]
            tnt5 = img[t_18: h_18, l_18: w_18]
            ntt5 = img[t_19: h_19, l_19: w_19]
            ct5 = img[t_20: h_20, l_20: w_20]

            acct6 = img[t_21: h_21, l_21: w_21]
            tnt6 = img[t_22: h_22, l_22: w_22]
            ntt6 = img[t_23: h_23, l_23: w_23]
            ct6 = img[t_24: h_24, l_24: w_24]

            try:
                text_1 = pytesseract.image_to_string(acct1, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_1 = reg.sub('', text_1)
                text_1 = text_1[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_1 not in a:
                    if fuzz.ratio(text_1, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_1))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_2 = pytesseract.image_to_string(tnt1, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_2 = reg.sub('', text_2)
                text_2 = text_2[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_2 not in a:
                    if fuzz.ratio(text_2, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_2))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_3 = pytesseract.image_to_string(ntt1, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_3 = reg.sub('', text_3)
                text_3 = text_3[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_3 not in a:
                    if fuzz.ratio(text_3, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_3))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_4 = pytesseract.image_to_string(ct1)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_4 = reg.sub('', text_4)
                text_4 = text_4[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'w')
                txt = text_4
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_5 = pytesseract.image_to_string(acct2, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_5 = reg.sub('', text_5)
                text_5 = text_5[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_5 not in a:
                    if fuzz.ratio(text_5, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_5))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue

            try:
                text_6 = pytesseract.image_to_string(tnt2, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_6 = reg.sub('', text_6)
                text_6 = text_6[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_6 not in a:
                    if fuzz.ratio(text_6, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_6))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_7 = pytesseract.image_to_string(ntt2, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_7 = reg.sub('', text_7)
                text_7 = text_7[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_7 not in a:
                    if fuzz.ratio(text_7, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_7))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_8 = pytesseract.image_to_string(ct2)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_8 = reg.sub('', text_8)
                text_8 = text_8[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_8
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_9 = pytesseract.image_to_string(acct3, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_9 = reg.sub('', text_9)
                text_9 = text_9[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_9 not in a:
                    if fuzz.ratio(text_9, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_9))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_10 = pytesseract.image_to_string(tnt3, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_10 = reg.sub('', text_10)
                text_10 = text_10[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_10 not in a:
                    if fuzz.ratio(text_10, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_10))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_11 = pytesseract.image_to_string(ntt3, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_11 = reg.sub('', text_11)
                text_11 = text_11[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_11 not in a:
                    if fuzz.ratio(text_11, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_11))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_12 = pytesseract.image_to_string(ct3)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_12 = reg.sub('', text_12)
                text_12 = text_12[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_12
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_13 = pytesseract.image_to_string(acct4, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_13 = reg.sub('', text_13)
                text_13 = text_13[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_13 not in a:
                    if fuzz.ratio(text_13, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_13))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_14 = pytesseract.image_to_string(tnt4, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_14 = reg.sub('', text_14)
                text_14 = text_14[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_14 not in a:
                    if fuzz.ratio(text_14, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_14))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_15 = pytesseract.image_to_string(ntt4, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_15 = reg.sub('', text_15)
                text_15 = text_15[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_15 not in a:
                    if fuzz.ratio(text_15, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_15))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_16 = pytesseract.image_to_string(ct4)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_16 = reg.sub('', text_16)
                text_16 = text_16[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_16
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_17 = pytesseract.image_to_string(acct5, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_17 = reg.sub('', text_17)
                text_17 = text_17[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_17 not in a:
                    if fuzz.ratio(text_17, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_17))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_18 = pytesseract.image_to_string(tnt5, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_18 = reg.sub('', text_18)
                text_18 = text_18[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_18 not in a:
                    if fuzz.ratio(text_18, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_18))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_19 = pytesseract.image_to_string(ntt5, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_19 = reg.sub('', text_19)
                text_19 = text_19[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_19 not in a:
                    if fuzz.ratio(text_19, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_19))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_20 = pytesseract.image_to_string(ct5)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_20 = reg.sub('', text_20)
                text_20 = text_20[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_20
                f.write(txt)
                f.close()
            except:
                continue

            try:
                text_21 = pytesseract.image_to_string(acct6, lang = 'eng')
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_21 = reg.sub('', text_21)
                text_21 = text_21[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_21 not in a:
                    if fuzz.ratio(text_21, a) < 2:
                        x += 1
                        color = uitable.tableWidget.item(0, x).background()
                        uitable.tableWidget.setItem(0, x, QtWidgets.QTableWidgetItem(text_21))
                        uitable.tableWidget.item(0, x).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_22 = pytesseract.image_to_string(tnt6, lang = 'chi_sim')
                reg = re.compile('[^\u4e00-\u9fff0-9]')
                text_22 = reg.sub('', text_22)
                text_22 = text_22[0:30]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_22 not in a:
                    if fuzz.ratio(text_22, a) < 2:
                        y += 1
                        color = uitable.tableWidget.item(y, 0).background()
                        uitable.tableWidget.setItem(y, 0, QtWidgets.QTableWidgetItem(text_22))
                        uitable.tableWidget.item(y, 0).setBackground(color)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_23 = pytesseract.image_to_string(ntt6, lang = 'chi_sim')
                reg = re.compile('[^0-9]')
                text_23 = reg.sub('', text_23)
                text_23 = text_23[0:4]
                rows_an = uitable.tableWidget.rowCount()
                cols_an = uitable.tableWidget.columnCount()
                data_an = []
                for row in range(rows_an):
                    tmp_an = []
                    for col in range(cols_an):
                        try:
                            tmp_an.append(uitable.tableWidget.item(row, col).text())
                        except:
                            tmp_an.append('0')
                    data_an.append(tmp_an)
                a = sum(data_an, [])
                if text_23 not in a:
                    if fuzz.ratio(text_23, a) < 5:
                        z += 1
                        color = uitable.tableWidget.item(z, 2).background()
                        uitable.tableWidget.setItem(z, 2, QtWidgets.QTableWidgetItem(text_23))
                        uitable.tableWidget.item(z, 2).setBackground(color)
                        autoset(z, x)
                uitable.tableWidget.update()
                QtGui.QGuiApplication.processEvents()
            except:
                continue
            try:
                text_24 = pytesseract.image_to_string(ct6)
                reg = re.compile('[^a-zA-ZА-Яа-я0-9]')
                text_24 = reg.sub('', text_24)
                text_24 = text_24[0:30]
                txtname = 'Cards.txt'
                f = open(txtname, 'a')
                txt = text_24
                f.write(txt)
                f.close()
            except:
                continue

            os.remove('Image1.png')
        except:
            break
#-------------------------------------------------------------------------



# Поток
#-------------------------------------------------------------------------
def stop():
    globals.RUN = False
    uiwin.pushButton_555.hide()
    uiwin.pushButton_55.show()
    uiwin.timer.stop()


def startstop():
    globals.RUN = True
    uiwin.pushButton_55.hide()
    uiwin.pushButton_555.setStyleSheet("background:#fff2d3")
    uiwin.pushButton_555.show()


def starter():
    startstop()
    th = threading.Thread(target=how_many_tables)
    th.start()
    uiwin.timer.setInterval(1000)
    uiwin.timer.timeout.connect(displayTime)
    uiwin.timer.start()


def displayTime():
    uiwin.textEdit.clear()
    uiwin.textEdit.setPlainText(QtCore.QDateTime.currentDateTime().toString())
#-------------------------------------------------------------------------



# Таблица
#-------------------------------------------------------------------------
def settime():
    y = uitable.tableWidget.currentRow()
    x = uitable.tableWidget.currentColumn()
    now = datetime.datetime.now()
    num = x%2
    color = uitable.tableWidget.item(y, x).background()
    if y > 1 and x > 2:
        if num == 1:
            uitable.tableWidget.setItem(y, x, QtWidgets.QTableWidgetItem(now.strftime("%H:%M:%S")))
            uitable.tableWidget.item(y, x).setBackground(color)
            try:
                dt_from = uitable.tableWidget.item(y, x).text()
                dt_to = now.strftime("%H:%M:%S")
                dt_from = datetime.datetime.strptime(dt_from, '%H:%M:%S')
                dt_to = datetime.datetime.strptime(dt_to, '%H:%M:%S')
                delta = dt_to - dt_from
                uitable.tableWidget.setItem(y, x+1, QtWidgets.QTableWidgetItem(str(delta)))
                uitable.tableWidget.item(y, x + 1).setBackground(color)
            except:
                uitable.tableWidget.setItem(y, x+1, QtWidgets.QTableWidgetItem(''))


def autoset(row, col):
    y = row
    x = col
    now = datetime.datetime.now()
    num = x % 2
    color = uitable.tableWidget.item(y, x).background()
    if y > 1 and x > 2:
        if num == 1:
            uitable.tableWidget.setItem(y, x, QtWidgets.QTableWidgetItem(now.strftime("%H:%M:%S")))
            uitable.tableWidget.item(y, x).setBackground(color)
            try:
                dt_from = uitable.tableWidget.item(y, x).text()
                dt_to = now.strftime("%H:%M:%S")
                dt_from = datetime.datetime.strptime(dt_from, '%H:%M:%S')
                dt_to = datetime.datetime.strptime(dt_to, '%H:%M:%S')
                delta = dt_to - dt_from
                uitable.tableWidget.setItem(y, x + 1, QtWidgets.QTableWidgetItem(str(delta)))
                uitable.tableWidget.item(y, x + 1).setBackground(color)
            except:
                uitable.tableWidget.setItem(y, x + 1, QtWidgets.QTableWidgetItem(''))


def update():
    row = 25
    while row !=1:
        col = uitable.tableWidget.item(row, 3).text()
        if col != '':
            y = row
            x = 4
            now = datetime.datetime.now()
            color = uitable.tableWidget.item(y, x).background()
            if y > 1 and x > 2:
                try:
                    dt_from = uitable.tableWidget.item(y, 3).text()
                    dt_to = now.strftime("%H:%M:%S")
                    dt_from = datetime.datetime.strptime(dt_from, '%H:%M:%S')
                    dt_to = datetime.datetime.strptime(dt_to, '%H:%M:%S')
                    delta = dt_to - dt_from
                    uitable.tableWidget.setItem(y, x, QtWidgets.QTableWidgetItem(str(delta)))
                    uitable.tableWidget.item(y, x).setBackground(color)
                except:
                    row = row
        row = row-1

        row2 = 25
        while row2 != 1:
            col2 = uitable.tableWidget.item(row2, 5).text()
            if col2 != '':
                y2 = row2
                x2 = 6
                now2 = datetime.datetime.now()
                color2 = uitable.tableWidget.item(y2, x2).background()
                if y2 > 1 and x2 > 2:
                    try:
                        dt_from2 = uitable.tableWidget.item(y2, 5).text()
                        dt_to2 = now2.strftime("%H:%M:%S")
                        dt_from2 = datetime.datetime.strptime(dt_from2, '%H:%M:%S')
                        dt_to2 = datetime.datetime.strptime(dt_to2, '%H:%M:%S')
                        delta2 = dt_to2 - dt_from2
                        uitable.tableWidget.setItem(y2, x2, QtWidgets.QTableWidgetItem(str(delta2)))
                        uitable.tableWidget.item(y2, x2).setBackground(color2)
                    except:
                        row2 = row2
            row2 = row2 - 1

        row3 = 25
        while row3 != 1:
            col3 = uitable.tableWidget.item(row3, 7).text()
            if col3 != '':
                y3 = row3
                x3 = 8
                now3 = datetime.datetime.now()
                color3 = uitable.tableWidget.item(y3, x3).background()
                if y3 > 1 and x3 > 2:
                    try:
                        dt_from3 = uitable.tableWidget.item(y3, 7).text()
                        dt_to3 = now3.strftime("%H:%M:%S")
                        dt_from3 = datetime.datetime.strptime(dt_from3, '%H:%M:%S')
                        dt_to3 = datetime.datetime.strptime(dt_to3, '%H:%M:%S')
                        delta3 = dt_to3 - dt_from3
                        uitable.tableWidget.setItem(y3, x3, QtWidgets.QTableWidgetItem(str(delta3)))
                        uitable.tableWidget.item(y3, x3).setBackground(color3)
                    except:
                        row3 = row3
            row3 = row3 - 1

        row4 = 25
        while row4 != 1:
            col4 = uitable.tableWidget.item(row4, 9).text()
            if col4 != '':
                y4 = row4
                x4 = 10
                now4 = datetime.datetime.now()
                color4 = uitable.tableWidget.item(y4, x4).background()
                if y4 > 1 and x4 > 2:
                    try:
                        dt_from4 = uitable.tableWidget.item(y4, 9).text()
                        dt_to4 = now4.strftime("%H:%M:%S")
                        dt_from4 = datetime.datetime.strptime(dt_from4, '%H:%M:%S')
                        dt_to4 = datetime.datetime.strptime(dt_to4, '%H:%M:%S')
                        delta4 = dt_to4 - dt_from4
                        uitable.tableWidget.setItem(y4, x4, QtWidgets.QTableWidgetItem(str(delta4)))
                        uitable.tableWidget.item(y4, x4).setBackground(color4)
                    except:
                        row4 = row4
            row4 = row4 - 1

        row5 = 25
        while row5 != 1:
            col5 = uitable.tableWidget.item(row5, 11).text()
            if col5 != '':
                y5 = row5
                x5 = 12
                now5 = datetime.datetime.now()
                color5 = uitable.tableWidget.item(y5, x5).background()
                if y5 > 1 and x5 > 2:
                    try:
                        dt_from5 = uitable.tableWidget.item(y5, 11).text()
                        dt_to5 = now5.strftime("%H:%M:%S")
                        dt_from5 = datetime.datetime.strptime(dt_from5, '%H:%M:%S')
                        dt_to5 = datetime.datetime.strptime(dt_to5, '%H:%M:%S')
                        delta5 = dt_to5 - dt_from5
                        uitable.tableWidget.setItem(y5, x5, QtWidgets.QTableWidgetItem(str(delta5)))
                        uitable.tableWidget.item(y5, x5).setBackground(color5)
                    except:
                        row5 = row5
            row5 = row5 - 1

        row6 = 25
        while row6 != 1:
            col6 = uitable.tableWidget.item(row6, 13).text()
            if col6 != '':
                y6 = row6
                x6 = 14
                now6 = datetime.datetime.now()
                color6 = uitable.tableWidget.item(y6, x6).background()
                if y6 > 1 and x6 > 2:
                    try:
                        dt_from6 = uitable.tableWidget.item(y6, 13).text()
                        dt_to6 = now6.strftime("%H:%M:%S")
                        dt_from6 = datetime.datetime.strptime(dt_from6, '%H:%M:%S')
                        dt_to6 = datetime.datetime.strptime(dt_to6, '%H:%M:%S')
                        delta6 = dt_to6 - dt_from6
                        uitable.tableWidget.setItem(y6, x6, QtWidgets.QTableWidgetItem(str(delta6)))
                        uitable.tableWidget.item(y6, x6).setBackground(color6)
                    except:
                        row6 = row6
            row6 = row6 - 1

        row7 = 25
        while row7 != 1:
            col7 = uitable.tableWidget.item(row7, 15).text()
            if col7 != '':
                y7 = row7
                x7 = 16
                now7 = datetime.datetime.now()
                color7 = uitable.tableWidget.item(y7, x7).background()
                if y7 > 1 and x7 > 2:
                    try:
                        dt_from7 = uitable.tableWidget.item(y7, 15).text()
                        dt_to7 = now7.strftime("%H:%M:%S")
                        dt_from7 = datetime.datetime.strptime(dt_from7, '%H:%M:%S')
                        dt_to7 = datetime.datetime.strptime(dt_to7, '%H:%M:%S')
                        delta7 = dt_to7 - dt_from7
                        uitable.tableWidget.setItem(y7, x7, QtWidgets.QTableWidgetItem(str(delta7)))
                        uitable.tableWidget.item(y7, x7).setBackground(color7)
                    except:
                        row7 = row7
            row7 = row7 - 1

        row8 = 25
        while row8 != 1:
            col8 = uitable.tableWidget.item(row8, 17).text()
            if col8 != '':
                y8 = row8
                x8 = 18
                now8 = datetime.datetime.now()
                color8 = uitable.tableWidget.item(y8, x8).background()
                if y8 > 1 and x8 > 2:
                    try:
                        dt_from8 = uitable.tableWidget.item(y8, 17).text()
                        dt_to8 = now8.strftime("%H:%M:%S")
                        dt_from8 = datetime.datetime.strptime(dt_from8, '%H:%M:%S')
                        dt_to8 = datetime.datetime.strptime(dt_to8, '%H:%M:%S')
                        delta8 = dt_to8 - dt_from8
                        uitable.tableWidget.setItem(y8, x8, QtWidgets.QTableWidgetItem(str(delta8)))
                        uitable.tableWidget.item(y8, x8).setBackground(color8)
                    except:
                        row8 = row8
            row8 = row8 - 1

        row9 = 25
        while row9 != 1:
            col9 = uitable.tableWidget.item(row9, 19).text()
            if col9 != '':
                y9 = row9
                x9 = 20
                now9 = datetime.datetime.now()
                color9 = uitable.tableWidget.item(y9, x9).background()
                if y9 > 1 and x9 > 2:
                    try:
                        dt_from9 = uitable.tableWidget.item(y9, 19).text()
                        dt_to9 = now9.strftime("%H:%M:%S")
                        dt_from9 = datetime.datetime.strptime(dt_from9, '%H:%M:%S')
                        dt_to9 = datetime.datetime.strptime(dt_to9, '%H:%M:%S')
                        delta9 = dt_to9 - dt_from9
                        uitable.tableWidget.setItem(y9, x9, QtWidgets.QTableWidgetItem(str(delta9)))
                        uitable.tableWidget.item(y9, x9).setBackground(color9)
                    except:
                        row9 = row9
            row9 = row9 - 1

        row10 = 25
        while row10 != 1:
            col10 = uitable.tableWidget.item(row10, 21).text()
            if col10 != '':
                y10 = row10
                x10 = 22
                now10 = datetime.datetime.now()
                color10 = uitable.tableWidget.item(y10, x10).background()
                if y10 > 1 and x10 > 2:
                    try:
                        dt_from10 = uitable.tableWidget.item(y10, 21).text()
                        dt_to10 = now10.strftime("%H:%M:%S")
                        dt_from10 = datetime.datetime.strptime(dt_from10, '%H:%M:%S')
                        dt_to10 = datetime.datetime.strptime(dt_to10, '%H:%M:%S')
                        delta10 = dt_to10 - dt_from10
                        uitable.tableWidget.setItem(y10, x10, QtWidgets.QTableWidgetItem(str(delta10)))
                        uitable.tableWidget.item(y10, x10).setBackground(color10)
                    except:
                        row10 = row10
            row10 = row10 - 1

        row11 = 25
        while row11 != 1:
            col11 = uitable.tableWidget.item(row11, 23).text()
            if col11 != '':
                y11 = row11
                x11 = 24
                now11 = datetime.datetime.now()
                color11 = uitable.tableWidget.item(y11, x11).background()
                if y11 > 1 and x11 > 2:
                    try:
                        dt_from11 = uitable.tableWidget.item(y11, 21).text()
                        dt_to11 = now11.strftime("%H:%M:%S")
                        dt_from11 = datetime.datetime.strptime(dt_from11, '%H:%M:%S')
                        dt_to11 = datetime.datetime.strptime(dt_to11, '%H:%M:%S')
                        delta11 = dt_to11 - dt_from11
                        uitable.tableWidget.setItem(y11, x11, QtWidgets.QTableWidgetItem(str(delta11)))
                        uitable.tableWidget.item(y11, x11).setBackground(color11)
                    except:
                        row11 = row11
            row11 = row11 - 1

        row12 = 25
        while row12 != 1:
            col12 = uitable.tableWidget.item(row12, 25).text()
            if col12 != '':
                y12 = row12
                x12 = 26
                now12 = datetime.datetime.now()
                color12 = uitable.tableWidget.item(y12, x12).background()
                if y12 > 1 and x12 > 2:
                    try:
                        dt_from12 = uitable.tableWidget.item(y12, 25).text()
                        dt_to12 = now12.strftime("%H:%M:%S")
                        dt_from12 = datetime.datetime.strptime(dt_from12, '%H:%M:%S')
                        dt_to12 = datetime.datetime.strptime(dt_to12, '%H:%M:%S')
                        delta12 = dt_to12 - dt_from12
                        uitable.tableWidget.setItem(y12, x12, QtWidgets.QTableWidgetItem(str(delta12)))
                        uitable.tableWidget.item(y12, x12).setBackground(color12)
                    except:
                        row12 = row12
            row12 = row12 - 1

        row13 = 25
        while row13 != 1:
            col13 = uitable.tableWidget.item(row13, 27).text()
            if col13 != '':
                y13 = row13
                x13 = 28
                now13 = datetime.datetime.now()
                color13 = uitable.tableWidget.item(y13, x13).background()
                if y13 > 1 and x13 > 2:
                    try:
                        dt_from13 = uitable.tableWidget.item(y13, 27).text()
                        dt_to13 = now13.strftime("%H:%M:%S")
                        dt_from13 = datetime.datetime.strptime(dt_from13, '%H:%M:%S')
                        dt_to13 = datetime.datetime.strptime(dt_to13, '%H:%M:%S')
                        delta13 = dt_to13 - dt_from13
                        uitable.tableWidget.setItem(y13, x13, QtWidgets.QTableWidgetItem(str(delta13)))
                        uitable.tableWidget.item(y13, x13).setBackground(color13)
                    except:
                        row13 = row13
            row13 = row13 - 1

        row14 = 25
        while row14 != 1:
            col14 = uitable.tableWidget.item(row14, 29).text()
            if col14 != '':
                y14 = row14
                x14 = 30
                now14 = datetime.datetime.now()
                color14 = uitable.tableWidget.item(y14, x14).background()
                if y14 > 1 and x14 > 2:
                    try:
                        dt_from14 = uitable.tableWidget.item(y14, 29).text()
                        dt_to14 = now14.strftime("%H:%M:%S")
                        dt_from14 = datetime.datetime.strptime(dt_from14, '%H:%M:%S')
                        dt_to14 = datetime.datetime.strptime(dt_to14, '%H:%M:%S')
                        delta14 = dt_to14 - dt_from14
                        uitable.tableWidget.setItem(y14, x14, QtWidgets.QTableWidgetItem(str(delta14)))
                        uitable.tableWidget.item(y14, x14).setBackground(color14)
                    except:
                        row14 = row14
            row14 = row14 - 1

        row15 = 25
        while row15 != 1:
            col15 = uitable.tableWidget.item(row15, 31).text()
            if col15 != '':
                y15 = row15
                x15 = 32
                now15 = datetime.datetime.now()
                color15 = uitable.tableWidget.item(y15, x15).background()
                if y15 > 1 and x15 > 2:
                    try:
                        dt_from15 = uitable.tableWidget.item(y15, 31).text()
                        dt_to15 = now15.strftime("%H:%M:%S")
                        dt_from15 = datetime.datetime.strptime(dt_from15, '%H:%M:%S')
                        dt_to15 = datetime.datetime.strptime(dt_to15, '%H:%M:%S')
                        delta15 = dt_to15 - dt_from15
                        uitable.tableWidget.setItem(y15, x15, QtWidgets.QTableWidgetItem(str(delta15)))
                        uitable.tableWidget.item(y15, x15).setBackground(color15)
                    except:
                        row15 = row15
            row15 = row15 - 1

        row16 = 25
        while row16 != 1:
            col16 = uitable.tableWidget.item(row16, 33).text()
            if col16 != '':
                y16 = row16
                x16 = 34
                now16 = datetime.datetime.now()
                color16 = uitable.tableWidget.item(y16, x16).background()
                if y16 > 1 and x16 > 2:
                    try:
                        dt_from16 = uitable.tableWidget.item(y16, 33).text()
                        dt_to16 = now16.strftime("%H:%M:%S")
                        dt_from16 = datetime.datetime.strptime(dt_from16, '%H:%M:%S')
                        dt_to16 = datetime.datetime.strptime(dt_to16, '%H:%M:%S')
                        delta16 = dt_to16 - dt_from16
                        uitable.tableWidget.setItem(y16, x16, QtWidgets.QTableWidgetItem(str(delta16)))
                        uitable.tableWidget.item(y16, x16).setBackground(color16)
                    except:
                        row16 = row16
            row16 = row16 - 1

        row17 = 25
        while row17 != 1:
            col17 = uitable.tableWidget.item(row17, 35).text()
            if col17 != '':
                y17 = row17
                x17 = 36
                now17 = datetime.datetime.now()
                color17 = uitable.tableWidget.item(y17, x17).background()
                if y17 > 1 and x17 > 2:
                    try:
                        dt_from17 = uitable.tableWidget.item(y17, 35).text()
                        dt_to17 = now17.strftime("%H:%M:%S")
                        dt_from17 = datetime.datetime.strptime(dt_from17, '%H:%M:%S')
                        dt_to17 = datetime.datetime.strptime(dt_to17, '%H:%M:%S')
                        delta17 = dt_to17 - dt_from17
                        uitable.tableWidget.setItem(y17, x17, QtWidgets.QTableWidgetItem(str(delta17)))
                        uitable.tableWidget.item(y17, x17).setBackground(color17)
                    except:
                        row17 = row17
            row17 = row17 - 1

        row18 = 25
        while row18 != 1:
            col18 = uitable.tableWidget.item(row18, 37).text()
            if col18 != '':
                y18 = row18
                x18 = 38
                now18 = datetime.datetime.now()
                color18 = uitable.tableWidget.item(y18, x18).background()
                if y18 > 1 and x18 > 2:
                    try:
                        dt_from18 = uitable.tableWidget.item(y18, 37).text()
                        dt_to18 = now18.strftime("%H:%M:%S")
                        dt_from18 = datetime.datetime.strptime(dt_from18, '%H:%M:%S')
                        dt_to18 = datetime.datetime.strptime(dt_to18, '%H:%M:%S')
                        delta18 = dt_to18 - dt_from18
                        uitable.tableWidget.setItem(y18, x18, QtWidgets.QTableWidgetItem(str(delta18)))
                        uitable.tableWidget.item(y18, x18).setBackground(color18)
                    except:
                        row18 = row18
            row18 = row18 - 1

        row19 = 25
        while row19 != 1:
            col19 = uitable.tableWidget.item(row19, 39).text()
            if col19 != '':
                y19 = row19
                x19 = 40
                now19 = datetime.datetime.now()
                color19 = uitable.tableWidget.item(y19, x19).background()
                if y19 > 1 and x19 > 2:
                    try:
                        dt_from19 = uitable.tableWidget.item(y19, 39).text()
                        dt_to19 = now19.strftime("%H:%M:%S")
                        dt_from19 = datetime.datetime.strptime(dt_from19, '%H:%M:%S')
                        dt_to19 = datetime.datetime.strptime(dt_to19, '%H:%M:%S')
                        delta19 = dt_to19 - dt_from19
                        uitable.tableWidget.setItem(y19, x19, QtWidgets.QTableWidgetItem(str(delta19)))
                        uitable.tableWidget.item(y19, x19).setBackground(color19)
                    except:
                        row19 = row19
            row19 = row19 - 1

        row20 = 25
        while row20 != 1:
            col20 = uitable.tableWidget.item(row20, 41).text()
            if col20 != '':
                y20 = row20
                x20 = 42
                now20 = datetime.datetime.now()
                color20 = uitable.tableWidget.item(y20, x20).background()
                if y20 > 1 and x20 > 2:
                    try:
                        dt_from20 = uitable.tableWidget.item(y20, 41).text()
                        dt_to20 = now20.strftime("%H:%M:%S")
                        dt_from20 = datetime.datetime.strptime(dt_from20, '%H:%M:%S')
                        dt_to20 = datetime.datetime.strptime(dt_to20, '%H:%M:%S')
                        delta20 = dt_to20 - dt_from20
                        uitable.tableWidget.setItem(y20, x20, QtWidgets.QTableWidgetItem(str(delta20)))
                        uitable.tableWidget.item(y20, x20).setBackground(color20)
                    except:
                        row20 = row20
            row20 = row20 - 1
#-------------------------------------------------------------------------



# 'ok'
#-------------------------------------------------------------------------
def done():
    Dialog.hide()
    DialogII.hide()

    reg = re.compile('[^0-9]')
    a_y1 = reg.sub('', uimap.lineEdit_2.text())
    a_x1 = reg.sub('', uimap.lineEdit.text())
    a_y2 = reg.sub('', uimap.lineEdit_3.text())
    a_x2 = reg.sub('', uimap.lineEdit_4.text())
    a_y3 = reg.sub('', uimap.lineEdit_5.text())
    a_x3 = reg.sub('', uimap.lineEdit_6.text())
    a_y4 = reg.sub('', uimap.lineEdit_7.text())
    a_x4 = reg.sub('', uimap.lineEdit_10.text())
    a_y5 = reg.sub('', uimap.lineEdit_8.text())
    a_x5 = reg.sub('', uimap.lineEdit_11.text())
    a_y6 = reg.sub('', uimap.lineEdit_9.text())
    a_x6 = reg.sub('', uimap.lineEdit_12.text())

    b_y1 = reg.sub('', uimap.lineEdit_15.text())
    b_x1 = reg.sub('', uimap.lineEdit_22.text())
    b_y2 = reg.sub('', uimap.lineEdit_28.text())
    b_x2 = reg.sub('', uimap.lineEdit_23.text())
    b_y3 = reg.sub('', uimap.lineEdit_18.text())
    b_x3 = reg.sub('', uimap.lineEdit_20.text())
    b_y4 = reg.sub('', uimap.lineEdit_21.text())
    b_x4 = reg.sub('', uimap.lineEdit_26.text())
    b_y5 = reg.sub('', uimap.lineEdit_24.text())
    b_x5 = reg.sub('', uimap.lineEdit_17.text())
    b_y6 = reg.sub('', uimap.lineEdit_25.text())
    b_x6 = reg.sub('', uimap.lineEdit_27.text())

    c_y1 = reg.sub('', uimap.lineEdit_29.text())
    c_x1 = reg.sub('', uimap.lineEdit_36.text())
    c_y2 = reg.sub('', uimap.lineEdit_42.text())
    c_x2 = reg.sub('', uimap.lineEdit_37.text())
    c_y3 = reg.sub('', uimap.lineEdit_32.text())
    c_x3 = reg.sub('', uimap.lineEdit_34.text())
    c_y4 = reg.sub('', uimap.lineEdit_35.text())
    c_x4 = reg.sub('', uimap.lineEdit_40.text())
    c_y5 = reg.sub('', uimap.lineEdit_38.text())
    c_x5 = reg.sub('', uimap.lineEdit_31.text())
    c_y6 = reg.sub('', uimap.lineEdit_39.text())
    c_x6 = reg.sub('', uimap.lineEdit_41.text())

    d_y1 = reg.sub('', uimap.lineEdit_43.text())
    d_x1 = reg.sub('', uimap.lineEdit_50.text())
    d_y2 = reg.sub('', uimap.lineEdit_56.text())
    d_x2 = reg.sub('', uimap.lineEdit_51.text())
    d_y3 = reg.sub('', uimap.lineEdit_46.text())
    d_x3 = reg.sub('', uimap.lineEdit_48.text())
    d_y4 = reg.sub('', uimap.lineEdit_49.text())
    d_x4 = reg.sub('', uimap.lineEdit_54.text())
    d_y5 = reg.sub('', uimap.lineEdit_52.text())
    d_x5 = reg.sub('', uimap.lineEdit_45.text())
    d_y6 = reg.sub('', uimap.lineEdit_53.text())
    d_x6 = reg.sub('', uimap.lineEdit_55.text())

    w1 = reg.sub('', uimap.lineEdit_13.text())
    h1 = reg.sub('', uimap.lineEdit_14.text())
    w2 = reg.sub('', uimap.lineEdit_16.text())
    h2 = reg.sub('', uimap.lineEdit_19.text())
    w3 = reg.sub('', uimap.lineEdit_30.text())
    h3 = reg.sub('', uimap.lineEdit_33.text())
    w4 = reg.sub('', uimap.lineEdit_44.text())
    h4 = reg.sub('', uimap.lineEdit_47.text())

    with open('settings.txt', 'w') as file:
        file.write(
            a_y1 + '\n' +
            a_x1 + '\n' +
            a_y2 + '\n' +
            a_x2 + '\n' +
            a_y3 + '\n' +
            a_x3 + '\n' +
            a_y4 + '\n' +
            a_x4 + '\n' +
            a_y5 + '\n' +
            a_x5 + '\n' +
            a_y6 + '\n' +
            a_x6 + '\n' +

            b_y1 + '\n' +
            b_x1 + '\n' +
            b_y2 + '\n' +
            b_x2 + '\n' +
            b_y3 + '\n' +
            b_x3 + '\n' +
            b_y4 + '\n' +
            b_x4 + '\n' +
            b_y5 + '\n' +
            b_x5 + '\n' +
            b_y6 + '\n' +
            b_x6 + '\n' +

            c_y1 + '\n' +
            c_x1 + '\n' +
            c_y2 + '\n' +
            c_x2 + '\n' +
            c_y3 + '\n' +
            c_x3 + '\n' +
            c_y4 + '\n' +
            c_x4 + '\n' +
            c_y5 + '\n' +
            c_x5 + '\n' +
            c_y6 + '\n' +
            c_x6 + '\n' +

            d_y1 + '\n' +
            d_x1 + '\n' +
            d_y2 + '\n' +
            d_x2 + '\n' +
            d_y3 + '\n' +
            d_x3 + '\n' +
            d_y4 + '\n' +
            d_x4 + '\n' +
            d_y5 + '\n' +
            d_x5 + '\n' +
            d_y6 + '\n' +
            d_x6 + '\n' +
            w1 + '\n' +
            h1 + '\n' +
            w2 + '\n' +
            h2 + '\n' +
            w3 + '\n' +
            h3 + '\n' +
            w4 + '\n' +
            h4 + '\n'
        )
    file.close()
#-------------------------------------------------------------------------

def savetable():
    fileName, _ = QtWidgets.QFileDialog.getSaveFileName(caption="Сохранить файл", filter="All Files(*.xlsx)"
    )
    if not fileName:
        return

    _list = []
    model = uitable.tableWidget.model()
    for row in range(model.rowCount()):
        _r = []
        for column in range(model.columnCount()):
            _r.append("{}".format(model.index(row, column).data() or ""))
        _list.append(_r)
    print(fileName)

    workbook = Workbook(fileName)
    worksheet = workbook.add_worksheet()

    for r, row in enumerate(_list):
        for c, col in enumerate(row):
            worksheet.write(r, c, col)
    workbook.close()


# "Map"
uiwin.pushButton.clicked.connect(lambda: show_table_map())

# "Data"
uiwin.pushButton_100.clicked.connect(lambda: show_table())

# Чекбоксы раздела Areas
uiwin.checkBox.stateChanged.connect(lambda: t_or_f_checktables())
uiwin.checkBox_2.stateChanged.connect(lambda: t_or_f_checktables())
uiwin.checkBox_3.stateChanged.connect(lambda: t_or_f_checktables())
uiwin.checkBox_4.stateChanged.connect(lambda: t_or_f_checktables())
uiwin.checkBox_5.stateChanged.connect(lambda: t_or_f_checktables())
uiwin.checkBox_6.stateChanged.connect(lambda: t_or_f_checktables())

# Чекбоксы окна Map
uimap.checkBox.stateChanged.connect(lambda: yx_acc_t1())
uimap.checkBox_2.stateChanged.connect(lambda: yx_acc_t2())
uimap.checkBox_3.stateChanged.connect(lambda: yx_acc_t3())
uimap.checkBox_4.stateChanged.connect(lambda: yx_acc_t4())
uimap.checkBox_5.stateChanged.connect(lambda: yx_acc_t5())
uimap.checkBox_6.stateChanged.connect(lambda: yx_acc_t6())
uimap.checkBox_7.stateChanged.connect(lambda: yx_tablename_t1())
uimap.checkBox_8.stateChanged.connect(lambda: yx_tablename_t2())
uimap.checkBox_9.stateChanged.connect(lambda: yx_tablename_t3())
uimap.checkBox_10.stateChanged.connect(lambda: yx_tablename_t4())
uimap.checkBox_11.stateChanged.connect(lambda: yx_tablename_t5())
uimap.checkBox_12.stateChanged.connect(lambda: yx_tablename_t6())
uimap.checkBox_13.stateChanged.connect(lambda: yx_table_n_t6())
uimap.checkBox_14.stateChanged.connect(lambda: yx_table_n_t5())
uimap.checkBox_15.stateChanged.connect(lambda: yx_table_n_t4())
uimap.checkBox_16.stateChanged.connect(lambda: yx_table_n_t3())
uimap.checkBox_17.stateChanged.connect(lambda: yx_table_n_t2())
uimap.checkBox_18.stateChanged.connect(lambda: yx_table_n_t1())
uimap.checkBox_19.stateChanged.connect(lambda: yx_cards_t6())
uimap.checkBox_20.stateChanged.connect(lambda: yx_cards_t5())
uimap.checkBox_21.stateChanged.connect(lambda: yx_cards_t4())
uimap.checkBox_22.stateChanged.connect(lambda: yx_cards_t3())
uimap.checkBox_23.stateChanged.connect(lambda: yx_cards_t2())
uimap.checkBox_24.stateChanged.connect(lambda: yx_cards_t1())

# Прицелы
uimap.pushButton_100.clicked.connect(lambda: video())
uimap.pushButton_200.clicked.connect(lambda: video())
uimap.pushButton_300.clicked.connect(lambda: video())
uimap.pushButton_400.clicked.connect(lambda: video())

# Поля ширины и высоты
uimap.lineEdit_13.textChanged.connect(lambda: acc_name())
uimap.lineEdit_14.textChanged.connect(lambda: acc_name())
uimap.lineEdit_16.textChanged.connect(lambda: table_name())
uimap.lineEdit_19.textChanged.connect(lambda: table_name())
uimap.lineEdit_30.textChanged.connect(lambda: n_table())
uimap.lineEdit_33.textChanged.connect(lambda: n_table())
uimap.lineEdit_44.textChanged.connect(lambda: cards())
uimap.lineEdit_47.textChanged.connect(lambda: cards())

# 'Start'
uiwin.pushButton_55.clicked.connect(starter)

#'Stop'
uiwin.pushButton_555.clicked.connect(lambda: stop())

# 'ok'
uimap.pushButton_1000.clicked.connect(lambda: done())

# Data
uitable.tableWidget.cellDoubleClicked.connect(lambda: settime())
uitable.pushButton_100.clicked.connect(lambda: savetable())
uitable.pushButton_800.clicked.connect(lambda: update())



sys.exit(app.exec_())
