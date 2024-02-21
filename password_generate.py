import random
import string

def generate_password(min_length,number=True,specia_character=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    character=letters
    if number:
        character+=digits
    if specia_character:
        character+=special
    pwd=""
    meets_criteria=False
    has_number=False
    has_special=False
    while not meets_criteria or len(pwd)<min_length:
        new_char=random.choice(character)
        pwd+=new_char
        
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
            
        meets_criteria=True
        if number:
            meets_criteria=has_number
        if special:
            specia_character=meets_criteria and has_special
    return pwd


min_length=int(input("Enter the minimum length of Password :"))
number=input("Do you want add in paswword numbers y/n :").lower().strip()=='y'
specia_character=input("Do you want add in paswword  specialcharacters y/n :").lower().strip()=='y'

result=generate_password(min_length, number, specia_character)
print(f'Current generate Password: {result}')