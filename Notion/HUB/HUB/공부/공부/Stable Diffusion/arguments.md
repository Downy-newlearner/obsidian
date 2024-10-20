|   |   |   |   |
|---|---|---|---|
|Argument|타입|기본값|설명|
|`--prompt`|문자열|"a painting of a virus monster playing guitar"|렌더링할 프롬프트|
|`--init-img`|문자열|없음|입력 이미지의 경로|
|`--outdir`|문자열|"outputs/img2img-samples"|결과를 저장할 디렉토리|
|`--ddim_steps`|정수|50|DDIM 샘플링 단계 수|
|`--fixed_code`|불리언|없음|활성화 시 모든 샘플에서 동일한 시작 코드를 사용|
|`--ddim_eta`|실수|0.0|DDIM eta (eta=0.0은 결정론적 샘플링에 해당)|
|`--n_iter`|정수|1|주어진 프롬프트에 대해 샘플을 생성할 빈도|
|`--C`|정수|4|잠재 채널 수|
|`--f`|정수|8|다운샘플링 비율, 일반적으로 8 또는 16|
|`--n_samples`|정수|2|각 프롬프트에 대해 생성할 샘플 수 (즉, 배치 크기)|
|`--n_rows`|정수|0|그리드의 행 수 (기본값: n_samples)|
|`--scale`|실수|9.0|조건 없는 가이드 스케일|
|`--strength`|실수|0.8|노이즈 및 비노이징의 강도|
|`--from-file`|문자열|없음|지정된 경우 이 파일에서 프롬프트 로드|
|`--config`|문자열|"configs/stable-diffusion/v2-inference.yaml"|모델을 구성하는 경로|
|`--ckpt`|문자열|없음|모델의 체크포인트 경로|
|`--seed`|정수|42|재현 가능한 샘플링을 위한 시드|
|`--precision`|문자열|"autocast"|이 정밀도로 평가|
||||선택 사항: ["full", "autocast"]|
|   |   |   |   |
|---|---|---|---|
|Argument|타입|기본값|설명|
|`--prompt`|문자열|"a painting of a virus monster playing guitar"|렌더링할 프롬프트|
|`--init-img`|문자열|없음|입력 이미지의 경로|
|`--outdir`|문자열|"outputs/img2img-samples"|결과를 저장할 디렉토리|
|`--ckpt`|문자열|없음|모델의 체크포인트 경로|