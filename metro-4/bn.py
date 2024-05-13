import pandas as pd
df = pd.read_csv("./4.csv")
target_value = '별가람'

# '열차번호' 열에서 대상 값이 포함된 행을 추출합니다
filtered_df = df[df['열차번호'].isin([target_value])]
filtered_df = filtered_df.dropna(axis=1)


# (여기에 데이터프레임이나 데이터 입력 코드를 추가하세요.)

# 첫 번째 열을 제외한 나머지 열을 배열에 담기
train_times = filtered_df.iloc[:, 1:].values.flatten()

# print(train_times)


train_times = pd.Series(train_times).replace('24:', '00:', regex=True)

# 20231122 '20231122 ' 추가, 시간 변환
datetime_data = pd.to_datetime('20231122 ' + train_times, format='%Y%m%d %H:%M:%S')

# 입력한 시간
print("지하철 파업기간 시간표 정보 (진접 -> 오이도 방면 (하행))")
input_time = input("별가람역에 도착하는 시간을 입력해주세요 : ")
input_time += ':00'
    
# 주어진 데이터를 시리즈로 변환하고 datetime 형식으로 변환
datetime_data = pd.to_datetime('20231122 ' + pd.Series(train_times).replace('24:', '00:'), format='%Y%m%d %H:%M:%S')

# 입력한 시간을 datetime 형식으로 변환
input_datetime = pd.to_datetime('20231122 ' + input_time, format='%Y%m%d %H:%M:%S')

# 주어진 데이터 중에서 가장 가까운 시간 찾기
closest_time = datetime_data.iloc[(datetime_data - input_datetime).abs().idxmin()]
after_input_time = datetime_data[datetime_data > input_datetime].iloc[0]

data = ['05:33:30', '05:54:30', '06:11:00', '06:27:00', '06:41:00', '06:59:00',
 '07:19:00', '07:29:00', '07:35:30', '09:32:00', '07:47:00', '07:57:00',
 '08:06:00', '09:43:30', '08:13:30', '10:14:00', '08:26:00', '08:38:00',
 '08:44:00', '10:45:00', '09:08:00', '09:18:00', '11:15:00', '10:24:00',
 '10:56:30', '11:48:30', '12:09:00', '14:45:30', '13:03:00', '13:41:30',
 '14:01:00', '14:57:00', '15:39:00', '18:10:00', '16:28:00', '16:45:00',
 '17:34:00', '19:20:00', '18:24:00', '19:04:00', '20:01:00','20:33:00',
 '21:01:00', '21:31:00', '21:47:00', '22:19:00', '22:39:00', '23:22:00',
 '23:41:00', '24:03:30', '24:17:30', '24:34:30']


def split_time(time_str):
    return list(map(int, time_str.split(':')))

# 시간을 기준으로 정렬
sorted_train_times = sorted(data, key=split_time)


print("----시간표----")
print(*sorted_train_times,sep="\n")
print("입력한 시간:", input_datetime.time())

print("가장 근접 열차 시간:", closest_time)
print("입력 시간 이후 탑승 가능 열차 시간:", after_input_time)