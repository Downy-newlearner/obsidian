import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
import matplotlib.pyplot as plt
import wandb
from wandb.integration.keras import WandbMetricsLogger

# wandb 로그인 (API 키가 필요)
wandb.login()  # API 키가 환경 변수에 저장되어 있으면 자동 로그인

# wandb 초기화
wandb.init(
    project="DeepCl_LSTM_Prac2",  # 프로젝트 이름
    name="Dahun_241204",  # 실행 이름
    entity="jdh251425142514-dankook-university",  # 엔터티 이름
    sync_tensorboard=True  # TensorBoard 로그를 wandb로 동기화
)

# CSV 파일 경로
file_path = r"C:\Users\user\Downloads\archive\MSFT_2006-01-01_to_2018-01-01.csv"

# 데이터 로드
df = pd.read_csv(file_path)

# 날짜 열을 datetime 형식으로 변환
df['Date'] = pd.to_datetime(df['Date'])

# 데이터 정렬
df = df.sort_values('Date')

# 필요한 열 선택
df = df[['Date', 'Open', 'High', 'Low', 'Close']]

# 데이터 분리
train_df = df[df['Date'] <= '2017-06-30']
test_df = df[df['Date'] > '2017-06-30']

# 날짜 열 삭제 (모델 학습에 필요하지 않음)
train_df = train_df.drop(columns=['Date'])
test_df = test_df.drop(columns=['Date'])

# 데이터 정규화
scaler = MinMaxScaler()
train_scaled = scaler.fit_transform(train_df)
test_scaled = scaler.transform(test_df)

# 입력 시퀀스와 타겟 생성 함수
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(seq_length, len(data)):
        X.append(data[i-seq_length:i, :-1])  # 마지막 열(Close)을 제외한 입력 데이터
        y.append(data[i, -1])               # 마지막 열(Close)만 타겟으로 사용
    return np.array(X), np.array(y)

# 시퀀스 길이 설정 (30일)
sequence_length = 30

# 훈련 데이터 시퀀스 생성
X_train, y_train = create_sequences(train_scaled, sequence_length)

# 테스트 데이터 시퀀스 생성
X_test, y_test = create_sequences(test_scaled, sequence_length)

# wandb 데이터셋 로깅
wandb.config.update({
    "sequence_length": sequence_length,
    "train_data_points": len(X_train),
    "test_data_points": len(X_test),
})

# LSTM 모델 구성
model = Sequential()
model.add(LSTM(units=50, return_sequences=False, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')

# 모델 요약 출력
model.summary()

# 모델 학습
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.1,
    verbose=1,
    callbacks=[WandbMetricsLogger()]
)

# 예측
y_pred = model.predict(X_test)

# 예측값 역변환 (스케일링 복원)
test_scaled_df = pd.DataFrame(test_scaled, columns=['Open', 'High', 'Low', 'Close'])
y_test_actual = scaler.inverse_transform(np.hstack((test_scaled_df.iloc[sequence_length:, :-1], y_test.reshape(-1, 1))))[:, -1]
y_pred_actual = scaler.inverse_transform(np.hstack((test_scaled_df.iloc[sequence_length:, :-1], y_pred)))[:, -1]

# wandb 예측 결과 로깅
wandb.log({"Test RMSE": np.sqrt(np.mean((y_test_actual - y_pred_actual)**2))})

# 결과 시각화
plt.figure(figsize=(10, 6))
plt.plot(y_test_actual, label='Actual')
plt.plot(y_pred_actual, label='Predicted')
plt.title('Actual vs Predicted Close Prices')
plt.legend()
plt.show()

# wandb 로그 종료
wandb.finish()
