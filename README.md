# Blowfish

Joc desenvolupat amb Python i la llibreria PyGame Zero.

Imatges dels sprites: https://kenney.nl/assets/fish-pack

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

Crearem una nova funció per moure el jugador:
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
