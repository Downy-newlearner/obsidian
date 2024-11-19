![[chap15_keras_GAN_page-0001.jpg]]

![[chap15_keras_GAN_page-0002.jpg]]

![[chap15_keras_GAN_page-0003.jpg]]
x,y: 오브젝트의 시작 좌표점
w, h: width & height

![[chap15_keras_GAN_page-0004.jpg]]

![[chap15_keras_GAN_page-0005.jpg]]

![[chap15_keras_GAN_page-0006.jpg]]

![[chap15_keras_GAN_page-0007.jpg]]

![[chap15_keras_GAN_page-0008.jpg]]
class_ids는 이미지에서 detect하고자 하는 사물의 이름이다. (모델에 이미 9천개 정도 들어있는데 그 중 일부만 선택한 것이다.)
	선택한 사물 중 이미지에 있는 것이 존재한다면 나타내달라는 명령을 하기 위해 특정한 것이다.
![[chap15_keras_GAN_page-0009.jpg]]
y_pred를 출력한 것을 보면 boxes가 4개 존재하고 confidence가 존재한다.
	이미지에서 바운딩 박스를 4개 찾았다는 의미이고, 각 박스의 xywh를 출력한 것이다.
	confidence는 확신을 의미하며 detect한 물체가 정답일 확률이다.

또한 classes는 11이 Dog, 15가 Potted plant를 의미한다.(이전 슬라이드의 인덱싱 참고고)
![[chap15_keras_GAN_page-0010.jpg]]

![[chap15_keras_GAN_page-0011.jpg]]

![[chap15_keras_GAN_page-0012.jpg]]

![[chap15_keras_GAN_page-0013.jpg]]

![[chap15_keras_GAN_page-0014.jpg]]

![[chap15_keras_GAN_page-0015.jpg]]

![[chap15_keras_GAN_page-0016.jpg]]

![[chap15_keras_GAN_page-0017.jpg]]

![[chap15_keras_GAN_page-0018.jpg]]

![[chap15_keras_GAN_page-0019.jpg]]

![[chap15_keras_GAN_page-0020.jpg]]

![[chap15_keras_GAN_page-0021.jpg]]

![[chap15_keras_GAN_page-0022.jpg]]

![[chap15_keras_GAN_page-0023.jpg]]

![[chap15_keras_GAN_page-0024.jpg]]

![[chap15_keras_GAN_page-0025.jpg]]

![[chap15_keras_GAN_page-0026.jpg]]

![[chap15_keras_GAN_page-0027.jpg]]

![[chap15_keras_GAN_page-0028.jpg]]

![[chap15_keras_GAN_page-0029.jpg]]

![[chap15_keras_GAN_page-0030.jpg]]

![[chap15_keras_GAN_page-0031.jpg]]

![[chap15_keras_GAN_page-0032.jpg]]

![[chap15_keras_GAN_page-0033.jpg]]

![[chap15_keras_GAN_page-0034.jpg]]

![[chap15_keras_GAN_page-0035.jpg]]