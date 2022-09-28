import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 폭
screen_height = 640 # 세로 높이
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("HS Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\Kang HyeonSu\\Desktop\\WorkSpace\\PythonWorkSpace\\13_오락실게임\\background.png") # 탈출 문자 때문에 백슬래쉬를 두개 넣어주거나 그냥 슬래쉬 하나로 바꿔줘야한다

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가? 
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    # screen.fill((0,0,255)) # 화면 채우기(파란색)
    screen.blit(background, (0, 0)) # 실제로 배경을 그리기

    pygame.display.update() # 게임 화면을 업데이트!

# pygame 종료
pygame.quit()
