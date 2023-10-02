from random import randint


# Генерація паролю
def get_random_password():
    passw = ""
    for _ in range(8):
        rand_pass = randint(40, 126)
        passw += chr(rand_pass)
    return passw


print(get_random_password())


# перевірка пароля
def is_valid_password(password):
    if len(password) != 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False

    return True


print(is_valid_password(get_random_password()))
