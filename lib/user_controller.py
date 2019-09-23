

class UserController():
    def __init__(self, user_df):
        self.user_df = user_df
        return None

    def exist(self, user_id):
        if self.user_df.has_key(str(user_id)):
            return True
        else:
            raise ValueError("User id, %s doesnt exist" % user_id)
