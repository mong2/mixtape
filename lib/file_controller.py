import json
import os

class FileController():
    def __init__(self):
        self.mixtape = None
        return None 

    def read_file(self, file_name):
        with open(file_name) as f:
            try:
                data = json.load(f)
            except:
                raise ValueError('Invalid file type. All file should be in json format.')
        return data

    def build_dataframe(self, file_name):
        self.mixtape = self.read_file(file_name)
        user_df = {}
        song_df = {}
        pl_df = {}

        for user in self.mixtape['users']:
            user_df[user['id']] = user['name']

        for song in self.mixtape['songs']:
            song_df[song['id']] = 1 

        for playlist in self.mixtape['playlists']:
            pl_df[playlist['id']] = {'user_id': playlist['user_id'], 'song_ids': playlist['song_ids']}

        return user_df, pl_df, song_df

    def write_file(self, file_name, content):
        self.mixtape['playlists'] = content
        with open(file_name, "w") as f:
            json.dump(self.mixtape, f)