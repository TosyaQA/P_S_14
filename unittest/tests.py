import unittest

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

class TestStudent(unittest.TestCase):
    def test_valid_name(self):
        s = Student('Иванов', 'Иван', 'Иванович')
        self.assertEqual(s.last_name, 'Иванов')
        self.assertEqual(s.first_name, 'Иван')
        self.assertEqual(s.middle_name, 'Иванович')

    def test_invalid_name(self):
        with self.assertRaises(InvalidNameError):
            Student('Иванов', 'И2ван', 'Иванович')

    def test_print(self):
        s = Student('Иванов', 'Иван', 'Иванович')
        captured_output = self._run_print_method(s)
        self.assertEqual(captured_output, 'Иванов Иван Иванович\n')

    def _run_print_method(self, student):
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            student.print()
        return f.getvalue()

if __name__ == '__main__':
    unittest.main()