import pytest

@pytest.mark.parametrize("num",[1,2,3,-1]) #"num" должен совпадать с передаваемым  параметром. Посмотреть входные данные ИЗ файла
def test_numbers(num:int):
    assert num > 0

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["mac","win","lin","deb"],)
@pytest.mark.parametrize("host", ["https://2323", "https://ggl"])
def test_multiplication_of_nums(os:str, host:str):
    assert len( os+ host) > 0