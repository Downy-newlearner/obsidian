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
