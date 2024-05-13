import random
import math
import matplotlib.pyplot as plt

attempt = 500000
glass_num, member = map(int, input("please input glass data and people data : ").split())
result = [0 for _ in range(member)] #0으로 초기화
mark_number = [i for i in range(1, member+1)] #matplotlib.pyplot에서 x축 정보를 list로 받기 때문
survival_sum = 0

def update_path(now):
    path[now] = random.randint(0,1)
    now+=1
    if(now==glass_num):return
    update_path(now)

def generate_bridge(num): 
    random_glass = random.randint(0,1)
    glass_bridge[num][0] = random_glass 
    glass_bridge[num][1] = abs(random_glass-1) 
    num+=1
    if(num == glass_num):return
    generate_bridge(num)

def simulation():
    check = 0
    generate_bridge(0)
    update_path(0)
    current_member = 0
    survival_index = -1 # not find
    while(current_member + 1 != member):
        for j in range(check, glass_num):
            check+=1
            select = path[j]
            if(glass_bridge[j][select] == 0):
                current_member+=1
                path[j]=abs(select-1)
                break
        if(check==glass_num):
            survival_index = current_member
            break
        else: update_path(check) 
    if (survival_index!=-1):
        for i in range(survival_index, member):result[i] += 1
    return member - survival_index #생존인원 반환

def calculate_mathematical_probability():
    total = 0
    case = []
    mathematical_result = []
    for i in range(glass_num):
        total += math.comb(glass_num, i)
        if(i<member):
            case.append(total)
    
    for i in range(member):
        mathematical_result.append(case[i]/total *100)
        print(i+1, "번째 선택자의 수학적 생존 확률 : " , format(case[i]/total *100, ".5f"), "%", sep="")       
    
    fig = plt.figure(figsize=(16, 8))
    ax = fig.add_subplot(1, 1, 1)
    bar = plt.bar(mark_number, mathematical_result, width=0.3, color="y")
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.4f' % height, ha='center', va='bottom', size = 12)
    plt.xlabel("participant number")
    plt.ylabel("survival probability(%)")
    ax.set_xticks(mark_number)
    plt.title("mathematical_result")
    plt.show()


def evaluate_result():
    avg_survival = survival_sum/attempt
    simulation_result = []
    print("시뮬레이션 횟수 :", attempt, "|" " 유리판 수 :", glass_num, "|" " 인원 수 :", member)
    print("번호 별 살아남은 횟수", result, sep="")
    print("평균 생존 인원 : ", format(avg_survival, ".4f"), "명", sep="")   
    for i in range(member):
        print(i+1,"번의 생존 확률 : ", format(result[i] / attempt *100, ".4f"), "%", sep="")
        simulation_result.append(result[i] / attempt *100)
    fig = plt.figure(figsize=(16, 8))
    ax = fig.add_subplot(1, 1, 1)
    bar = plt.bar(mark_number, simulation_result, width=0.3, color="r")
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.4f' % height, ha='center', va='bottom', size = 12)
    plt.xlabel("participant number")
    plt.ylabel("survival probability(%)")
    ax.set_xticks(mark_number)
    plt.title("simulation_result")
    plt.show()
    calculate_mathematical_probability()

for _ in range(attempt):
    glass_bridge = [[0,0]for _ in range(glass_num)]
    path = [0 for _ in range(glass_num)]
    survival_sum += simulation()

evaluate_result()