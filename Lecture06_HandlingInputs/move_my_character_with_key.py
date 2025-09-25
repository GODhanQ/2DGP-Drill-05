from pico2d import *

# §상하좌우 방향키이를 이용해서 캐릭터를 상하좌우로 이동.
# §IDLE 애니메이션 있어야 함.
# §배경 : TUK_GROUND.png 사용
# §화면 경계면에 다다르면 더 이상 진행하지 않음.
# §소스코드 이름은 move_my_character_with_key.py

Window_width, Window_height = 1280, 1024
open_canvas(Window_width, Window_height)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

while True:
    pass

close_canvas()