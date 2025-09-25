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

def event_handler():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

frame = 0
while True:
    clear_canvas()
    tuk_ground.draw(Window_width // 2, Window_height // 2)
    character.clip_draw(Sprite[frame][0], Sprite[frame][1], Sprite[frame][2], Sprite[frame][3], Window_width // 2, Window_height // 2)
    update_canvas()

    event_handler()
    if not running:
        break

    frame = (frame + 1) % 8
    delay(0.1)
    pass

close_canvas()