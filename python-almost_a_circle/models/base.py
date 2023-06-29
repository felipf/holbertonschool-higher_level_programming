#!/usr/bin/python3
"""
task 0
"""
import json
import os.path


class Base():
    """
    creating a base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initiation
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_to_write = f"{cls.__name__}.json"
        to_dict_list = []
        if not list_objs:
            pass
        else:
            for x in range(len(list_objs)):
                to_dict_list.append(list_objs[x].to_dictionary())

        to_write = cls.to_json_string(to_dict_list)

        with open(file_to_write, 'w') as file:
            file.write(to_write)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            newby = cls(5, 5)
        else:
            newby = cls(5)
        newby.update(**dictionary)
        return newby

    @classmethod
    def load_from_file(cls):
        file_to_load = "{}.json".format(cls.__name__)
        loaded_list = []
        if not os.path.isfile(file_to_load):
            return []
        with open(file_to_load, 'r') as f:
            json_readed = f.read()

        json_list = cls.from_json_string(json_readed)

        for i in range(len(json_list)):
            loaded_list.append(cls.create(**json_list[i]))
        return loaded_list
