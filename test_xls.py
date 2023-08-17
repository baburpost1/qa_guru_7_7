import xlrd, os
from conftest import RESOURCE_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_xls():
    book = xlrd.open_workbook(os.path.join(RESOURCE_PATH, 'file_example_XLS_10.xls'))

    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    sheet = book.sheet_by_index(0)
    print(f'Количество колонок  {sheet.ncols}')
    print(f'Количество строк    {sheet.nrows}')
    print(f'Пересечение строки и столбца {sheet.cell_value(rowx=3, colx=2)}')
    for rx in range(sheet.nrows):
        print(sheet.row(rx))

    assert book.nsheets == 1, "Количество листов не совпадает с ОЗ"
    assert book.sheet_names() == ['Sheet1'], "Имя листа не совпадает с ОЗ"
    assert sheet.ncols == 8, "Количество колонок на первом листе не равн с ОЗ"
    assert sheet.nrows == 10, "Количество строк не совпадает с ОЗ"
    assert sheet.cell_value(rowx=3, colx=2) == "Gent", "Пересечение строки и столбца не совпадает с ОЗ"
