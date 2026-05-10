import random
import string

# num = random.choice(ascii(),k = 3)
def accountNumberGenerator():
    num = random.choices(string.digits,k=2)
    low_alpha = random.choices(string.ascii_lowercase,k=3)
    upper_alpha = random.choices(string.ascii_uppercase,k=3)
    sepChar = random.choices("!@#$%^&*",k=1)

    accountNumber = random.shuffle(num+low_alpha+upper_alpha+sepChar)
    return "".join(accountNumber)

print(accountNumberGenerator())