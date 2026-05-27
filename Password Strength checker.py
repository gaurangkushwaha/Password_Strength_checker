def is_strong_password(password):
    """This function checks whether the password is strong or not"""

    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char in '!@#$%^&*()_+' for char in password):
        return False

    return True


# Taking input from user
password = input("Enter your password: ")

# Checking password strength
if is_strong_password(password):
    print("Strong Password")
else:
    print("Weak Password")