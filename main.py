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
    for filename in os.listdir(original_folder):
        # определяем пути для оригинального, сжатого и разницы изображений, чтобы работать с ImageMagick
        original_path = os.path.join(original_folder, filename)

        compressed_filename = filename[0:filename.find('.')] + '.jpg'
        compressed_path = os.path.join(compressed_folder, compressed_filename)

        diff_filename = filename[0:filename.find('.')] + '.png'
        diff_path = os.path.join(diff_folder, compressed_filename)
        # сжимаем изображение до 40% качества в jpg
        compress = subprocess.run(['magick', 'convert', original_path, '-quality', '40%', compressed_path])
        # получаем разность изображений в png
        diff = subprocess.run(
            ['magick', 'convert', original_path, compressed_path, '-compose', 'difference', '-composite', diff_path])