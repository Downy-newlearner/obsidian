---
created: 2024-11-20
tags: 
aliases: 
reference: https://python.langchain.com/docs/concepts/prompt_templates/
---
프롬프트 템플릿은 사용자 입력과 매개변수를 언어 모델에 대한 지침으로 변환하는 데 도움이 됩니다. 이는 모델의 응답을 안내하여 컨텍스트를 이해하고 관련성 있고 일관된 언어 기반 출력을 생성하는 데 도움이 될 수 있습니다.

프롬프트 템플릿은 사전을 입력으로 받으며, 각 키는 프롬프트 템플릿에서 채워야 할 변수를 나타냅니다.

Prompt Templates는 PromptValue를 출력합니다. 이 PromptValue는 LLM 또는 ChatModel에 전달될 수 있으며 문자열 또는 메시지 목록으로 캐스팅될 수도 있습니다. 이 PromptValue가 존재하는 이유는 문자열과 메시지 간을 쉽게 전환할 수 있게 하기 위해서입니다.

## String PromptTemplates
String 프롬프트 템플릿은 단일 문자열을 포멧한다. 단순한 input에 사용되는 프롬프트 템플릿이다.

```
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")

prompt_template.invoke({"topic": "cats"})
```
StringPromptValue(text='Tell me a joke about cats')

## ChatPromptTemplates
Chat 프롬프트 템플릿은 메시지 리스트를 포멧한다.
이 템플릿은 템플릿 자기 자신의 리스트로 구성된다.

```
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("user", "Tell me a joke about {topic}")
])

prompt_template.invoke({"topic": "cats"})
```
ChatPromptValue(messages=[SystemMessage(content='You are a helpful assistant', additional_kwargs={}, response_metadata={}), HumanMessage(content='Tell me a joke about cats', additional_kwargs={}, response_metadata={})])

*참고*
`{topic}`같은 부분을 format이라고 부른다.

위 예제 코드의 ChatPromptTemplate는 호출될 때 두 개의 메시지를 구조화한다.
	하나는 format이 없는 시스템 메시지
	나머지 하나는 format(`{topic}`)이 있는 HumanMessage이다.
		이 format은 유저가 입력하게 될 것이다.


## MessagesPlaceholder
이 프롬프트 템플릿은 메시지 리스트를 특정 위치에 추가하는 역할을 한다.

```
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder("msgs")
])

prompt_template.invoke({"msgs": [HumanMessage(content="hi!")]})
```
ChatPromptValue(messages=[SystemMessage(content='You are a helpful assistant', additional_kwargs={}, response_metadata={}), HumanMessage(content='hi!', additional_kwargs={}, response_metadata={})])

이렇게 하면 첫 번째 메시지는 시스템 메시지이고 두 번째 메시지는 우리가 전달한 인간 메시지인 두 개의 메시지 목록이 생성됩니다. 

5개의 메시지로 전달했다면 총 6개의 메시지(시스템 메시지와 전달한 5개를 더한 것)가 생성되었을 것입니다. 이는 메시지 목록을 특정 지점에 슬롯할 수 있도록 하는 데 유용합니다.