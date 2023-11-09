import pgzrun
import random

# Mesures pantalla. No cal fer res més
WIDTH = 600
HEIGHT = 600

# Títol pantalla
TITLE = "Blowfish"

# Variables globals joc
puntuacio = 0
game_over = False

# Sprites
jugador = Actor('jugador')
jugador.centerx = WIDTH / 2
jugador.centery = HEIGHT / 2

menjar = Actor('menjar')
enemic1 = Actor('enemic')
enemic1.top = 0
enemic1.centerx = WIDTH / 2
enemic1.velx = 5
enemic1.vely = 5

enemic2 = Actor('enemic')
enemic2.left = 0
enemic2.centery = HEIGHT / 2
enemic2.velx = 5
enemic2.vely = 5

enemic3 = Actor('enemic')
enemic3.right = WIDTH
enemic3.centery = HEIGHT / 2
enemic3.velx = 5
enemic3.vely = 5

# Funció que mou el jugador en funció de les tecles presionades
# Aquesta funció es cridada en cada frame
def mou_jugador():
    if keyboard.LEFT and jugador.left > 0:
        jugador.centerx -= 5
    if keyboard.RIGHT and jugador.right < WIDTH:
        jugador.centerx += 5
    if keyboard.UP and jugador.top > 0:
        jugador.centery -= 5
    if keyboard.DOWN and jugador.bottom < HEIGHT:
        jugador.centery += 5

# Funció que mourà els enemics de forma automàtica
# Aquesta funció és cridada en cada frame
def mou_enemics():
    # Enemic 1
    if enemic1.left < 0 or enemic1.right > WIDTH:
        enemic1.velx *= -1
    if enemic1.top < 0 or enemic1.bottom > HEIGHT:
        enemic1.vely *= -1
    enemic1.centerx += enemic1.velx
    enemic1.centery += enemic1.vely

    # Enemic 2
    if enemic2.left < 0 or enemic2.right > WIDTH:
        enemic2.velx *= -1
    if enemic2.top < 0 or enemic2.bottom > HEIGHT:
        enemic2.vely *= -1
    enemic2.centerx += enemic2.velx
    enemic2.centery += enemic2.vely

    # Enemic 3
    if enemic3.left < 0 or enemic3.right > WIDTH:
        enemic3.velx *= -1
    if enemic3.top < 0 or enemic3.bottom > HEIGHT:
        enemic3.vely *= -1
    enemic3.centerx += enemic3.velx
    enemic3.centery += enemic3.vely

# Funció que posiciona el menjar en una posició aleatòria dins la pantalla
def posicio_menjar():
    menjar.centerx = random.randint(0+round(menjar.width/2), WIDTH-round(menjar.width/2))
    menjar.centery = random.randint(0+round(menjar.height/2), HEIGHT-round(menjar.height/2))

# La cridem un primer cop en començar el joc
posicio_menjar()

# Comença música
music.play("island_meet_greet")

def draw():
    # Netegem pantalla dibuixant-la tota de blanc
    screen.fill((255, 255, 255))

    jugador.draw()
    menjar.draw()
    enemic1.draw()
    enemic2.draw()
    enemic3.draw()

    # Actualitzem el text de la puntuació a cada frame
    screen.draw.text("Puntuació: " + str(puntuacio), left=5, top=5, color=(0, 0, 0), 
        fontsize=25, fontname="gloria-hallelujah")

    # Si s'ha produït el game over mostrem el text
    if game_over:
        screen.draw.text("GAME OVER", centerx=WIDTH/2, centery=HEIGHT/2, color=(0, 0, 0), 
            fontsize=80, fontname="gloria-hallelujah")

def update():
    global puntuacio, game_over

    if game_over:
        return
    
    # Col·lisió del jugador amb el menjar
    if jugador.colliderect(menjar):
        puntuacio += 1
        # Reproduim so
        sounds.menja_peix.play()
        posicio_menjar()
    
    # Col·lisió del jugador amb un dels enemics
    if jugador.colliderect(enemic1) or jugador.colliderect(enemic2) or jugador.colliderect(enemic3):
        game_over = True
        # Reproduim so
        sounds.game_over.play()
        # Aturem música del joc
        music.stop()

    # A cada frame cridem les funcions per moure el jugador i els enemics
    mou_jugador()
    mou_enemics()

if __name__ == 'pgzero.builtins':
     pgzrun.go()