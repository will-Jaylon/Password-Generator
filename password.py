import random
import string

def generate_password(length, use_lower=True, use_upper=True, use_digits=True, use_special=True, restricted_chars=""):
    characters = ""

    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    characters = ''.join(char for char in characters if char not in restricted_chars)

    password = ''.join(random.choice(characters) for _ in range(length))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    try:
        length = int(input("\nEnter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        use_lower = input("Use lowercase letters? (yes/no): ").lower() == "yes"
        use_upper = input("Use uppercase letters? (yes/no): ").lower() == "yes"
        use_digits = input("Use numbers? (yes/no): ").lower() == "yes"
        use_special = input("Use special symbols? (yes/no): ").lower() == "yes"
        restricted_chars = input("\nEnter restricted characters (if any): ")

        password = generate_password(length, use_lower, use_upper, use_digits, use_special, restricted_chars="")
        print(f"\nGenerated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nPassword generation canceled.")