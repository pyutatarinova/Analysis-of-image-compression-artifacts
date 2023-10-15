import os
import cv2
import subprocess


print('Введите название папки с исходными изображениями:')
original_folder = input()  # папка с исходными изображениями
while not os.path.exists(original_folder):
    print('Такой папки не существует. Введите корректное название:')
    original_folder = input()
compressed_folder = "compressed_images"  # папка со сжатыми изображениями
if not os.path.exists(compressed_folder):
    os.mkdir(compressed_folder)
diff_folder = "diff_images"  # папка с разницей изображений
if not os.path.exists(diff_folder):
    os.mkdir(diff_folder)
result_file = "results.txt"  # файл для записи результатов анализа

with open(result_file, "w") as f:  # открываем файл для записи результатов
    f.write("Имя файла | Номер зоны | Уровень помех\n")
    f.write("-" * 60 + "\n")