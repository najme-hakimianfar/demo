# test_add_numbers.py

from add_numbers import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5  # تست جمع صحیح
    assert add_numbers(-1, 1) == 0  # تست مقادیر منفی
    assert add_numbers(0, 0) == 0  # تست صفر
