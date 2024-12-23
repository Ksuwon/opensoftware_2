# 블록 깨기 게임

## 게임 설명
본 게임은 블록 깨기 게임으로, 패들로 공을 튕겨 화면에 있는 모든 블록을 깨면 클리어되는 게임입니다.<br> 
총 생명은 3개이며, 생명이 모두 소진될 때까지 블록을 모두 깨지 못하면 게임 오버가 됩니다. 
 <p align = "center">
   <img src="https://github.com/user-attachments/assets/972c58ed-0776-4cbb-903d-fd507b3ab151" width="300" alt="image">
 </p>
<br>

## 게임 플레이 방식
- 게임 시작 --> spacebar 누르기
- 움직임 --> 좌 (왼쪽 방향키), 우 (오른쪽 방향키)
- 종료 --> Esc 

## 게임 주요기능
1. **ITEM DROP (issue\#2)**<br>
블록을 깨면 20%의 확률로 아이템(빨간색 공 또는 파란색 공 중 하나)이 떨어지도록 구현했습니다. <br>
그러나 빨간색 공과 파란색 공은 아직 구현된 기능이 없으므로, 패들과 닿을 경우 사라지도록 설정되어 있습니다.
<p align = "center">
  <img src="https://github.com/user-attachments/assets/45271208-4533-4db2-9449-37bb64c4c6ef" width="300" alt="image">
</p>

2. **GREY WALL BLOCK & MULTI-HIT BLOCKS(issue\#3)**<br>
회색 벽 블록, 여러번 부딪혀야 깨지는 블록을 구현했습니다. 회색 벽 블록에 공이 부딪히면 회색 벽은 깨지지 않고, 공은 회색 벽에 의해 튕겨 나갑니다. <br>
블록은 노랑 블록, 주황 블록, 빨강 블록으로 이루어져 있습니다. 
노랑 블록은 한 번에 깨지며, 주황 블록은 두 번 부딪혀야 깨지고, 깨지면서 주황 블록은 노랑 블록으로 변합니다.
빨강 블록은 세 번 부딪혀야 깨지고, 깨지면서 빨강 블록은 주황 블록으로, 주황 블록은 다시 노랑 블록으로 변합니다.

<p align = "center">
  <img src="https://github.com/user-attachments/assets/bfe0b1af-542f-42af-b2fa-42900c412b38" width ="300" alt="gif">
</p>

## 게임환경
- Pygame (pip install pygame) 
- Python 3.10 or 3.12 (recommend) 

## Contributor
<table>
  <tr>
    <td align="center"><a href="https://github.com/phghub">
    <img src="https://avatars.githubusercontent.com/u/189502856?v=4" width="100px;" alt=""/>
    <td align ="center"><a href="https://github.com/Ksuwon">
    <img src ="https://avatars.githubusercontent.com/u/181618655?v=4" width="100px;" alt=""/>
  </tr>
  <tr>
    <td align ="center"><a href="https://github.com/phghub" title="member">박호군</a></td>
    <td align ="center"><a href="https://github.com/Ksuwon" title="member">김수원</a></td>
  </tr>
  <tr>
    <td align ="center">Contributor</td>
    <td align = "center">Project Manager</td>
  </tr>
</table>
