import random
import string


def generate_password(minimum_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < minimum_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


min_length = int(input("Enter the length of the password: "))
has_numbers = input('Do you want to have numbers in your password (Y/N) ').lower() == "y"
has_special = input("Do you want ti have special characters in your password? (Y/N) ").lower() == "y"

pwd = generate_password(min_length, has_numbers, has_special)
print("Here's your password: ", pwd)
