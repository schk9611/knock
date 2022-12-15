# Knock

## 👤 팀원 및 업무분담
|손찬규(BE)|박지훈(BE)|
|---|---|
|소셜 로그인 구현|게시판 API 개발(project app)|

## 🗓 개발 일정
- Phase1(Backend API 개발, 배포): 2022.12.07 ~ 2022.12.31

## 🖥 프로젝트 

#### 프로젝트 소개
- 스터디, 프로젝트 팀을 매칭해주는 서비스 입니다.
- 등록된 프로젝트 팀 공고를 보고 유저가 참가하는 방식 뿐만 아니라 프로젝트 소유 자도 다른 유저에게 프로젝트 참가제안 하는 경우도 가능합니다.

#### 사용된 기술

- Back-End
    - Python, Django(DRF), Mysql, Poetry
- Collaboration
    - Git, Github, Notion, Discord, Figma

#### ERD
![knock_erd_1](https://user-images.githubusercontent.com/98141328/207893196-9891d2e0-eb3a-4ad8-8a97-df772854cca3.png)

#### API endpoint

|URI|METHOD|DESC|
|---|---|---|
|/domain/project/|GET, POST|프로젝트 생성, 리스트 조회|
|/domain/project/\<int:pk\>/|GET, PUT, DELETE|프로젝트 detail 조회, 수정, 삭제|
|/domain/study/|GET, POST|스터디 생성, 리스트 조회|
|/domain/study/\<int:pk\>/|GET, PUT, DELETE|스터디 detail 조회, 수정, 삭제|
|/domain/user/|GET, PUT|유저 정보 조회, 수정|
|/domain/user/profile/|GET, PUT|유저 프로필 조회, 수정|
|/domain/user/post/|GET|유저 생성글 조회|

#### API 요구사항
- 유저 로그인/회원가입 API

    - 
- 유저 프로필 API

    -
- 유저 작성글 API

    -
- 프로젝트 API

    - 
- 스터디 API

    -
## 🛠 Unit Test
테스트코드 작성시 업데이트!
 