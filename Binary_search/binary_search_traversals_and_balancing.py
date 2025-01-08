"""
As a senior backend engineer at Jovian, you are tasked with developing
a fast in-memory data structure to manage profile information
(username, name and email) for 100million users.
it should allow the folowing operations to be performed efficiently:
1- insert new user profile information
2- find the profile information of a user, given their name
3. update the profile information of a user, given a username
4. list all users on the platform, sorted by username

assume usernames are unique
"""

# create a user class to store all the required user info
# instatiate an object of the class
# insert: loop through the list and add new user at aposition keeping a sorted list
# find: loop through the user list and find object with username matching the query
# update: loop through the list, find the user object matching the query and update profile
# List: output datastructure, return the  list of objects

class User:
    def __init__(self, user, username, email):
        self.user = user
        self.username = username
        self.email = email

    def __repr__(self):
        return "user(username='{}', name='{}', email='{}')".format(self.user)
class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
            
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_of_users(self):
        return self.users
