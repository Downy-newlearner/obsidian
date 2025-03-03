# CUDA 환경 확인 및 설정
import tensorflow as tf
from tensorflow.keras.mixed_precision import set_global_policy

# GPU 확인
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"GPUs Available: {len(gpus)}")
    for gpu in gpus:
        print(f" - {gpu.name}")
else:
    print("No GPU available. Using CPU.")

# 혼합 정밀도 설정 (optional, NVIDIA RTX 이후 GPU에서 사용 권장)
set_global_policy('mixed_float16')

# 기본 코드 시작
import numpy as np
import keras.backend as K
from keras.models import Sequential
from keras.layers import Conv2D, Activation, Dropout, Flatten, Dense, BatchNormalization, Reshape, UpSampling2D, LeakyReLU 
from keras.optimizers import RMSprop
from keras.preprocessing.image import array_to_img

import warnings 
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
from tqdm import tqdm                      # progress bar

K.clear_session()

# load MNIST dataset
from keras.datasets import mnist

(X_train, _), (_, _) = mnist.load_data()  # 라벨 불필요하므로 _ 처리
X_train = X_train / 255.0  # 정규화 (픽셀 값 0~1로 변환)
X_train = np.expand_dims(X_train, axis=-1)  # (28, 28, 1)로 변환

Xtrain = X_train  # 코드에서 사용하기 위한 데이터 변수 설정

# 입력 이미지의 shape (28, 28, 1)
img_shape = (X_train.shape[1], X_train.shape[2], X_train.shape[3])

# 판별자 만들기 ###############################################
discriminator = Sequential()
discriminator.add(Conv2D(64, kernel_size=(5, 5), 
                        input_shape=img_shape, 
                        strides=2, padding='same', 
                        activation=LeakyReLU(alpha=0.2)))
discriminator.add(Dropout(rate=0.4))
discriminator.add(Conv2D(64, kernel_size=(5, 5), 
                        strides=2, padding='same', 
                        activation=LeakyReLU(alpha=0.2)))
discriminator.add(Dropout(rate=0.4))
discriminator.add(Conv2D(128, kernel_size=(5, 5), 
                        strides=2, padding='same', 
                        activation=LeakyReLU(alpha=0.2)))
discriminator.add(Dropout(rate=0.4))
discriminator.add(Flatten())
discriminator.add(Dense(units=1, activation='sigmoid'))

discriminator.summary()

# 생성자 만들기 #######################################
gen_dense_size=(7, 7, 64)

generator = Sequential()
generator.add(Dense(units=np.prod(gen_dense_size), input_shape=(100,)))
generator.add(BatchNormalization())
generator.add(Activation('relu'))
generator.add(Reshape(gen_dense_size))

generator.add(UpSampling2D())
generator.add(Conv2D(filters=128, kernel_size=5, padding='same', strides=1))
generator.add(BatchNormalization(momentum=0.9))
generator.add(Activation('relu'))

generator.add(UpSampling2D())
generator.add(Conv2D(filters=64, kernel_size=5, padding='same', strides=1))
generator.add(BatchNormalization(momentum=0.9))
generator.add(Activation('relu'))

generator.add(Conv2D(filters=64, kernel_size=5, padding='same', strides=1))
generator.add(BatchNormalization(momentum=0.9))
generator.add(Activation('relu'))

generator.add(Conv2D(filters=1, kernel_size=5, padding='same', strides=1))
generator.add(Activation('sigmoid'))

generator.summary()

# compile #####################################
# 혼합 정밀도 학습을 위한 optimizer 설정
discriminator.compile(optimizer=RMSprop(learning_rate=0.0008), loss='binary_crossentropy', metrics=['accuracy'])

model = Sequential()
model.add(generator)
model.add(discriminator)

model.compile(optimizer=RMSprop(learning_rate=0.0004), loss='binary_crossentropy', metrics=['accuracy'])

# learning
def train_discriminator(x_train, batch_size):
    valid = np.ones((batch_size, 1))
    fake = np.zeros((batch_size, 1))
    
    idx = np.random.randint(0, len(x_train), batch_size)
    true_imgs = x_train[idx]
    discriminator.fit(true_imgs, valid, verbose=0)
    
    noise = np.random.normal(0, 1, (batch_size, 100))
    gen_imgs = generator.predict(noise)
    
    discriminator.fit(gen_imgs, fake, verbose=0)
    
def train_generator(batch_size):
    valid = np.ones((batch_size, 1))
    noise = np.random.normal(0, 1, (batch_size, 100))
    model.fit(noise, valid, verbose=1)

for epoch in tqdm(range(2000)):  # Try 2000 
    train_discriminator(Xtrain, 128)  # 배치 크기를 늘림
    train_generator(128)

# 결과물 확인
original = array_to_img(Xtrain[0])
plt.imshow(original, cmap='gray')
plt.show()

np.random.seed(123)
random_noise = np.random.normal(0, 1, (1, 100))
gen_result = generator.predict(random_noise)
gen_img = array_to_img(gen_result[1])
plt.imshow(gen_img, cmap='gray')
plt.show()
