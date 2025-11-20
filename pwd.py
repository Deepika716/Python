# password_generator.py

import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

print("Password Generator")
while True:
    size = int(input("Length of password: "))
    print("Generated:", generate_password(size))

    again = input("Generate another? (y/n): ")
    if again.lower() != "y":
        break
