import pygame
from modelos import Nodo
from configuracion import GRIS, BLANCO, VERDE, ROJO, AMARILLO


class Cuadricula:
    def __init__(self, filas, ancho):
        self.filas = filas
        self.ancho = ancho
        self.espacio = ancho // filas
        self.cuadricula = self._crear_cuadricula()
    
    def _crear_cuadricula(self):
        cuadricula = []
        for i in range(self.filas):
            cuadricula.append([])
            for j in range(self.filas):
                nodo = Nodo(i, j, self.espacio, self.filas)
                cuadricula[i].append(nodo)
        return cuadricula
    
    def obtener_nodo(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.filas:
            return self.cuadricula[fila][columna]
        return None
    
    def reiniciar(self):
        self.cuadricula = self._crear_cuadricula()
    
    def actualizar_vecinos_todos(self):
        for fila in self.cuadricula:
            for nodo in fila:
                nodo.actualizar_vecinos(self.cuadricula)
    
    def dibujar(self, ventana):
        ventana.fill(BLANCO)
        
        for fila in self.cuadricula:
            for nodo in fila:
                nodo.dibujar(ventana)
        
        self._dibujar_lineas(ventana)
        pygame.display.update()
    
    def _dibujar_lineas(self, ventana):
        for i in range(self.filas):
            pygame.draw.line(ventana, GRIS, (0, i * self.espacio), (self.ancho, i * self.espacio))
            pygame.draw.line(ventana, GRIS, (i * self.espacio, 0), (i * self.espacio, self.ancho))
    
    def obtener_pos_clic(self, pos):
        y, x = pos
        fila = y // self.espacio
        columna = x // self.espacio
        
        if fila < 0 or fila >= self.filas or columna < 0 or columna >= self.filas:
            return None, None
        
        return fila, columna
    
    def limpiar_cuadricula(self):
        for fila in self.cuadricula:
            for nodo in fila:
                if nodo.color in [VERDE, ROJO, AMARILLO]:
                    if nodo.colorAnterior != BLANCO:
                        nodo.color = nodo.colorAnterior
                        nodo.colorAnterior = BLANCO
                    else:
                        nodo.reiniciar()