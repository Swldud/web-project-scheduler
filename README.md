<h1> 일정 </h1>

|날짜|계획|진행상황|
|---|---|---|
|~4월 10일|달력구현|한 달치(4월) 달력만 구현 성공|
|4월 11일|scheduler 앱 구현|schedule의 filter 기능 구현에서 오류 발생 수정 필요|
|4월 12일|user 앱 구현| 모델에 User 요소 작성을 안 해서 수정함. 저장했던 data 삭제 했음 주의, 만년달력 구현 실패 -> 기본 구현 이후에 알아보기!, user 넣으면서 create 작성에서 오류 발생 수정필요|
|4월 13일|발표를 위해 CSS 사이트 꾸미기★|CSS 계속 및 Notice app추가하기|

<br>

<h1> 프로젝트명: Scheduler </h1>
    
<h2>프로젝트 설명</h2>

- 팀 일정 공유가 목적
- Main: 오늘 일정과 Notice 목록
    (+ 스케줄과 관련된 게시글을 따로 작성할 수 있도록 하는 Notice는 추가 개발 중)

- nav-bar New: 일정을 새로 만듦 (단, 로그인 필요)
- nav-bar April calendar: 4월의 달력 및 달력 아래 각 요일의 일정 확인 가능
  (만년 달력을 구현해내지 못해서 23년 4월만 작성 가능)
  
+ CSS를 통한 UI 디자인 수정 필요

<br>
<br>


<h3> APP: Scheduler </h3>

<p> URL </p> 

- scheduler/month/
    (views.month)
    - 달력에 각 날짜에 맞는 일정 리스트를 추가하기 위해 filter 사용
      (자동화 필요. 개발 중)


- scheduler/create/
    (views.create_schedule)
    - 작성을 위해서 반드시 로그인을 거쳐야 함
    - POST로 출입해야만 검증 후에 작성한 유저의 이름과 함께 저장됨.

- scheduler/
    (views.index_schedule)
    - Main 오늘 일정과 Notice 목록을 불러옴
    - 클릭시 상세 페이지로 이동 가능


- scheduler/1/
    (views.detail_schedule)
    - 일정의 상세 페이지


- scheduler/1/update/
    (views.update_schedule)
    - 기존 일정을 수정하는 form 제공
    - 글을 작성한 본인이 아니면 수정 불가 -> 버튼을 눌러도 변화 없이 그대로 상세페이지에 머무름


- scheduler/1/delete/
    (views.delete_schedule)
    - 선택한 일정을 삭제
    - 삭제 후에는 메인 페이지로 돌아감

<br>
<br>

<h3> APP: accounts </h3>

* 내장되어았는 CustomUserCreationForm과 User model 사용

- accounts/signup/
    (views.signup)
    - 이미 로그인 했다면 signup에 접속할 수 없음 (로그인 되어있다면, nav-bar에 signup 버튼이 보이지 않음)
    - 로그인하지 않은 상태에서만 계정을 만들 수 있는 페이지로 이동

- accounts/signout/
    (views.signout)
    - 로그인 한 상태로 상단의 logout 버튼을 누르면, 계정에서 로그아웃되고 메인화면으로 돌아감
    - 게시물 작성이 제한됨


- accounts/signin/
    (views.signin)
    - 유효한 로그인을 했다면 메인화면으로 이동함
    - 유효하지 않은 로그인을 했다면 주의 문구가 추가 됨.