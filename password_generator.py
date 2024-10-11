import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Ask the user for the desired password length
        length = int(input("Enter the desired length of the password: "))
        
        # Ensure length is a positive integer
        if length <= 0:
            print("Password length should be a positive integer.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated password: {password}")
    
    except ValueError:
        print("Please enter a valid number for the password length.")

# Run the program
if __name__ == "__main__":
    main()
