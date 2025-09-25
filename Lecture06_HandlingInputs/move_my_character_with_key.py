from pico2d import *
from sprite_info import Sprite

# §상하좌우 방향키이를 이용해서 캐릭터를 상하좌우로 이동.
# §IDLE 애니메이션 있어야 함.
# §배경 : TUK_GROUND.png 사용
# §화면 경계면에 다다르면 더 이상 진행하지 않음.
# §소스코드 이름은 move_my_character_with_key.py

Window_width, Window_height = 1280, 1024
open_canvas(Window_width, Window_height)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
mov_vec = [0, 0]

RIGHT_IDLE = 0
LEFT_IDLE = 1
RIGHT_RUN = 2
LEFT_RUN = 3
WhichAction = RIGHT_IDLE

right_move, left_move = False, False
x = Window_width // 2
y = Window_height // 2

def event_handler():
    global running, WhichAction, mov_vec, right_move, left_move
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                WhichAction = RIGHT_RUN
                right_move = True
                left_move = False
                mov_vec[0] = 1
            elif event.key == SDLK_LEFT:
                WhichAction = RIGHT_RUN  # 같은 애니메이션을 좌우 반전해서 사용
                right_move = False
                left_move = True
                mov_vec[0] = -1
            elif event.key == SDLK_UP:
                # 위로 이동할 때도 뛰는 애니메이션 적용
                if WhichAction == RIGHT_IDLE:
                    WhichAction = RIGHT_RUN
                mov_vec[1] = 1
            elif event.key == SDLK_DOWN:
                # 아래로 이동할 때도 뛰는 애니메이션 적용
                if WhichAction == RIGHT_IDLE:
                    WhichAction = RIGHT_RUN
                mov_vec[1] = -1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                # 다른 방향키가 눌려있는지 확인
                if mov_vec[1] == 0:  # 상하 이동이 없으면 IDLE로
                    WhichAction = RIGHT_IDLE
                right_move = True
                left_move = False
                mov_vec[0] = 0
            elif event.key == SDLK_LEFT:
                # 다른 방향키가 눌려있는지 확인
                if mov_vec[1] == 0:  # 상하 이동이 없으면 IDLE로
                    WhichAction = RIGHT_IDLE
                right_move = False
                left_move = True
                mov_vec[0] = 0
            elif event.key == SDLK_UP:
                # 다른 방향키가 눌려있는지 확인
                if mov_vec[0] == 0:  # 좌우 이동이 없으면 IDLE로
                    WhichAction = RIGHT_IDLE
                mov_vec[1] = 0
            elif event.key == SDLK_DOWN:
                # 다른 방향키가 눌려있는지 확인
                if mov_vec[0] == 0:  # 좌우 이동이 없으면 IDLE로
                    WhichAction = RIGHT_IDLE
                mov_vec[1] = 0

def Draw_character():
    global frame
    left, bottom, width, height = Sprite[WhichAction][frame]

    if left_move:
        # 좌측 이동 시 이미지를 좌우 반전
        character.clip_composite_draw(
            left, bottom, width, height,
            0, 'h',  # 'h'는 수평 반전
            x, y, width, height
        )
    else:
        # 우측 이동 또는 기본 상태
        character.clip_draw(left, bottom, width, height, x, y)

move_amount = 10
frame = 0
while running:
    clear_canvas()
    tuk_ground.draw(Window_width // 2, Window_height // 2)
    Draw_character()
    update_canvas()

    event_handler()
    if not running:
        break

    # 이동 처리 (벡터의 각 요소에 속도를 곱함)
    new_x = x + mov_vec[0] * move_amount
    new_y = y + mov_vec[1] * move_amount

    # 경계 체크
    if 0 <= new_x <= Window_width:
        x = new_x
    if 0 <= new_y <= Window_height:
        y = new_y

    frame = (frame + 1) % 8
    delay(0.1)

close_canvas()