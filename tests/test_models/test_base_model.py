"""
This module contains unit tests for the BaseModel class.

The tests ensure the correctness of the BaseModel class methods by checking their behavior
and comparing the expected outcomes.

Classes:
    TestBaseModel: Unit tests for the BaseModel class.

Usage:
    To run the tests, execute the following command in the terminal:
    python -m unittest test_base_model.py
"""

import unittest
import datetime
from  models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.

    Test methods:
        test_str_representation: Test the __str__ representation of the BaseModel object.
        test_save_method: Test the save method's effect on the updated_at attribute.
        test_to_dict_method: Test the to_dict method's output.
    """

    def setUp(self):
        """
        Create an instance of the BaseModel class before each test.
        """
        self.base_model = BaseModel()

    def test_str_representation(self):
        """
        Test the __str__ representation of the BaseModel object.
        """
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        """
        Test the save method's effect on the updated_at attribute.
        """
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method's output.
        """
        data_dict = self.base_model.to_dict()

        self.assertEqual(data_dict['id'], str(self.base_model.id))
        self.assertIsInstance(data_dict['created_at'], str)
        self.assertIsInstance(data_dict['updated_at'], str)
        self.assertEqual(data_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()

