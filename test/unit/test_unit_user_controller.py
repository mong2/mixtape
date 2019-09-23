import sys
import os
import pytest
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../../', ''))
from lib.user_controller import UserController

MOCK_DATA = { '1': 'apple red',
              '2': 'grape green',
              '3': 'banana yellow',
              '5': 'mango orange',
              '10': 'adam smith',
              '20': 'joe johnson'}


class TestUnitUserController(unittest.TestCase):
    def test_user_exist(self):
        uc = UserController(MOCK_DATA)
        assert uc.exist(2)

    def test_user_doesnt_exist(self):
        with self.assertRaises(ValueError) as context:
            uc = UserController(MOCK_DATA)
            uc.exist(100)
        self.assertTrue('User id, 100 doesnt exist' in context.exception)