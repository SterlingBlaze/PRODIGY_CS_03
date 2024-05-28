import string

def check_password_strength(password):
    # Define criteria for password strength
    length_criteria = 8
    uppercase_criteria = False
    lowercase_criteria = False
    number_criteria = False
    special_char_criteria = False

    # Check length
    if len(password) >= length_criteria:
        length_criteria_passed = True
    else:
        length_criteria_passed = False

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        uppercase_criteria = True

    # Check for lowercase letters
    if any(char.islower() for char in password):
        lowercase_criteria = True

    # Check for numbers
    if any(char.isdigit() for char in password):
        number_criteria = True

    # Check for special characters
    if any(char in string.punctuation for char in password):
        special_char_criteria = True

    # Calculate overall strength
    strength = 0
    if length_criteria_passed:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    return strength

def main():
    # Get password input from user
    password = input("Enter your password: ")

    # Check password strength
    strength = check_password_strength(password)

    # Provide feedback based on strength
    if strength == 5:
        print("Password is very strong!")
    elif strength >= 3:
        print("Password is strong.")
    elif strength >= 2:
        print("Password is moderate.")
    elif strength >= 1:
        print("Password is weak.")
    else:
        print("Password does not meet minimum criteria.")

if __name__ == "__main__":
    main()
