#!/usr/bin/python3
"""
Module: 11-student
Defines a Student class with serialization and deserialization capabilities.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.

        Args:
            attrs (list): A list of attribute names to include
                            in the dictionary representation.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the values
        from the provided JSON dictionary.

        Args:
            json (dict): The JSON dictionary containing the attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
