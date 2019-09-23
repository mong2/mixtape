from lib.options import Options
from lib.playlist_controller import PlaylistController
from lib.user_controller import UserController
from lib.song_controller import SongController
from lib.file_controller import FileController


class Mixtape():
    def __init__(self, options):
        self.input_file = self.validate_option(options['input'])
        self.output = self.validate_option(options['output'])
        self.changefile = self.validate_option(options['changefile'])
        self.file_controller = FileController()
        self.load_files()
        self.load_controllers()

    def validate_option(self, option):
        if option[0].endswith('.json'):
            return option[0]
        else: 
            raise ValueError('Invalid file type. All file should be in json format.')
            
    def load_files(self):
        self.user_df, self.playlist_df, self.song_df = self.file_controller.build_dataframe(self.input_file)
        self.changes = self.file_controller.read_file(self.changefile)['changes']

    def load_controllers(self):
        self.pl = PlaylistController(self.playlist_df)
        self.user = UserController(self.user_df)
        self.song = SongController(self.song_df)

    def run(self):
        for change in self.changes:
            if change['action'] == 'delete':
                self.playlist_df = getattr(self.pl, change['action'])(change['playlist_id'])
            elif change['action'] == 'update':
                if self.song.exist(change['song_id']):
                    self.playlist_df = getattr(self.pl, change['action'])(change['playlist_id'], change['song_id'])
            elif change['action'] == 'create':
                if self.user.exist(change['user_id']):
                    if self.song.exist(change['song_ids']):
                        self.playlist_df = getattr(self.pl, 'create')(change['user_id'], change['song_ids'])
            else:
                raise ValueError('Invalid action: %s' % change['action'])
        self.file_controller.write_file(self.output, self.playlist_df)
        return None 

if __name__ == "__main__":
    options = Options()
    mt = Mixtape(options)
    mt.run()