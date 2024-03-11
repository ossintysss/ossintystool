# Creating a password encrption program

import base64


def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)

user_pass = input("Enter your password: ")
print("This is your encrypted password ")
encrypt_pass(user_pass)
print("Thanks for using Ossintys Tool")


