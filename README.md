# Blowfish

Joc desenvolupat amb Python i la llibreria PyGame Zero.

Imatges dels sprites: [Kenney - Fish Pack](https://kenney.nl/assets/fish-pack)

Sons del joc: [Kenney - Music Jingles](https://kenney.nl/assets/music-jingles)

Música del joc: [Incompetech - Island Meet and Greet](https://incompetech.com/music/royalty-free/music.html)

## Configuració bàsica de la pantalla de joc

El següent codi crearà una pantalla de joc en blanc.

```
import pgzrun
import random

# Mesures pantalla
WIDTH = 600
HEIGHT = 600

# Títol pantalla
TITLE = "Blowfish"

# Variables globals joc
puntuacio = 0
game_over = False

# Funció cridada 60 cops per segons (FPS) i que serveix per dibuixar l'escena
def draw():
    pass

# Funció cridada 60 cops per segons (FPS) i que serveix per moure elements i comprovar col·lissions
def update():
    pass

if __name__ == 'pgzero.builtins':
     pgzrun.go()
```

Les constants ***WIDTH***, ***HEIGHT*** i ***TITLE*** serveixen per definir amplada, alçada i títol de la pantalla respectivament.

Les funcions ***draw()*** i ***update()*** són molt importants. Aquestes dues funcions són cridades per la llibreria 60 cops per segons (FPS - *Frame Per Second*). La funció *draw()* serà utilitzada per netejar la pantalla i tornar a dibuixar els sprites en cada frame. La funció *update()* s'encarregarà de moure els elements, comprovar les col·lissions i els events de teclat i/o ratolí.

## Sprite del jugador
En la part principal del codi (abans de les funcions *draw()* i *update()*), creem un primer sprite, el del jugador i el col·loquem a la posició inicial.

```
# Sprites
jugador = Actor('jugador')
jugador.centerx = WIDTH / 2
jugador.centery = HEIGHT / 2
```

Crearem una nova funció per moure el jugador dins els límits de la pantalla:
```
def mou_jugador():
    if keyboard.LEFT and jugador.left > 0:
        jugador.centerx -= 5
    if keyboard.RIGHT and jugador.right < WIDTH:
        jugador.centerx += 5
    if keyboard.UP and jugador.top > 0:
        jugador.centery -= 5
    if keyboard.DOWN and jugador.bottom < HEIGHT:
        jugador.centery += 5
```

A la funció *update()* cridem aquesta funció per moure el jugador, si escau, en cada frame.

```
def update():
    mou_jugador()
```
I a la funcio *draw()* pintell la pantalla de blanc i el jugador en cada frame.
```
def draw():
        # Pintem tota la pantalla de blanc (RGB)
        screen.fill((255, 255, 255))

        # Dibuixem el jugador
        jugador.draw()
```

## Sprite del menjar
Creem un segon sprite que serà el peix a menjar pel jugador.
```
menjar = Actor('menjar')
```

Per posicionar el menjar, crearem una funció que serà cridada cada cop que el jugador col·lisioni amb el sprite en una posició aleatòria. Just després de crear la funció la cridem per col·local el menjar el primer cop.

```
def posicio_menjar():
    menjar.centerx = random.randint(0+round(menjar.width/2), WIDTH-round(menjar.width/2))
    menjar.centery = random.randint(0+round(menjar.height/2), HEIGHT-round(menjar.height/2))

posicio_menjar()
```
Dibuixem el menjar en cada frame a la funció *draw()*.
```
def draw():
    ...

    menjar.draw()

    ...
```

En la funció *update()* comprovem si el jugador i el menjar al col·lisionat. En cas afirmatiu cal augmentar la puntuació i tornar a posicions el menjar, per la qual tasca tenim la funció *posicion_menjar()*.
```
def update():
    global puntuacio

    # Col·lisions
    if jugador.colliderect(menjar):
        puntuació += 1
        posicio_menjar()

    mou_jugador()
```
La variable ***puntuacio*** és una variable global. L'hem de definir com a global en la funció *udpate()* perquè hi pugui accedir.

Per mostrar la puntuació actualitzada per pantalla, actualitzem el text en cada frame en la funció *draw()*.
```
def draw():
    screen.fill((255, 255, 255))

    jugador.draw()
    menjar.draw()

    screen.draw.text("Puntuació: " + str(puntuacio), left=5, top=5, color=(0, 0, 0),
        fontsize=25, fontname="gloria-hallelujah")

```

## Sprites dels enemics
A la part principal del codi (abans de les funcions *draw()* i *update()*), creem i posicionem els sprites dels tres enemics.

```
...

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

...
```

Els enemics es mouran automàticament i en diagonal. Necessitem la velocitat de l'eix x (*velx*) i y (*vely*) de cada enemic.

Crearem un funció per moure els tres enèmics dins els límits de la pantalla.
```
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
```

Quan un enemic col·lisiona amb una de les quatre vores s'inverteix la seva velocitat multiplicant per -1, *velx* per les vores laterals o *vely* per les vores superios i inferiors.

Dibuixem els tres enemics a cada frame en la funció *draw()*.
```
def draw():
    ...

    enemic1.draw()
    enemic2.draw()
    enemic3.draw()

    ...
```

A la funció *update()*, comprovem si el jugador ha col·lisionat amb algun enemic i movem els enemics fent ús de la funció creada.
```
def udpate():
    global puntuacio, game_over

    if jugador.colliderect(enemic1) or jugador.colliderect(enemic2) or jugador.colliderect(enemic3):
        game_over = True

    ...

    mou_enemics()

    ...
```
***game_over*** torna a ser una variable global que necessitem utilitzar dins la funció *update()*.

## Sprites dels enemics
En produir-se el final del joc (Game Over) la pantalla es seguirà actualitzant a 60 FPS. En la funció draw dibuixarem el text de Game Over.
```
def draw():
    ...

    if game_over:
        screen.draw.text("GAME OVER", centerx=WIDTH/2, centery=HEIGHT/2, color=(0, 0, 0),
            fontsize=80, fontname="gloria-hallelujah")

```

En la funció *update()* posarem un return al principi per provocar que no executi la resta d'ordres de la funció i no modifique les posicions dels sprites ni comprovi col·lisions.
```
def update():
    global puntuacio, game_over

    if game_over:
        return

    ...
```


