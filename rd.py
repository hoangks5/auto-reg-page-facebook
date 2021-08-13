import random
ho = open('ho.txt',encoding="utf8")
ten = open('ten.txt',encoding="utf8")
a = ho.read().splitlines()
b = ten.read().splitlines()
def name():
    namep = random.choice(list(a)) +' '+ random.choice(list(b))
    return namep