import os
import json
from PIL import Image
import torchvision.transforms as transforms


# 이미지 flip 변환 설정 (좌우와 상하 flip 모두 설정)
def apply_flip(image, flip_type):
    if flip_type == 'horizontal':
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)  # 좌우 flip
    elif flip_type == 'vertical':
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)  # 상하 flip
    return flipped_image


# JSON 파일에서 이미지 파일과 레이블 정보 불러오기
def load_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data


# 좌표를 flip에 맞게 변환 (음수 방지 처리)
def update_points_for_flip(points, image_size, flip_type='horizontal'):
    width, height = image_size
    new_points = []

    for point in points:
        print(f"Original point: {point}")  # 원본 좌표 출력

        # 절대 좌표 (X, Y)만 있는 경우 처리 (예: [1043.913043478261, 214.78260869565227])
        if len(point) == 2:
            x_abs, y_abs = point  # 절대 좌표 (픽셀 값)

            # 좌표를 이미지 크기로 정규화 (0~1 사이 값으로 변환)
            x = x_abs / width
            y = y_abs / height

            if flip_type == 'horizontal':
                # X 좌표 반전
                new_x = 1.0 - x
                new_y = y  # Y 좌표는 그대로 유지
            elif flip_type == 'vertical':
                new_x = x  # X 좌표는 그대로 유지
                new_y = 1.0 - y  # Y 좌표 반전

            # 반전된 좌표를 다시 절대 좌표로 변환하여 저장
            new_x_abs = new_x * width
            new_y_abs = new_y * height

            # 음수 값이 발생하지 않도록 강제 제한
            new_points.append([max(0, new_x_abs), max(0, new_y_abs)])

        # YOLO 형식 (클래스 번호, 중심 X, 중심 Y, 너비, 높이)일 경우 처리
        elif len(point) == 5:
            class_id, center_x, center_y, obj_width, obj_height = point

            # 중심 좌표 반전, 너비와 높이는 변하지 않도록 유지
            if flip_type == 'horizontal':
                new_center_x = 1.0 - center_x  # X 좌표 반전
                new_center_y = center_y  # Y 좌표는 그대로 유지
            elif flip_type == 'vertical':
                new_center_x = center_x  # X 좌표는 그대로 유지
                new_center_y = 1.0 - center_y  # Y 좌표 반전

            # 너비와 높이는 변하지 않음
            new_width = obj_width
            new_height = obj_height

            # 음수 값이 발생하지 않도록 강제 제한
            new_points.append([class_id, max(0, new_center_x), max(0, new_center_y), new_width, new_height])

            # 중간 결과 로그 출력
            print(
                f"Transformed: class_id: {class_id}, new_center_x: {new_center_x}, new_center_y: {new_center_y}, width: {new_width}, height: {new_height}")

        else:
            # 좌표 포맷이 맞지 않는 경우 오류 출력 후 건너뛰기
            print(f"Error: Invalid point format {point}, skipping...")
            continue

    return new_points


# 이미지와 좌표를 처리하는 함수
def process_image_and_label(image_path, shapes, flip_type='horizontal'):
    image = Image.open(image_path)
    original_size = image.size

    # 지정된 flip을 적용
    flipped_image = apply_flip(image, flip_type)

    flipped_shapes = []
    for shape in shapes:
        flipped_points = update_points_for_flip(shape['points'], original_size, flip_type)
        flipped_shapes.append({
            'label': shape['label'],
            'points': flipped_points,
            'shape_type': shape['shape_type']
        })

    return flipped_image, flipped_shapes


# 디렉토리 내 모든 JSON 및 이미지 파일을 처리하는 함수 (horizontal + vertical 모두 수행)
def process_directory(json_dir, image_dir):
    json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

    for json_file in json_files:
        json_path = os.path.join(json_dir, json_file)
        data = load_json(json_path)  # JSON 데이터 로드

        # JSON 파일명에서 이미지 파일명 추출 (예: '3_000234.json' -> '3_000234.jpg')
        image_file = os.path.splitext(json_file)[0] + '.jpg'
        image_path = os.path.join(image_dir, image_file)

        if os.path.exists(image_path):
            # JSON의 shapes에서 좌표 정보 가져오기
            shapes = data['shapes']

            # 1. Horizontal Flip 처리
            flipped_image, flipped_shapes = process_image_and_label(image_path, shapes, flip_type='horizontal')
            flipped_image.save(os.path.join(image_dir, 'flipped_horizontal_' + image_file))  # horizontal flip 이미지 저장

            # flipped 좌표를 새로운 JSON 파일에 저장 (선택 사항)
            data['shapes'] = flipped_shapes
            flipped_json_path = os.path.join(json_dir, 'flipped_horizontal_' + json_file)
            with open(flipped_json_path, 'w') as f:
                json.dump(data, f, indent=4)

            # 2. Vertical Flip 처리
            flipped_image, flipped_shapes = process_image_and_label(image_path, shapes, flip_type='vertical')
            flipped_image.save(os.path.join(image_dir, 'flipped_vertical_' + image_file))  # vertical flip 이미지 저장

            # flipped 좌표를 새로운 JSON 파일에 저장 (선택 사항)
            data['shapes'] = flipped_shapes
            flipped_json_path = os.path.join(json_dir, 'flipped_vertical_' + json_file)
            with open(flipped_json_path, 'w') as f:
                json.dump(data, f, indent=4)

            print(f'Processed {image_file} with horizontal and vertical flips.')

        else:
            print(f'Image file {image_file} not found.')


# JSON 파일과 이미지 파일이 있는 디렉토리 경로
json_dir = '/home/kimsy9587/yolov7/CADP/28/json'
image_dir = '/home/kimsy9587/yolov7/CADP/28/raw_image'

# 디렉토리 내 모든 파일에 대해 증강 작업 수행 (horizontal + vertical)
process_directory(json_dir, image_dir)