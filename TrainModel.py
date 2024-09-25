import os
from imutils import paths
import face_recognition
import pickle
import cv2


# Путь к папке с изображениями для обучения
image_folder_path = 'ImageTrain'
# Путь к папке с моделями
model_folder_path = 'Models'

# Создаем папку для сохранения моделей, если она не существует
os.makedirs(model_folder_path, exist_ok=True)

# Список путей к изображениям в папке обучения
imagePaths = list(paths.list_images(image_folder_path))

knownEncodings = []
knownNames = []
def Train(Name_model):
    # перебираем все папки с изображениями
    print("Обрабатываю...")
    for (i, imagePath) in enumerate(imagePaths):
        # извлекаем имя человека из названия папки
        name = imagePath.split(os.path.sep)[-2]
        # загружаем изображение и конвертируем его из BGR (OpenCV ordering)
        # в dlib ordering (RGB)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # используем библиотеку Face_recognition для обнаружения лиц
        boxes = face_recognition.face_locations(rgb, model='hog')
        # вычисляем эмбеддинги для каждого лица
        encodings = face_recognition.face_encodings(rgb, boxes)
        # loop over the encodings
        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)
    # сохраним эмбеддинги вместе с их именами в формате словаря
    print("Сохраняю модель...")
    data = {"encodings": knownEncodings, "names": knownNames}
    # для сохранения данных в файл используем метод pickle
    output_file_path = os.path.join(model_folder_path, Name_model)
    with open(output_file_path, "wb") as f:
        f.write(pickle.dumps(data))
    print("Закрываю")
    return 0


