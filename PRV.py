import tkinter as tk
from tkinter import scrolledtext
from tkinter import END
import random

# Função para inicializar a população de partículas com rotas aleatórias
def inicializar_particulas(num_particulas, num_clientes, num_veiculos):
    particulas = []
    for _ in range(num_particulas):
        # Inicializa a sequência de visitação dos clientes
        sequencia_clientes = list(range(num_clientes))
        random.shuffle(sequencia_clientes)
        # Inicializa a atribuição dos clientes aos veículos
        particula = [random.randint(1, num_veiculos) for _ in range(num_clientes)]
        particulas.append(particula)
    return particulas

# Função para calcular a distância total percorrida por um veículo em uma rota
def distancia_rota(rota, distancias):
    distancia_total = 0
    for i in range(len(rota) - 1):
        distancia_total += distancias[rota[i]][rota[i+1]]
    return distancia_total

# Função de fitness (avaliação) de uma partícula
def fitness(particula, distancias):
    num_veiculos = max(particula)
    distancia_total = 0
    for veiculo in range(1, num_veiculos + 1):
        rota_veiculo = [cliente for cliente, v in enumerate(particula) if v == veiculo]
        distancia_total += sum(distancias[cliente1][cliente2] for cliente1, cliente2 in zip(rota_veiculo[:-1], rota_veiculo[1:]))
    return distancia_total

# Algoritmo de Otimização por Enxame de Partículas (PSO)
def pso(num_particulas, num_geracoes, num_clientes, num_veiculos, distancias, w, c1, c2):
    # Inicialização das partículas e seus melhores locais
    particulas = inicializar_particulas(num_particulas, num_clientes, num_veiculos)
    melhores_locais = particulas.copy()
    fitness_melhores_locais = [fitness(particula, distancias) for particula in melhores_locais]
    melhor_global = melhores_locais[fitness_melhores_locais.index(min(fitness_melhores_locais))]
    fitness_melhor_global = min(fitness_melhores_locais)
    
    # Iteração
    for _ in range(num_geracoes):
        for i, particula in enumerate(particulas):
            # Atualização da velocidade e posição da partícula
            for j in range(len(particula)):
                if random.random() < c1:
                    particula[j] = random.randint(1, num_veiculos)
                elif random.random() < c2:
                    particula[j] = melhores_locais[i][j]
            # Atualização do melhor local da partícula
            if fitness(particula, distancias) < fitness_melhores_locais[i]:
                melhores_locais[i] = particula.copy()
                fitness_melhores_locais[i] = fitness(particula, distancias)
            # Atualização do melhor global
            if fitness_melhores_locais[i] < fitness_melhor_global:
                melhor_global = particula.copy()
                fitness_melhor_global = fitness_melhores_locais[i]
    
    return melhor_global

# Lista para armazenar todas as rotas encontradas
rotas_encontradas = []

# Função para executar o PSO e mostrar a melhor rota encontrada
def executar_pso():
    num_particulas = 20
    num_geracoes = 1000
    num_clientes = 20
    num_veiculos = 2
    w = 0.9
    c1 = 1.5
    c2 = 1.5
    distancias = [
        [ 0, 52, 13,  3, 31,  4, 75, 50, 29,  5, 55, 48, 14, 39, 63, 46, 68, 75, 49, 74],
        [ 9,  0, 69, 23, 65,  2,  6,  3, 75, 69, 45, 43, 55, 73, 48, 79, 68,  7, 25, 71],
        [72, 24,  0, 37, 47, 49, 32, 18, 79,  6,  5,  2,  8, 39, 46, 24, 68, 29, 60, 53],
        [15, 38, 48,  0, 78, 25, 25, 69, 45, 64, 76, 73, 18, 38, 11, 50, 78,  4, 31, 19],
        [30, 32,  3, 27,  0, 60, 34, 61, 30, 29, 65, 58, 49, 33, 31, 78, 31, 31, 74, 71],
        [10, 13, 10, 67, 16,  0, 58, 73, 52, 42, 18, 55, 19, 63, 34, 16,  6, 11, 31, 28],
        [26, 11, 38, 65, 43, 55,  0,  3, 68, 75,  4, 31, 76, 10, 77, 57, 18, 39, 37,  5],
        [24, 23, 61, 68, 19, 35, 51,  0, 65, 42,  8, 50, 37, 10, 17,  4, 79, 35, 27, 74],
        [47, 68, 45, 74, 23,  4, 21, 13,  0, 10, 50, 40, 55, 70,  1, 39, 15, 59,  2, 31],
        [30, 40, 58, 39, 42, 64, 48,  7, 79,  0, 41, 19, 29,  8, 50, 11, 59, 40, 10, 21],
        [52,  2, 25, 55, 45, 23, 49, 57, 49, 38,  0, 57, 38, 73, 65, 75,  6, 27, 16, 23],
        [10,  4,  7,  3, 57, 69, 73, 38, 70, 40, 19,  0, 68, 41, 74, 29, 45, 70, 65,  3],
        [47, 76,  3, 10, 54, 65, 74, 54, 71, 78, 66, 59,  0, 68, 78, 53, 74, 59, 65, 16],
        [35,  2, 43, 73, 14,  1, 39,  2, 34, 38, 16, 77,  6,  0, 48, 65,  5, 48, 57, 60],
        [41,  7, 13, 15, 61, 61,  8, 49,  5, 38, 66, 61,  3, 19,  0, 76, 38,  6, 56, 49],
        [ 4, 51,  1, 47,  7, 10, 31, 68, 51, 40, 23,  4, 79, 79, 41,  0, 46,  1, 44, 48],
        [77, 79, 51, 14, 41,  1, 52, 69, 37, 70, 47, 43, 68, 44, 15, 33,  0, 25, 39, 50],
        [14,  3, 53, 58,  8, 44, 53, 46, 53, 75,  2, 44, 71, 40, 34, 46, 72,  0, 57, 19],
        [33, 57, 54, 15, 31, 39,  3, 15, 27, 71,  2, 10, 58, 13, 53, 44, 56, 39,  0, 43],
        [78, 27,  5, 77, 15, 48,  5,  8, 23, 61,  7, 33,  2, 34, 40, 24, 21, 26, 61,  0],
    ]
    melhor_rota = pso(num_particulas, num_geracoes, num_clientes, num_veiculos, distancias, w, c1, c2)
    custo_total = fitness(melhor_rota, distancias)
    rotas_encontradas.append((melhor_rota, custo_total))
    texto_resultado.delete(1.0, END)
    texto_resultado.insert(tk.INSERT, "Rotas encontradas:\n")
    for i, (rota, custo) in enumerate(rotas_encontradas):
        texto_resultado.insert(tk.INSERT, f"Rota {i+1}: {rota} - Custo: {custo}\n")
    texto_resultado.insert(tk.INSERT, "\n")

# Criar a janela principal
janela = tk.Tk()
janela.title("PSO para Otimização de Rotas")

# Criar um botão para executar o PSO
botao_executar = tk.Button(janela, text="Executar PSO", command=executar_pso)
botao_executar.pack(pady=10)

# Criar um campo de texto para exibir o resultado
texto_resultado = scrolledtext.ScrolledText(janela, width=40, height=10, wrap=tk.WORD)
texto_resultado.pack(padx=10, pady=10)

# Iniciar a interface gráfica
janela.mainloop()
