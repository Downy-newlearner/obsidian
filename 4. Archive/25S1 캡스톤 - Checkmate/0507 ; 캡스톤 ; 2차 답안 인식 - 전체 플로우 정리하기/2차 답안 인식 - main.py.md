Global:
  과목명 (subject_name) - 문자열
  문제번호_이미지_디렉토리_경로 (qn_directory_path) - 문자열 (기본값 존재)
  답안_JSON_파일_경로 (answer_json_path) - 문자열 (기본값 존재)
  답안_이미지_디렉토리_경로 (answer_dir_path) - 문자열 (기본값 존재)
  1차_학번인식_결과_JSON (previous_step_json_data) - JSON 객체 (기본값 None)

함수 main_recognition_process (입력: 과목명, [경로들], [1차_결과_JSON]):

  1. ==결과_JSON_초기화==:
     - `make_recognition_json_structure(과목명)` 호출
     - 반환 값: {"subject": 과목명, "recognized_answers": [], "failed_recognition": [], "error": "", "warning": ""}

  2. ==문제_번호_정보_딕셔셔너리_생성==:
     - `create_question_info_dict(문제번호_이미지_디렉토리_경로, 답안_JSON_파일_경로)` 호출
     - 반환 값: 문제_정보_딕셔너리 (예: {"1-1": [y_top, y_bottom], "2": [y_top, y_bottom]})
     - 만약 문제_정보_딕셔너리 생성 실패 시:
       - 결과_JSON["error"] = "문제_정보_딕셔너리 생성 실패 메시지"
       - 결과_JSON 반환

  3. ==답안_파일_이름_변경_및_1차_결과_반영 (TODO 상세 구현 필요)==:
     - /*
     -   만약 `1차_학번인식_결과_JSON`이 존재하고, 그 안에 파일명 변경 정보가 있다면,
     -   `답안_이미지_디렉토리_경로` 내의 파일명을 해당 정보에 따라 우선 변경합니다.
     -   (예: `previous_step_json_data["student_list"]` 참고하여 파일명 변경)
     - */
     - `rename_answer_files(문제_정보_딕셔너리, 답안_JSON_파일_경로, 답안_이미지_디렉토리_경로)` 호출
       - 이 함수는 문제_정보_딕셔너리와 답안_JSON을 참고하여,
       - 답안_이미지_디렉토리 내 파일들을 (기존명)_qn_{문제번호}_ac_{정답개수}.{확장자} 형태로 변경합니다.
     - 콘솔에 "답안 파일 이름 변경 완료" 메시지 출력

  4. ==이미지_전처리_및_답안_인식 (TODO 상세 구현 필요)==:
     - 처리된_파일_개수 = 0
     - `답안_이미지_디렉토리_경로` 내의 각 이미지 파일에 대해 반복:
       - (숨김 파일 등 예외 처리)
       - /*
       -   여기에 실제 전처리 및 인식 로직이 들어갑니다.
       -   - `text_crop.py` 등을 사용하여 이미지 전처리 수행
       -   - `split_and_recognize_single_digits.py` 등을 사용하여 답안 인식 수행
       -   인식_성공_데이터 = (인식된 문제 번호, 인식된 답안, 신뢰도 등...)
       -   인식_실패_데이터 = (원본 파일명, 실패 사유, 필요시 이미지 base64 등...)
       - */
       - 임시_로직:
         - 결과_JSON["recognized_answers"]에 {"filename": 현재_파일명, "status": "pending_actual_recognition"} 추가
       - 처리된_파일_개수 증가

     - 만약 처리된_파일_개수가 0이면:
       - 결과_JSON["warning"] = "처리할 답안 이미지가 없음 경고 메시지"

  5. ==최종_결과_JSON_반환==:
     - 결과_JSON 반환
