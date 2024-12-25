## 논문 주제
- co-DETR를 이용한 차량 파손 및 부품 detection(vs YOLOv4, VGG16) 
	- [[YOLOv4를 이용한 차량파손 검출 모델 개선]]

## 데이터
- https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=581 (기각: Segmentation 데이터임)

- https://github.com/jennyluciav/car-damage-dataset (논문에서 사용한 github 데이터) -> 전처리 필요
	- 라벨링이 안되어있음

- https://universe.roboflow.com/capstone-nh0nc/car-damage-detection-t0g92/dataset/4/images/4a6dce624f619d83a4fddc73208d98bd (Detection 데이터셋)

## co-DETR란?
- DETRs with Collaborative Hybrid Assignments Training

## 모델
- github 코드 공개 여부
- 파라미터 수 (현재 리소스에서 실행 및 저장 가능한지)
- 입출력 구조 (디버깅하면서 텐서 단위로 확인 추천)
- 사전학습 가중치 (pretrained weight): huggingface에 공개된 것을 사용하는지, 아니라면 github에 공개 돼 있는지

co-DETR vs YOLOv7

## 실험

- 학습시간: batch가 커지면 좀 더 빨라지긴 하지만, 어차피 데이터 자체가 많으면 1회 학습 당 걸리는 시간이 늘어남. 학습데이터수-모델용량-배치를 현재 리소스에 맞게 잘 조절해서 학습
- 메모리(중요!! ram, vram 모두해당): 모델과 데이터(1 batch)가 모두 로드 가능한 정도의 용량이 확보되어야 함. 학습 과정에서 vram 사용량이 점점 증가하는 경우가 있으므로 여유를 두고 학습하는 것 추천
- 코드 디버깅(중요!!): 학습은 시간이 오래걸리는 작업이므로 돌려두고 기다려야하는데, 학습 마지막단계(ex. best 파라미터 저장. metric 저장, validation)에서 오류가 나면 골치아파질 수도 있음. 처음부터 꼼꼼히 디버깅 하기.
	- 추천: 학습 1 iteration 디버깅 -> (train코드 주석 후)validation 디버깅 -> (train, validation 주석 후)모델 save 코드 디버깅

- DETR은 학습 시간이 많이 걸리므로 pretrained model을 사용하거나 transform for learning(?)기법을 사용해서 학습 시간을 줄이는 것을 추천한다.(https://youtu.be/hCWUTvVrG7E?t=1635)