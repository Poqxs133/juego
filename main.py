import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
FPS = 60
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquivar obstáculos")
clock = pygame.time.Clock()

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Jugador
jugador = pygame.Rect(400, 500, 50, 50)
velocidad_jugador = 5

# Obstáculos
obstaculos = []
TAM_OBSTACULO = 50
velocidad_obstaculo = 5
tiempo_nuevo_obstaculo = pygame.USEREVENT + 1
pygame.time.set_timer(tiempo_nuevo_obstaculo, 1000)  # cada 1 segundo

# Bucle principal
jugando = True
while jugando:
    clock.tick(FPS)
    pantalla.fill(BLANCO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        if evento.type == tiempo_nuevo_obstaculo:
            x = random.randint(0, ANCHO - TAM_OBSTACULO)
            obstaculos.append(pygame.Rect(x, 0, TAM_OBSTACULO, TAM_OBSTACULO))

    # Movimiento jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador.left > 0:
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.x += velocidad_jugador

    # Mover obstáculos
    for obstaculo in obstaculos[:]:
        obstaculo.y += velocidad_obstaculo
        if obstaculo.top > ALTO:
            obstaculos.remove(obstaculo)
        if jugador.colliderect(obstaculo):
            print("¡Colisión! Game Over")
            jugando = False

    # Dibujar
    pygame.draw.rect(pantalla, AZUL, jugador)
    for obstaculo in obstaculos:
        pygame.draw.rect(pantalla, ROJO, obstaculo)

    pygame.display.flip()

pygame.quit()
sys.exit()
