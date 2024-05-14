import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 예시 데이터 생성
data = {
    'REB': [82.3, 37.3, 18.7, 5.7, 1.7, 22.0, 49.6, 8.7, 34.2, 12.3, 78.7],
    'AST': [77.7, 32.7, 16.7, 4.0, 4.0, 18.0, 55.7, 10.0, 30.6, 11.7, 81.4],
    'STL': [77.2, 31.7, 16.4, 6.5, 2.2, 16.5, 51.0, 11.6, 32.4, 9.4, 74.4],
    '2P': [24.8, 22.0, 55.7, 18.0, 16.5, 51.5, 49.6, 6.7, 34.2, 12.3, 78.7],
    '2P%': [51.5, 49.6, 55.7, 18.0, 16.5, 51.5, 49.6, 6.7, 34.2, 12.3, 78.7],
    '3P': [10.9, 12.3, 30.6, 11.7, 9.4, 73.2, 78.7, 51.5, 49.6, 6.7, 34.2],
    '3P%': [73.2, 78.7, 30.6, 11.7, 9.4, 73.2, 78.7, 51.5, 49.6, 6.7, 34.2],
    'FT': [30.6, 34.2, 30.6, 34.2, 32.4, 10.9, 12.3, 81.4, 74.4, 51.5, 49.6],
    'FT%': [73.2, 78.7, 30.6, 34.2, 32.4, 10.9, 12.3, 81.4, 74.4, 51.5, 49.6],
    'HomeAway': [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],  # 홈(1) 어웨이(0)
    'WinStreak': [0, 2, 1, 0, 3, 0, 2, 0, 1, 0, 4],  # 연승 횟수
    'GoodMood': [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],  # 분위기 좋음(1) 나쁨(0)
    'PlayerInjury': [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],  # 결장 선수 있음(1) 없음(0)
    'Result': [85, 88, 92, 78, 79, 102, 97, 85, 93, 82, 105]  # 예시: 실제 득점
}

df = pd.DataFrame(data)

# 특성과 타겟 나누기
X = df.drop('Result', axis=1)
y = df['Result']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 특성 스케일링
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 선형 회귀 모델 초기화 및 훈련
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 테스트 데이터에 대한 예측
y_pred = model.predict(X_test_scaled)

# 회귀 모델의 성능 평가
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# 예측 결과 출력
print("Predicted Scores:", y_pred)

# 특성별 계수 확인
feature_coefficients = dict(zip(X.columns, model.coef_))
print("Feature Coefficients:", feature_coefficients)
