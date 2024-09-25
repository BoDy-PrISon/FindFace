from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QApplication, QDialog, QPushButton
from PyQt5.QtCore import Qt, QRect

import FaceDetected


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Creating Preview")
        Dialog.resize(657, 701)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(20, 10, 600, 600))
        self.label.setObjectName("label")
        
        self.YesButton = QPushButton(Dialog)
        self.YesButton.setGeometry(QRect(420, 640, 181, 51))
        self.YesButton.setObjectName("YesButton")
        
        self.NextImage = QPushButton(Dialog)
        self.NextImage.setGeometry(QRect(230, 640, 181, 51))
        self.NextImage.setObjectName("NextImage")
        
        self.BackImage = QPushButton(Dialog)
        self.BackImage.setGeometry(QRect(40, 640, 181, 51))
        self.BackImage.setObjectName("BackImage")
        
        self.faces_images = []  # Список для хранения путей к изображениям
        self.current_image_index = 0
        
        self.retranslateUi(Dialog)
        
        self.YesButton.clicked.connect(self.next_frame)
        #self.NextImage.clicked.connect(self.accept)  # Если нужен отдельный слот для NextImage, определите его
        self.BackImage.clicked.connect(self.previous_frame)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.YesButton.setText(_translate("Dialog", "Да"))
        self.NextImage.setText(_translate("Dialog", "Следующий кадр"))
        self.BackImage.setText(_translate("Dialog", "Предыдущий кадр"))

    def show_current_image(self):
        # Отображаем текущее изображение в QLabel
        pixmap = QPixmap(self.faces_images[self.current_image_index])
        self.label.setPixmap(pixmap)
        self.label.show()

    def next_frame(self):
        # Отображаем следующее изображение в списке
        if self.current_image_index < len(self.faces_images) - 1:
            self.current_image_index += 1
            self.show_current_image()
            self.label.update()

    def previous_frame(self):
        # Отображаем предыдущее изображение в списке
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.show_current_image()
            self.label.update()
    def load_images(self, images_paths):
        if images_paths:
                # Загрузка первого изображения из списка
                pixmap = QPixmap(images_paths[0])
                self.label.setPixmap(pixmap.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio))
        else:
                print("Нет изображений с лицами для показа.")
    def create_preview(self):
        if self.preview_dialog:
            self.preview_dialog.show()
        else:
            raise ValueError("Окно Превью не инициализированно")
        
        images_with_faces_paths = FaceDetected.FindFace()
        if images_with_faces_paths:
            self.load_images(images_with_faces_paths)
        else:
            print("Нет изображений с лицами для показа.")
        
        if Dialog:
            Dialog.show()
        else:
            raise ValueError("Диалоговое меню инициализированно")
        
        ui.create_preview = Dialog
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.create_preview()
    ui.setupUi(Dialog)

   


