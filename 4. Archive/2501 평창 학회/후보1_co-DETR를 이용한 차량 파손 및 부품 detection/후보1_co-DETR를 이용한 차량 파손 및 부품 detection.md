jdh251425@220.149.231.136:9004
[[Co-Deformable-DETR]]

## 환경
python 3.7.1
pip install torch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 --index-url https://download.pytorch.org/whl/cu113

## 실행 코드
python tools/train_wandb.py projects/configs/co_deformable_detr/co_deformable_detr_r50_1x_coco.py --work-dir path_to_exp --hyperparams projects/configs/hyperparams/default_hyperparams.yaml


nohup bash tools/dist_train.sh projects/configs/co_deformable_detr/co_deformable_detr_r50_1x_coco.py 4 path_to_exp > nohup_241230.out &


## 해야할 것
1. 데이터 증강
2. VGGNET모델과 성능 비교
3. 논문 작성
4. co-Deformable-DETR 아키텍처 그리기(ppt)

좋아 코드 짜줘.

모델: VGG19

train_dataset root: /home/jdh251425/co-deformable-detr/data/coco/train2017

train_dataset annFile: /home/jdh251425/co-deformable-detr/data/coco/annotations/instances_train17.json

batch_size = 60

Pretrained = True

손실함수

## 논문 주제
- co-DETR를 이용한 차량 파손 및 부품 detection(vs YOLOv4, VGG16) 
	- [[YOLOv4를 이용한 차량파손 검출 모델 개선]]

## 데이터
### 1. 데이터
- https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=581 (기각: Segmentation 데이터임)

- https://github.com/jennyluciav/car-damage-dataset (논문에서 사용한 github 데이터) -> 전처리 필요
	- 라벨링이 안되어있음

- https://universe.roboflow.com/car-damage-kadad (Detection 데이터셋)

### 2. 데이터 규모
DETR이 학습 데이터를 얼마나 필요로 하는지 DETR논문 확인해보기


### 3. 클래스 통일
각 데이터들의 라벨의 클래스들을 통일시켜야함



## 모델
### 1. 체크리스트
- github 코드 공개 여부
- 파라미터 수 (현재 리소스에서 실행 및 저장 가능한지)
- 입출력 구조 (디버깅하면서 텐서 단위로 확인 추천)
- 사전학습 가중치 (pretrained weight): huggingface에 공개된 것을 사용하는지, 아니라면 github에 공개 돼 있는지





### 2. 알고리즘 적용하기


### 3. DETR vs YOLO vs Co-Deformable-DETR
1. *YOLO 모델과 비교해 Co-Deformable-DETR의 장점*

Co-Deformable-DETR은 YOLO 모델보다 객체 간의 관계를 고려한 정밀한 검출이 가능하다는 점에서 우위를 가진다. YOLO는 주로 격자 기반의 전역적 처리를 통해 빠른 속도와 경량화를 목표로 하지만, Co-Deformable-DETR은 변형 가능한(deformable) Attention 메커니즘을 활용하여 특정 객체 주변의 중요한 특징들만 집중적으로 학습한다. 이를 통해 복잡한 장면에서의 객체 검출 성능과 정확도가 향상되며, 특히 물체 간의 상호작용이나 혼잡한 환경에서도 보다 정확한 검출이 가능하다.

---

2. *DETR 모델과 비교해 Co-Deformable-DETR의 장점*

Co-Deformable-DETR은 DETR 대비 연산 효율성이 뛰어나고 수렴 속도가 빠르다는 강점을 가진다. DETR은 모든 픽셀에 대해 전역적인 주의(attention)를 계산하므로 학습 과정이 느리고 고해상도 이미지 처리 시 메모리 사용량이 높다. 반면, Co-Deformable-DETR은 변형 가능한 주의 메커니즘을 통해 관심 영역만을 선택적으로 처리함으로써 연산량을 크게 줄이고, 학습 효율성을 극대화한다. 이를 통해 더 짧은 학습 시간으로도 DETR과 비슷하거나 더 나은 성능을 달성할 수 있다.


### 4. Co-Deformable-DETR의 Architecture

Deformable Attention

## 실험
- 백그라운드에서 실행하기 - nohup
https://joonyon.tistory.com/entry/%EC%89%BD%EA%B2%8C-%EC%84%A4%EB%AA%85%ED%95%9C-nohup-%EA%B3%BC-%EB%B0%B1%EA%B7%B8%EB%9D%BC%EC%9A%B4%EB%93%9C-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%82%AC%EC%9A%A9%EB%B2%95
	- nohup bash tools/dist_train.sh projects/configs/co_deformable_detr/co_deformable_detr_r50_1x_coco.py 4 path_to_exp > nohup_241230.out

- 체크포인트 모델 저장 장소
	- /home/jdh251425/co-deformable-detr/path_to_exp by HardDiskBackend.

실험 과정을 확인하고싶으면 같은 디렉토리에 저장되는 로그를 열어 확인하면 된다.

전이학습 할 때 gradient freezing해야하는 곳을 판별해서 잘 freezing하기


- 학습시간: batch가 커지면 좀 더 빨라지긴 하지만, 어차피 데이터 자체가 많으면 1회 학습 당 걸리는 시간이 늘어남. 학습데이터수-모델용량-배치를 현재 리소스에 맞게 잘 조절해서 학습
- 메모리(중요!! ram, vram 모두해당): 모델과 데이터(1 batch)가 모두 로드 가능한 정도의 용량이 확보되어야 함. 학습 과정에서 vram 사용량이 점점 증가하는 경우가 있으므로 여유를 두고 학습하는 것 추천
- 코드 디버깅(중요!!): 학습은 시간이 오래걸리는 작업이므로 돌려두고 기다려야하는데, 학습 마지막단계(ex. best 파라미터 저장. metric 저장, validation)에서 오류가 나면 골치아파질 수도 있음. 처음부터 꼼꼼히 디버깅 하기.
	- 추천: 학습 1 iteration 디버깅 -> (train코드 주석 후)validation 디버깅 -> (train, validation 주석 후)모델 save 코드 디버깅


## co-DETR란?
- DETRs with Collaborative Hybrid Assignments Training

## 모델
- github 코드 공개 여부
- 파라미터 수 (현재 리소스에서 실행 및 저장 가능한지)
- 입출력 구조 (디버깅하면서 텐서 단위로 확인 추천)
- 사전학습 가중치 (pretrained weight): huggingface에 공개된 것을 사용하는지, 아니라면 github에 공개 돼 있는지

co-DETR vs YOLOv7

- co-DETR을 사용하고자 한 이유
	- DETR은 큰 Object에 대한 Detection 성능이 우수한데, 데이터 특성 상 큰 Object가 많아서 적합한 모델이라고 생각한다.
	- co-DETR은 DETR보다 

## 실험

- 학습시간: batch가 커지면 좀 더 빨라지긴 하지만, 어차피 데이터 자체가 많으면 1회 학습 당 걸리는 시간이 늘어남. 학습데이터수-모델용량-배치를 현재 리소스에 맞게 잘 조절해서 학습
- 메모리(중요!! ram, vram 모두해당): 모델과 데이터(1 batch)가 모두 로드 가능한 정도의 용량이 확보되어야 함. 학습 과정에서 vram 사용량이 점점 증가하는 경우가 있으므로 여유를 두고 학습하는 것 추천
- 코드 디버깅(중요!!): 학습은 시간이 오래걸리는 작업이므로 돌려두고 기다려야하는데, 학습 마지막단계(ex. best 파라미터 저장. metric 저장, validation)에서 오류가 나면 골치아파질 수도 있음. 처음부터 꼼꼼히 디버깅 하기.
	- 추천: 학습 1 iteration 디버깅 -> (train코드 주석 후)validation 디버깅 -> (train, validation 주석 후)모델 save 코드 디버깅

- DETR은 학습 시간이 많이 걸리므로 pretrained model을 사용하거나 transform for learning(?)기법을 사용해서 학습 시간을 줄이는 것을 추천한다.(https://youtu.be/hCWUTvVrG7E?t=1635)
## 구현

timm 패키지에서 