import pygame
import sys
from abc import ABC, abstractmethod
from configuracion import DELAY_VISUALIZACION


class Pathfinder(ABC):
    def __init__(self, cuadricula, inicio, fin, dibujar_callback):
        self.cuadricula = cuadricula
        self.inicio = inicio
        self.fin = fin
        self.dibujar_callback = dibujar_callback
        self.delay = DELAY_VISUALIZACION
    
    @abstractmethod
    def ejecutar(self):
        pass
    
    def reconstruir_camino(self, vino_de, actual):
        while actual in vino_de:
            actual = vino_de[actual]
            if not actual.es_inicio():
                actual.hacer_camino()
            self.dibujar_callback()
            self.delay_visualizacion()
    
    def delay_visualizacion(self):
        pygame.time.delay(self.delay)
    
    def verificar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()