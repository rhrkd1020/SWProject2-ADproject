# SW2 Ad project
------------------------
### What is This?

 - python 언어를 사용한 탈출 게임
 
### Story
 - 국민대 정문에서 조형물로 야간근무를 한 쿠민이는 퇴근시간이 되어 집에 갈 준비를 하러 웰니스 센터의 샤워실로 향한다. 즐겁게 샤워를 하던 도중 갑자기 불이 꺼지게 되는데... 과연 쿠민이는 무사히 집에 갈 수 있을까?
 
---
 
# Prerequisites

### Install List

 - Python `3.7.1`

 ```
    pip install pygame
    pip install pytmx
 ```

## USAGE (사용방법)

 1. Clone file
 2. run main.py
- project를 열때 경로를 탈국민으로 잡아야 한다.

------------------------
## 주의 사항

1. 맥 최신버전(Catalina)은 작동하지 않는다.
2. 게임속 map을 확인하고 끌때 캐릭터의 움직임 키를 꾹 누르면서 끄면 캐릭터가 순간이동한다.
3. 캐릭터가 맵에서 탈출하거나 멈췄다면 e 키를 눌러 비상탈출을 하자. -단 맵별로 한번만 사용가능하다.
4. prologue가 컴퓨터에 따라 화면이 나오지 않는 경우가 있다. 노래는 들리는데 화면이 안뜬다면 기다리면 게임이 시작된다. (main에서 g.startscreen()과 g.prologue()를 주석처리하면 스킵하고 시작이 가능하다.)
5. 게임 진행이 막힌다면 플레이영상 혹은 공략영상을 참고하도록 하자.
