# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME) as csv_file:
        lines = [line_ for line_ in csv.DictReader(csv_file)]
    ...  # TODO считать содержимое csv файла
    with open(OUTPUT_FILENAME, "w") as json_file:
        json.dump(lines, json_file, indent=4)
    ...  # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
