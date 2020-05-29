import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("game1") #게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\Administrator\\Desktop\\python\\pygame_basic\\back01.png")

#스프라이터 (캐릭터) 불러오기
character =  pygame.image.load("C:\\Users\\Administrator\\Desktop\\python\\pygame_basic\\character.png")
character_size = character.get_rect().size  # 이지미의 크기 구해옴
character_width = character_size[0]   #캐릭터 가로크기
character_height = character_size[1]  #캐릭터 세로 크기
character_x_position = screen_width / 2 - (character_width/2)  # 화면 가로 절반 크기에 위치
character_y_position = screen_height  - character_height   # 화면 가장 아래 위치


#이동할 좌표
to_x = 0
to_y = 0


# 이벤트 루프
running = True #게임이 진행중
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생시
            running = False           # 게임이 진행중이 아님
            
        if event.type == pygame.KEYDOWN: #키가 눌러졌으면
            if event.key == pygame.K_LEFT:  #왼쪽 방향 키
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:  #방향키를 때면
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_position += to_x
    character_y_position += to_y

    screen.blit(background, (0,0)) #배경 그리기 (좌표)
    #screen.fill((0,0,255))  # 배경 직접 rgb 설정

    screen.blit(character,(character_x_position,character_y_position))

    pygame.display.update()  # 배경 다시 그리기

# pygame 종료
pygame.quit()
