from .pathfinder import Pathfinder


class DFS(Pathfinder):
    def ejecutar(self):
        pila = [self.inicio]
        vino_de = {}
        visitados = {self.inicio}
        
        while pila:
            self.verificar_eventos()
            
            actual = pila.pop()
            
            if actual == self.fin:
                self.reconstruir_camino(vino_de, self.fin)
                self.fin.hacer_fin()
                self.inicio.hacer_inicio()
                return True
            
            for vecino in actual.vecinos:
                if vecino not in visitados:
                    visitados.add(vecino)
                    vino_de[vecino] = actual
                    pila.append(vecino)
                    if vecino != self.fin:
                        vecino.hacer_abierto()
            
            self.dibujar_callback()
            self.delay_visualizacion()
            
            if actual != self.inicio:
                actual.hacer_cerrado()
        
        return False