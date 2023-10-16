import unittest
import io
import unittest.mock
from models.square import Square


class TestSquareArea(unittest.TestCase):
    """
    Test class for the area method of the Square class.
    """

    def test_area(self):
        """
        Test if the area method calculates the area correctly.
        """
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_area_positive_values(self):
        """
        Test if the area method handles positive values correctly.
        """
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_area_zero_values(self):
        """
        Test if the area method handles zero values correctly.
        """
        s = Square(0)
        self.assertEqual(s.area(), 0)

    def test_area_negative_values(self):
        """
        Test if the area method raises a ValueError for negative values.
        """
        s = Square(-4)
        with self.assertRaises(ValueError):
            s.area()

    def test_area_large_values(self):
        """
        Test if the area method handles large values correctly.
        """
        s = Square(10**6)
        self.assertEqual(s.area(), 10**12)


class TestSquareDisplay(unittest.TestCase):
    """
    Test class for the display method of the Square class.
    """

    def setUp(self):
        """
        Set up method for capturing stdout.
        """
        self.mocked_stdout = unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
        self.mock_stdout = self.mocked_stdout.__enter__()

    def tearDown(self):
        """
        Clean up method for closing stdout capture.
        """
        self.mocked_stdout.__exit__(None, None, None)

    def test_display(self):
        """
        Test if the display method prints the square correctly.
        """
        s = Square(3)
        s.display()
        expected_output = "###\n###\n###\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_display_no_x_y(self):
        """
        Test if the display method handles square with no x and y correctly.
        """
        s = Square(2)
        s.display()
        expected_output = "##\n##\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_display_large_size(self):
        """
        Test if the display method handles a large size correctly.
        """
        s = Square(10)
        s.display()
        expected_output = "##########\n##########\n##########\n##########\n##########\n\
                          ##########\n##########\n##########\n##########\n##########\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_display_zero_size(self):
        """
        Test if the display method handles a square with zero size correctly.
        """
        s = Square(0)
        s.display()
        expected_output = ""
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)


class TestSquareStr(unittest.TestCase):
    """
    Test class for the str method of the Square class.
    """

    def test_str(self):
        """
        Test if the str method returns the correct string representation.
        """
        s = Square(4, 2, 1, 5)
        expected_str = "[Square] (5) 2/1 - 4"
        self.assertEqual(str(s), expected_str)

    def test_str_default_id(self):
        """
        Test if the str method handles the default id correctly.
        """
        s = Square(4, 2, 1)
        expected_str = "[Square] (1) 2/1 - 4"
        self.assertEqual(str(s), expected_str)

    def test_str_large_values(self):
        """
        Test if the str method handles large values correctly.
        """
        s = Square(10**6, 0, 0, 10**6)
        expected_str = "[Square] (1000000) 0/0 - 1000000"
        self.assertEqual(str(s), expected_str)


class TestSquareUpdate(unittest.TestCase):
    """
    Test class for the update method of the Square class.
    """

    def test_update(self):
        """
        Test if the update method updates attributes correctly.
        """
        s = Square(2)
        s.update(1, 3, 4, 5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_update_no_args(self):
        """
        Test if the update method handles no arguments correctly.
        """
        s = Square(2)
        s.update()
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_update_keyword_args(self):
        """
        Test if the update method handles keyword arguments correctly.
        """
        s = Square(2)
        s.update(id=2, size=4, x=1, y=2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_update_invalid_args(self):
        """
        Test if the update method raises TypeError for invalid arguments.
        """
        s = Square(2)
        with self.assertRaises(TypeError):
            s.update(1, "invalid", 4, 5)

    def test_update_invalid_kwargs(self):
        """
        Test if the update method raises ValueError for invalid keyword arguments.
        """
        s = Square(2)
        with self.assertRaises(ValueError):
            s.update(id=1, size=-3, x=5)


class TestSquareToDictionary(unittest.TestCase):
    """
    Test class for the to_dictionary method of the Square class.
    """

    def test_to_dictionary(self):
        """
        Test if the to_dictionary method returns a dictionary with correct values.
        """
        s = Square(3, 1, 2, 5)
        expected_dict = {"id": 5, "size": 3, "x": 1, "y": 2}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_default_values(self):
        """
        Test if the to_dictionary method handles default values correctly.
        """
        s = Square(2)
        expected_dict = {"id": 1, "size": 2, "x": 0, "y": 0}
        self.assertEqual(s.to_dictionary(), expected_dict)


class TestSquareInstantiation(unittest.TestCase):
    """
    Test class for the instantiation of the Square class.
    """

    def test_square_is_rectangle(self):
        """
        Test if a Square instance is also an instance of the Square class.
        """
        self.assertIsInstance(Square(10), Square)
        self.assertIsInstance(Square(10), Square)
        self.assertIsInstance(Square(2), Square)
        self.assertIsInstance(Square(1), Square)


if __name__ == "__main__":
    unittest.main()
