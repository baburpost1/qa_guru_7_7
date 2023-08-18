import zipfile, os
from conftest import RESOURCE_PATH


# TODO:# 1. Создать новые тесты, которые заархивируют имеющиеся в resources различные типы файлов в один архив в директорию tmp
# 2. Тесты должны проверять в архиве каждый из файлов, что он является тем самым, который был заархивирован, не распаковывая архив.
def test_zip():
    list_files = os.listdir(RESOURCE_PATH)
    with zipfile.ZipFile(os.path.join(RESOURCE_PATH, 'test.zip'), 'w') as zf:
        for file in list_files:
            add_zip = os.path.join(RESOURCE_PATH, file)
            zf.write(add_zip, file)

    assert zf.namelist() == list_files

    os.remove(os.path.join(RESOURCE_PATH, 'test.zip'))