import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("game1") #게임 이름

#FPS
clock = pygame.time.Clock()

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

#이동속도
character_speed = 0.5


#적 enemy
enemy =  pygame.image.load("C:\\Users\\Administrator\\Desktop\\python\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size  # 이지미의 크기 구해옴
enemy_width = enemy_size[0]   #캐릭터 가로크기
enemy_height = enemy_size[1]  #캐릭터 세로 크기
enemy_x_position = screen_width / 2 - (enemy_width/2)  # 화면 가로 절반 크기에 위치
enemy_y_position = (screen_height /2)  - (enemy_height/2)   # 화면 가장 아래 위치


# 폰트 정의
game_font = pygame.font.Font(None,40) #폰트 객체 생성(폰트,크기)

#총 시간
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks() #시간 tick을 받아옴



# 이벤트 루프
running = True #게임이 진행중
while running:
    dt = clock.tick(60)  # r초당 프레임수
    #print("fps: " + str(clock.get_fps()))
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생시
            running = False           # 게임이 진행중이 아님
            
        if event.type == pygame.KEYDOWN: #키가 눌러졌으면
            if event.key == pygame.K_LEFT:  #왼쪽 방향 키
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:  #방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_position += to_x * dt
    character_y_position += to_y * dt

#가로 경계값 처리
    if character_x_position < 0:
        character_x_position =0
    elif character_x_position > screen_width - character_width:
        character_x_position = screen_width - character_width

        #세로 경계값 처리
    if character_y_position < 0:
        character_y_position = 0
    elif character_y_position > screen_height - character_height:
        character_y_position = screen_height - character_height


#충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_position
    character_rect.top = character_y_position

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_position
    enemy_rect.top = enemy_y_position

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌")
       

    screen.blit(background, (0,0)) #배경 그리기 (좌표)
    #screen.fill((0,0,255))  # 배경 직접 rgb 설정

    screen.blit(enemy,(enemy_x_position,enemy_y_position)) 

    screen.blit(character,(character_x_position,character_y_position))

    #타이머/ 경과 시간계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) /1000  #(ms)를 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255))
    #출력할 글자, True, 글자색상
    screen.blit(timer,(10,10))

    # 시간이 0이하면 
    if total_time - elapsed_time <=0:
        print("타임아웃")
        running = False
        #잠시 대기 2초
        #pygame.time.delay(2000)
        

    pygame.display.update()  # 배경 다시 그리기

# pygame 종료
pygame.quit()
