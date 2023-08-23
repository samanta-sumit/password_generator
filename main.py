import random
import string

def password_generator(letter , number=True , special_character=True):
    
     letter=string.ascii_letters
     digits=string.digits
     special=string.punctuation

     character = letter
     if number:
          character+=digits
     if special_character:
          character+=special

     pwd=""
     meet_criteria=False
     has_numbers=False
     has_special=False

     while not meet_criteria or len(pwd)< min_length:
          new_char= random.choice(character)
          pwd += new_char

          if new_char in digits:
               has_numbers=True
          elif new_char in special:
               has_special=True
        
          meet_criteria = True
          if number:
               meet_criteria = has_numbers
          if special_character:
               meet_criteria = meet_criteria and has_numbers
     return pwd

min_length = int(input("enter the minimum length : "))
has_numbers= input("do you wahnt no.s ").lower() == "y"
has_special=  input("do you wahnt specail characters ").lower() == "y"     

pwd= password_generator(min_length,has_special,has_numbers)
print("your password is :"+ pwd)
