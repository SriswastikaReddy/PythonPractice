class WeakPasswordException(Exception):
    pass


def check_password(password):

    if len(password) < 8:
        raise WeakPasswordException("Password must be at least 8 characters")

    if not any(c.isupper() for c in password):
        raise WeakPasswordException("Password must contain at least one uppercase letter")

    if not any(c.islower() for c in password):
        raise WeakPasswordException("Password must contain at least one lowercase letter")

    if not any(c.isdigit() for c in password):
        raise WeakPasswordException("Password must contain at least one digit")

    if not any(c in "!@#$%^&*" for c in password):
        raise WeakPasswordException("Password must contain at least one special character")

    return "Strong Password"


try:
    password = input("Enter password: ")
    print(check_password(password))

except WeakPasswordException as e:
    print("Error:", e)

