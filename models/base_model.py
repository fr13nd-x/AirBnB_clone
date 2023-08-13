"""
This module defines the BaseModel class for creating objects with unique identifiers and timestamps.

Classes:
    BaseModel: A base class for creating objects with a unique identifier, creation timestamp,
               and update timestamp.

Usage:
    from base_model import BaseModel
    obj = BaseModel()
    print(obj)
    obj.save()
    data_dict = obj.to_dict()
"""

import datetime
import uuid

class BaseModel:
    """
    A base class for creating objects with a unique identifier, creation timestamp, and update timestamp.

    Attributes:
        id (uuid.UUID): The unique identifier (UUID) for the object.
        created_at (datetime.datetime): The timestamp when the object was created.
        updated_at (datetime.datetime): The timestamp when the object was last updated.

    Methods:
        __str__: Return a string representation of the BaseModel object.
        save: Update the updated_at attribute to the current timestamp.
        to_dict: Return a dictionary representation of the BaseModel object.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel.

        Attributes:
            id (uuid.UUID):- The unique identifier (UUID) for the object.
            created_at (datetime.datetime): The timestamp when the object was created.
            updated_at (datetime.datetime): The timestamp when the object was last updated.
        """
        if not kwargs:
            self.id = uuid.uuid4()
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
        else:
            for key, val in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
                elif key == "id":
                    self.__dict__[key] = str(val)
                else:
                    self.__dict__[key] = val

    def __str__(self):
        """
        Return a string representation of the BaseModel object.

        Returns:
            str: A string representation of the object, showing its class name,
                 id, and the dictionary of instance attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute to the current timestamp.

        This method sets the updated_at attribute to the current timestamp
        indicating that the object has been recently updated.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel object.

        Returns:
            dict: A dictionary containing the object's attributes with 'id', 'created_at',
                  'updated_at', and '__class__' keys.
        """
        data_dict = self.__dict__.copy()
        data_dict['__class__'] = self.__class__.__name__
        data_dict['id'] = str(data_dict['id'])
        data_dict['created_at'] = data_dict['created_at'].isoformat()
        data_dict['updated_at'] = data_dict['updated_at'].isoformat()
        return data_dict
