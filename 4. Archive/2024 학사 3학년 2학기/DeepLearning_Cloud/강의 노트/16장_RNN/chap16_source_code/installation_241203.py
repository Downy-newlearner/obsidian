from transformers import BartForConditionalGeneration, BartTokenizer


model = BartForConditionalGeneration.from_pretrained("facebook/bart-base", 
                                              forced_bos_token_id=0)
tokenizer = BartTokenizer.from_pretrained("facebook/bart-base")


# pipeline은 사전 학습된 모델을 손쉽게 사용할 수 있는 고수준 API입니다. 코드에서 다양한 태스크에 대해 pipeline이 설정되었습니다.

from transformers import pipeline
pipe = pipeline('sentiment-analysis',
       model='nlptown/bert-base-multilingual-uncased-sentiment')
pipe = pipeline('text-generation')
pipe = pipeline("text2text-generation")
pipe = pipeline("question-answering")