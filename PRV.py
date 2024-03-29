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
    num_particulas = 100
    num_geracoes = 1000
    num_clientes = 4
    num_veiculos = 2
    w = 0.5
    c1 = 0.5
    c2 = 0.5
    distancias = [
        [0, 10, 20, 15],  # Cliente 0
        [10, 0, 25, 20],  # Cliente 1
        [20, 25, 0, 10],  # Cliente 2
        [15, 20, 10, 0],  # Cliente 3
    ]
    melhor_rota = pso(num_particulas, num_geracoes, num_clientes, num_veiculos, distancias, w, c1, c2)
    rotas_encontradas.append(melhor_rota)
    texto_resultado.delete(1.0, END)
    texto_resultado.insert(tk.INSERT, "Rotas encontradas:\n")
    for i, rota in enumerate(rotas_encontradas):
        texto_resultado.insert(tk.INSERT, f"Rota {i+1}: {rota}\n")
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
