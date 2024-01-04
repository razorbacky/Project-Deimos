![Project_Deimos](https://github.com/razorbacky/Project-Deimos/assets/51449986/33873892-6772-46a0-a002-ba9ae7bcccc1)

![Main_Program](https://github.com/razorbacky/Project-Deimos/assets/51449986/b4a1b5a2-1c66-48d5-ba71-a7b5bfa78697)

[Python] Project Deimos "Moons of Planets"
====

# Moons of Planets (행성들의 위성들)
프로젝트명을 각 행성들의 위성들의 이름으로 지으려고 했는데, 매번 위성을 찾아다니는 것이 너무 귀찮은 나머지, 그럼 그냥 '행성들 이름을 입력하면 그 행성의 위성들 목록을 가져오는 프로그램을 처음으로 만들어보자' 라는 것에서 시작된 파이썬 배우기 시작한 후, **"Helloworld"** 를 제외하고 생애 첫 그나마 봐줄만한 프로그램입니다.

그리고, 제 Github 에서 최초로 Public 으로 공개되는 프로그램 및 소스 코드이기도 합니다.
<p align="right">2024년 1월 5일</p>

------

# 개요
이 프로그램은 우리 태양계에 존재하는 행성들의 이름을 입력하면, 입력한 행성들의 위성들 목록을 출력합니다.
> * Python의 Request 라이브러리를 이용합니다.
> * [le-systeme-solaire](https://api.le-systeme-solaire.net/)의 API로 행성들의 위성 목록을 가져옵니다.
> * 아직도 수정해야 할 부분이 많이 남아있습니다.

# 이용하는 법
프로그램을 실행하여 목록을 확인하고자 하는 행성의 이름을 영어로 입력합니다.
입력한 행성의 위성 조회결과가 출력됩니다.

* 사용
```
행성의 이름을 입력하십시오. : [행성 이름 입력]
[결과 출력]
```

* 예시
```
행성의 이름을 입력하십시오. : mars
Phobos Deimos
```

# TODO List
TODO 목록은 앞으로 고쳐야합니다.