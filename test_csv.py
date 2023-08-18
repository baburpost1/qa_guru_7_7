import csv, os
from conftest import RESOURCE_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_csv():
    with open(os.path.join(RESOURCE_PATH, 'new_csv.csv'), 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    rows = []
    with open(os.path.join(RESOURCE_PATH, 'new_csv.csv'), newline='') as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        for row in csvreader:
            rows.append(row)
            print(row)
    assert rows[0] == ['Bonny', 'Born', 'Peter']
    assert rows[1] == ['Alex', 'Serj', 'Yana']
