import random
import string


def generate_email():
    username = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = "".join(random.choices(string.ascii_lowercase, k=6))
    return f"{username}@{domain}.com"


def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for i in range(length))
