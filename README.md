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

Les constants *WIDTH*, *HEIGHT* i *TITLE* serveixen per definir amplada, alçada i títol de la pantalla respectivament.

Les funcions *draw()* i *update()* són molt importants. Aquestes dues funcions són cridades per la llibreria 60 cops per segons (FPS - *Frame Per Second*). La funció *draw()* serà utilitzada per netejar la pantalla i tornar a dibuixar els sprites en cada frame. La funció *update()* s'encarregarà de moure els elements, comprovar les col·lissions i els events de teclat i/o ratolí.

