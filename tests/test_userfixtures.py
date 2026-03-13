import pytest

@pytest.fixture
def clear_books_database():
    print("[FIXTURE] УДАЛЯЕМ ИЗ БАЗЫ")
    
@pytest.fixture
def fill_books_database():
    print("[FIXTURE] СОЗДАЕМ НОВЫЕ ДАННЫЕ")

@pytest.mark.usefixtures('clear_books_database', 'fill_books_database') #Выполняются в том порядке, в котором заданы. В таком виде значения не возвращаются
class TestLibrary:
    def test_read_book_from_library(self):
        ...
    def test_delete_book_from_library(self):
        ...