import pygame
import sys
from abc import ABC, abstractmethod


class Pathfinder(ABC):
    def __init__(self, cuadricula, inicio, fin, dibujar_callback):
        self.cuadricula = cuadricula
        self.inicio = inicio
        self.fin = fin
        self.dibujar_callback = dibujar_callback
    
    @abstractmethod
    def ejecutar(self):
        pass
    
    def reconstruir_camino(self, vino_de, actual):
        while actual in vino_de:
            actual = vino_de[actual]
            if not actual.es_inicio():
                actual.hacer_camino()
            self.dibujar_callback()
    
    def verificar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()