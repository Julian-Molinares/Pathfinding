import heapq
from .pathfinder import Pathfinder


class AEstrella(Pathfinder):
    @staticmethod
    def heuristica(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)
    
    def ejecutar(self):
        contador = 0
        conjunto_abierto = []
        heapq.heappush(conjunto_abierto, (0, contador, self.inicio))
        vino_de = {}
        
        puntaje_g = {nodo: float("inf") for fila in self.cuadricula for nodo in fila}
        puntaje_g[self.inicio] = 0
        
        puntaje_f = {nodo: float("inf") for fila in self.cuadricula for nodo in fila}
        puntaje_f[self.inicio] = self.heuristica(self.inicio.obtener_pos(), self.fin.obtener_pos())
        
        hash_conjunto_abierto = {self.inicio}
        
        while conjunto_abierto:
            self.verificar_eventos()
            
            actual = heapq.heappop(conjunto_abierto)[2]
            hash_conjunto_abierto.remove(actual)
            
            if actual == self.fin:
                self.reconstruir_camino(vino_de, self.fin)
                self.fin.hacer_fin()
                self.inicio.hacer_inicio()
                return True
            
            for vecino in actual.vecinos:
                puntaje_g_temporal = puntaje_g[actual] + vecino.obtener_costo()
                
                if puntaje_g_temporal < puntaje_g[vecino]:
                    vino_de[vecino] = actual
                    puntaje_g[vecino] = puntaje_g_temporal
                    puntaje_f[vecino] = puntaje_g_temporal + self.heuristica(vecino.obtener_pos(), self.fin.obtener_pos())
                    
                    if vecino not in hash_conjunto_abierto:
                        contador += 1
                        heapq.heappush(conjunto_abierto, (puntaje_f[vecino], contador, vecino))
                        hash_conjunto_abierto.add(vecino)
                        vecino.hacer_abierto()
            
            self.dibujar_callback()
            self.delay_visualizacion()
            
            if actual != self.inicio:
                actual.hacer_cerrado()
        
        return False