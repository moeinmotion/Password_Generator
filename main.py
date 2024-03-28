import random
import string

#ask users what the minimum length must be, etc...
def generate_password(min_length, numbers=True, special_characters=True):
    #get letters, digits and special characters here
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #need to combine into one large list or stringthat we're going to randomly choose from
    #Then create string that contains all different characters i can be selecting from
    characters = letters
    if numbers:
        characters = characters + digits
    if special_characters:
        characters = characters + special
    #Generating loop where during every iteration, we generate a new character to add to our new password;
    #continue loop until we meet criteria
    pwd = ""
    meet_criteria = False #current, not meeting criteria
    has_number = False #Don't have a number
    has_special = False #Don't have a special character

    #if either of these are true, then continue loop
    while not meet_criteria or len(pwd) < min_length:
        #generate new character by randomly selecting from characters i can pick from (characters = letters)
        new_char = random.choice(characters)
        pwd += new_char
        #and add to our password and then determine if new character was a number, sets has_number = True or if it was a special chacter, sets has_special = true
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers? (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is", pwd)