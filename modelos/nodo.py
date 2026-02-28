import pygame
from configuracion import BLANCO, NEGRO, AZUL, PURPURA, ROJO, VERDE, AMARILLO, AMARILLO_ARENOSO, VERDE_PANTANOSO


class Nodo:
    def __init__(self, fila, columna, ancho, total_filas):
        self.fila = fila
        self.columna = columna
        self.x = self.fila * ancho
        self.y = self.columna * ancho
        self.color = BLANCO
        self.colorAnterior = BLANCO
        self.vecinos = []
        self.ancho = ancho
        self.total_filas = total_filas
        self.tipo_terreno = "normal"
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.ancho))
        
    def es_barrera(self):
        return self.color == NEGRO
    
    def es_arena(self):
        return self.color == AMARILLO_ARENOSO
    
    def es_pantano(self):
        return self.color == VERDE_PANTANOSO
    
    def es_inicio(self):
        return self.color == AZUL
    
    def es_fin(self):
        return self.color == PURPURA
    
    def reiniciar(self):
        self.color = BLANCO
    
    def hacer_inicio(self):
        self.color = AZUL
    
    def hacer_barrera(self):
        self.color = NEGRO
    
    def hacer_arena(self):
        self.color = AMARILLO_ARENOSO
        self.tipo_terreno = "arena"
    
    def hacer_pantano(self):
        self.color = VERDE_PANTANOSO
        self.tipo_terreno = "pantano"
    
    def hacer_fin(self):
        self.color = PURPURA
        
    def obtener_pos(self):
        return self.fila, self.columna
    
    def hacer_cerrado(self):
        if self.es_arena() or self.es_pantano():
            self.colorAnterior = self.color
        self.color = ROJO
        
    def hacer_abierto(self):
        if self.es_arena() or self.es_pantano():
            self.colorAnterior = self.color
        self.color = VERDE
        
    def hacer_camino(self):
        if self.es_arena() or self.es_pantano():
            self.colorAnterior = self.color
        self.color = AMARILLO
        
    def actualizar_vecinos(self, cuadricula):
        self.vecinos = []
        
        if self.fila < self.total_filas - 1 and not cuadricula[self.fila + 1][self.columna].es_barrera():
            self.vecinos.append(cuadricula[self.fila + 1][self.columna])
        
        if self.fila > 0 and not cuadricula[self.fila - 1][self.columna].es_barrera():
            self.vecinos.append(cuadricula[self.fila - 1][self.columna])
        
        if self.columna < self.total_filas - 1 and not cuadricula[self.fila][self.columna + 1].es_barrera():    
            self.vecinos.append(cuadricula[self.fila][self.columna + 1])
        
        if self.columna > 0 and not cuadricula[self.fila][self.columna - 1].es_barrera():
            self.vecinos.append(cuadricula[self.fila][self.columna - 1])
    
    def obtener_costo(self):
        if self.es_arena():
            return 2
        elif self.es_pantano():
            return 4
        else:
            return 1
    
    def __lt__(self, otro):
        return False