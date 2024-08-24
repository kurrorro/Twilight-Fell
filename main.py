import pgzrun
from pgzero.builtins import Actor, animate, keyboard

import pgzero.screen
screen : pgzero.screen.Screen

import random

#jendela game
WIDTH = 500
HEIGHT = 500

TITLE = "Twilight Fell"
FPS = 30

#posisi
a = random.randint(50, 100) #pillar1
b = random.randint(400, 450) #pillar2
g = random.randint(50, 100) #pillar3
h = random.randint(400, 450) #pillar4
i = random.randint(50, 100) #pillar5
j = random.randint(400, 450) #pillar6
d = random.randint(220, 280) #disc
e = random.randint(220, 280) #heart

#pemanggilan objek
f = random.randint(1, 500)

#objek-objek
bg = Actor('rsz_1bg')
pillar1 = Actor('rsz_1pillar_up', (550, a))
pillar2 = Actor('rsz_1pillar_down', (550, b))
pillar3 = Actor('rsz_1pillar_up', (750, g))
pillar4 = Actor('rsz_1pillar_down', (750, h))
pillar5 = Actor('rsz_1pillar_up', (950, i))
pillar6 = Actor('rsz_1pillar_down', (950, j))
char = Actor('chara', (120, 250))
heart = Actor('rsz_heart', (550, e))
shuriken = Actor('rsz_shuriken', (550, 250))
disc = Actor('rsz_disc', (550, d))
speed = 5 #kecepatan
new_image = 'chara' #chara melompat
hati = Actor('rsz_heart', (430, 40)) #jumlah nyawa
nyawa = 50 #jumlah nyawa
score = 0 #skor permainan
game_over = 0 #game over

#draw
def draw():
    global a
    global b
    if game_over == 0:
        bg.draw()
        heart.draw()
        disc.draw()
        shuriken.draw()
        char.draw()
        pillar1.draw()
        pillar2.draw()
        pillar3.draw()
        pillar4.draw()
        pillar5.draw()
        pillar6.draw()
        hati.draw()
        screen.draw.text(f'{nyawa}', pos=(450, 27), color='white', fontsize=24, background='black')
        screen.draw.text(f'{score}', pos=(250, 40), color="white", fontsize=40, background='black')
    else:
        bg.draw()
        screen.draw.text('Game Over', pos=(150, 220), color="white", fontsize=50, background='black')
        
#pillar
def pipe1():
    if pillar1.x > -20:
        pillar1.x -= 5
    else:
        pillar1.x = WIDTH + 75
        pillar1.y = random.randint(50, 100)
        
def pipe2():
    if pillar2.x > -20:
        pillar2.x -= 5
    else:
        pillar2.x = WIDTH + 75
        pillar2.y = random.randint(400, 450)
        
def pipe3():
    if pillar3.x > -20:
        pillar3.x -= 5
    else:
        pillar3.x = WIDTH + 75
        pillar3.y = random.randint(50, 100)
        
def pipe4():
    if pillar4.x > -20:
        pillar4.x -= 5
    else:
        pillar4.x = WIDTH + 75
        pillar4.y = random.randint(400, 450)
        
def pipe5():
    if pillar5.x > -20:
        pillar5.x -= 5
    else:
        pillar5.x = WIDTH + 75
        pillar5.y = random.randint(50, 100)
        
def pipe6():
    if pillar6.x > -20:
        pillar6.x -= 5
    else:
        pillar6.x = WIDTH + 75
        pillar6.y = random.randint(400, 450)
        
#musuh
def enemy():
    global speed
    global f
    global c
    if shuriken.x > -20:
        shuriken.x -= 10
        shuriken.angle += 20
    else:
        shuriken.x = WIDTH + 20
        f = random.randint(1, 5)

#nyawa
def life():
    global f
    if heart.x > -20:
        heart.x -= 5
    else:
        heart.x = WIDTH + 20
        heart.y = random.randint(220, 280)
        f = random.randint(1, 5)
        
#item    
#def item():
    #global f
    #if disc.x > -20:
        #disc.x -= 5
        #disc.angle += 10
    #else:
        #disc.x = WIDTH + 20
        #disc.y = random.randint(220, 280)
        #f = random.randint(1, 5)
        
#update
def update(dt):
    global f
    pipe1()
    pipe2()
    pipe3()
    pipe4()
    pipe5()
    pipe6()
    if f == 1:
        enemy()
    elif f == 2:
        life()
    #elif f == 3:
        #item()
    else:
        f = random.randint(1, 500)
    collide()
    gameover()

#tabrakan
def collide():
    global nyawa
    global score
    if char.colliderect(shuriken):
        nyawa -= 1
    if char.colliderect(heart):
        nyawa += 10
        heart.x = -15
    if char.colliderect(pillar1) or char.colliderect(pillar2) or char.colliderect(pillar3) or char.colliderect(pillar4) or char.colliderect(pillar5) or char.colliderect(pillar6):
        nyawa -= 1
    #penambahan skor
    if pillar1.x == 100 or pillar2.x == 100 or pillar3.x == 100 or pillar4.x == 100 or pillar5.x == 100 or pillar6.x == 100:
        score += 1
    #karakter jatuh
    if char.y > 500 or char.y < 0:
        nyawa -= 1

#permainan berakhir
def gameover():
    global game_over
    if nyawa == 0:
        game_over = 1
    
#kontrol
def on_key_down(key):
    global new_image
    if keyboard.space or keyboard.up or keyboard.w:
        char.y -= 35
        animate(char, tween='bounce_end', duration=5, y=550)
        if new_image != 'rsz_1jump':
            char.image = 'rsz_1jump'
            new_image = 'rsz_1jump'
        else:
            if new_image != 'chara':
                char.image = 'chara'
                new_image = 'chara'
                
    else:
        if new_image != 'chara':
            char.image = 'chara'
            new_image = 'chara'

pgzrun.go()