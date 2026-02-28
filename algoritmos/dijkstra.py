import heapq
from .pathfinder import Pathfinder


class Dijkstra(Pathfinder):
    def ejecutar(self):
        contador = 0
        conjunto_abierto = []
        heapq.heappush(conjunto_abierto, (0, contador, self.inicio))
        vino_de = {}
        
        distancia = {nodo: float("inf") for fila in self.cuadricula for nodo in fila}
        distancia[self.inicio] = 0
        
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
                distancia_temporal = distancia[actual] + vecino.obtener_costo()
                
                if distancia_temporal < distancia[vecino]:
                    vino_de[vecino] = actual
                    distancia[vecino] = distancia_temporal
                    
                    if vecino not in hash_conjunto_abierto:
                        contador += 1
                        heapq.heappush(conjunto_abierto, (distancia[vecino], contador, vecino))
                        hash_conjunto_abierto.add(vecino)
                        if not vecino.es_arena() and not vecino.es_pantano() and vecino != self.fin:
                            vecino.hacer_abierto()
            
            self.dibujar_callback()
            self.delay_visualizacion()
            
            if actual != self.inicio:
                if not actual.es_arena() and not actual.es_pantano():
                    actual.hacer_cerrado()
        
        return False