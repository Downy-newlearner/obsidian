import numpy as np
import keras.backend as K
from keras.models import Sequential
from keras.layers import Conv2D, Activation, Dropout, Flatten, Dense, BatchNormalization, Reshape, UpSampling2D, LeakyReLU
from keras.optimizers import RMSprop
from keras.preprocessing import image
from keras.preprocessing.image import array_to_img
from skimage import color
import matplotlib.pyplot as plt
from tqdm import tqdm

K.clear_session()

# 이미지 로드 및 전처리
img_path = r"C:\Obsidian\obsidian\1. Projects\DeepLearning_Cloud\강의 노트\15장_keras_GAN\prac1\input_images\Golden Retriever.jpeg"
img = image.load_img(img_path, target_size=(28, 28))
img = color.rgb2gray(image.img_to_array(img))
img = np.expand_dims(img, axis=0)
Xtrain = img / 255
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
discriminator.compile(optimizer=RMSprop(learning_rate=0.0008), loss='binary_crossentropy', metrics=['accuracy'])

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
gan_model.compile(optimizer=RMSprop(learning_rate=0.0004), loss='binary_crossentropy', metrics=['accuracy'])

# 학습 함수
def train_discriminator(x_train, batch_size):
    valid = np.ones((batch_size, 1))
    fake = np.zeros((batch_size, 1))
    idx = np.random.randint(0, len(x_train), batch_size)
    true_imgs = x_train[idx]
    discriminator.train_on_batch(true_imgs, valid)
    noise = np.random.normal(0, 1, (batch_size, 100))
    gen_imgs = generator.predict(noise)
    discriminator.train_on_batch(gen_imgs, fake)

def train_generator(batch_size):
    valid = np.ones((batch_size, 1))
    noise = np.random.normal(0, 1, (batch_size, 100))
    gan_model.train_on_batch(noise, valid)

# 학습
epochs = 20000
batch_size = 64
for epoch in tqdm(range(epochs)):
    train_discriminator(Xtrain, batch_size)
    train_generator(batch_size)

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
