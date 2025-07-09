import random
import string

CHARS = string.digits + string.ascii_letters

DIGITS = 8

PASSWORD = []
for i in range(DIGITS):
    j = random.choice(CHARS)
    PASSWORD.append(j)

print("초깃값ㅣ", PASSWORD)

def create_chromosome():
    chromosome = []
    for i in range(DIGITS):
        j = random.choice(CHARS)
        chromosome.append(j)

    return chromosome

def fitness(password):
    score = 0
    for i in range(0, len(password)):
        if password[i] == PASSWORD[i]:
            score += 1

    return score / len(password) * 100

def select(pw):
    a = sorted(pw, key=fitness, reverse=True)[:2]
    return a

temp = select(create_pws())
print(temp, fitness(temp[0]))