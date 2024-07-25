import random
import string

def generate_password(length=12, complexity=3):
    """
    Generate a password of a given length and complexity.
    
    Complexity levels:
    1 - Only letters
    2 - Letters and digits
    3 - Letters, digits, and special characters
    
    :param length: Length of the password
    :param complexity: Complexity level of the password
    :return: Generated password
    """
    if complexity < 1 or complexity > 3:
        raise ValueError("Complexity must be 1, 2, or 3")
    
    if length < 1:
        raise ValueError("Length must be greater than 0")

    characters = string.ascii_letters
    if complexity >= 2:
        characters += string.digits
    if complexity == 3:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        complexity = int(input("Enter the desired complexity level (1 - Letters, 2 - Letters and digits, 3 - Letters, digits, and special characters): "))
        
        password = generate_password(length, complexity)
        print(f"Generated password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
