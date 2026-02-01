from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
    rotation_range=40,             # 0~180도 회전
    width_shift_range=0.2,         # 너비 이동 범위
    height_shift_range=0.2,        # 높이 이동 범위
    rescale=1./255,                # 픽셀 값을 0~1로 변환
    shear_range=0.2,               # 시어링 변환
    zoom_range=0.2,                # 랜덤 줌
    horizontal_flip=True,          # 랜덤 수평 뒤집기
    fill_mode='nearest'            # 새로 생성된 픽셀 채우기
)

img = load_img('C:/Obsidian/obsidian/1. Projects/DeepLearning_Cloud/13장_keras_CNN_augmentation\dog_original.jpg')  # 이미지를 로드
x = img_to_array(img)              # 이미지를 배열로 변환
x = x.reshape((1,) + x.shape)      # 형태를 (1, 3, 331, 237)로 변경

# flow() 함수를 사용하여 랜덤 변환된 이미지 배치를 생성하고
# 결과를 'd:/data/aug/' 디렉토리에 저장
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir="C:/Obsidian/obsidian/1. Projects/DeepLearning_Cloud/13장_keras_CNN_augmentation/dog_augmentation/", save_prefix='dog', 
                          save_format='jpeg'):
    i += 1
    if i > 30:
        break                      # 무한 반복 방지
