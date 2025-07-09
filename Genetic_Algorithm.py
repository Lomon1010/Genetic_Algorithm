import random
import string

CHARS = string.digits + string.ascii_letters # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

DIGITS = 15 # 몇 자리 비밀번호
POPULATION = 100 # 군집의 개체 수
MUTATION_RATE = 0.1 # 유전자별 돌연변이 확률
MAX_GENERATION = 100 # 세대를 거듭하게 될텐데, 이 세대의 한계

### 개체 생성 함수
def create_chromosome():
    chromosome = []
    for i in range(DIGITS):
        j = random.choice(CHARS) # CHARS에서 랜덤으로 하나 뽑기 * 비밀번호 자릿수
        chromosome.append(j)

    return chromosome

### 초기 비밀번호 세팅
PASSWORD = create_chromosome() # 개체 생성 함수 이용
print("초깃값:", PASSWORD, "\n")

### 적합도 검사
def fitness(password):
    score = 0
    for i in range(0, len(password)): # 어떤 임의의 비밀번호의 앞에서부터 쭉 훑음
        if password[i] == PASSWORD[i]: # 그 자리의 비밀번호가 동일하다면 +1점
            score += 1
        '''
        # 여기서부터는 적합도 함수의 응용
        else:
            if password[i] in PASSWORD: # 만일 해당 자리의 비밀번호가 틀렸지만 다른 위치에 존재할 때
                score += 0.5 # 0.5점 가산점
        '''

    return score / len(password) * 100 # 총점 = 점수 / 길이 * 100, (ex) 4개가 동일 = 4점, 가능한 최대 점수 = 8점 따라서 4/8*100 = 50점 

### 상위 유전자 개체 2
def select(pw):
    a = sorted(pw, key=fitness, reverse=True)[:2] # 적합도 함수 점수를 바탕으로 만든 정렬기준을 통해 내림차 순으로 정리 후, 상위 2개 반환
    return a

### 유전자 선택
def cross(g1, g2): 
    point = DIGITS // 2 # 반띵
    return g1[:point] + g2[point:], g2[:point] + g1[point:] # 반띵한거 갈아끼우기 (케이스 2개겠죠? 예를 들면 AB BA)

# 돌연변이
def mutate(chromosome, mutation_rate=MUTATION_RATE):
    new_gene = [] # 돌연변이를 통해 바뀔 새 유전자 틀 생성
    for gene in chromosome:
        if random.random() > mutation_rate: # 돌연변이율이 아닌 경우
            new_gene.append(gene) # 해당 유전자 그대로 사용
        else:
            new_gene.append(random.choice(CHARS)) # 아니면 그냥 해당 유전자 새로운 걸로(랜덤) 갈아끼움

    return new_gene

def genetic_algorithm(): # 메인 함수
    population = []
    for i in range(POPULATION): # 개체 군집 생성
        population.append(create_chromosome())
        
    generation = 0 # 세대 수 생성
    while generation < MAX_GENERATION: # 제일 처음에 정한 세대 수 한계의 전까지
        population = sorted(population, key=fitness, reverse=True) # 군집 = 적합도 함수 점수 바탕으로 오름차순 정리
        best = population[0] # 이를 바탕으로 한 최상의 개체(점수 최고점)
        print(generation, "세대:", best, "점수:", fitness(best)) # 알려주기 (진행 상황 알리기 위함)

        if fitness(best) == 100: # 점수가 100점이면
            print("비밀번호를 찾았습니다! :", best) # 찾은거임
            break # 찾았으니 끝. 반복문 탈출 해야함

        parents = select(population) # 탈출하지 못했으면 = 100점 안 나왔으면 부모 개체 정하기
        next_generation = [] # 자식 개체 틀

        while len(next_generation) < POPULATION: # 군집 개체 수 될때까지
            child1, child2 = cross(parents[0], parents[1]) # 교배
            next_generation.append(mutate(child1)) # 첫째 돌연변이 일으키고 추가
            if len(next_generation) < POPULATION: # 그래도 안 되면
                next_generation.append(mutate(child2)) # 둘째 돌연변이 일으키고 추가

        population = next_generation # 세대 갈아버리기 
        generation += 1 # 다음 스텝
    print("정답:", population[0], "세대:", generation) # 위의 작업이 끝나면 정답 말하기

genetic_algorithm() # 실행
