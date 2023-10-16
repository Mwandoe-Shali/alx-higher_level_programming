#!/usr/bin/python3
import unittest
import inspect
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test class for the Base class.
    """

    def test_base_none_id(self):
        """
        Test if the Base class sets the id
                    attribute to 1 when None is provided as the id.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_negative_id(self):
        """
        Test if the Base class can handle negative id values.
        """
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_base_custom_id(self):
        """
        Test if the Base class sets the id
                    attribute correctly when a custom id is provided.
        """
        b1 = Base(10)
        b2 = Base(20)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)

    def test_base_string_id(self):
        """
        Test if the Base class sets the id
                    attribute correctly when a string id is provided.
        """
        b1 = Base("Uniq")
        self.assertEqual(b1.id, "Uniq")

    def test_base_float_id(self):
        """
        Test if the Base class sets the id
                    attribute correctly when a float id is provided.
        """
        b1 = Base(3.14)
        self.assertEqual(b1.id, 3.14)

    def test_id_dict(self):
        """
        Test if the Base class id is set correctly if id is a dictionary.
        """
        b = Base({"id": 109})
        self.assertEqual({"id": 109}, b.id)


class TestSquare(unittest.TestCase):
    """
    class for testing Base class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

if __name__ == "__main__":
    unittest.main
