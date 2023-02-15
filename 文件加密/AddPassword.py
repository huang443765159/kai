import getpass
import pickle
import json
import hashlib
from os import path


# First we check if the database exists.
if path.isfile('hello.json'):
    with open('hello.json', 'r') as fh:
        db = json.load(fh)
        print(db['user'])

# And then we dump the variable into the filehandle.
# This will keep the variable intact between sessions,
# meaning the next time you start your script, the variable will look the same.

# Then we ask the user for his/hers credentials.
user = input('Username: ')
_pass = getpass.getpass('Password: ')

# If the user exists in the "db" and the decoded password
# Matches the logged in user, it's a-ok :)
print(db['user'] == user, db['password'] == _pass, user, _pass)
if user == db['user'] and db['password'] == int(_pass):
    print('You logged in')
