# Outline
* 2023학년도 3학년 1학기 정보통신공학과 캡스톤디자인 3조 프로젝트 안내 페이지입니다.

# Team
* 팀명 : Old Jeans
 
* 팀원 및 팀원 역할

|윤성원(팀장)|오동준|김장섭|이승우|장우진(개발 총괄)|
|:---------------------:|:---------------------:|:---------------------:|:---------------------:|:---------------------:|
|201716066|201716042|201816048|201916401|201916071|
|Frontend|Frontend|Frontend|Frontend|Backend|

* 윤성원(팀장)

  * 전반적인 프로젝트 진행 
  
  * 주차별 PPT 발표 자료 제작 및 개발 일정 기획
  
  * 오픈소스 템플릿을 활용한 탁상 달력 커스텀 디자인 제작

* 오동준
 
  * 일러스트 담당

* 김장섭

  * 인스타 홍보 마케팅 담당
  
  * 메인 페이지 & 달력 페이지 UI/UX

  * 페이지 구성

* 이승우 

  * 카카오톡 채널 홍보 마케팅 담당
  
  * 메인 페이지 & 달력 페이지 UI/UX

  * 페이지 구성

* 장우진(개발 총괄)

  * 모든 백엔드 기능 개발
  
  * Flask 웹 서버 구축 & 관리
  
  * PostgreSQL 데이터베이스 생성 & 관리

# Development Environment & Tool

|System|Name|
|:---|:---|
|Database|PostgreSQL|
|Framework|Flask|
|SCM|Git|
|Backend|Python 3.10.x|
|Frontend|Javascript, HTML5, CSS, Jquery, Ajax|
|IDE|Vs Code, Pycharm Community Professional 2023.1.1|

# Service Mechanism

* Python Flask와 FullCalendar 간의 통신을 Ajax(Asynchronous Javascript and XML)를 사용하여 구현

* FullCalendar는 클라이언트 측 Javascript 라이브러리이고 웹 페이지에 대한 동적인 캘린더 기능을 제공

* Flask는 서버 측 Python 프레임워크로 클라이언트의 요청에 대한 응답을 수신하고 처리하는 역할 수행

1. FullCalendar 표시 : FullCalendar을 웹 페이지에 출력하고 캘린더에 대한 모든 요소를 준비

2. Ajax 요청 : FullCalendar에서 이벤트를 가져오거나 서버로 데이터를 전송하기 위해 Ajax 요청을 수행

3. Flask Route(경로) 설정 : 해당 Ajax 요청을 처리할 라우트를 설정하고 라우트를 정상적으로 이루어지게 설정하여 클라이언트의 요청을 수신하고 필요한 데이터를 처리

4. 데이터 처리 및 응답 : Python 프레임워크에서 JSON 라이브러리를 임포트하여 데이터를 JSON 형식으로 변환하여 클라이언트에게 응답으로 전송

5. 클라이언트 측 처리 : 클라이언트는 받은 JSON 응답을 FullCalendar에 적용(CRUD)

# Tech Stack

<div class="container">
 <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> 
 <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> 
 <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
 <img src="https://img.shields.io/badge/jquery-FFCA28?style=for-the-badge&logo=jquery&logoColor=white">
 <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
 <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
 <img src="https://img.shields.io/badge/PostgreSQL-003545?style=for-the-badge&logo=PostgreSQL&logoColor=white"> 
 <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">
 <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
</div>

# File Structure

```bash
├── templates
│   ├── index.html    # FullCalendar loading page
│   └── login.html    # login & Sign Up page
├── static
│   ├── css           # FullCalendar css
│   ├── fonts         # FullCalendar fonts
│   ├── images        # FullCalendar images
│   ├── js            # Display Setting
│   └── videos        
└── code
│   ├── app.py        # Backend
``` 

# File Guide

   * test.csv(=schedule.csv) : 날짜 형식이 맞춰진 연간 데이터 파일
   
   * guide.pdf : 탁상 달력 제작 가이드 PDF 파일
   
   * template.zip : 템플릿 안내 파일

# Setup Environment

Create Database Environment setting:
```bash
DB_HOST = "DB 호스트 이름"
DB_NAME = "DB 이름"
DB_USER = "DB 사용자 이름"
DB_PASS = "DB 비밀번호"
app.secret_key = "암호화 인증 비밀키"
```

Install Flask:
```bash
pip install flask
```
Flask Execution:
```bash
flask run
```
