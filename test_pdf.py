import pypdf
import os
from conftest import RESOURCE_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_pdf():
    reader = pypdf.PdfReader(os.path.join(RESOURCE_PATH, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    size = os.path.getsize(os.path.join(RESOURCE_PATH, 'docs-pytest-org-en-latest.pdf'))

    print(size)
    count = 0
    for image_file in first_page.images:
        with open(str(count) + image_file.name, 'wb') as fp:
            fp.write(image_file.data)
            count += 1
    assert number_of_pages == 412, "Неверное число страниц"
    assert size == 1739253, "Неверный размер файла"
