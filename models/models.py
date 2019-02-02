from datetime import datetime

users = []




class Users:
    user_id = 1

    def __init__(self, firstname=None, lastname=None, username=None, password=None, email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.dateRegistered = datetime.now().replace(second=0, microsecond=0)
        self.id = Users.user_id

        Users.user_id += 1

    def serializer(self):
        return dict(
            user_id=self.user_id,
            firstname=self.firstname,
            lastname=self.lastname,
            username=self.username,
            password=self.password,
            email=self.email,
            dateRegistered=str(self.dateRegistered)

        )

    def get_user_by_username(self,username):
        for user in users:
            if user == username:
                return user

    def get_user_by_email(self,email):
         for user in users:
            if user.email == email:
                return user

