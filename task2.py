# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

import csv
import json


def task() -> None:
    dict_data = dict()

    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as f:
        dict_data=[line for line in csv.DictReader(f)]

    # TODO Сериализовать в файл с отступами равными 4
    json.dumps(dict_data)
    OUTPUT_FILENAME=open("output.json", "w")
    OUTPUT_FILENAME.write(json.dumps((dict_data), indent=4))

    return OUTPUT_FILENAME


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
