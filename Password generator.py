import random
import string

def generate_password(length):
    # Define character sets for password generation
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to Secure Password Generator!")
    print("")

    # Get user input for password length
    length = int(input("Enter the length of the password: "))

    # Generate password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
