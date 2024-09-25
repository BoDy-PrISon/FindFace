from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia
from PyQt5.QtMultimediaWidgets import QVideoWidget


class Ui_PrevievLab(object):
    def setupUi(self, PrevievLab):
        PrevievLab.setObjectName("PrevievLab")
        PrevievLab.resize(1741, 693)
        PrevievLab.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(PrevievLab)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 951, 601))
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet("QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 4px;\n"
"    background-color: #ffffff;\n"
"    padding: 4px;\n"
"    color: #333;\n"
"    /* Дополнительные стили для текста, если нужно */\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"}")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.Video_Choise = QtWidgets.QPushButton(self.centralwidget)
        self.Video_Choise.setGeometry(QtCore.QRect(400, 650, 225, 31))
        self.Video_Choise.setStyleSheet(" QPushButton {\n"
"     border: 2px solid black;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* для плоской кнопки границы нет */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* делаем кнопку по умолчанию выпуклой */\n"
" }")
        self.Video_Choise.setObjectName("Video_Choise")
        self.Train_model = QtWidgets.QPushButton(self.centralwidget)
        self.Train_model.setGeometry(QtCore.QRect(640, 650, 225, 31))
        self.Train_model.setStyleSheet(" QPushButton {\n"
"     border: 2px solid black;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* для плоской кнопки границы нет */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* делаем кнопку по умолчанию выпуклой */\n"
" }")
        self.Train_model.setObjectName("Train_model")
        self.Frame_Back = QtWidgets.QPushButton(self.centralwidget)
        self.Frame_Back.setGeometry(QtCore.QRect(170, 610, 300, 31))
        self.Frame_Back.setMinimumSize(QtCore.QSize(84, 10))
        self.Frame_Back.setStyleSheet(" QPushButton {\n"
"     border: 2px solid black;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* для плоской кнопки границы нет */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* делаем кнопку по умолчанию выпуклой */\n"
" }")
        self.Frame_Back.setObjectName("Frame_Back")
        self.Frame_Next = QtWidgets.QPushButton(self.centralwidget)
        self.Frame_Next.setEnabled(True)
        self.Frame_Next.setGeometry(QtCore.QRect(490, 610, 300, 31))
        self.Frame_Next.setMinimumSize(QtCore.QSize(84, 10))
        self.Frame_Next.setAutoFillBackground(False)
        self.Frame_Next.setStyleSheet(" QPushButton {\n"
"     border: 2px solid black;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* для плоской кнопки границы нет */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* делаем кнопку по умолчанию выпуклой */\n"
" }")
        self.Frame_Next.setObjectName("Frame_Next")
        self.Create_Preview = QtWidgets.QPushButton(self.centralwidget)
        self.Create_Preview.setGeometry(QtCore.QRect(1120, 650, 225, 31))
        self.Create_Preview.setStyleSheet(" QPushButton {\n"
"     border: 2px solid black;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* для плоской кнопки границы нет */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* делаем кнопку по умолчанию выпуклой */\n"
" }")
        self.Create_Preview.setObjectName("Create_Preview")
        self.Find_Face = QtWidgets.QPushButton(self.centralwidget)
        self.Find_Face.setGeometry(QtCore.QRect(880, 650, 225, 31))
        self.Find_Face.setMinimumSize(QtCore.QSize(84, 0))
        self.Find_Face.setStyleSheet(" QPushButton {\n"
"     border: 2px solid black;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* для плоской кнопки границы нет */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* делаем кнопку по умолчанию выпуклой */\n"
" }")
        self.Find_Face.setObjectName("Find_Face")
        self.Video_Widget = QVideoWidget(self.centralwidget)
        self.Video_Widget.setGeometry(QtCore.QRect(980, 10, 741, 591))
        self.Video_Widget.setObjectName("Video_Widget")
        self.Video_play = QtWidgets.QPushButton(self.centralwidget)
        self.Video_play.setGeometry(QtCore.QRect(1120, 610, 225, 31))
        self.Video_play.setStyleSheet(" QPushButton {\n"
"     border: 2px solid black;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* для плоской кнопки границы нет */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* делаем кнопку по умолчанию выпуклой */\n"
" }")
        self.Video_play.setObjectName("Video_play")
        self.Video_stop = QtWidgets.QPushButton(self.centralwidget)
        self.Video_stop.setGeometry(QtCore.QRect(1360, 610, 225, 31))
        self.Video_stop.setStyleSheet(" QPushButton {\n"
"     border: 2px solid black;\n"
"     border-radius: 6px;\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"     min-width: 80px;\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* для плоской кнопки границы нет */\n"
" }\n"
"\n"
" QPushButton:default {\n"
"     border-color: navy; /* делаем кнопку по умолчанию выпуклой */\n"
" }")
        self.Video_stop.setObjectName("Video_stop")
        PrevievLab.setCentralWidget(self.centralwidget)

        self.retranslateUi(PrevievLab)
        QtCore.QMetaObject.connectSlotsByName(PrevievLab)

    def retranslateUi(self, PrevievLab):
        _translate = QtCore.QCoreApplication.translate
        PrevievLab.setWindowTitle(_translate("PrevievLab", "PrevievLab"))
        self.label.setText(_translate("PrevievLab", "Отобранные кадры"))
        self.Video_Choise.setText(_translate("PrevievLab", "Выбрать видео"))
        self.Train_model.setText(_translate("PrevievLab", "Создать эмбеддинг "))
        self.Frame_Back.setText(_translate("PrevievLab", "Предыдущий кадр"))
        self.Frame_Next.setText(_translate("PrevievLab", "Следующий кадр"))
        self.Create_Preview.setText(_translate("PrevievLab", "Установить превью"))
        self.Find_Face.setText(_translate("PrevievLab", "Поиск Человека на видео"))
        self.Video_Widget.setStyleSheet(_translate("PrevievLab", "QPushButton { border: 2px solid black; border-radius: 6px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde); min-width: 80px; } QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa); } QPushButton:flat { border: none; /* для плоской кнопки границы нет / } QPushButton:default { border-color: navy; / делаем кнопку по умолчанию выпуклой */ } "))
        self.Video_play.setText(_translate("PrevievLab", "Воспроизвести"))
        self.Video_stop.setText(_translate("PrevievLab", "Пауза"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrevievLab = QtWidgets.QMainWindow()
    ui = Ui_PrevievLab()
    ui.setupUi(PrevievLab)
    PrevievLab.show()
    sys.exit(app.exec_())
