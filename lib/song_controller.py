

class SongController():
    def __init__(self, song_df):
        self.song_df = song_df
        return None

    def exist(self, song_id):
        if type(song_id) is list: 
            return self.songs_exist(song_id)
        else:
            try:
                return self.song_df[str(song_id)]
            except:
                raise ValueError("Invalid input: song id, %s doesnt exist" % song_id)   

    def songs_exist(self, song_ids):
        if set(map(str, song_ids)).issubset(self.song_df.keys()):
            return True 
        else: 
            raise ValueError("Invalid input: song ids, %s dont exist" % song_ids)   
