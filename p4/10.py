from random import randint


def get_random_password():
    passw = ""
    for _ in range(8):
        rand_pass = randint(40, 126)
        passw += chr(rand_pass)
    return passw


print(get_random_password())
