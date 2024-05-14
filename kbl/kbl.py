import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
plt.rcParams['font.family'] = 'NanumGothic'

team_list = ["원주 DB", "서울 삼성", "서울 SK", "창원 LG", "고양 소노", "부산 KCC", "안양 정관장", "수원 KT", "대구 한국가스공사", "울산 현대모비스", "상무"]
print("=========홈팀 번호를 입력해주세요!!! ===========")
team_num = 0
for team in team_list: 
    print(f"{team} - {team_num}")
    team_num +=1
team1 = int(input())
print("=========원정팀 번호를 입력해주세요!!! ===========")
team_num = 0
for team in team_list: 
    print(f"{team} - {team_num}")
    team_num +=1
team2 = int(input())

url = "https://www.kbl.or.kr/game/compare-team"
driver = webdriver.Chrome()
driver.get(url)

select_element = driver.find_element(By.XPATH, '//ul[@class="filter-wrap"]/li[3]//select')

select = Select(select_element)
select.select_by_value(team_list[team1])

select_element = driver.find_element(By.XPATH, '//ul[@class="filter-wrap"]/li[4]//select')

select = Select(select_element)
select.select_by_value(team_list[team2])

time.sleep(2)


page_source = driver.page_source

# BeautifulSoup으로 파싱
soup = BeautifulSoup(page_source, 'html.parser')

# 하위 3번째 div에서 테이블 선택
table = soup.select('div.con-box:nth-of-type(3) table')[0]


rows = table.find_all('tr')
data = []

columnsTest = [th.text.strip() for th in rows[0].find_all('th')]
for row in rows[1:]:
    row_data = [td.text.strip() for td in row.find_all('td')]
    data.append(row_data)

print(data)
driver.quit()

select_team_1 = team_list[team1]
select_team_2 = team_list[team2]


# Pandas DataFrame 생성
columns = [f"{team_list[team1]} 시즌 평균", f"vs {team_list[team2]}", '기록', f"{team_list[team2]} 시즌 평균", f"vs {team_list[team1]}"]

df = pd.DataFrame(data, columns=columns)
df = df.iloc[1:].reset_index(drop=True)

print(df)
data = [row for row in data if row]

team_1_avg = []
team_2_avg = []
category = []
team_1_opt = []
team_2_opt = []
rank = 0

for value in data:
    team_1_avg.append(value[0])
    team_2_avg.append(value[3])
    data1 = float(value[0])*0.55 + float(value[1])*0.45
    data2 = float(value[3])*0.55 + float(value[4])*0.45
    team_1_opt.append(data1)
    team_2_opt.append(data2)
    category.append(value[2])
    if data1 > data2: rank +=1

team_1_info = [float(val) for val in team_1_avg]
team_2_info = [float(val) for val in team_2_avg]

new_data = {
    'Category': category,
    select_team_1 : team_1_info,
    select_team_2 : team_2_info,
}

opt_dat = {
    'Category' : category,
    select_team_1 : team_1_opt,
    select_team_2 : team_2_opt,
}

df = pd.DataFrame(new_data)
opt_df = pd.DataFrame(opt_dat)
print(df)
print(opt_df)

print(f"추천 언오버 기준점 : {(team_1_opt[0] + team_2_opt[0])*0.995}")
if rank > 5:print(f"{rank} : {select_team_1} 사이드 추천")
else: print(f"{rank} : {select_team_2} 사이드 추천")


df.set_index('Category').plot(kind='bar', stacked=False, figsize=[6, 6], fontsize=8)
plt.legend([select_team_1,select_team_2],fontsize=14)

opt_df.set_index('Category').plot(kind='bar', stacked=False, figsize=[6, 6], fontsize=8)
plt.legend([select_team_1,select_team_2],fontsize=14)
plt.xlabel("예측 결과 시각화")
plt.show()

# 추가요인
# 머신러닝 모델 찾기
# 영향을 주는 변수들
# 선수 결장 및 컨디션 여부 체크
