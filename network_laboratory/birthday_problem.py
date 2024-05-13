import random
NUM = 70

def find_simulation_result():
    birthday_check = [False for _ in range (366)]
    for _ in range(NUM):
        random_birthday = random.randint(1,365)
        if(birthday_check[random_birthday] == False):birthday_check[random_birthday] = True
        else:return 1
    return 0

def find_math_result():
    complement = 1
    for i in range(NUM):
        complement *= (365-i)/365
    return 1 - complement

def main():
    trial = 50000
    match = 0
    for _ in range(trial):
        match += find_simulation_result()
    print(NUM, "명이 모였을 때 생일이 같은 사람이 한 명이라도 존재 할 확률", sep="")
    print("시뮬레이션 결과 : ", format(match/trial * 100, ".4f"), "%", sep="")
    mathmatical_result = find_math_result()     
    print("수학적 결과 : ", format(mathmatical_result * 100, ".4f"), "%", sep="")

main()