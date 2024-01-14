# TODO импортировать необходимые молули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as f:
        object_python = list(csv.DictReader(f, delimiter=','))  # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, 'w') as f:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(object_python, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
