from pygame import *
init()

window_size =(700,500)
window = display.set_mode(window_size)
display.set_caption("игра")
time = time.Clock()
FPS = 60
game = True

player = Rect(0,0,100,100)

big_rock = transform.scale(image.load("big_rock.png"),(100,100))
full_g_block = transform.scale(image.load("full_g_block.png"),(250,100))
full_h_block = transform.scale(image.load("full_h_block.png"),(100,300))
full_ggh = transform.scale(image.load("ggh.png"),(100,200))
full_sprout_1 = transform.scale(image.load("sprout_1.png"),(100,200))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((0,0,0))  
    draw.rect(window,(255,0,0),player) #
    window.blit(big_rock,(100,310)) #
    window.blit(full_g_block,(10,400)) #
    window.blit(full_g_block,(200,400)) #
    window.blit(full_g_block,(400,400)) #
    window.blit(full_g_block,(500,400)) #
    window.blit(full_h_block,(-10,200)) #
    window.blit(full_ggh,(300,250)) #
    window.blit(full_sprout_1,(500,250)) #
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
