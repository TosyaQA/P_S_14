import pytest

class InvalidNameError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NameDescriptor:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise InvalidNameError("ФИО должно начинаться с заглавной буквы и может содержать только буквы")
        setattr(instance, self._name, value)

class Student:
    last_name = NameDescriptor()
    first_name = NameDescriptor()
    middle_name = NameDescriptor()

    def __init__(self, last_name: str, first_name: str, middle_name: str):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name

    def print(self):
        print(self.last_name + ' ' + self.first_name + ' ' + self.middle_name)

def test_valid_name():
    s = Student('Иванов', 'Иван', 'Иванович')
    assert s.last_name == 'Иванов'
    assert s.first_name == 'Иван'
    assert s.middle_name == 'Иванович'


def test_invalid_name():
    with pytest.raises(InvalidNameError):
        Student('Иванов', 'И2ван', 'Иванович')


def test_print(capsys):
    s = Student('Иванов', 'Иван', 'Иванович')
    s.print()
    captured = capsys.readouterr()
    assert captured.out == 'Иванов Иван Иванович\n'