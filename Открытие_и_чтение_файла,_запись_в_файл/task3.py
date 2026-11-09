import os

filenames = ["sorted/1.txt", "sorted/2.txt", "sorted/3.txt"]

files_info = []

for filename in filenames:


    with open(filename, "r", encoding="utf-8") as file :

        lines = file.readlines()
        line_count = len(lines)

        print(line_count)

        file_info = {
            "filename": filename,
            "line_count": line_count,
            "lines": lines
        }

        files_info.append(file_info)


files_info.sort(key=lambda item: item["line_count"])

print(files_info)


# Начинаем объединение файлов в result.txt

with open("result.txt", "w", encoding="utf-8") as file:
    for item in files_info:

        file.write(os.path.basename(item["filename"]) + "\n")
        file.write(str(item["line_count"]) + "\n")

        print(item["filename"], item["line_count"])

        for line in item["lines"]:
            file.write(line)

print("\nВсе файлы успешно объединены в result.txt")










