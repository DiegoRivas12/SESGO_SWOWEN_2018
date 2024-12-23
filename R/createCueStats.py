import matplotlib.pyplot as plt
from importDataFunctions import import_data_swow
from networkFunctions import create_graph, normalize_edge_weights,compute_edge_table
import networkx as nx
# Configuración
data_file = './data/2018/processed/SWOW-EN.R100.csv'
response = 'R123'

# Importar y procesar datos
data = import_data_swow(data_file, response)

# Crear y procesar grafo
G = create_graph(data)
G = normalize_edge_weights(G)

# Calcular estadísticas
network_stats = {
    "transitivity": nx.transitivity(G),
    "density": nx.density(G) * 100,
    "nodes": G.number_of_nodes(),
    "edges": G.number_of_edges(),
    "avg_in_degree": sum(d for _, d in G.in_degree()) / G.number_of_nodes(),
    "avg_out_degree": sum(d for _, d in G.out_degree()) / G.number_of_nodes(),
}

# Mostrar estadísticas
print("Estadísticas del grafo:")
for stat, value in network_stats.items():
    print(f"{stat}: {value}")

# Graficar histogramas
plt.figure(figsize=(12, 6))

# Distribución de nodos por grado entrante
in_degrees = [d for _, d in G.in_degree()]
plt.subplot(1, 2, 1)
plt.hist(in_degrees, bins=30, color='skyblue', edgecolor='black')
plt.title('Distribución de Grados Entrantes')
plt.xlabel('Grado Entrante')
plt.ylabel('Frecuencia')

# Distribución de nodos por grado saliente
out_degrees = [d for _, d in G.out_degree()]
plt.subplot(1, 2, 2)
plt.hist(out_degrees, bins=30, color='orange', edgecolor='black')
plt.title('Distribución de Grados Salientes')
plt.xlabel('Grado Saliente')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()
