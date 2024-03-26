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
        # Distâncias de condução em quilômetros entre as capitais, segundo br.distanciacidades.net
        distancias = {
            # Regiao norte
                # Roraima
            ("Boa Vista", "Manaus"): 781,
            ("Boa Vista", "Belem"): 4133,
                # Amapá
            ("Macapa", "Belem"): 539,
                # Amazonas
            ("Manaus", "Boa Vista"): 781,
            ("Manaus", "Belem"): 3073,
            ("Manaus", "Rio Branco"): 1415,
            ("Manaus", "Porto Velho"): 901,
            ("Manaus", "Cuiaba"): 2356,
                # Pará
            ("Belem", "Macapa"): 539,
            ("Belem", "Boa Vista"): 4133,
            ("Belem", "Manaus"): 3073,
            ("Belem", "Cuiaba"): 2506,
            ("Belem", "Palmas"): 1236,
            ("Belem", "Sao Luis"): 579,
                # Acre
            ("Rio Branco", "Manaus"): 1415,
            ("Rio Branco", "Porto Velho"): 515,
                # Rondonia
            ("Porto Velho", "Manaus"): 901,
            ("Porto Velho", "Rio Branco"): 515,
            ("Porto Velho", "Cuiaba"): 1457,
                # Tocantins
            ("Palmas", "Belem"): 1236,
            ("Palmas", "Sao Luis"): 1270,
            ("Palmas", "Teresina"): 1127,
            ("Palmas", "Salvador"): 1437,
            ("Palmas", "Brasilia"): 298,
            ("Palmas", "Cuiaba"): 1498,

            # Regiao nordeste
                # Maranhao
            ("Sao Luis", "Belem"): ,
            ("Sao Luis", "Palmas"):,
            ("Sao Luis", "Teresina"):,
                # Ceara
            ("Fortaleza", "Natal"): ,
            ("Fortaleza", "Teresina"):,
                # Rio Grande do Norte
            ("Natal", "Fortaleza"): ,
            ("Natal", "Joao Pessoa"): ,
                # Paraiba
            ("Joao Pessoa", "Natal"): ,
            ("Joao Pessoa", "Recife"): ,
                # Piaui
            ("Teresina", "Sao Luis"): ,
            ("Teresina", "Fortaleza"):,
            ("Teresina", "Recife"):,
            ("Teresina", "Salvador"):,
            ("Teresina", "Palmas"):,
                # Pernambuco
            ("Recife", "Joao Pessoa"): ,
            ("Recife", "Teresina"):,
            ("Recife", "Maceio"):,
                # Alagoas
            ("Maceio", "Recife"): ,
            ("Maceio", "Aracaju"):,
                # Sergipe
            ("Aracaju", "Maceio"):,
            ("Aracaju", "Salvador"):,
                # Bahia
            ("Salvador", "Aracaju"): ,
            ("Salvador", "Teresina"):,
            ("Salvador", "Palmas"):,
            ("Salvador", "Brasilia"):,
            ("Salvador", "Belo Horizonte"):,
            ("Salvador", "Vitoria"):,

            # Regiao centro-oeste
                # Mato Grosso
            ("Cuiaba", "Porto Velho"): ,
            ("Cuiaba", "Manaus"):,
            ("Cuiaba", "Belem"):,
            ("Cuiaba", "Palmas"):,
            ("Cuiaba", "Brasilia"):,
            ("Cuiaba", "Goiania"):,
            ("Cuiaba", "Campo Grande"):,
                # Goias
            ("Goiania", "Cuiaba"):,
            ("Goiania", "Brasilia"):,
            ("Goiania", "Belo Horizonte"):,
            ("Goiania", "Campo Grande"):,
                # Mato Grosso do Sul
            ("Campo Grande", "Cuiaba"): ,
            ("Campo Grande", "Goiania"):,
            ("Campo Grande", "Belo Horizonte"):,
            ("Campo Grande", "Sao Paulo"):,
            ("Campo Grande", "Curitiba"):,
                # Distrito Federal
            ("Brasilia", "Palmas"): ,
            ("Brasilia", "Salvador"):,
            ("Brasilia", "Belo Horizonte"):,
            ("Brasilia", "Goiania"):,
            ("Brasilia", "Cuiaba"):,

            # Regiao sudeste
                # Minas Gerais
            ("Belo Horizonte", "Brasilia"):,
            ("Belo Horizonte", "Salvador"):,
            ("Belo Horizonte", "Vitoria"):,
            ("Belo Horizonte", "Rio de Janeiro"):,
            ("Belo Horizonte", "Sao Paulo"):,
            ("Belo Horizonte", "Campo Grande"):,
            ("Belo Horizonte", "Goiania"):,
                # São Paulo
            ("Sao Paulo", "Belo Horizonte"):,
            ("Sao Paulo", "Rio de Janeiro"):,
            ("Sao Paulo", "Curitiba"):,
            ("Sao Paulo", "Campo Grande"):,
                # Espirito Santo
            ("Vitoria", "Salvador"):,
            ("Vitoria", "Belo Horizonte"):,
            ("Vitoria", "Rio de Janeiro"):,
                # Rio de Janeiro
            ("Rio de Janeiro", "Vitoria"):,
            ("Rio de Janeiro", "Belo Horizonte"):,
            ("Rio de Janeiro", "Sao Paulo"):,

            # Regiao sul
                # Parana
            ("Curitiba", "Campo Grande"):,
            ("Curitiba", "Sao Paulo"):,
            ("Curitiba", "Florianópolis"):,
                # Santa Catarina
            ("Florianópolis", "Curitiba"):,
            ("Florianópolis", "Porto Alegre"): 467,
                # Rio Grande do Sul
            ("Porto Alegre", "Florianópolis"): 467,
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
