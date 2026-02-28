# Visualizador de Algoritmos de Pathfinding

Proyecto que permite visualizar y comparar los comportamientos de distinsos algoritmos de buscado o "Pathfinding" en una cuadrícula que simula un laberinto, implementando barreras, arena y pantano como distintos tipos de terreno. Se hizo uso de la libreria Pygame.

## Indice

- [Instalación](#instalación)
- [Cómo Usar](#cómo-usar)
- [Algoritmos Usados](#algoritmos-usados)
- [¿Por qué A* es más eficiente que BFS?](#por-qué-a-es-más-eficiente-que-bfs)

## Instalación

### Requisitos Previos

- Python 3.8 +
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clona o descarga el proyecto**

2. **Crea un entorno virtual (recomendado)**
   ```bash
   python -m venv .venv
   ```

3. **Activa el entorno virtual**
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - En Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecuta el programa**
   ```bash
   python main.py
   ```

6. **Extra**
    En caso de no tener instalado python, se puede instalar en windows con el uso de winget, ejecutando el siguiente comando.
    ```bash
    winget install -e --id Python.Python.3.12
    ```
    En el caso de estar en linux se puede ejecutar el siguiente comando.
    ```bash
    sudo apt install python3.12
    ```

## ¿Cómo usarlo?

### Controles del Mouse

| Acción | Descripción |
|--------|-------------|
| **Clic Izquierdo** (primer clic) | Establece el **nodo inicial** (azul) |
| **Clic Izquierdo** (segundo clic) | Establece el **nodo final** (púrpura) |
| **Clic Izquierdo** (clics siguientes) | Crea **barreras** (negro) |
| **Clic Izquierdo + N** | Crea **arena** (amarillo arenoso) - costo de movimiento: 2 |
| **Clic Izquierdo + M** | Crea **pantano** (verde pantanoso) - costo de movimiento: 4 |
| **Clic Derecho** | Borra el nodo seleccionado |

### Controles del Teclado

| Tecla | Acción |
|-------|--------|
| **D** | Ejecuta el algoritmo **Dijkstra** |
| **B** | Ejecuta el algoritmo **BFS** (Breadth-First Search) |
| **S** | Ejecuta el algoritmo **DFS** (Depth-First Search) |
| **A** | Ejecuta el algoritmo **A*** (A-Star) |
| **C** | **Limpia toda la cuadrícula** y reinicia |

### Representación de los colores en los algoritmos

- **Azul**: Nodo inicial
- **Púrpura**: Nodo final
- **Negro**: Barrera (obstáculo)
- **Amarillo arenoso**: Terreno de arena (costo 2)
- **Verde pantanoso**: Terreno de pantano (costo 4)
- **Verde**: Nodos en la **lista abierta** (por explorar)
- **Rojo**: Nodos en la **lista cerrada** (ya explorados)
- **Amarillo**: **Camino final** encontrado

### Ejemplo de uso

1. **Primer clic izquierdo**: Coloca el punto de inicio (azul)
2. **Segundo clic izquierdo**: Coloca el punto de destino (púrpura)
3. **Dibuja obstáculos**: Clic izquierdo para barreras, o mantén N/M para terrenos especiales
4. **Ejecuta un algoritmo**: Presiona D, B, S o A
5. **Observa**: Los nodos verdes son explorados, rojos son visitados, amarillo es el camino más optimo según el algoritmo
6. **Compara algoritmos**: Si quieres mantener el mismo terreno, inicio y fin, solo presiona otro algoritmo. En caso de que quieras cambiar el terreno presiona C
7. **Configura**: Experimenta con diferentes configuraciones a través del archivo **configuración.py**

## Configuración Extra

A través del archivo **configuración.py** puedes acceder a los distintos atributos que determinan los colores de las barreras, tipos de terreno, nodos de inicio o fin. Además,
puedes configurar el tamaño de la ventana, así como, el tamaño de filas y columnas pero cuidado con los valores insertados ya que pueden afectar a la visualización.
El atributo **DELAY_VISUALIZACION** determina que tan rapido es el cambio de colores, entre menor el valor más rapido sera el cambio.

## Algoritmos Usados

### 1. **Dijkstra**

**Descripción**: Algoritmo de búsqueda que encuentra el camino más corto desde un nodo inicial a todos los demás nodos del grafo. Garantiza encontrar el camino óptimo.

**Cómo funciona**:
1. Inicializa todas las distancias a infinito excepto el nodo inicial (distancia 0)
2. Usa una cola de prioridad ordenada por distancia acumulada
3. Extrae el nodo con menor distancia
4. Actualiza las distancias de sus vecinos considerando el costo del terreno
5. Repite hasta encontrar el destino

---

### 2. **BFS (Breadth-First Search)**

**Descripción**: Algoritmo de búsqueda que explora nivel por nivel, visitando todos los nodos a una distancia k antes de visitar nodos a distancia k+1.

**Cómo funciona**:
1. Usa una cola FIFO (First In, First Out)
2. Comienza desde el nodo inicial
3. Visita todos los vecinos del nodo actual
4. Añade los vecinos no visitados a la cola
5. Repite con el siguiente nodo de la cola

---

### 3. **DFS (Depth-First Search)**

**Descripción**: Algoritmo de búsqueda que explora lo más profundo posible por cada rama antes de retroceder.

**Cómo funciona**:
1. Usa una pila LIFO (Last In, First Out)
2. Comienza desde el nodo inicial
3. Visita un vecino no visitado
4. Repite desde ese vecino (profundizando)
5. Retrocede cuando no hay vecinos sin visitar

---

### 4. **A\* (A-Star)**

**Descripción**: Algoritmo de búsqueda informada que usa una función heurística para guiar la búsqueda hacia el objetivo de manera eficiente.

**Cómo funciona**:
1. Usa dos funciones de puntuación:
   - **g(n)**: Costo real desde el inicio hasta el nodo n
   - **h(n)**: Heurística estimada desde n hasta el objetivo (distancia Manhattan)
   - **f(n) = g(n) + h(n)**: Puntuación total
2. Usa una cola de prioridad ordenada por f(n)
3. Extrae el nodo con menor f(n)
4. Actualiza los costos de sus vecinos
5. Repite hasta encontrar el destino

**Heurística utilizada**: Distancia de Manhattan: `|x1 - x2| + |y1 - y2|`

## ¿Por qué A\* es más eficiente que BFS?

### Exploración Dirigida vs. Exploración Ciega

**BFS** es un algoritmo de búsqueda **no informada** (ciega) que explora el espacio de búsqueda de manera uniforme en todas direcciones. No tiene conocimiento sobre dónde está el objetivo, por lo que debe explorar todos los nodos a una distancia k antes de explorar nodos a distancia k+1, sin importar si se están alejando o acercando al destino.

**A\***, por otro lado, es un algoritmo de búsqueda **informada** que utiliza una función heurística (distancia de Manhattan en este caso) para estimar qué tan cerca está cada nodo del objetivo.

**Ventaja de costos**: A* también considera los costos de terreno (arena y pantano), mientras que BFS trata todos los movimientos como iguales, lo que hace que A* no solo sea más eficiente sino también capaz de encontrar caminos realmente óptimos en términos de costo total.