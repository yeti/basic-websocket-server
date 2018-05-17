from passlib.hash import argon2
import sys

def print_argon2_token(userpass):
    print(argon2.hash(userpass))

if __name__ == '__main__':
    try:
        userpass = sys.argv[1]
        print_argon2_token(userpass)
    except IndexError:
        print("Usage: python print_argon2_token.py <username>:<password>")
