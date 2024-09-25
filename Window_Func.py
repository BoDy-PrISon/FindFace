from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtMultimedia

import UI
import VideoCrash
import TrainModel
import FaceDetected
import sys
import CreatePreview
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QMessageBox

#-x имя файла.ui -o имя файлв.py
#pyuic5 -x OneWindow.ui -o OneWindow.py
class MainWindow(QMainWindow, UI.Ui_PrevievLab):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)  # Инициализируем интерфейс из сгенерированного класса Ui_MainWindow

        # Подключаем обработчики событий для кнопок
        self.Video_Choise.clicked.connect(self.choose_video)
        self.Train_model.clicked.connect(self.train_model)
        self.Create_Preview.clicked.connect(self.Create_preview)
        self.Find_Face.clicked.connect(self.Find_face)
        self.Frame_Next.clicked.connect(self.Frame_next)
        self.Frame_Back.clicked.connect(self.Frame_back)
        self.Video_play.clicked.connect(self.Play_Video)
        self.Video_stop.clicked.connect(self.Stop_Video)
        # Создаем экземпляр окна с превью
        self.preview_dialog = QtWidgets.QDialog()
        self.ui_preview = CreatePreview.Ui_Dialog()
        self.ui_preview.setupUi(self.preview_dialog)
        #Проигрыватель видео
        self.media_player = QtMultimedia.QMediaPlayer(self)
        self.media_player.setVideoOutput(self.Video_Widget)

        self.faces_images = []
        self.current_image_index = 0
        self.file_path=""
    def choose_video(self):
        print("Ok_V")
        # Открываем диалоговое окно выбора файла
        self.file_path, _ = QFileDialog.getOpenFileName(None, "Выбор видео", "", "Видео файлы (*.mp4 *.avi)")
        print(self.file_path)
        # Проверяем, был ли выбран файл
        if self.file_path:
            # Очищаем папку Video Frame перед началом записи кадров
            VideoCrash.clear_folder("Video Frame")
            print("Чистая папка")
            # Передаем путь к выбранному файлу в другой скрипт
            trigger =VideoCrash.main(self.file_path)
            print("Video Frame Extract :", self.file_path)
            if trigger == 0:
                # Выводим сообщение о готовности видео к поиску лица
                QMessageBox.information(None, "Готовность видео", "Видео готово к обработке.")

    def train_model(self):
        print("Ok_T")
        # Проверяем, пуста ли папка с изображениями
        if not os.listdir(TrainModel.image_folder_path):
            # Папка пуста, показываем предупреждение
            QMessageBox.warning(None, "Предупреждение", "Папка с изображениями для обучения пуста. Добавьте изображения и повторите попытку.")
        else:
            print("Training model...")
            # Папка не пуста, запускаем процесс обучения
            output_filename = QFileDialog.getSaveFileName(None, "Сохранить модель как")[0]
            trigger = TrainModel.Train(output_filename)
            if trigger == 0:
                # Выводим сообщение о готовности видео к поиску лица
                QMessageBox.information(None, "Обучение модели", "Модель обучена.")

    def Find_face(self):
        print("Ok_Face")
        print("Ищем лицо")
        self.label.setText("Идет отбор кадров...")
        QApplication.processEvents()
        # Открываем диалоговое окно выбора файла
        self.file_path, _ = QFileDialog.getOpenFileName(None, "Выбор файла модели", "Models")
        if self.file_path != (None or ""):
            self.faces_images = FaceDetected.FindFace(self.file_path)
            QMessageBox.information(None, "Предупреждение", "Поиск завершен.")
            self.Frame_Current()

    def Frame_Current(self):
        print("Ok_F1")
        if self.faces_images:
            print("Выбранные лица:", self.faces_images)
            self.current_image_path = self.faces_images[self.current_image_index]  # Сохраняем текущий путь к изображению
            pixmap = QPixmap(self.faces_images[self.current_image_index])
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio))
            self.label.setScaledContents(True)
            self.label.show()
            print("Текущий путь к изображению:", self.current_image_path)
        else:
            QMessageBox.warning(None, "Предупреждение", "Нет выбранного файла.")
            print("Нет выбранного файла")

    def Frame_next(self):
        print("Ok_F3")
        if self.faces_images and self.current_image_index < len(self.faces_images) - 1:
            self.current_image_index += 1  # Вперед по массиву
            self.current_image_path = self.faces_images[self.current_image_index]
            pixmap = QPixmap(self.faces_images[self.current_image_index])
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio))
            self.label.setScaledContents(True)
            self.label.show()
            print("Текущий путь к изображению:", self.current_image_path)

    def Frame_back(self):
        if self.faces_images and self.current_image_index > 0:
            self.current_image_index -= 1  # Назад по массиву путей
            self.current_image_path = self.faces_images[self.current_image_index]
            pixmap = QPixmap(self.faces_images[self.current_image_index])
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio))
            self.label.setScaledContents(True)
            self.label.show()
            print("Текущий путь к изображению:", self.current_image_path)

    def Create_preview(self):
        print("Подтверждение превью")
        reply = QMessageBox.question(
            None,
            "Подтверждение выбора",
            "Вы уверены, что хотите продолжить?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
    )

        if reply == QMessageBox.Yes:
            # Позволяет пользователю выбрать кадр для видео
            selected_frame = self.current_image_path
            print()
            print("Путь до кадра:", selected_frame)
            if not selected_frame:
                print("Кадр не выбран.")
                return  # Выходим, если кадр не был выбран

        # Позволяет пользователю выбрать название для результирующего видео
            output_filename = QFileDialog.getSaveFileName(None, "Сохранить видео как", "", "AVI files (*.avi)")[0]
            if not output_filename:
                print("Файл не сохранен.")
                return  # Выходим, если пользователь не указал имя файла

            # Вызов функции слияния видео с выбранными параметрами
            trigger = VideoCrash.Video_Merge(selected_frame, output_filename)
            if trigger == 0:
                # Выводим сообщение о готовности видео к поиску лица
                QMessageBox.information(None, "Оповещение", "Видео было сохранено.")
                self.Open(output_filename)


        else:
            print("Операция отменена пользователем.")
    def Open(self, Output_fileName):
            # Загружаем видео в плеер
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(Output_fileName)))
            # Воспроизводим видео
            self.media_player.play()
            self.media_player.pause()
            return 0
    def Play_Video(self):
        # Проверяем, находится ли видео в состоянии паузы
        if self.media_player.state() == QMediaPlayer.PausedState:
            # Снимаем видео с паузы
            self.media_player.play()
            print("Воспроизведение видео")
        elif self.media_player.state() == QMediaPlayer.StoppedState:
            # Если видео остановлено, начинаем воспроизведение сначала
            self.media_player.play()
            print("Воспроизведение видео с начала")
        else:
            print("Видео уже воспроизводится или не загружено")
    def Stop_Video(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
            print("Видео приостановлено")
        else:
            print("Видео не воспроизводится")
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec()