from moviepy.editor import VideoFileClip
import numpy as np
import os
import shutil
import sys
import cv2
from datetime import timedelta


# Частота сохранения кадров в секунду
Saving_Frames_Per_Second = 30

# Функция для форматирования timedelta в строку
def format_timedelta(td):
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return result + ".00".replace(":","")

    ms = round(int(ms) / 10000)
    return f"{result}.{ms:02}".replace(":","-")
def clear_folder(folder_name):
    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

# Основная функция для извлечения кадров из видео
def main(video_file):
    # Загружаем видеофайл
    video_clip = VideoFileClip(video_file)
    filename, _ =os.path.splitext(video_file)
    # Имя папки для сохранения кадров
    folder_name = "Video Frame"
    clear_folder(folder_name)

    # Определяем путь к папке
    file_path = os.path.join(os.getcwd(), folder_name)

    # Создаем папку, если она не существует
    os.makedirs(file_path, exist_ok=True)

    # Определяем частоту сохранения кадров в зависимости от частоты кадров в исходном видео и заданной частоты
    saving_frames_per_second = min(video_clip.fps, Saving_Frames_Per_Second)
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second

    # Проходим по каждому интервалу времени в видео
    for current_duration in np.arange(0, video_clip.duration, step):
        # Форматируем длительность текущего кадра в строку
        frame_duration_formatted = format_timedelta(timedelta(seconds=current_duration)).replace(":","-")
        # Формируем имя файла кадра
        frame_filename = os.path.join(file_path, f"frame{frame_duration_formatted}.jpg")

        # Сохраняем текущий кадр в указанном файле
        video_clip.save_frame(frame_filename, current_duration)
    return 0

# Очистка папки для кадров видео
def clear_folder(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    if os.path.exists(folder_path):
        # Удаляем все файлы и папки внутри директории
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Удаление файла или символической ссылки
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Удаление вложенной директории и её содержимого
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        os.makedirs(folder_path)  # Создаем папку, если она не существует
        print(f"The folder {folder_name} was created because it did not exist.")
        
def Video_Merge(selected_frame, output_filename, frames_dir='Video Frame'):
    print("Начинаю склеивать кадры")
    print("А вот путь до выбранного кадра:",selected_frame)
    # Загружаем выбранный кадр и используем его для определения размера видео
    print(selected_frame)
    frame = cv2.imread(selected_frame)
    writer = cv2.VideoWriter(
        output_filename,
        cv2.VideoWriter_fourcc(*'XVID'), # тут надо выяснить вообще какой формат юзать, выбор говна такой: MJPG, DIVX, XVID, WMV1, WMV2
        25.0,
        (frame.shape[1], frame.shape[0]),
        isColor=len(frame.shape) > 2
    )

    # Пишем выбранный кадр в видео
    print("Вклеиваю превью:",frame)
    writer.write(frame)

    # Получаем список остальных кадров
    frames = [os.path.join(frames_dir, f) for f in os.listdir(frames_dir) if os.path.isfile(os.path.join(frames_dir, f))]
    
    # Пишем остальные кадры в видео
    for frame_path in frames:
        frame = cv2.imread(frame_path)
        writer.write(frame)
    
    writer.release()
    cv2.destroyAllWindows()


    return 0
