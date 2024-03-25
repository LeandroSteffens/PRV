import random
from collections import deque

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
    
    def adicionar_aresta(self, origem, destino, valor):
        if origem in self.vertices and destino in self.vertices:
            if (origem, destino) not in self.arestas and (destino, origem) not in self.arestas:
                self.arestas[(origem, destino)] = valor
                self.vertices[origem].append((destino, valor))
                self.vertices[destino].append((origem, valor))
    
    def imprimir_capitais_disponiveis(self, estado_atual):
        print(f"Você está em: {estado_atual}")
        print("Capitais disponíveis para ir:")
        for vizinho, _ in self.vertices.items():
            if vizinho != estado_atual:
                print(vizinho)
    
    def conectar_capitais(self):
        # Distâncias aproximadas em quilômetros entre as capitais
        distancias = {
            ("Rio Branco", "Porto Velho"): 742,
            ("Rio Branco", "Manaus"): 873,
            ("Porto Velho", "Manaus"): 934,
            ("Manaus", "Boa Vista"): 785,
            ("Boa Vista", "Macapa"): 1075,
            ("Macapa", "Belem"): 350,
            ("Macapa", "Sao Luis"): 1100,
            ("Sao Luis", "Belem"): 720,
            ("Belem", "Fortaleza"): 1660,
            ("Fortaleza", "Natal"): 510,
            ("Natal", "Joao Pessoa"): 180,
            ("Joao Pessoa", "Recife"): 120,
            ("Recife", "Maceio"): 260,
            ("Maceio", "Aracaju"): 210,
            ("Aracaju", "Salvador"): 330,
            ("Salvador", "Vitoria"): 1160,
            ("Vitoria", "Rio de Janeiro"): 520,
            ("Vitoria", "Belo Horizonte"): 520,
            ("Belo Horizonte", "Sao Paulo"): 586,
            ("Belo Horizonte", "Brasilia"): 716,
            ("Brasilia", "Goiania"): 173,
            ("Brasilia", "Cuiaba"): 1083,
            ("Cuiaba", "Campo Grande"): 710,
            ("Campo Grande", "Sao Paulo"): 1016,
            ("Campo Grande", "Curitiba"): 1086,
            ("Curitiba", "Florianopolis"): 300,
            ("Curitiba", "Porto Alegre"): 461,
            ("Porto Alegre", "Florianopolis"): 476,
            ("Sao Paulo", "Rio de Janeiro"): 430,
            ("Sao Paulo", "Belo Horizonte"): 586,
            ("Sao Paulo", "Brasilia"): 873,
            ("Sao Paulo", "Curitiba"): 408,
            ("Rio de Janeiro", "Vitoria"): 520,
            ("Rio de Janeiro", "Belo Horizonte"): 434
        }
        
        for origem, destino in distancias:
            self.adicionar_aresta(origem, destino, distancias[(origem, destino)])

    def tem_caminho(self, origem, destino):
        visitados = set()
        fila = deque([origem])
        while fila:
            vertice_atual = fila.popleft()
            if vertice_atual == destino:
                return True
            if vertice_atual in visitados:
                continue
            visitados.add(vertice_atual)
            for vizinho, _ in self.vertices[vertice_atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)
        return False

    def encontrar_caminho(self, origem, destino):
        visitados = set()
        fila = deque([(origem, [origem], 0)])  # (vertice, caminho, distancia)
        while fila:
            vertice_atual, caminho_atual, distancia_atual = fila.popleft()
            if vertice_atual == destino:
                return caminho_atual, distancia_atual
            if vertice_atual in visitados:
                continue
            visitados.add(vertice_atual)
            for vizinho, valor_aresta in self.vertices[vertice_atual]:
                if vizinho not in visitados:
                    novo_caminho = caminho_atual + [vizinho]
                    nova_distancia = distancia_atual + valor_aresta
                    fila.append((vizinho, novo_caminho, nova_distancia))
        return None, float('inf')  # Não há caminho

# Criando o grafo
grafo = Grafo()

# Adicionando os vértices (capitais)
capitais = ["Rio Branco", "Maceio", "Macapa", "Manaus", "Salvador", "Fortaleza", "Brasilia", "Vitoria", "Goiania",
            "Sao Luis", "Cuiaba", "Campo Grande", "Belo Horizonte", "Belem", "Joao Pessoa", "Curitiba", "Recife",
            "Teresina", "Rio de Janeiro", "Natal", "Porto Alegre", "Porto Velho", "Boa Vista", "Florianopolis",
            "Sao Paulo", "Aracaju", "Palmas"]

for capital in capitais:
    grafo.adicionar_vertice(capital)

# Conectando todas as capitais
grafo.conectar_capitais()

# Imprimindo a capital onde está e as capitais disponíveis para ir
estado_inicial = random.choice(capitais)
grafo.imprimir_capitais_disponiveis(estado_inicial)

# Solicitando ao usuário o estado de destino
print("\nDigite o nome da capital para onde deseja ir:")
estado_final = input().strip()

# Encontrando o caminho e calculando a distância percorrida
caminho, distancia_percorrida = grafo.encontrar_caminho(estado_inicial, estado_final)
if caminho:
    print(f"\nMenor caminho de {estado_inicial} até {estado_final}:")
    print(" -> ".join(caminho))
    print(f"Distância percorrida: {distancia_percorrida} km")
else:
    print(f"\nNão há caminho de {estado_inicial} até {estado_final}")
