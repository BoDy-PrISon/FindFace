import concurrent.futures
import cv2
import os
import pickle
import face_recognition

def FindFace(file_path):
    print("Орабатываю изображения...")
    # Найдите путь к файлу xml с каскадным классификатором
    cascPathface = os.path.dirname(
        cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
    # Загрузите каскад в классификатор каскада
    faceCascade = cv2.CascadeClassifier(cascPathface)
    # Загрузите известные лица и вложения, сохраненные в последнем файле
    data_path = os.path.join("Models", file_path)
    data = pickle.loads(open(data_path, "rb").read())
    # Найдите путь к изображению, на котором хотите обнаружить лицо, и передайте его сюда
    image_files = os.listdir("Video Frame")
    # Проходимся по каждому файлу и обрабатываем изображение
    # Список для хранения изображений с обнаруженными лицами
    images_with_faces_paths = []
    print("Начало отбора")
    for image_file in image_files:
        # Получаем полный путь к изображению
        image_path = os.path.join("Video Frame", image_file)
        image = cv2.imread(image_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Преобразуйте изображение в оттенки серого для каскадного классификатора
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,
                                             scaleFactor=1.1,
                                             minNeighbors=5,
                                             minSize=(60, 60),
                                             flags=cv2.CASCADE_SCALE_IMAGE)

        # встраивания лиц для лица ввода
        encodings = face_recognition.face_encodings(rgb)
        names = []
        # перебираем встраивания лиц, на случай
        # если у нас есть несколько вложений для нескольких лиц
        print("Подготовка изображений")
        for encoding in encodings:
            # Сравниваем встраивания с встраиваниями в data["encodings"]
            # Совпадения содержат массив с логическими значениями и True для вложений, которые соответствуют близко
            # и False для остальных
            matches = face_recognition.compare_faces(data["encodings"],
                                                     encoding)
            # установить name = Unknown, если нет совпадающего встраивания
            name = "Unknown"
            # проверяем, есть ли у нас совпадение
            print("Начало сравнения изображений")
            if True in matches:

                # Найдите позиции, в которых мы получаем True, и сохраните их
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                # перебираем совпавшие индексы и ведем подсчет для каждого распознанного лица
                for i in matchedIdxs:
                    # Проверяем имена в соответствующих индексах, которые мы сохранили в matchedIdxs
                    name = data["names"][i]
                    # увеличить счетчик для полученного имени
                    counts[name] = counts.get(name, 0) + 1
                    # установить имя с наибольшим счетом
                    name = max(counts, key=counts.get)
                # обновляем список имен
                names.append(name)
                # перебираем распознанные лица
                print("Перебираем распознанные лица")
                for ((x, y, w, h), name) in zip(faces, names):
                    # масштабируем координаты лица
                    # нарисовать предполагаемое имя лица на изображении
                    #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    #cv2.putText(image, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    #            0.75, (0, 255, 0), 2)
                    #cv2.imshow("Frame", image)
                    #cv2.waitKey(0)
                    images_with_faces_paths.append(image_path) # Добавляем изображение с лицами в список
    return images_with_faces_paths


