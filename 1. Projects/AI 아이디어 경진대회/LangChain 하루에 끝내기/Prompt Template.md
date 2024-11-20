---
created: 2024-11-20
tags: 
aliases: 
reference: https://python.langchain.com/docs/concepts/prompt_templates/
---
프롬프트 템플릿은 사용자 입력과 매개변수를 언어 모델에 대한 지침으로 변환하는 데 도움이 됩니다. 이는 모델의 응답을 안내하여 컨텍스트를 이해하고 관련성 있고 일관된 언어 기반 출력을 생성하는 데 도움이 될 수 있습니다.

프롬프트 템플릿은 사전을 입력으로 받으며, 각 키는 프롬프트 템플릿에서 채워야 할 변수를 나타냅니다.

Prompt Templates는 PromptValue를 출력합니다. 이 PromptValue는 LLM 또는 ChatModel에 전달될 수 있으며 문자열 또는 메시지 목록으로 캐스팅될 수도 있습니다. 이 PromptValue가 존재하는 이유는 문자열과 메시지 간을 쉽게 전환할 수 있게 하기 위해서입니다.