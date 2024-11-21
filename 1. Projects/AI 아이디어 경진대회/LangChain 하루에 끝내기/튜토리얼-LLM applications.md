---
created: 2024-11-20
tags: 
aliases: 
reference: https://python.langchain.com/docs/tutorials/llm_chain/
---
## Using Language Model
Let's first use the model directly. [ChatModels](https://python.langchain.com/docs/concepts/chat_models/) are instances of LangChain [Runnables](https://python.langchain.com/docs/concepts/runnables/), which means they expose a standard interface for interacting with them. To simply call the model, we can pass in a list of messages to the `.invoke` method.

```
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

model.invoke(messages)
```
이렇게 명령해서 모델에게 직접 답변을 들을 수 있다.

지금 한 것: 메시지 목록을 언어 모델에 직접 전달
	메시지 목록이란? 
		"사용자의 입력 + 애플리케이션 로직" 조합
		애플리케이션 로직은 사용자의 입력을 받아 LLM에 전달할 준비가 되도록 메시지 목록 *변환*을 한다.
			*변환*: 시스템 메시지를 추가하거나 사용자 입력으로 템플릿을 형식화함

Prompt Templates는 이 '변환(Transformation)'에 대한 Tools이다.

여기서 LangSmith를 사용한다면 이런 기록들을 추적할 수 있다.
	token usage information, latency, standard model parameters (such as temperature), and other information를 추적가능하다.

## Prompt Templates
LangChain의 핵심은 입력과 출력의 중간에 LLM이 이해할 수 있는 **최적의 프롬프트**를 제공하는 것이다.

![[Pasted image 20241120151714.png]]

**Prompt template 만들기**
```
from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
```
API Reference: ChatPromptTemplate
	![[Pasted image 20241120151825.png]]

**결과 받아보기**
```
result = prompt_template.invoke({"language": "Italian", "text": "hi!"})

result
```
ChatPromptValue(messages=[SystemMessage(content='Translate the following from English into Italian', additional_kwargs={}, response_metadata={}), HumanMessage(content='hi!', additional_kwargs={}, response_metadata={})])

.invoke 메소드의 입력은 dictionary 형태이다.

메시지만 뽑아서 보고싶다면 아래 코드를 적용하면 된다.

```
result.to_messages()
```
[SystemMessage(content='Translate the following from English into Italian', additional_kwargs={}, response_metadata={}), HumanMessage(content='hi!', additional_kwargs={}, response_metadata={})]

**결론**
지금까지 모델에 입력할 _최적의 프롬프트_ 를 만드는 방법에 대해서 알아본 것이다. 이제 Chain을 이용해서 모델에 입력해보자.( `|` 연산자 사용)

## Chaining together components with LCEL
이제 우리는 파이프 연산자(`|`)를 이용하여 최적의 프롬프트와 모델을 연결할 수 있다.

```
chain = prompt_template | model
```

```
response = chain.invoke({"language": "Italian", "text": "hi!"})
print(response.content)
```
Ciao!


