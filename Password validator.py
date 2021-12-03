# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid
import re
# Input
def dataInput():
    password = str(input("Enter password: "))
    return password

passcode = dataInput()

# Validate rules
if not len(passcode) > 15:
    print("Password must be greater than 15 characters!")
elif not re.search("[A-Z]" ,passcode):
    print("Password must have atleast one capital letter!")
elif not re.search("[0-9]" ,passcode):
    print("Password must have atleast one number!")
elif not re.search("[!$#@%^&*-_=+;:,.<>]" ,passcode):
    print("Password must have atleast one character (ex:!$#@%^&*-_=+;:,.<>)")
else:
    print("Your password is VALID")
