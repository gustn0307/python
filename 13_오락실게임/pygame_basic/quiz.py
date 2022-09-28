# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. X 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로 가로) -> background.png
# 2. 캐릭터 : 70 * 70 -> character.png
# 3. 똥 : 70 * 70 -> enemy.png

# ## 내 답안
from random import *
import pygame
###############################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 폭
screen_height = 640 # 세로 높이
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기") # 게임 이름

# FPS
clock = pygame.time.Clock()
###############################################################################

## 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("C:\\Users\\Kang HyeonSu\\Desktop\\WorkSpace\\PythonWorkSpace\\13_오락실게임\\background.png") # 탈출 문자 때문에 백슬래쉬를 두개 넣어주거나 그냥 슬래쉬 하나로 바꿔줘야한다

character = pygame.image.load("C:/Users/Kang HyeonSu/Desktop/WorkSpace/PythonWorkSpace/13_오락실게임/character.png") # 탈출 문자 때문에 백슬래쉬를 두개 넣어주거나 그냥 슬래쉬 하나로 바꿔줘야한다
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 캐릭터의 가로 위치를 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 캐릭터의 세로 위치를 화면 세로의 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0

# 이동 속도
character_speed = 0.6
enemy_speed = 5

# 적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/Kang HyeonSu/Desktop/WorkSpace/PythonWorkSpace/13_오락실게임/enemy.png") # 탈출 문자 때문에 백슬래쉬를 두개 넣어주거나 그냥 슬래쉬 하나로 바꿔줘야한다
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = randint(0, (screen_width - enemy_width)) # enemy의 가로 위치를 화면 랜덤으로 설정
enemy_y_pos = 0 # 캐릭터의 세로 위치를 화면 세로의 가장 아래에 해당하는 곳에 위치

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체를 생성(폰트 종류, 크기)

running = True 
while running:
    dt = clock.tick(30) 

    ## 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤 (character_x_pos, character_y_pos 에 to_x, to_y를 0만큼만 더해서 멈추도록)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            
    ## 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt # 프레임이 바뀌어도 이동속도는 동일하게

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)

    enemy_y_pos += enemy_speed # 똥 내려가게 하기
    
    if enemy_y_pos > (screen_height - enemy_height):
        enemy_x_pos = randint(0, (screen_width - enemy_width))
        enemy_y_pos = 0

    ## 4. 충돌 처리
    # 충돌 처리를 위한 rect(rectangle) 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect): # 충돌이 일어났는가?
        print("충돌했어요")
        # collision_text = game_font.render(str(1234), True, (255,255,255)) # 충돌 시 텍스트는 어떻게 표시하나
        # screen.blit(collision_text, (10, 10))
        running = False

    ## 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 실제로 배경을 그리기
    screen.blit(character,(character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos)) # enemy 캐릭터 그리기
      
    pygame.display.update() 

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 (ms)

pygame.quit()

## 나도코딩 답안
# import random
# import pygame
# ###############################################################################
# # 기본 초기화 (반드시 해야 하는 것들)
# pygame.init() # 초기화 (반드시 필요)

# # 화면 크기 설정
# screen_width = 480 # 가로 폭
# screen_height = 640 # 세로 높이
# screen = pygame.display.set_mode((screen_width, screen_height))

# # 화면 타이틀 설정
# pygame.display.set_caption("Quiz") # 게임 이름

# # FPS
# clock = pygame.time.Clock()
# ###############################################################################

# # 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# # 배경 만들기
# background = pygame.image.load("C:/Users/Kang HyeonSu/Desktop/WorkSpace/PythonWorkSpace/13_오락실게임/background.png")

# # 캐릭터 만들기
# character = pygame.image.load("C:/Users/Kang HyeonSu/Desktop/WorkSpace/PythonWorkSpace/13_오락실게임/character.png")
# character_size = character.get_rect().size
# character_width = character_size[0]
# character_height = character_size[1]
# character_x_pos = (screen_width / 2) - (character_width / 2)
# character_y_pos = screen_height - character_height

# # 이동 위치
# to_x = 0
# character_speed = 10

# # 똥 만들기
# ddong = pygame.image.load("C:/Users/Kang HyeonSu/Desktop/WorkSpace/PythonWorkSpace/13_오락실게임/enemy.png")
# ddong_size = ddong.get_rect().size
# ddong_width = ddong_size[0]
# ddong_height = ddong_size[1]
# ddong_x_pos = random.randint(0, screen_width - ddong_width)
# ddong_y_pos = 0
# ddong_speed = 10

# running = True 
# while running:
#     dt = clock.tick(30) 

#     # 2. 이벤트 처리 (키보드, 마우스 등)
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT: 
#             running = False
        
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 to_x -= character_speed
#             elif event.key == pygame.K_RIGHT:
#                 to_x += character_speed
        
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 to_x = 0

#     # 3. 게임 캐릭터 위치 정의
#     character_x_pos += to_x

#     if character_x_pos < 0:
#         character_x_pos = 0
#     elif character_x_pos > screen_width - character_width:
#         character_x_pos = screen_width - character_width

#     ddong_y_pos += ddong_speed

#     if ddong_y_pos > screen_height:
#         ddong_y_pos = 0
#         ddong_x_pos = random.randint(0, screen_width - ddong_width)

#     # 4. 충돌 처리
#     character_rect = character.get_rect()
#     character_rect.left = character_x_pos
#     character_rect.top = character_y_pos

#     ddong_rect = ddong.get_rect()
#     ddong_rect.left = ddong_x_pos
#     ddong_rect.top = ddong_y_pos

#     if character_rect.colliderect(ddong_rect):
#         print("충돌했어요")
#         running = False

#     # 5. 화면에 그리기
#     screen.blit(background, (0, 0))
#     screen.blit(character, (character_x_pos, character_y_pos))
#     screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

#     pygame.display.update() 

# pygame.quit()