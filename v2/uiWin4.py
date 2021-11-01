from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window4(object):
    def setupUi(self, Window4):
        Window4.setObjectName("Window4")

        Window4.resize(360, 253)

        Window4.setStyleSheet("QMainWindow { \n"
                              "background: #674e4d\n"
                              "}\n"
                              "QTextEdit {\n"
                              "background: #4e3938;\n"
                              "color: #f1e2e0;\n"
                              "border: 1px solid #420c12;\n"
                              "border-radius: 3px;\n"
                              "color: #d06814;\n"
                              "}"
                              "QScrollBar:vertical {\n"
                              "background: #4e3938;\n"
                              "width: 2px\n"
                              "}")

        self.centralwidget = QtWidgets.QWidget(Window4)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        font = QtGui.QFont()
        font.setFamily("Yandex-UI-Icons-Private")
        font.setPointSize(12)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.textEdit.setReadOnly(True)

        Window4.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window4)
        self.statusbar.setObjectName("statusbar")
        Window4.setStatusBar(self.statusbar)

        self.retranslateUi(Window4)
        QtCore.QMetaObject.connectSlotsByName(Window4)

    def retranslateUi(self, Window4):
        _translate = QtCore.QCoreApplication.translate
        Window4.setWindowTitle(_translate("Window4", "MainWindow"))
        self.textEdit.setHtml(_translate("Window4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Yandex-UI-Icons-Private\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Тессеракт. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Официальный источник: https://github.com/tesseract-ocr/ </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Установщик располагается в папке «tesseract».</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Кликните дважды по файлу «tesseract-ocr-setup-v5.0.0.exe». Должно появиться уведомление – разрешить ли приложению свою работу. Спустя несколько секунд после согласия загрузится окно-приветствие мастера установки Tesseract-OCR. Нажмите «Далее» для продолжения. Поставьте галочку, что принимаете условия лицензионного соглашения, и снова нажмите «Далее». Install for anyone или install just for me – вариативно; выбрав, нажмите «Далее». На этом этапе откроется наиболее важное окно: «Компоненты устанавливаемой программы». Первые 4 пункта оставьте без изменений, на них должны быть проставлены галочки. Последний пункт – Additional language data (download) – будет без галочки, но слева от этого пункта будет плюсик, который вас интересует. Откроется список.  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">В списке первый пункт – Math / equation detection module. Поставьте галочку на нем, если планируете распознавать цифры. Спуститесь ниже и выберете все необходимые языки, которые нужно будет распознавать. Слева будет написано, сколько памяти на диске это займет. Например  если выбрать только цифры и два китайских языка, то будет 259-260 Мбайт. Нажмите на кнопку «Далее», затем на «Установить». После загрузки нажмите «Далее». Последний шаг – нажать на кнопку «Готово».  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Если не знаете, в какую папку установился Тессеракт, то снова кликните дважды по файлу «tesseract-ocr-setup-3.05.01», который находится в архиве данной программы. Установщик снова спросит разрешение на внесение изменений, затем снова попросит выбрать язык и далее предупредит, что Тессеракт уже установлен, с указанием директории. Запомните, где находится папка, и отмените повторную установку.  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Обычно папка устанавливается в «users». Можете перенести ее оттуда в «Program Files». Так путь к папке будет короче и в именах наверняка не будут встречаться недопустимые символы.  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Если Тессеракт установился в «users», тогда в проводнике во вкладке «Вид» надммте на кнопку с названием «Показать или скрыть», поставьте галочку рядом с пунктом «Скрытые элементы», если она не стоит, иначе в пути не будет видна папка «AppData». Установив галочку, зайдите в папку «users», а далее – в папку нужного пользователя. Далее – в папку «AppData», далее – в «Local». Найдите папку с именем «Tesseract-OCR».  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Зайдите внутрь папки «Tesseract-OCR». Наверху в проводнике будет директория: «Program Files[например] &gt; Tesseract-OCR &gt;». Кликните туда 1 раз, чтобы выделить полный путь к папке (С:\\Program Files\\Tesseract-OCR) [может отличаться в зависимости от диска и выбранной папки]. Скопируйте путь к папке «Tesseract-OCR». </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">После этого в проводнике наведите курсор на «Этот компьютер», нажмите правую кнопку мыши и выберите пункт «Свойства». Откроется окно «Система». Слева в этом окне будет панель управления, вам нужен пункт «Дополнительные параметры системы». Нажмите, откроется окно «Свойства системы». В этом окне найдите внизу кнопку «Переменные среды...» и нажмите на нее. Откроется окно «Переменные среды». В разделе «Параметры среды пользователя для {имя вашего юзера}» есть список с двумя колонками: «Переменная» и «Значение». Клткните на переменную «Path» и нажмите на кнопку «Изменить...». Должно открыться окно «Изменить переменную среды», а справа в этом окне – ряд кнопок. Первая кнопка – «Создать», – нажмите на нее и вставьте заранее скопированную директорию в поле ввода. Далее везде нажмите «Ок».  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Готово. Теперь программа во время исполнения будет обращаться к движку.</p> \n<p>Догрузить языковые файлы можно вручную отсюда: https://github.com/tesseract-ocr/tessdata</p></body></html>"))
