import secrets
import string

def generate_password(length):
    letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    main = ''.join(secrets.choice(letters) for i in range(length))
    digit = secrets.choice(digits)
    symbol = secrets.choice(symbols)

    return f"{main}{digit}{symbol}"

# print(generate_password(10))