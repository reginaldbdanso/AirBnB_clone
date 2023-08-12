#!/usr/bin/python3
"""FileStorage module"""
import json


class FileStorage:
    """
        class serializes instances to a JSON
        file and deserializes JSON to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
            
            Args:
                obj - an instance object
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON file"""
        obj_dict = {}
        for key, val in FileStorage.__objects.items():
            if hasattr(val, 'to_dict') and callable(val.to_dict):
                obj_dict[key] = val.to_dict()
        else:
            obj_dict[key] = str(val)
        
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(obj_dict, fd)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)

        except FileNotFoundError:
            pass
