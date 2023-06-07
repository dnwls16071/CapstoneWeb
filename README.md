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
