from pygame import *
init()

window_size =(500,500)
window = display.set_mode(window_size)
display.set_caption("игра")
time = time.Clock()
FPS = 60
game = True

player = Rect(0,0,100,100)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((0,0,0))
    draw.rect(window,(255,0,0),player) #
    keys = key.get_pressed()
    if keys[K_w]:
        player.y -= 5
    if keys[K_s]:
        player.y += 5
    if keys[K_a]:
        player.x -= 5
    if keys[K_d]:
        player.x += 5

    time.tick(FPS)
    display.update()
