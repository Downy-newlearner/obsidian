import numpy as np
import keras.backend as K
from keras.models import Sequential
from keras.layers import Conv2D, Activation, Dropout, Flatten, Dense, BatchNormalization, Reshape, UpSampling2D, LeakyReLU
from keras.optimizers import RMSprop, Adam
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array, array_to_img
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from tqdm import tqdm

# 세션 초기화
K.clear_session()

# 이미지 로드 및 전처리
img_path = r"C:\Obsidian\obsidian\1. Projects\DeepLearning_Cloud\강의 노트\15장_keras_GAN\prac1\input_images\Golden Retriever.jpeg"
img = image.load_img(img_path, target_size=(28, 28), color_mode='grayscale')  # 흑백 이미지로 변환
img_array = img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # 배치 차원 추가
Xtrain = img_array / 255.0  # 정규화
img_shape = (Xtrain.shape[1], Xtrain.shape[2], 1)

# 판별자 정의
discriminator = Sequential([
    Conv2D(64, kernel_size=(5, 5), strides=2, padding='same', input_shape=img_shape),
    LeakyReLU(alpha=0.2),
    Dropout(0.4),
    Conv2D(64, kernel_size=(5, 5), strides=2, padding='same'),
    LeakyReLU(alpha=0.2),
    Dropout(0.4),
    Conv2D(128, kernel_size=(5, 5), strides=2, padding='same'),
    LeakyReLU(alpha=0.2),
    Dropout(0.4),
    Flatten(),
    Dense(1, activation='sigmoid')
])
discriminator.compile(optimizer=Adam(learning_rate=0.0002), loss='binary_crossentropy', metrics=['accuracy'])

# 생성자 정의
gen_dense_size = (7, 7, 64)
generator = Sequential([
    Dense(np.prod(gen_dense_size), input_shape=(100,)),
    BatchNormalization(),
    Activation('relu'),
    Reshape(gen_dense_size),
    UpSampling2D(),
    Conv2D(128, kernel_size=5, padding='same'),
    BatchNormalization(momentum=0.9),
    Activation('relu'),
    UpSampling2D(),
    Conv2D(64, kernel_size=5, padding='same'),
    BatchNormalization(momentum=0.9),
    Activation('relu'),
    Conv2D(1, kernel_size=5, padding='same', activation='sigmoid')
])

# GAN 모델 정의 및 컴파일
discriminator.trainable = False
gan_model = Sequential([generator, discriminator])
gan_model.compile(optimizer=Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

# 조기 종료 콜백 정의
early_stopping = EarlyStopping(
    monitor='loss',  # 학습 손실 모니터링
    patience=10,     # 10 에폭 동안 개선이 없으면 중단
    restore_best_weights=True,  # 가장 좋은 가중치 복원
    verbose=1
)

# 학습 함수 정의
def train_discriminator(x_train, batch_size):
    valid = np.ones((batch_size, 1))
    fake = np.zeros((batch_size, 1))
    idx = np.random.randint(0, len(x_train), batch_size)
    true_imgs = x_train[idx]
    discriminator.train_on_batch(true_imgs, valid)  # 진짜 이미지 학습
    noise = np.random.normal(0, 1, (batch_size, 100))
    gen_imgs = generator.predict(noise)  # 가짜 이미지 생성
    discriminator.train_on_batch(gen_imgs, fake)  # 가짜 이미지 학습

def train_generator(batch_size):
    valid = np.ones((batch_size, 1))
    noise = np.random.normal(0, 1, (batch_size, 100))
    gan_model.fit(noise, valid, verbose=0, callbacks=[early_stopping])  # 조기 종료 추가

# 학습
epochs = 2000
batch_size = 64
for epoch in tqdm(range(epochs)):
    train_discriminator(Xtrain, batch_size)  # 판별자 학습
    train_generator(batch_size)  # 생성자 학습
    if early_stopping.stopped_epoch > 0:  # 조기 종료 확인
        print(f"Training stopped early at epoch {early_stopping.stopped_epoch}")
        break

# 결과 시각화
original = array_to_img(Xtrain[0])
plt.title("Original Image")
plt.imshow(original, cmap='gray')
plt.show()

random_noise = np.random.normal(0, 1, (1, 100))
gen_result = generator.predict(random_noise)
gen_img = array_to_img(gen_result[0])
plt.title("Generated Image")
plt.imshow(gen_img, cmap='gray')
plt.show()
