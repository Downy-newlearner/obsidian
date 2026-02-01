---
created: 2025-11-02
tags: []
aliases:
  - ghcr
  - Github Container Registry
reference:
---
ghcr.io는 **GitHub Container Registry**의 약자입니다.

즉, **Docker 이미지를 저장하고 배포하기 위한 GitHub의 공식 레지스트리 서비스**예요.

## 1. 기본 개념
Docker 생태계에는 이미지를 보관하고 가져오는 "이미지 창고"가 있다. 이걸 Container Registry라고 부른다.

Container Registry 예시는 아래와 같다.

|**서비스 이름**|**주소**|**주체**|
|---|---|---|
|**Docker Hub**|docker.io|Docker 공식|
|**GitHub Container Registry**|ghcr.io|GitHub|
|**Google Artifact Registry**|gcr.io|Google Cloud|
|**Amazon ECR**|public.ecr.aws|AWS|
|**Railway, Hugging Face 등**|자체 Registry|각각의 플랫폼|


## 2. ghcr.io/railwayapp/nixpacks 해석

이 전체 경로를 쪼개서 보면 이렇게 된다.

|**구분**|**의미**|
|---|---|
|ghcr.io|GitHub Container Registry 도메인|
|railwayapp|GitHub 조직명 (Railway 팀의 공식 계정)|
|nixpacks|이미지 이름 (Railway의 자동 빌드 환경 패키지)|
|ubuntu-1745885067|특정 버전(tag) 이름 — 즉, 이미지 버전 ID|
즉, 의미는 “GitHub Container Registry에 저장된 Railway 팀의 Nixpacks Docker 이미지 중, Ubuntu 기반 1745885067 버전을 가져와라.”이 된다.