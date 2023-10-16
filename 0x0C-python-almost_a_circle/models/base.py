#!/usr/bin/python3
"""
Module Base
Super class
"""
import json


class Base:
    """
    Base class for managing id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int): The id value for the object.
                        If None, a unique id will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves the JSON string representation of a list of instances to a file.

        Args:
            list_objs (list): A list of instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as j_file:
            if list_objs is None:
                j_file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_string = Base.to_json_string(list_dicts)
                j_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Args:
            json_string (str): A JSON string representation.

        Returns:
            list: The list of instances from the JSON string representation.
        """
        if type(json_string) is not str:
            raise TypeError("json_string must be a string")
        if json_string is None or len(json_string) == 0:
            return ("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of an existing class

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Instance: An instance with all attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a file in JSON format.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as j_file:
                json_string = j_file.read()
                json_list = cls.from_json_string(json_string)
                instances = []
                for dictionary in json_list:
                    instances.append(cls.create(**dictionary))
                return instances
        except FileNotFoundError:
            return ("[]")
