# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    dict_data = dict()

    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as f:
        dict_data=[line for line in csv.DictReader(f)]

    # TODO Сериализовать в файл с отступами равными 4

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(dict_data, f, indent=4)

    return OUTPUT_FILENAME

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
