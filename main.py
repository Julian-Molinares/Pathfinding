import pygame

ANCHO = 800
ALTO = 800
FILAS = 40
COLUMNAS = 40

BLANCO = (255, 255, 255)
GRIS = (128, 128, 128)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
PURPURA = (128, 0, 128)

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
    
    pygame.quit()

if __name__ == "__main__":
    VENTANA = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Visualizador de Algoritmos de Pathfinding")
    principal(VENTANA, ANCHO)