from PyQt5 import QtCore, QtGui, QtWidgets
from uiWin1 import Ui_MainWindow
from uiWin2 import Ui_Window2
from uiWin3 import Ui_Window3
from uiWin4 import Ui_Window4
from uiWin5 import Ui_Window5
from uiWin6 import Ui_Window6

import sys
import os
from xlsxwriter.workbook import Workbook
from ctypes import windll, Structure, c_long, byref
import cv2
import mss
import numpy as np
from decimal import Decimal
import pytesseract
from win32api import GetSystemMetrics
import keyboard
import ctypes
import threading
import datetime
import re
import json
import requests
import shutil


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
win1 = Ui_MainWindow()
win1.setupUi(MainWindow)

Window2 = QtWidgets.QMainWindow()
win2 = Ui_Window2()
win2.setupUi(Window2)

Window3 = QtWidgets.QMainWindow()
win3 = Ui_Window3()
win3.setupUi(Window3)

Window4 = QtWidgets.QMainWindow()
win4 = Ui_Window4()
win4.setupUi(Window4)

Window5 = QtWidgets.QMainWindow()
win5 = Ui_Window5()
win5.setupUi(Window5)

Window6 = QtWidgets.QMainWindow()
win6 = Ui_Window6()
win6.setupUi(Window6)


MainWindow.show()


class globals():
    MON_Y = 0
    MON_X = 0
    W = 400
    H = 400


def showMap():
    Window2.show()


class POINT(Structure):
    _fields_ = [('x', c_long), ('y', c_long)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {'x': pt.x, 'y': pt.y}

title = 'Recognizer'
sct = mss.mss()

def aim():
    win1.label.setText('Выбери участок и нажми "q",\n'
                       'затем просто закрой окно.\n\n'
                       'Изменение ширины и высоты:\n'
                       'кнопки "a", "d", "w", "s"')
    Window2.hide()
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
            if cv2.waitKey(1) & keyboard.is_pressed('a'):
                try:
                    globals.W = globals.W - 5
                except:
                    pass
            if cv2.waitKey(1) & keyboard.is_pressed('d'):
                try:
                    globals.W = globals.W + 5
                except:
                    pass
            if cv2.waitKey(1) & keyboard.is_pressed('w'):
                try:
                    globals.H = globals.H - 5
                except:
                    pass
            if cv2.waitKey(1) & keyboard.is_pressed('s'):
                try:
                    globals.H = globals.H + 5
                except:
                    pass
            if cv2.waitKey(1) & keyboard.is_pressed('q'):
                break
        except:
            break

    cv2.destroyAllWindows()
    Window2.show()
    win2.lineEditTop.setText(str(globals.MON_Y))
    win2.lineEditLeft.setText((str(globals.MON_X)))
    win2.lineEditWidt.setText(str(globals.W))
    win2.lineEditHeight.setText(str(globals.H))
    win1.label.setText('Координаты установлены')


def tools():
    Window3.show()


def conditions():
    Window4.show()


def mode():
    Window5.show()


def helpbutton():
    Window6.show()


win1.mapButton.clicked.connect(lambda: showMap())
win2.pushButton.clicked.connect(lambda: aim())
win1.toolButton.clicked.connect(lambda: tools())
win3.conditionsButton.clicked.connect(lambda: conditions())
win3.modeButton.clicked.connect(lambda: mode())
win5.helpButton.clicked.connect(lambda: helpbutton())


sys.exit(app.exec_())
