
# Juego de Carreras Kodland

Este es un juego de carreras simple creado con Pygame. El juego incluye un menú de inicialización que permite al jugador elegir la dificultad antes de comenzar a jugar. El objetivo del juego es esquivar obstáculos y acumular puntos.



### Requisitos
- Python 3.x
- Pygame

### Ejecución
1. Asegúrate de tener las imágenes `fondo.png` y `jugador.png` en el mismo directorio que el código del juego.
2. Ejecuta el archivo Python `Game.py` para iniciar el juego.

## Características del juego

- La ventana del juego tiene un tamaño de 800x800 píxeles y muestra un fondo y un personaje (jugador).
- El jugador puede moverse hacia la izquierda y hacia la derecha utilizando las teclas de dirección.
- Se generan obstáculos aleatorios que se mueven hacia abajo.
- El jugador acumula puntos a medida que evita colisionar con los obstáculos.
- El juego termina cuando el jugador colisiona con un obstáculo de frente.
- El juego incluye tres niveles de dificultad: Fácil, Medio y Difícil, que se pueden seleccionar en el menú de inicialización.

## Personalización de la dificultad
- La velocidad de los obstáculos se ajusta según la dificultad seleccionada en el menú de inicialización.
- La velocidad predeterminada de los obstáculos es de 5 unidades por fotograma.
- En la dificultad "Fácil", la velocidad de los obstáculos se reduce a 3 unidades por fotograma.
- En la dificultad "Difícil", la velocidad de los obstáculos se aumenta a 7 unidades por fotograma.

## Control del juego
- Tecla de flecha izquierda: Mover el jugador hacia la izquierda.
- Tecla de flecha derecha: Mover el jugador hacia la derecha.

## Puntuación
- La puntuación se muestra en la parte superior izquierda de la ventana del juego.
- La puntuación se incrementa a medida que el jugador evita colisionar con obstáculos.

## Fin del juego
- Cuando el jugador colisiona con un obstáculo, el juego muestra un mensaje de "Juego Terminado" y la puntuación final.
- Después de unos segundos, el juego se cierra automáticamente.



