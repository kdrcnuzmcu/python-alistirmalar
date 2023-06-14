import random
from faker import Faker

def CumledenParola():
    from random import choice
    from faker import Faker
    fake = Faker()
    text = fake.text(30)
    Capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Lowers = "abcdefghijklmnopqrstuvwxyz"
    Numbers = "1234567890"
    Symbols = "+-*/!?-_()%&.,"
    text_list = list(text)
    for i, j in enumerate(text_list):
        x = random.choice([Capitals, Lowers, Numbers, Symbols])

    modified_text = ''.join(text_list)
    print(text)
    print(modified_text)

CumledenParola()

"""
Capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lowers = "abcdefghijklmnopqrstuvwxyz"
Numbers = "1234567890"
Symbols = "+-*/!?-_()%&.,"

def ParolaOlustur(uzunluk):
    parola = ""
    for i in range(int(uzunluk)):
        x = random.randint(1, 4)
        if x == 1:
            parola += random.choice(hL)
        elif x == 2:
            parola += random.choice(lL)
        elif x == 3:
            parola += random.choice(n)
        elif x == 4:
            parola += random.choice(s)
    return parola

print("Parolanız:", ParolaOlustur(12))
"""