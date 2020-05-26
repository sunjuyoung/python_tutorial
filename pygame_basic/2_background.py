import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("game1") #게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\Administrator\\Desktop\\python\\pygame_basic\\background.png")

# 이벤트 루프
running = True #게임이 진행중
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생시
            running = False           # 게임이 진행중이 아님

    screen.blit(background, (0,0)) #배경 그리기 (좌표)
    #screen.fill((0,0,255))  # 배경 직접 rgb 설정

    pygame.display.update()  # 배경 다시 그리기

# pygame 종료
pygame.quit()
