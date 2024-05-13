import numpy as np
from random import uniform
import pandas as pd
# import matplotlib.pyplot as plt
d = 1 #평행선 사이의 거리
l = 1 #바늘의 길이
k = 2
event = 0 #바늘이 선에 걸치는 사건횟수
long_case = l*k
long_data = []
long_expectation = 0
trial = 10000 #시행횟수
rad_data = []
length_data = []
for _ in range(trial): #몬테카를로 시뮬레이션 시행
    z = 0
    random_rad = uniform(0, np.pi) #0 ~ PI사이 랜덤 변수(theta)에 대한 N개의 무작위 샘플링
    random_length = uniform(0,d/2) #0 ~ D/2사이의 랜덤 변수(x)에 대한 N개의 무작위 샘플링
    rad_data.append(random_rad)
    length_data.append(random_length)
    if((long_case/2) * np.sin(random_rad)>=random_length):
        long_data.append((long_case/2) * np.sin(random_rad)*1)
    # else:long_data.append((long_case/2) * np.sin(random_rad)*(1-0.6366197723675814))
    if((l/2) * np.sin(random_rad)>=random_length):
        event+=1
long_expectation+=sum(long_data) / trial
print(long_expectation) 
    #1/2 * l * sin(theta) >= x이면 선과 걸침, 모델 
    # if((k/2) * np.sin(random_rad)>=random_length):B+=1
    
    
simulation_result = event/trial #몬테카를로 시뮬레이션을 통한 확률 계산(큰수의 법칙) 
mathematical_result = (2*l)/(d*np.pi) #뷔퐁의 바늘의 수학적 결과값
if(simulation_result>mathematical_result):accuracy = mathematical_result/simulation_result # 정확도 비교를 위한 부분
else:accuracy = simulation_result/mathematical_result
print("set length(l):", l, "set distance(d):", d)
print("시뮬레이션 시행 횟수: ", trial, "번", sep='')
# print("result of A :", A)
# print("시뮬레이션 결과 :", format(simulation_result, '.15f')) 
# print("수학적 분석 결과 : ", format(mathematical_result, '.15f'))
print("정확도 : ",accuracy*100, "%", sep='')
print("radian(x) min :", format(min(rad_data), '.15f'), "\nradian(x) max :" , format(max(rad_data), '.15f'))
print("length(l) min : ", format(min(length_data), '.15f'), "\nlength(l) max : ", format(max(length_data), '.15f'))
print("Probability : ", mathematical_result)
print("Np : ", k*mathematical_result)

# pd.set_option('float_format', '{:.10f}'.format)
# rad_data = pd.Series(rad_data)
# length_data = pd.Series(length_data)
# print("radian(x) data\n--------------------------\n",rad_data.describe(), "\n", sep='')
# print("length(l) data\n--------------------------\n" , length_data.describe(), sep='')
# print(2*N*l / (A*d)) #pi값 추정