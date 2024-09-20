import random
import string

def generate_password(length:int)-> str:
    # Define the possible characters for the password: letters, digits, and punctuation
    characters = #ToDo
    
    # Randomly choose 'length' number of characters from the characters list
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Ask the user for the desired password length

def main():

    try:
    
        #ToDO
    
        if password_length <= 0:
            print("Please enter a positive number.")
        else:
            # Generate and display the password
            print(f"Generated password: {generate_password(password_length)}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
