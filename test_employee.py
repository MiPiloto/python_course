import unittest
from class_employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("bruce","wayne",30000)

    def test_give_default_raise(self):
        self.employee.raise_salary()
        self.assertEqual(self.employee.salary, 35000)

    def test_give_custom_raise(self):
        self.employee.raise_salary(20000)
        self.assertEqual(self.employee.salary, 50000)

unittest.main()
