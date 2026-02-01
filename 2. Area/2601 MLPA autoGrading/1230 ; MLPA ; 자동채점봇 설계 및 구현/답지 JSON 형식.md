사용자가 직접 입력한 답지 정보를 JSON 형식으로 구조화해서 답지 인식 단계의 성능 향상을 기대

```JSON
{
  "problem_1": {

  "sub_problems": {

    "1": {
    "pt": 4,
    "answer_count": 2,
    "answer_type": "binary",
    "expected_format": ["0", "1"],
    "rec_answer": []
    },

    "2": {
    "pt": 4,
    "answer_count": 2,
    "answer_type": "binary",
    "expected_format": ["0", "1"],
    "rec_answer": []
    },
    
    ...
    
    "28": {
    "pt": 4,
    "answer_count": 2,
    "answer_type": "binary",
    "expected_format": ["0", "1"],
    "rec_answer": []
    }
    
  },
  
  "problem_2": {
    "pt": 4,
    "answer_count": 2,
    "answer_type": "integer_list",
    "expected_format": "comma_separated_integers",
    "rec_answer": []
  },
  
  "problem_3": {
    "pt": 4,
    "answer_count": 2,
    "answer_type": "integer_list",
    "expected_format": "comma_separated_integers",
    "rec_answer": []
  },
  
  ...
}
```

> "problem_{pn}": {"pt": , "answer_count": , "rec_answer": }

### 1. 꼬리문제 여부

꼬리문제가 있는 문제는 {qn} = {main_qn}-{sub_qn}
꼬리문제가 없는 문제는 {qn} = {main_qn}

### 2. 답이 여러개인 경우

"rec_answer" 필드의 형식은 list이다.

답이 1개인 경우 list에는 1개의 요소만 존재하고,
답이 여러개인 경우 list에는 n개의 요소가 존재한다.