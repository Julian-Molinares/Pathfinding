import pygame
import sys
from collections import deque
import heapq

ANCHO = 800
ALTO = 800
FILAS = 40
COLUMNAS = 40

BLANCO = (255, 255, 255)
GRIS = (128, 128, 128)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
PURPURA = (128, 0, 128)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)

class Nodo:
    def __init__(self, fila, columna, ancho, total_filas):
        self.fila = fila
        self.columna = columna
        self.x = self.fila * ancho
        self.y = self.columna * ancho
        self.color = BLANCO
        self.vecinos = []
        self.ancho = ancho
        self.total_filas = total_filas
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.ancho))
        
    def es_barrera(self):
        return self.color == NEGRO
    
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
    
    def hacer_fin(self):
        self.color = PURPURA
        
    def obtener_pos(self):
        return self.fila, self.columna
    
    def hacer_cerrado(self):
        self.color = ROJO
        
    def hacer_abierto(self):
        self.color = VERDE
        
    def hacer_camino(self):
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
    
    def __lt__(self, otro):
        return False

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

def obtener_pos_clic(pos, filas, ancho):
    espacio = ancho // filas
    y, x = pos
    fila = y // espacio
    columna = x // espacio
    
    if fila < 0 or fila >= filas or columna < 0 or columna >= filas:
        return None, None
    
    return fila, columna

def reconstruir_camino(vino_de, actual, dibujar):
    while actual in vino_de:
        actual = vino_de[actual]
        if not actual.es_inicio():
            actual.hacer_camino()
        dibujar()

def dijkstra(dibujar, cuadricula, inicio, fin):
    contador = 0
    conjunto_abierto = []
    heapq.heappush(conjunto_abierto, (0, contador, inicio))
    vino_de = {}
    
    distancia = {nodo: float("inf") for fila in cuadricula for nodo in fila}
    distancia[inicio] = 0
    
    hash_conjunto_abierto = {inicio}
    
    while conjunto_abierto:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        actual = heapq.heappop(conjunto_abierto)[2]
        hash_conjunto_abierto.remove(actual)
        
        if actual == fin:
            reconstruir_camino(vino_de, fin, dibujar)
            fin.hacer_fin()
            inicio.hacer_inicio()
            return True
        
        for vecino in actual.vecinos:
            distancia_temporal = distancia[actual] + 1
            
            if distancia_temporal < distancia[vecino]:
                vino_de[vecino] = actual
                distancia[vecino] = distancia_temporal
                
                if vecino not in hash_conjunto_abierto:
                    contador += 1
                    heapq.heappush(conjunto_abierto, (distancia[vecino], contador, vecino))
                    hash_conjunto_abierto.add(vecino)
                    vecino.hacer_abierto()
        
        dibujar()
        
        if actual != inicio:
            actual.hacer_cerrado()
    
    return False

def bfs(dibujar, cuadricula, inicio, fin):
    cola = deque([inicio])
    vino_de = {}
    visitados = {inicio}
    
    while cola:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        actual = cola.popleft()
        
        if actual == fin:
            reconstruir_camino(vino_de, fin, dibujar)
            fin.hacer_fin()
            inicio.hacer_inicio()
            return True
        
        for vecino in actual.vecinos:
            if vecino not in visitados:
                visitados.add(vecino)
                vino_de[vecino] = actual
                cola.append(vecino)
                vecino.hacer_abierto()
        
        dibujar()
        
        if actual != inicio:
            actual.hacer_cerrado()
    
    return False

def dfs(dibujar, cuadricula, inicio, fin):
    pila = [inicio]
    vino_de = {}
    visitados = {inicio}
    
    while pila:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        actual = pila.pop()
        
        if actual == fin:
            reconstruir_camino(vino_de, fin, dibujar)
            fin.hacer_fin()
            inicio.hacer_inicio()
            return True
        
        for vecino in actual.vecinos:
            if vecino not in visitados:
                visitados.add(vecino)
                vino_de[vecino] = actual
                pila.append(vecino)
                if vecino != fin:
                    vecino.hacer_abierto()
        
        dibujar()
        
        if actual != inicio:
            actual.hacer_cerrado()
    
    return False

def principal(ventana, ancho):
    cuadricula = crear_cuadricula(FILAS, ancho)
    
    inicio = None
    fin = None
    
    ejecutando = True
    
    while ejecutando:
        dibujar(ventana, cuadricula, FILAS, ancho)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                fila, columna = obtener_pos_clic(pos, FILAS, ancho)
                
                if fila is not None and columna is not None:
                    nodo = cuadricula[fila][columna]
                    
                    if not inicio and nodo != fin:
                        inicio = nodo
                        inicio.hacer_inicio()
                    
                    elif not fin and nodo != inicio:
                        fin = nodo
                        fin.hacer_fin()
                    
                    elif nodo != fin and nodo != inicio:
                        nodo.hacer_barrera()
            
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                fila, columna = obtener_pos_clic(pos, FILAS, ancho)
                
                if fila is not None and columna is not None:
                    nodo = cuadricula[fila][columna]
                    nodo.reiniciar()
                    
                    if nodo == inicio:
                        inicio = None
                    elif nodo == fin:
                        fin = None
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_c:
                    inicio = None
                    fin = None
                    cuadricula = crear_cuadricula(FILAS, ancho)
                
                if evento.key == pygame.K_d and inicio and fin:
                    for fila in cuadricula:
                        for nodo in fila:
                            nodo.actualizar_vecinos(cuadricula)
                    dijkstra(lambda: dibujar(ventana, cuadricula, FILAS, ancho), cuadricula, inicio, fin)
                    
                if evento.key == pygame.K_b and inicio and fin:
                    for fila in cuadricula:
                        for nodo in fila:
                            nodo.actualizar_vecinos(cuadricula)
                    bfs(lambda: dibujar(ventana, cuadricula, FILAS, ancho), cuadricula, inicio, fin)
                    
                if evento.key == pygame.K_s and inicio and fin:
                    for fila in cuadricula:
                        for nodo in fila:
                            nodo.actualizar_vecinos(cuadricula)
                    dfs(lambda: dibujar(ventana, cuadricula, FILAS, ancho), cuadricula, inicio, fin)
    
    pygame.quit()

if __name__ == "__main__":
    VENTANA = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Visualizador de Algoritmos de Pathfinding")
    principal(VENTANA, ANCHO)