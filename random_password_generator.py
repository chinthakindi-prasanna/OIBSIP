import random
import string

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4 characters."
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

try:
    num = int(input("How many passwords do you want to generate? "))
    length = int(input("Enter the password length: "))

    for i in range(num):
        print(f"Password {i+1}: {generate_password(length)}")

except ValueError:
    print("⚠ Please enter valid numbers only.")