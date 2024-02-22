import random
from string import ascii_lowercase, ascii_uppercase

def add_lowercase():
    choice = random.choice(ascii_lowercase)
    return choice

def add_uppercase():
    choice = random.choice(ascii_uppercase)
    return choice

def add_symbol():
    symbol_1 = random.choice(range(33, 48))
    symbol_2 = random.choice(range(91,97))
    symbol_3 = random.choice(range(123, 127))
    choice = random.choice([symbol_1, symbol_2, symbol_3])
    return chr(choice)

def add_number():
    choice = random.choice(range(0,10))
    return str(choice)

def generate_random_password(true_options : list, length : int = 8):
    my_password = ""
    
    len_password = length
    for password in range(len_password):
        try:
            random_choice = random.choice(true_options)
        except IndexError:
            return ""
            
        if random_choice == "LowerCase":
            password = add_lowercase()
            my_password += password
        
        elif random_choice == "UpperCase":
            password = add_uppercase()
            my_password += password
        
        elif random_choice == "Symbol":
            password = add_symbol()
            my_password += password
        
        elif random_choice == "Number":
            password = add_number()
            my_password += password
        
        elif random_choice == "Space":
            my_password += " "

        else:
            pass
    return my_password



            
    


        