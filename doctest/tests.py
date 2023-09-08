import doctest

#Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты. 2-5 тестов на задание в трёх
#вариантах:
#- doctest,
#- unittest,
#- pytest.
#(Просьба, тесты хранить в разных папках, отдельно под pytest, отдельно под unittest и т.д.)

#семинар 13


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
        """
        >>> s = Student('Иванов', 'Иван', 'Иванович')
        >>> s.print()
        Иванов Иван Иванович

        >>> s = Student('Петров', 'Петр', 'Петрович')
        >>> s.print()
        Петров Петр Петрович

        >>> try:
        ...     s = Student('Неправильно', 'ФИО', 'Ученика')
        ... except Exception as e:
        ...     str(e)
        ...
        'ФИО должно начинаться с заглавной буквы и может содержать только буквы'
        """
        print(self.last_name + ' ' + self.first_name + ' ' + self.middle_name)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
