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

LangGraph는 대화형 애플리케이션에서 메시지 기록을 유지하고, 간단한 체크포인트 기능을 지원하여 개발 편의성을 높여주는 도구입니다. SQLite 또는 Postgres와 같은 저장소와도 통합 가능하다.

### config을 이용한 스레드 이용
```
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)


# Define the function that calls the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}


# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)
```
우선 LangGraph를 이용하여 워크플로우를 만들어주었다.

```
config = {"configurable": {"thread_id": "abc123"}}

query = "Hi! I'm Bob."

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()  # output contains all messages in state

query = "What's my name?"

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()
```
이렇게 스레드를 생성해서 대화를 할 수 있고, 다른 스레드를 만들어서 새로운 대화를 할 수 있다.

```
config = {"configurable": {"thread_id": "abc234"}}

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()
```
`==================================[1m Ai Message [0m==================================`
`I'm sorry, but I don't have access to personal information about you unless you provide it. How can I assist you today?`

