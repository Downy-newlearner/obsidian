## 모델 훈련할 때 필요한 것
1. 데이터
2. [[데이터셋 파일]]

3. [[모델 구성 파일]]

4. 하이퍼파라미터 파일

### 학습 시작

```
python train.py --batch-size 16 --epochs 100 --device 0 --name custom_training
```

| Option       | Change NV as Default | Privious Value                                      | New Value                                                                                         | Relative Path                  |
| ------------ | -------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------ |
| --data       | O                    | ../AI/dataset/dataset5.yaml                         | /Users/downy/Documents/2025_DKU_Capstone/2025_DKU_Capstone/AI/YOLOv7/data.yaml                    | ./data.yaml                    |
| --cfg        | O                    | /home/kimsy9587/yolov7/cfg/training/yolov7.yaml     | /Users/downy/Documents/2025_DKU_Capstone/2025_DKU_Capstone/AI/YOLOv7/cfg/training/yolov7.yaml     | ./cfg/training/yolov7.yaml     |
| --weights    | O                    | yolov7.pt                                           | /Users/downy/Documents/2025_DKU_Capstone/2025_DKU_Capstone/AI/YOLOv7/weights/yolov7-e6e.pt        | ./weights/yolov7-e6e.pt        |
| --batch-size | O                    | 16                                                  | 32                                                                                                |                                |
| --epochs     |                      | 100                                                 | 100                                                                                               |                                |
| --img-size   | O                    | 640 640                                             | 640 640                                                                                           |                                |
| --device     |                      | 0                                                   | 0                                                                                                 |                                |
| --name       |                      | custom_training                                     |                                                                                                   |                                |
| --hyp        | O                    | /home/kimsy9587/yolov7/data/hyp.scratch.custom.yaml | /Users/downy/Documents/2025_DKU_Capstone/2025_DKU_Capstone/AI/YOLOv7/data/hyp.scratch.custom.yaml | ./data/hyp.scratch.custom.yaml |
python train.py --batch-size 16 --epochs 100 --device 0 --name custom_training

### 옵션 설명

- `--data`: 데이터 설정 파일 경로
- `--cfg`: 모델 설정 파일 경로
- `--weights`: 초기 가중치 파일 경로 (사전 학습된 가중치 사용 가능)
- `--batch-size`: 배치 크기
- `--epochs`: 학습 반복 수
- `--img-size`: 입력 이미지 크기
- `--device`: 사용할 GPU
- `--name`: 세션 이름
- `--hyp`: 하이퍼파라미터 설정 파일 경로

학습이 완료되면 `weights` 디렉토리에 학습된 체크포인트(모델) 파일이 저장됩니다. `last.pt`는 최신 모델, `best.pt`는 최고의 모델일 것입니다.