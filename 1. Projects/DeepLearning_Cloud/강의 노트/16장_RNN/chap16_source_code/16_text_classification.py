import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = ['nice great best amazing', 
             'stop lies', 
             'pitiful nerd', 
             'excellent work', 
             'supreme quality', 
             'bad', 
             'highly respectable']

y_train = [1, 0, 0, 1, 1, 0, 1]   # 긍정 : 1, 부정 : 0

## 토큰화
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

breakpoint()

vocab_size = len(tokenizer.word_index) + 1 # 패딩을 고려하여 +1
print('단어 집합 :',vocab_size)

X_encoded = tokenizer.texts_to_sequences(sentences)
print('정수 인코딩 결과 :',X_encoded)

## 가장 긴 문장 찾기
max_len = max(len(l) for l in X_encoded)
print('최대 길이 :',max_len)

## 패딩 삽입
X_train = pad_sequences(X_encoded, maxlen=max_len, padding='post')
y_train = np.array(y_train)
print('패딩 결과 :')
print(X_train)

# Model 구성
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, Flatten

embedding_dim = 4

model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.fit(X_train, y_train, epochs=100, verbose=2)

result = model.predict(X_train)
print(result)
pred = [1 if i > 0.5 else 0 for i in result]
print(pred)

# breakpoint()

# 토큰화 -> 패딩 과정을 거쳐야한다.
# Test input
test_sentence = ["you are excellent"]

# Step 1: Tokenize the test sentence
test_encoded = tokenizer.texts_to_sequences(test_sentence)

# Step 2: Pad the sequence
test_padded = pad_sequences(test_encoded, maxlen=max_len, padding='post')

result2 = model.predict("you are excellent")
print(result2)
pred = [1 if i > 0.5 else 0 for i in result2]
print(pred)