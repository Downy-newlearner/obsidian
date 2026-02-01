---
created: 2025-06-24
Question: tsx 형식에 대해 설명해줘
---


## ✅ TSX란?

TSX는 TypeScript + JSX의 확장자입니다. 파일 확장자는 `.tsx`이고, React 컴포넌트를 TypeScript로 작성할 때 사용돼요.

## ✅ 구성 요소

- **TypeScript**: JavaScript에 타입을 추가한 언어 (정확한 코드 작성 가능)
- **JSX**: HTML 태그를 자바스크립트 안에서 직접 쓰는 문법 (React 전용)

### 그래서 TSX는?
→ 타입이 있는 JSX 문법을 사용할 수 있는 React용 파일이에요.

## ✅ 예시

```tsx
import React from "react";

type Props = {
  name: string;
};

function Hello({ name }: Props) {
  return <h1>안녕하세요, {name}님!</h1>;
}

export default Hello;
```

- `name`은 문자열(string) 이어야 함을 명확히 했고 JSX 문법(`<h1>...</h1>`)도 사용하고 있음 → 이게 바로 TSX!

## ✅ 언제 .tsx를 써야 하나요?

- 파일 안에 JSX/HTML 태그가 있다 → `.tsx`
- JSX 없이 순수한 TypeScript 코드만 있다 → `.ts`

## ✅ 요약

| 확장자  | 용도                                     |
| ------- | ----------------------------------------- |
| .ts     | 순수 TypeScript 코드                      |
| .tsx    | React + TypeScript (JSX 포함) 코드        |

궁금하면 `.js`, `.jsx`, `.ts`, `.tsx`의 차이도 표로 비교해줄게요!