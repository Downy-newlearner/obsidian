## keras_CNN

![[chap12_keras_CNN_page-0001.jpg]]

![[chap12_keras_CNN_page-0002.jpg]]

![[chap12_keras_CNN_page-0003.jpg]]

![[chap12_keras_CNN_page-0004.jpg]]

![[chap12_keras_CNN_page-0005.jpg]]

![[chap12_keras_CNN_page-0006.jpg]]

![[chap12_keras_CNN_page-0007.jpg]]
jupyter notebook을 쓰는 사람들이 이미지를 출력하기 위해서 scikit-image 라이브러리를 사용한다.

![[chap12_keras_CNN_page-0008.jpg]]

![[chap12_keras_CNN_page-0009.jpg]]
인덱싱으로 픽셀값을 알아볼 수 있다.

![[chap12_keras_CNN_page-0010.jpg]]

![[chap12_keras_CNN_page-0011.jpg]]

![[chap12_keras_CNN_page-0012.jpg]]
flip은 좌우반전, rotate는 회전이다.
![[chap12_keras_CNN_page-0013.jpg]]

![[chap12_keras_CNN_page-0014.jpg]]

![[chap12_keras_CNN_page-0015.jpg]]

![[chap12_keras_CNN_page-0016.jpg]]

![[chap12_keras_CNN_page-0017.jpg]]

![[chap12_keras_CNN_page-0018.jpg]]
이미지의 특징을 뽑아내기 위해서 convolution 연산을 한다.

![[chap12_keras_CNN_page-0019.jpg]]

![[chap12_keras_CNN_page-0020.jpg]]
원시적인 특징을 추출할 수 있는 low-level feature filter부터 복잡한 특징을 추출할 수 있는 middle, top level feature filter까지 사용한다.
![[chap12_keras_CNN_page-0021.jpg]]

![[chap12_keras_CNN_page-0022.jpg]]
[[stride]]
![[chap12_keras_CNN_page-0023.jpg]]
padding은 convolution연산을 하더라도 원본 이미지의 사이즈를 유지하기 위한 단계이다.
![[chap12_keras_CNN_page-0024.jpg]]
pooling은 padding과 반대로 출력 이미지의 사이즈를 줄이는 연산이다.
![[chap12_keras_CNN_page-0025.jpg]]

![[chap12_keras_CNN_page-0026.jpg]]

![[chap12_keras_CNN_page-0027.jpg]]

![[chap12_keras_CNN_page-0028.jpg]]

![[chap12_keras_CNN_page-0029.jpg]]

![[chap12_keras_CNN_page-0030.jpg]]
Dense는 DNN에서 배웠다.

![[chap12_keras_CNN_page-0031.jpg]]

![[chap12_keras_CNN_page-0032.jpg]]

![[chap12_keras_CNN_page-0033.jpg]]

![[chap12_keras_CNN_page-0034.jpg]]

![[chap12_keras_CNN_page-0035.jpg]]

![[chap12_keras_CNN_page-0036.jpg]]

![[chap12_keras_CNN_page-0037.jpg]]

![[chap12_keras_CNN_page-0038.jpg]]
==이게 어떤 원리로 성능이 좋아지는거야?==
	이 질문에 답변하기(11.07 9:48) 
![[chap12_keras_CNN_page-0039.jpg]]

![[chap12_keras_CNN_page-0040.jpg]]

![[chap12_keras_CNN_page-0041.jpg]]

![[chap12_keras_CNN_page-0042.jpg]]

![[chap12_keras_CNN_page-0043.jpg]]

![[chap12_keras_CNN_page-0044.jpg]]


## 과제: Keras_CNN_Workshop
이미지 사이즈가 적당히 작은 것, 총 용량이 적당히 적은 데이터셋을 골라서 CNN 학습시키기