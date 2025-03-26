# Project 6: Password Generator
# Author: Erum Azeemi Qaimkhani

import random
import string

def password_generator(length=9):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password
# user input

length = int(input("Enter the length of the password: "))
password = password_generator(length)
print ("Your password is: ", password)
