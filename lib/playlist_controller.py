

class PlaylistController():
    def __init__(self, playlist_df):
        self.pl_df = playlist_df
        return None 

    def create(self, user_id, song_ids):
        playlist_id = self.new_playlist_id()
        self.pl_df[str(playlist_id)] = { 'user_id': str(user_id),
                                         'song_ids': map(str, song_ids)
                                        }
        return self.pl_df 
    
    def update(self, playlist_id, song_id):
        if self.validate_single_input(song_id):
            if self.pl_df.has_key(str(playlist_id)):
                if str(song_id) not in self.pl_df[str(playlist_id)]['song_ids']:
                    self.pl_df[str(playlist_id)]['song_ids'].append(str(song_id))
            else:
                raise ValueError("Playlist id, %s doesnt exist" % playlist_id)
        return self.pl_df 

    def delete(self, playlist_id):
        try: 
            del self.pl_df[str(playlist_id)]
        except: 
            raise ValueError("Can not delete playlist, %s doesnt exist" % playlist_id)
        return self.pl_df 

    def validate_single_input(self, song_id):
        if type(song_id) is str:
            return song_id.isdigit()
        elif type(song_id) is int:
            return True
        else:
            raise TypeError('Invalid input. Please make sure song_id is in the correct format. Number in either string or integer format.')

    def new_playlist_id(self):
        if self.pl_df:
            return int(max(self.pl_df.keys())) + 1
        else:
            return 1