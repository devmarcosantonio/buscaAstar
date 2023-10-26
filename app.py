import networkx as nx
import matplotlib.pyplot as plt
from geopy.distance import geodesic

#criando o grafo
grafo = nx.Graph()


# Definindo os nós e suas características
municipios = {
    "Amajari": {"coordenadas": (3.64571, -61.3692), "dist_heuristica": None, "f_score": None},
    "Alto Alegre": {"coordenadas": (2.98858, -61.3072), "dist_heuristica": None, "f_score": None},
    "Boa Vista": {"coordenadas": (2.81954, -60.6714), "dist_heuristica": None, "f_score": None},
    "Bonfim": {"coordenadas": (3.36161, -59.8333), "dist_heuristica": None, "f_score": None},
    "Cantá": {"coordenadas": (2.60994, -60.6058), "dist_heuristica": None, "f_score": None},
    "Caracaraí": {"coordenadas": (1.8142432, -61.134494), "dist_heuristica": None, "f_score": None},
    "Caroebe": {"coordenadas": (0.884203, -59.6959), "dist_heuristica": None, "f_score": None},
    "Iracema": {"coordenadas": (2.18333, -61.0333), "dist_heuristica": None, "f_score": None},
    "Mucajaí": {"coordenadas": (2.43972, -60.9097), "dist_heuristica": None, "f_score": None},
    "Normandia": {"coordenadas": (3.88528, -59.6206), "dist_heuristica": None, "f_score": None},
    "Pacaraima": {"coordenadas": (4.47944, -61.1475), "dist_heuristica": None, "f_score": None},
    "Rorainópolis": {"coordenadas": (0.939444, -60.4381), "dist_heuristica": None, "f_score": None},
    "São João da Baliza": {"coordenadas": (0.951389, -59.9136), "dist_heuristica": None, "f_score": None},
    "São Luiz": {"coordenadas": (1.01083, -60.0417), "dist_heuristica": None, "f_score": None},
    "Uiramutã": {"coordenadas": (4.60306, -60.1817), "dist_heuristica": None, "f_score": None}
}


# Definindo conexões com pesos pegos no google maps (em km)
conexoes = [
    ("Amajari", "Pacaraima", {'weight':164}),  
    ("Amajari", "Alto Alegre", {'weight':145}), 
    ("Amajari", "Boa Vista", {'weight': 155}),  
    ("Alto Alegre", "Boa Vista", {'weight':84}),  
    ("Alto Alegre", "Mucajaí", {'weight': 125}),
    ("Boa Vista", "Mucajaí", {'weight': 58}),
    ("Boa Vista", "Uiramutã", {'weight': 289}),
    ("Boa Vista", "Normandia", {'weight': 187}),  
    ("Boa Vista", "Pacaraima", {'weight': 214}),  
    ("Boa Vista", "Bonfim", {'weight': 112}),  
    ("Boa Vista", "Cantá", {'weight': 36}),  
    ("Bonfim", "Normandia", {'weight': 131}),  
    ("Bonfim", "Cantá", {'weight': 123}),  
    ("Caracaraí", "Iracema", {'weight':44}),  
    ("Caracaraí", "Rorainópolis", {'weight':157}),  
    ("Caracaraí", "São Luiz", {'weight':172}),   
    ("Caroebe", "São João da Baliza", {'weight': 26}),  
    ("Cantá", "Rorainópolis", { "weight": 225}),
    ("Cantá", "São Luiz", { "weight": 225}),
    ("Iracema", "Mucajaí", { "weight":39}),  
    ("Normandia", "Pacaraima", {'weight':236}),  
    ("Normandia", "Uiramutã", {'weight':221}),  
    ("Pacaraima", "Uiramutã", {'weight':187}),  
    ("Rorainópolis", "São Luiz", {'weight':84}),   
    ("São Luiz", "São João da Baliza", {'weight':100})
]

# Adicionando nós com seus atributos e conexões ao grafo
for cidade, dados in municipios.items():
    grafo.add_node(cidade, **dados)
grafo.add_edges_from(conexoes)

    
# Criando o layout para posicionar os nós
pos = nx.spring_layout(grafo, seed=42)

# Configurando o plot do grafo.
nx.draw(grafo, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=8)
edge_labels = {(u, v): d['weight'] for u, v, d in grafo.edges(data=True)}
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels, font_size=8, label_pos=0.3)

# Plotando o grafo com título "Grafo dos Municípios de Roraima"
plt.title("Grafo dos Municípios de Roraima")
plt.show()

# função calculadora de distancia linear
# de um municipio até outro
def distancia_heuristica (coord_cidade1, coord_cidade2):
  distancia = geodesic(coord_cidade1, coord_cidade2).kilometers
  return distancia

# definir nó origem e objetivo
no_origem = "Uiramutã"
no_objetivo =  "Caroebe"

# Inicialize o nó de origem com distância heurística zero e f_score inicial
grafo.nodes[no_origem]['dist_heuristica'] = distancia_heuristica(
    grafo.nodes[no_origem]["coordenadas"],
    grafo.nodes[no_objetivo]["coordenadas"]
)
grafo.nodes[no_origem]['f_score'] = grafo.nodes[no_origem]['dist_heuristica']


# calculando a distancia linear (heuristica) de cada nó com o nó objetivo
for municipio in grafo.nodes():
    grafo.nodes[municipio]['dist_heuristica'] = distancia_heuristica(
        grafo.nodes[municipio]["coordenadas"],
        grafo.nodes[no_objetivo]["coordenadas"]
    )
    dist_heuristica = grafo.nodes[municipio]['dist_heuristica']
    # print(f"Distância Heurística de {municipio} até {no_objetivo}: {dist_heuristica:.2f} km")

#
def encontrar_menor_f_score():
    if (len(nos_abertos) == 1):
        return nos_abertos[0]
    else:
        menor_f_score = None
        municipio_menor_f_score = None

        for municipio in nos_abertos:
            f_score = grafo.nodes[municipio]["f_score"]
            if f_score is not None and (menor_f_score is None or f_score < menor_f_score):
                menor_f_score = f_score
                municipio_menor_f_score = municipio

        return municipio_menor_f_score


nos_abertos = [no_origem]
nos_expandidos = []
caminho = []
no_anterior = no_origem

while len(nos_abertos) > 0:
    no_atual = encontrar_menor_f_score()
    
    if (no_atual == no_objetivo):
        print('chegou no objetivo!')
        caminho.append(no_objetivo)
        break   

    nos_abertos.remove(no_atual)
    
    vizinhos_no_atual = list(grafo.neighbors(no_atual))

    if (len(vizinhos_no_atual) != 0):
        for vizinho in vizinhos_no_atual:
            if vizinho not in nos_abertos and vizinho not in nos_expandidos:
                f_score = grafo.nodes[vizinho]['dist_heuristica'] + grafo.get_edge_data(vizinho, no_atual)['weight']
                grafo.nodes[vizinho]['f_score'] = f_score            
                nos_abertos.append(vizinho)
                
        
        nos_expandidos.append(no_atual)
        no_anterior = no_atual
        caminho.append(no_atual)
        no_anterior = no_atual
           

i = 0
for cidade in caminho:
    print(i+1, cidade)
    i += 1

   
   