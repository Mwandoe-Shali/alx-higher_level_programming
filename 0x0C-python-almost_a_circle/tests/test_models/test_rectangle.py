#!/usr/bin/python3
import unittest
import io
import unittest.mock
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleArea(unittest.TestCase):
    """
    Test class for Rectangle area method.
    """

    def test_area(self):
        """
        Test if the area() method returns the correct area.
        """
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_area_positive_values(self):
        """
        Test if the area() method handles positive values correctly.
        """
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_area_zero_values(self):
        """
        Test if the area() method handles zero values correctly.
        """
        r = Rectangle(0, 0)
        self.assertEqual(r.area(), 0)

    def test_area_negative_values(self):
        """
        Test if the area() method raises an exception for negative values.
        """
        r = Rectangle(-4, 5)
        with self.assertRaises(ValueError):
            r.area()

    def test_area_large_values(self):
        """
        Test if the area() method handles large values correctly.
        """
        r = Rectangle(10**6, 10**6)
        self.assertEqual(r.area(), 10**12)


class TestRectangleDisplay(unittest.TestCase):
    """
    Test class for Rectangle display method.
    """

    def setUp(self):
        self.mocked_stdout = unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
        self.mock_stdout = self.mocked_stdout.__enter__()

    def tearDown(self):
        self.mocked_stdout.__exit__(None, None, None)

    def test_display(self):
        """
        Test if the display() method outputs the correct rectangle for a given size.
        """
        r = Rectangle(3, 2)
        r.display()
        expected_output = "###\n###\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_display_no_x_y(self):
        """
        Test if the display() method correctly displays a rectangle with no x and y values.
        """
        r = Rectangle(2, 1)
        r.display()
        expected_output = "##\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_display_large_size(self):
        """
        Test if the display() method handles large-sized rectangles correctly.
        """
        r = Rectangle(10, 5)
        r.display()
        expected_output = "##########\n##########\n##########\n##########\n##########\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_display_zero_size(self):
        """
        Test if the display() method correctly handles rectangles with zero size.
        """
        r = Rectangle(0, 0)
        r.display()
        expected_output = ""  # No output expected for zero size
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)


class TestRectangleStr(unittest.TestCase):
    """
    Test class for Rectangle str method.
    """

    def test_str(self):
        """
        Test if the str() method returns the correct string representation.
        """
        r = Rectangle(4, 3, 2, 1, 5)
        expected_str = "[Rectangle] (5) 2/1 - 4/3"
        self.assertEqual(str(r), expected_str)

    def test_str_default_id(self):
        """
        Test if the str() method handles default ID correctly.
        """
        r = Rectangle(4, 3, 2, 1)
        expected_str = "[Rectangle] (1) 2/1 - 4/3"
        self.assertEqual(str(r), expected_str)

    def test_str_large_values(self):
        """
        Test if the str() method handles large values correctly.
        """
        r = Rectangle(10**6, 10**6, 0, 0, 10**6)
        expected_str = "[Rectangle] (1000000) 0/0 - 1000000/1000000"
        self.assertEqual(str(r), expected_str)


class TestRectangleUpdate(unittest.TestCase):
    """
    Test class for Rectangle update method.
    """

    def test_update(self):
        """
        Test if the update() method updates attributes correctly with positional arguments.
        """
        r = Rectangle(2, 2)
        r.update(1, 3, 4, 5, 6)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_update_no_args(self):
        """
        Test if the update() method handles no arguments correctly.
        """
        r = Rectangle(2, 2)
        r.update()
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_update_keyword_args(self):
        """
        Test if the update() method handles keyword arguments correctly.
        """
        r = Rectangle(2, 2)
        r.update(id=2, width=4, height=3, x=1, y=2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_update_invalid_args(self):
        """
        Test if the update() method raises an exception for invalid positional arguments.
        """
        r = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            r.update(1, "invalid", 4, 5, 6)

    def test_update_invalid_kwargs(self):
        """
        Test if the update() method raises an exception for invalid keyword arguments.
        """
        r = Rectangle(2, 2)
        with self.assertRaises(ValueError):
            r.update(id=1, width=-3, height=4, x=5, y=6)

class TestRectangleToDictionary(unittest.TestCase):
    """
    Test class for Rectangle to_dictionary method.
    """

    def test_to_dictionary(self):
        """
        Test if the to_dictionary() method returns the correct dictionary representation.
        """
        r = Rectangle(3, 4, 1, 2, 5)
        expected_dict = {
            'id': 5,
            'width': 3,
            'height': 4,
            'x': 1,
            'y': 2
        }
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_default_values(self):
        """
        Test if the to_dictionary() method handles default values correctly.
        """
        r = Rectangle(2, 2)
        expected_dict = {
            'id': 1,
            'width': 2,
            'height': 2,
            'x': 0,
            'y': 0
        }
        self.assertEqual(r.to_dictionary(), expected_dict)


class TestRectangleInstantiation(unittest.TestCase):
    """
    Test class for Rectangle instantiation and attribute access.
    """

    def test_rectangle_is_base(self):
        """
        Test if Rectangle is an instance of Base class.
        """
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """
        Test if Rectangle instantiation with no arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """
        Test if Rectangle instantiation with one argument raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """
        Test if Rectangle instantiation with two arguments assigns unique IDs.
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """
        Test if Rectangle instantiation with three arguments assigns unique IDs.
        """
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """
        Test if Rectangle instantiation with four arguments assigns unique IDs.
        """
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """
        Test if Rectangle instantiation with five arguments assigns the correct ID.
        """
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """
        Test if Rectangle instantiation with more than five arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """
        Test if accessing the private width attribute raises an AttributeError.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        """
        Test if accessing the private height attribute raises an AttributeError.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        """
        Test if accessing the private x attribute raises an AttributeError.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        """
        Test if accessing the private y attribute raises an AttributeError.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """
        Test if the width getter returns the correct value.
        """
        r = Rectangle(5, 7, 7, 5, 1)



if __name__ == "__main__":
    unittest.main()
