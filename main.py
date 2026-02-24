import pygame
import sys

ANCHO = 800
ALTO = 800
FILAS = 40
COLUMNAS = 40

BLANCO = (255, 255, 255)
GRIS = (128, 128, 128)

class Nodo:
    def __init__(self, fila, columna, ancho, total_filas):
        self.fila = fila
        self.columna = columna
        self.x = self.fila * ancho
        self.y = self.columna * ancho
        self.color = BLANCO
        self.ancho = ancho
        self.total_filas = total_filas
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.ancho))

def crear_cuadricula(filas, ancho):
    cuadricula = []
    espacio = ancho // filas
    for i in range(filas):
        cuadricula.append([])
        for j in range(filas):
            nodo = Nodo(i, j, espacio, filas)
            cuadricula[i].append(nodo)
    return cuadricula

def dibujar_cuadricula(ventana, filas, ancho):
    espacio = ancho // filas
    for i in range(filas):
        pygame.draw.line(ventana, GRIS, (0, i * espacio), (ancho, i * espacio))
        for j in range(filas):
            pygame.draw.line(ventana, GRIS, (j * espacio, 0), (j * espacio, ancho))

def dibujar(ventana, cuadricula, filas, ancho):
    ventana.fill(BLANCO)
    
    for fila in cuadricula:
        for nodo in fila:
            nodo.dibujar(ventana)
    
    dibujar_cuadricula(ventana, filas, ancho)
    pygame.display.update()

def principal(ventana, ancho):
    cuadricula = crear_cuadricula(FILAS, ancho)
    
    ejecutando = True
    
    while ejecutando:
        dibujar(ventana, cuadricula, FILAS, ancho)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
    
    pygame.quit()

if __name__ == "__main__":
    VENTANA = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Visualizador de Algoritmos de Pathfinding")
    principal(VENTANA, ANCHO)