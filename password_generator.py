import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_pool = ""
    
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("No character types selected. Please select at least one character type.")
    
    password = ''.join(random.choice(character_pool) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the password length: "))
            if length <= 0:
                print("Password length should be a positive integer.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        if not use_letters and not use_numbers and not use_symbols:
            print("You must select at least one character type.")
            continue
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
        
        another = input("Generate another password? (y/n): ").strip().lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
