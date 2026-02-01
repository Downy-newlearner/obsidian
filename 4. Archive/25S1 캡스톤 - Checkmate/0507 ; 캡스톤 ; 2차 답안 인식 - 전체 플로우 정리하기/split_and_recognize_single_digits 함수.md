

1. directory_path 내의 모든 파일 및 디렉토리 이름을 sub_dirs 리스트에 할당
	directory_path: *"/home/jdh251425/2025_DKU_Capstone/AI/Algorithm/OCR/cropped_datasets/text_crop_new/answer"*
	sub_dir: 
	![[Pasted image 20250513095900.png|200]]
	이 파일명들이 리스트로 들어감
	
2. sub_dirs 리스트를 각 이름의 두 번째 언더스코어('\_') 뒤에 있는 숫자를 기준으로 정렬

3. JSON 파일이 존재하지 않거나 비어 있는 경우 초기화
   - JSON 파일 경로: '/path/to/recog_failed.json'

1.  sub_dirs 리스트의 각 디렉토리에 대해 반복:
	a. 하위 이미지 파일들의 경로를 image_paths 리스트에 담음
		![[Pasted image 20250513100047.png|600]]
	b. image_paths 리스트를 각 이름의 두 번째 언더스코어('\_') 뒤에 있는 숫자를 기준으로 정렬
		![[Pasted image 20250513100631.png]]

	c. 각 이미지 파일에 대해 반복:
		i. 이미지 파일 경로를 설정
		ii. 바운딩 박스 생성
		iii. 인식 결과 생성
		iv. 인식 실패 시 JSON 파일에 기록

	d. 인식 결과를 기반으로 유클리드 거리 계산
	e. 유클리드 거리를 기준으로 결과를 정렬

	f. 답의 개수를 기반으로 disconnect_num 계산
	g. disconnect_num을 사용하여 최종 결과 생성

2. 결과를 CSV 파일로 저장

