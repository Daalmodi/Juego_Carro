import pygame
import random
# Configuración de la ventana
ancho, alto = 800, 800
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de Carreras Kodland")
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
    # Cargar imágenes
fondo = pygame.image.load("fondo.png")  # Asegúrate de tener un archivo de fondo "fondo.png" en tudirectorio de trabajo
jugador_imagen = pygame.image.load("jugador.png")  # Asegúrate de tener una imagen de jugador "jugador.png"

# Escalar imágenes
fondo = pygame.transform.scale(fondo, (ancho, alto))
jugador_imagen = pygame.transform.scale(jugador_imagen, (70, 163.35 ))

# Variables del jugador
jugador_x = ancho // 2 - 35
jugador_y = alto - 200
jugador_velocidad = 5

# Variables de los obstáculos
obstaculos = []
obstaculo_velocidad = 5
obstaculo_ancho = 50
obstaculo_alto = 50

# Puntuación
puntuacion = 0


    
#Funcion de inicialización 
def menu_inicializacion():
    pygame.font.init()
    fuente_menu =pygame.font.Font(None,48)
    dificultades    =   ["Facil","Medio","Dificil"]
    seleccion = 0;
    while True:
        ventana.fill(NEGRO)
        for i, dificultad in enumerate(dificultades):
            color = BLANCO if i == seleccion else (100, 100, 100)
            texto = fuente_menu.render(dificultad, True, color)
            x = ancho // 2 - texto.get_width() // 2
            y = alto // 2 - len(dificultades) * 30 + i * 60
            ventana.blit(texto, (x, y))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(dificultades)
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(dificultades)
                if evento.key == pygame.K_RETURN:
                    return dificultades[seleccion]
# Función para generar obstáculos
def crear_obstaculo():
    x = random.randint(0, ancho - obstaculo_ancho)
    y = -obstaculo_alto
    obstaculos.append([x, y])
# Inicialización de Pygame
pygame.init()



# Fuente
fuente = pygame.font.Font(None, 36)

dificultad_seleccionada = menu_inicializacion()

if dificultad_seleccionada == "Facil":
    obstaculo_velocidad = 3
    print(obstaculo_velocidad)
elif dificultad_seleccionada == "Medio":
    obstaculo_velocidad = 5
elif dificultad_seleccionada == "Dificil":
    obstaculo_velocidad = 7


# Loop principal del juego

jugando = True
reloj = pygame.time.Clock()
crear_obstaculo()  # Comenzar con un obstáculo

while jugando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador_x -= jugador_velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_x += jugador_velocidad

    # Mover obstáculos
    for obstaculo in obstaculos:
        obstaculo[1] += obstaculo_velocidad

    # Verificar colisiones
    for obstaculo in obstaculos:
        if jugador_x < obstaculo[0] + obstaculo_ancho and jugador_x + 50 > obstaculo[0] and jugador_y < obstaculo[1] + obstaculo_alto and jugador_y + 50 > obstaculo[1]:
            # Colisión detectada
            jugando = False
    puntuacion +=1

    # Eliminar obstáculos que están fuera de la pantalla
    obstaculos = [obstaculo for obstaculo in obstaculos if obstaculo[1] < alto]

    # Generar nuevos obstaculos
    if len(obstaculos) < 5:  # Limitar la cantidad de obstáculos en pantalla
        crear_obstaculo()

    ventana.blit(fondo, (0, 0))
    ventana.blit(jugador_imagen, (jugador_x, jugador_y))
    
    for obstaculo in obstaculos:
        pygame.draw.rect(ventana, BLANCO, (obstaculo[0], obstaculo[1], obstaculo_ancho, obstaculo_alto))

    # Muestra puntuación
    texto = fuente.render(f'Puntuación: {puntuacion}', True, BLANCO)
    ventana.blit(texto, (10, 10))

    pygame.display.flip()

    reloj.tick(60)

#  Fin de juego
ventana.fill(NEGRO)
texto = fuente.render(f'¡Juego Terminado! Puntuación: {puntuacion}', True, BLANCO)
ventana.blit(texto, (ancho // 2 - texto.get_width() // 2, alto // 2 - texto.get_height() // 2))
pygame.display.flip()

# Esperar un momento antes de salir
pygame.time.delay(2000)

# Salir del juego
pygame.quit()
