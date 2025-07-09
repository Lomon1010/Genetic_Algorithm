import random
import string

CHARS = string.digits + string.ascii_letters

DIGITS = 15
POPULATION = 100
MUTATION_RATE = 0.1
MAX_GENERATION = 100

PASSWORD = []

### 초기 비밀번호 만들기
for i in range(DIGITS):
    j = random.choice(CHARS)
    PASSWORD.append(j)

print("초깃값:", PASSWORD)

### 개체 생성
def create_chromosome():
    chromosome = []
    for i in range(DIGITS):
        j = random.choice(CHARS)
        chromosome.append(j)

    return chromosome

### 적합도 검사
def fitness(password):
    score = 0
    for i in range(0, len(password)):
        if password[i] == PASSWORD[i]:
            score += 1

    return score / len(password) * 100

### 상위 유전자 개체 2
def select(pw):
    a = sorted(pw, key=fitness, reverse=True)[:2]
    return a

### 유전자 선택
def cross(g1, g2):
    point = DIGITS // 2
    return g1[:point] + g2[point:], g2[:point] + g1[point:]

# 돌연변이
def mutate(chromosome, mutation_rate=MUTATION_RATE):
    new_gene = []
    for gene in chromosome:
        if random.random() > mutation_rate:
            new_gene.append(gene)
        else:
            new_gene.append(random.choice(CHARS))

    return new_gene

def genetic_algorithm():
    population = []
    for i in range(POPULATION):
        population.append(create_chromosome())
    generation = 0
    while generation < MAX_GENERATION:
        population = sorted(population, key=fitness, reverse=True)
        best = population[0]
        print(generation, "세대:", best, "점수:", fitness(best))

        if fitness(best) == 100:
            print("비밀번호를 찾았습니다! :", best)
            break

        parents = select(population)
        next_generation = []

        while len(next_generation) < POPULATION:
            child1, child2 = cross(parents[0], parents[1])
            next_generation.append(mutate(child1))
            if len(next_generation) < POPULATION:
                next_generation.append(mutate(child2))

        population = next_generation
        generation += 1

    print("정답:", population[0], "세대:", generation)

genetic_algorithm()