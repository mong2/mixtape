import sys
import os
import pytest
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../../', ''))
from lib.song_controller import SongController

MOCK_DATA = { '1': 1,
              '2': 1,
              '3': 1,
              '5': 1,
              '10': 1,
              '20': 1}


class TestUnitSongController(unittest.TestCase):
    def test_song_exist(self):
        sc = SongController(MOCK_DATA)
        assert sc.exist(2)

    def test_songs_exist(self):
        sc = SongController(MOCK_DATA)
        assert sc.exist([3,10,5]) 

    def test_song_doesnt_exist(self):
        with self.assertRaises(ValueError) as context:
            sc = SongController(MOCK_DATA)
            sc.exist(100)
        self.assertTrue('Invalid input: song id, 100 doesnt exist' in context.exception)

    def test_one_of_the_songs_does_exist(self):
        with self.assertRaises(ValueError) as context:
            sc = SongController(MOCK_DATA)
            sc.exist([3,7,5])