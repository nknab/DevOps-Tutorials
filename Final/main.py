'''
File: main.py
Project: Final
File Created: Tuesday, 14th June 2022 10:17:22 AM
Author: nknab
Email: adverb_rushed_09@icloud.com
Version: 1.0
Brief: Implementation of a strong password validator.
-----
Last Modified: Tuesday, 14th June 2022 10:19:08 AM
Modified By: nknab
-----
Copyright ©2022 nknab
'''

def count_char(_password):
    """
    This function takes a string as an argument and returns the length of the string
    
    :param _password: The password to be tested
    :return: The length of the password
    """
    return len(_password)


def chk_maj(_password):
    """
    It checks if the password has a capital letter
    
    :param _password: The password to be checked
    :return: True or False
    """
    for letter in _password:
        if letter.isupper():
            return True
    return False

def chk_special(_password):
    """
    It checks if any of the characters in the password are in the list of special characters
    
    :param _password: The password to be checked
    :return: True or False
    """
    special = ['!', '*', '&']
    for letter in _password:
        if letter in special:
            return True
    return False

def chk_valid(_password):
    """
    It checks if the password is valid by checking if the length is greater than 10, if it contains a
    special character, and if it contains a capital letter
    
    :param _password: The password to be checked
    :return: True or False
    """
    password_len = 10
    if count_char(_password) >= password_len and chk_maj(_password) and chk_special(_password):
        return True
    return False

# Testing the function
passowrd = input("Kindly enter a password: ")
print(passowrd)
if chk_valid(passowrd):
    print("Password is Valid")
else:
    print("Password is Invalid")
