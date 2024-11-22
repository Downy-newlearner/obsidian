---
created: 2024-11-20
tags: 
aliases: 
reference: https://python.langchain.com/docs/tutorials/chatbot/
---
## LLM을 이용하여 대화 시작하기
```
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")

from langchain_core.messages import HumanMessage

model.invoke([HumanMessage(content="Hi! I'm Bob")])

model.invoke([HumanMessage(content="What's my name?")])
```
모델은 이전 대화를 기억하지 못하므로, 계속해서 이전 대화들을 모두 입력해줘야한다.

```
from langchain_core.messages import AIMessage

model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)
```

## 메시지 지속성
*LangGraph*는 내장된 Persistence Layer(데이터 유지 계층)를 제공하여, 여러 대화(turns)를 지원하는 채팅 애플리케이션 개발에 적합한 도구입니다.
	LangGraph를 이용하여 메시지 기록을 자동으로 저장할 수 있어, 위의 코드 예제처럼 이전 대화들을 모두 입력하지 않아도 되어 개발을 간소화 할 수 있다.

