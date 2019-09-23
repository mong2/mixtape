import sys
import os
import pytest
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../../', ''))
from lib.playlist_controller import PlaylistController


class TestUnitPlaylistController(unittest.TestCase):
    def setUp(self):
      self.mock_data = { 
        '1': {'song_ids': ['8', '32'], 'user_id': '2'}, 
        '2': {'song_ids': ['24', '3', '5'], 'user_id': '5'}, 
        '3': {'song_ids': ['6', '8', '11', '3'], 'user_id': '3'}
      }

    def test_delete_exist_playlist(self):
        uc = PlaylistController(self.mock_data)
        assert uc.delete(3)

    def test_delete_unexist_playlist(self):
        with self.assertRaises(ValueError) as context:
            uc = PlaylistController(self.mock_data)
            uc.delete(100)
        self.assertTrue('Can not delete playlist, 100 doesnt exist' in context.exception)

    def test_new_playlist_id(self):
        uc = PlaylistController(self.mock_data)
        self.assertEqual(uc.new_playlist_id(), 4)

    def test_new_playlist_id_empty_playlist(self):
        uc = PlaylistController({})
        self.assertEqual(uc.new_playlist_id(), 1)

    def test_create_playlist(self):
        uc = PlaylistController(self.mock_data)
        uc.create(user_id=2, song_ids=[1])
        self.assertEqual(uc.pl_df['4']['user_id'], '2')
        self.assertEqual(uc.pl_df['4']['song_ids'], ['1'])

    def test_create_playlist_with_multiple_songs(self):
        uc = PlaylistController(self.mock_data)
        uc.create(user_id=2, song_ids=[1,3,6])
        self.assertEqual(uc.pl_df['4']['user_id'], '2')
        self.assertEqual(uc.pl_df['4']['song_ids'], ['1','3','6'])

    def test_update_playlist_with_integer(self):
        uc = PlaylistController(self.mock_data)
        uc.update(playlist_id=2, song_id=4)
        assert '4' in uc.pl_df['2']['song_ids']

    def test_update_playlist_with_string(self):
        uc = PlaylistController(self.mock_data)
        uc.update(playlist_id=2, song_id='10')
        assert '10' in uc.pl_df['2']['song_ids']

    def test_update_playlist_no_dupe(self):
        uc = PlaylistController(self.mock_data)
        uc.update(playlist_id=2, song_id=3)
        self.assertEqual(len(uc.pl_df['2']['song_ids']), len(self.mock_data['2']['song_ids']))

    def test_update_playlist_failed_with_invalid_playlist_id(self):
      with self.assertRaises(ValueError) as context:
          uc = PlaylistController(self.mock_data)
          uc.update(playlist_id=100, song_id=4)
      self.assertTrue('Playlist id, 100 doesnt exist' in context.exception)

    def test_update_playlist_failed_with_invalid_song_id_format(self):
      with self.assertRaises(TypeError) as context:
          uc = PlaylistController(self.mock_data)
          uc.update(playlist_id=2, song_id=[4,3])
      self.assertTrue('Invalid input. Please make sure song_id is in the correct format. Number in either string or integer format.' in context.exception)
