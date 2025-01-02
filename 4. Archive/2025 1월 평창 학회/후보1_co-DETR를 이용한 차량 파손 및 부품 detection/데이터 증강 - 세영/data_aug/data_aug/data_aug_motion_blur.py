import os
import cv2
import numpy as np
from PIL import Image

# 모션 블러를 추가하는 함수
def add_motion_blur(image, kernel_size=15):
    """
    이미지에 모션 블러를 추가하는 함수
    :param image: 원본 이미지 (PIL Image 또는 numpy 배열)
    :param kernel_size: 모션 블러의 커널 크기 (크면 블러 효과가 더 강해짐)
    :return: 모션 블러가 추가된 이미지 (PIL Image)
    """
    # PIL 이미지를 numpy 배열로 변환 (만약 image가 PIL일 경우)
    if isinstance(image, Image.Image):
        image = np.array(image)

    # 모션 블러 커널 생성 (직선 방향으로 블러 효과를 만들기 위함)
    kernel = np.zeros((kernel_size, kernel_size))
    kernel[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
    kernel = kernel / kernel_size

    # 필터를 적용하여 모션 블러 추가
    blurred_image = cv2.filter2D(image, -1, kernel)

    # 결과를 다시 PIL 이미지로 변환
    return Image.fromarray(blurred_image)

# 이미지 파일에서 모션 블러를 추가하고 저장하는 함수
def apply_motion_blur_to_images(input_dir, output_dir, kernel_size=30):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.png'))]

    for image_file in image_files:
        image_path = os.path.join(input_dir, image_file)
        image = Image.open(image_path)

        # 모션 블러 추가
        blurred_image = add_motion_blur(image, kernel_size=kernel_size)

        # 출력 경로에 저장
        blurred_image_path = os.path.join(output_dir, f'blurred_{image_file}')
        blurred_image.save(blurred_image_path)

        print(f"Added motion blur to {image_file}, saved to {blurred_image_path}")


# 이미지 파일 경로 설정
input_dir = '/home/kimsy9587/yolov7/CADP/Szh/raw_image'  # 원본 이미지 폴더 경로
output_dir = '/home/kimsy9587/yolov7/CADP/Szh/image'  # 모션 블러 추가된 이미지 저장 경로

# 모션 블러 추가 수행
apply_motion_blur_to_images(input_dir, output_dir, kernel_size=30)
