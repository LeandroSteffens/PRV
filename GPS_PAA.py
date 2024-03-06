import random

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
    
    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            if (origem, destino) not in self.arestas and (destino, origem) not in self.arestas:
                valor = random.randint(1, 100)  # Valor aleatório de 1 a 100
                self.arestas[(origem, destino)] = valor
                self.vertices[origem].append((destino, valor))
                self.vertices[destino].append((origem, valor))
    
    def imprimir_grafo(self):
        for vertice in self.vertices:
            arestas = [f"{aresta[0]} ({aresta[1]})" for aresta in self.vertices[vertice]]
            print(f"{vertice}: {', '.join(arestas)}")

# Criando o grafo
grafo = Grafo()

# Adicionando os vértices (capitais)
capitais = ["Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília", "Vitória", "Goiânia",
            "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte", "Belém", "João Pessoa", "Curitiba", "Recife",
            "Teresina", "Rio de Janeiro", "Natal", "Porto Alegre", "Porto Velho", "Boa Vista", "Florianópolis",
            "São Paulo", "Aracaju", "Palmas"]

for capital in capitais:
    grafo.adicionar_vertice(capital)

# Adicionando as arestas (conexões entre as capitais)
conexoes = [("Rio Branco", "Porto Velho"), ("Maceió", "Recife"), ("Macapá", "Belém"), ("Manaus", "Boa Vista"),
            ("Manaus", "Porto Velho"), ("Salvador", "Aracaju"), ("Salvador", "Recife"), ("Fortaleza", "Teresina"),
            ("Fortaleza", "Natal"), ("Fortaleza", "Recife"), ("Brasília", "Goiânia"), ("Brasília", "Cuiabá"),
            ("Brasília", "Campo Grande"), ("Belo Horizonte", "Brasília"), ("Belo Horizonte", "São Paulo"),
            ("Belo Horizonte", "Rio de Janeiro"), ("Belém", "São Luís"), ("João Pessoa", "Recife"),
            ("João Pessoa", "Natal"), ("Curitiba", "São Paulo"), ("Curitiba", "Florianópolis"),
            ("Recife", "Maceió"), ("Recife", "João Pessoa"), ("Teresina", "São Luís"), ("Teresina", "Fortaleza"),
            ("Rio de Janeiro", "São Paulo"), ("Porto Alegre", "Florianópolis"), ("Porto Alegre", "Curitiba"),
            ("Boa Vista", "Manaus"), ("Florianópolis", "Porto Alegre"), ("São Paulo", "Rio de Janeiro"),
            ("São Paulo", "Belo Horizonte"), ("Aracaju", "Salvador"), ("Palmas", "Brasília")]

for conexao in conexoes:
    grafo.adicionar_aresta(conexao[0], conexao[1])

# Imprimindo o grafo
grafo.imprimir_grafo()
