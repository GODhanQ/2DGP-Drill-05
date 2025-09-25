from pico2d import *

Window_width, Window_height = 800, 600
open_canvas(Window_width, Window_height)
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


# fill here
running = True
x = Window_width // 2
dir = 0

def handle_events():
    global running, x, dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1


frame = 0
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    if 0 <= x <= Window_width:
        x += dir * 5
    else:
        if x <= 0:
            x = 0
        elif x >= Window_width:
            x = Window_width

    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()
