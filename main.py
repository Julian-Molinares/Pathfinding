import pygame
from configuracion import ANCHO, ALTO, FILAS
from interfaz import Visualizador


def main():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Visualizador de Algoritmos de Pathfinding")
    
    visualizador = Visualizador(ventana, ANCHO, FILAS)
    visualizador.ejecutar()


if __name__ == "__main__":
    main()