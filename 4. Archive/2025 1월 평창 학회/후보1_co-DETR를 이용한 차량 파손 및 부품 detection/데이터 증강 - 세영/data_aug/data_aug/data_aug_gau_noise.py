import os
import numpy as np
from PIL import Image

# Gaussian 노이즈를 추가하는 함수
def add_gaussian_noise(image, mean=0, std=50):
    """
    이미지에 Gaussian 노이즈를 추가하는 함수
    :param image: 원본 이미지 (PIL Image)
    :param mean: 노이즈의 평균
    :param std: 노이즈의 표준 편차
    :return: 노이즈가 추가된 이미지 (PIL Image)
    """
    # 이미지를 numpy 배열로 변환
    image_array = np.array(image)

    # Gaussian 노이즈 생성
    noise = np.random.normal(mean, std, image_array.shape)

    # 노이즈를 원본 이미지에 추가
    noisy_image = image_array + noise

    # 픽셀 값을 0~255 범위로 클리핑
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

    # 다시 PIL 이미지로 변환
    noisy_image_pil = Image.fromarray(noisy_image)

    return noisy_image_pil


# 이미지 파일에서 Gaussian 노이즈를 추가하고 저장하는 함수
def apply_gaussian_noise_to_images(input_dir, output_dir, mean=0, std=50):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.png'))]

    for image_file in image_files:
        image_path = os.path.join(input_dir, image_file)
        image = Image.open(image_path)

        # Gaussian 노이즈 추가
        noisy_image = add_gaussian_noise(image, mean, std)

        # 출력 경로에 저장
        noisy_image_path = os.path.join(output_dir, f'noisy_{image_file}')
        noisy_image.save(noisy_image_path)

        print(f"Added Gaussian noise to {image_file}, saved to {noisy_image_path}")


# 이미지 파일 경로 설정
input_dir = '/home/kimsy9587/yolov7/CADP/Szh/raw_image'  # 원본 이미지 폴더 경로
output_dir = '/home/kimsy9587/yolov7/CADP/Szh/image'  # 노이즈가 추가된 이미지 저장 경로

# Gaussian 노이즈 추가 수행
apply_gaussian_noise_to_images(input_dir, output_dir, mean=0, std=50)