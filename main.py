import pgzrun, random
from pgzero.builtins import Actor, animate, keyboard

import pgzero.screen
screen: pgzero.screen.Screen

# Game window
WIDTH = 500
HEIGHT = 500

# Window's title and FPS
TITLE = "Twilight Fell"
FPS = 30

# Position for the object
pos_pillar1 = random.randint(50, 100)
pos_pillar2 = random.randint(400, 450)
pos_pillar3 = random.randint(50, 100)
pos_pillar4 = random.randint(400, 450)
pos_pillar5 = random.randint(50, 100)
pos_pillar6 = random.randint(400, 450)
pos_disc = random.randint(220, 280)
pos_heart = random.randint(220, 280)

# Calling the object randomly
call_object = random.randint(1, 500)

# Initializing object
bg = Actor('rsz_1bg')
pillar1 = Actor('rsz_1pillar_up', (550, pos_pillar1))
pillar2 = Actor('rsz_1pillar_down', (550, pos_pillar2))
pillar3 = Actor('rsz_1pillar_up', (750, pos_pillar3))
pillar4 = Actor('rsz_1pillar_down', (750, pos_pillar4))
pillar5 = Actor('rsz_1pillar_up', (950, pos_pillar5))
pillar6 = Actor('rsz_1pillar_down', (950, pos_pillar6))
char = Actor('chara', (120, 250)) 
heart = Actor('rsz_heart', (550, pos_heart))
shuriken = Actor('rsz_shuriken', (550, 250))
disc = Actor('rsz_disc', (550, pos_disc))
heart_count = Actor('rsz_heart', (430, 40))

object = (bg, pillar1, pillar2, pillar3, pillar4, pillar5, pillar6, char, heart, shuriken, disc, heart_count)

new_image = 'chara' # Jump
speed = 5 # Speed
life_count = 50 # Life
score = 0 # Score
game_over = False # Game over

# Draw objects to the game window
def draw():
    global pos_pillar1
    global pos_pillar2
    if game_over == False:
        for item in object:
            item.draw()
        screen.draw.text(f'{life_count}', pos=(450, 27), color='white', fontsize=24, background='black')
        screen.draw.text(f'{score}', pos=(250, 40), color="white", fontsize=40, background='black')
    else:
        bg.draw()
        screen.draw.text('Game Over', pos=(150, 220), color="white", fontsize=50, background='black')

# Move pillars
def pillar():
    index = 0
    for pillar in object[1:7]:
        if index % 2 == 0:
            if pillar.x > -20:
                pillar.x -= 5
            else:
                pillar.x = WIDTH + 75
                pillar.y = random.randint(50, 100)  
        else:
            if pillar.x > -20:
                pillar.x -= 5
            else:
                pillar.x = WIDTH + 75
                pillar.y = random.randint(400, 450)
        index += 1       
        
# Enemy A.K.A. shuriken
def enemy():
    global speed
    global call_object
    if shuriken.x > -20:
        shuriken.x -= 10
        shuriken.angle += 20
    else:
        shuriken.x = WIDTH + 20
        call_object = random.randint(1, 5)

# Heart
def life():
    global call_object
    if heart.x > -20:
        heart.x -= 5
    else:
        heart.x = WIDTH + 20
        heart.y = random.randint(220, 280)
        call_object = random.randint(1, 5)

# Colliding with object
def collide():
    global life_count
    global score
    if char.colliderect(shuriken): # Collide with enemy, shorten ur life
        life_count -= 1
    if char.colliderect(heart): # Collide with heart, gaining life
        if 40 < life_count < 50:
            life_count += (50 - life_count)
        elif life_count <= 40:
            life_count += 10
        heart.x = -15
    for pillar in object[1:7]: # Collide pillar, close to heaven (or maybe hell :0)
        if char.colliderect(pillar):
            life_count -= 1
        if pillar.x == 100:
            score += 1
    if char.y > 500 or char.y < 0: # Fall
        life_count -= 1

# Game over, means u are ded
def gameover():
    global game_over
    if life_count == 0:
        game_over = True

# Update
def update(dt):
    global call_object
    pillar()
    if call_object == 1:
        enemy()
    elif call_object % 50 == 0:
        life()
    else:
        call_object = random.randint(1, 500)
    collide()
    gameover()

# Keyboard control
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

pgzrun.go() # Run
