import random
def password_funciton(lenght=16):
    password = ''.join(random.choices('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*', k=lenght))
    return password

random_password = password_funciton()
print("Your random password is :", random_password)