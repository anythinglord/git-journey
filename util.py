from random import choice
import string

def get_name():
    letters = string.ascii_lowercase
    return ''.join(choice(letters) for i in range(10))