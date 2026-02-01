import os
import json
from PIL import Image
import shutil

# 이미지 grayscale 변환 설정
def apply_grayscale(image):
    return image.convert('L')  # 이미지 grayscale 변환

# JSON 파일에서 데이터 불러오기 (shapes 정보 필요 없음)
def load_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

# 이미지 처리 함수 (grayscale 변환)
def process_image_and_label(image_path, json_path, output_image_dir, output_json_dir):
    # 이미지 변환
    image = Image.open(image_path)
    grayscale_image = apply_grayscale(image)

    # 이미지 저장
    output_image_path = os.path.join(output_image_dir, 'grayscale_' + os.path.basename(image_path))
    grayscale_image.save(output_image_path)

    # JSON 파일 복사 (같은 이름으로 저장)
    output_json_path = os.path.join(output_json_dir, 'grayscale_' + os.path.basename(json_path))
    shutil.copyfile(json_path, output_json_path)

    return output_image_path, output_json_path

# 디렉토리 내 모든 JSON 및 이미지 파일을 처리하는 함수 (grayscale 적용)
def process_directory(json_dir, image_dir, output_image_dir, output_json_dir):
    if not os.path.exists(output_image_dir):
        os.makedirs(output_image_dir)
    if not os.path.exists(output_json_dir):
        os.makedirs(output_json_dir)

    json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

    for json_file in json_files:
        json_path = os.path.join(json_dir, json_file)
        image_file = os.path.splitext(json_file)[0] + '.jpg'
        image_path = os.path.join(image_dir, image_file)

        if os.path.exists(image_path):
            # Grayscale 처리 및 파일 저장
            output_image_path, output_json_path = process_image_and_label(image_path, json_path, output_image_dir, output_json_dir)
            print(f'Processed {image_file} with grayscale. Saved image to {output_image_path} and JSON to {output_json_path}.')
        else:
            print(f'Image file {image_file} not found, skipping.')

# JSON 파일과 이미지 파일이 있는 디렉토리 경로
json_dir = '/home/kimsy9587/yolov7/CADP/Szh/json'
image_dir = '/home/kimsy9587/yolov7/CADP/Szh/raw_image'
output_image_dir = '/home/kimsy9587/yolov7/CADP/Szh/image'  # grayscale 이미지 저장 경로
output_json_dir = '/home/kimsy9587/yolov7/CADP/Szh/j'    # grayscale에 맞춘 JSON 파일 저장 경로

# 디렉토리 내 모든 파일에 대해 증강 작업 수행 (grayscale)
process_directory(json_dir, image_dir, output_image_dir, output_json_dir)
