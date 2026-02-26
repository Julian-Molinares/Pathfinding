import pygame
from interfaz.cuadricula import Cuadricula
from algoritmos import Dijkstra, BFS, DFS, AEstrella


class Visualizador:
    def __init__(self, ventana, ancho, filas):
        self.ventana = ventana
        self.ancho = ancho
        self.filas = filas
        self.cuadricula = Cuadricula(filas, ancho)
        self.inicio = None
        self.fin = None
        self.ejecutando = True
    
    def dibujar(self):
        self.cuadricula.dibujar(self.ventana)
    
    def manejar_clic_izquierdo(self, pos):
        fila, columna = self.cuadricula.obtener_pos_clic(pos)
        
        if fila is not None and columna is not None:
            nodo = self.cuadricula.obtener_nodo(fila, columna)
            
            if not self.inicio and nodo != self.fin:
                self.inicio = nodo
                self.inicio.hacer_inicio()
            
            elif not self.fin and nodo != self.inicio:
                self.fin = nodo
                self.fin.hacer_fin()
            
            elif nodo != self.fin and nodo != self.inicio:
                nodo.hacer_barrera()
    
    def manejar_clic_derecho(self, pos):
        fila, columna = self.cuadricula.obtener_pos_clic(pos)
        
        if fila is not None and columna is not None:
            nodo = self.cuadricula.obtener_nodo(fila, columna)
            nodo.reiniciar()
            
            if nodo == self.inicio:
                self.inicio = None
            elif nodo == self.fin:
                self.fin = None
    
    def ejecutar_algoritmo(self, AlgoritmoClase):
        if self.inicio and self.fin:
            self.cuadricula.actualizar_vecinos_todos()
            algoritmo = AlgoritmoClase(
                self.cuadricula.cuadricula, 
                self.inicio, 
                self.fin, 
                self.dibujar
            )
            algoritmo.ejecutar()
    
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                self.manejar_clic_izquierdo(pos)
            
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                self.manejar_clic_derecho(pos)
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_c:
                    self.inicio = None
                    self.fin = None
                    self.cuadricula.reiniciar()
                
                elif evento.key == pygame.K_d:
                    self.cuadricula.limpiar_cuadricula()
                    self.ejecutar_algoritmo(Dijkstra)
                
                elif evento.key == pygame.K_b:
                    self.cuadricula.limpiar_cuadricula()
                    self.ejecutar_algoritmo(BFS)
                
                elif evento.key == pygame.K_s:
                    self.cuadricula.limpiar_cuadricula()
                    self.ejecutar_algoritmo(DFS)
                
                elif evento.key == pygame.K_a:
                    self.cuadricula.limpiar_cuadricula()
                    self.ejecutar_algoritmo(AEstrella)
    
    def ejecutar(self):
        while self.ejecutando:
            self.dibujar()
            self.manejar_eventos()
        
        pygame.quit()