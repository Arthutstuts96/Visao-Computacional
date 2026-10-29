"""
Características:
- Sexo
- Período*
- Curso*
- Religião
- Origem
Tabuleiro 10 x 10
"""
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from animation import animar_evolucao_kmeans
from agent import gerar_grid_agentes
from plot_grafico import plot_comparacao


def main():
    HEIGHT, WIDTH = 10, 10
    K = 4
    peso_espacial = 0.5

    agents = gerar_grid_agentes(HEIGHT, WIDTH)

    atributos = np.array([a.get_features() for a in agents])
    coordenadas = np.array([[a.x, a.y] for a in agents])

    kmeans_inicial = KMeans(
        n_clusters=K, 
        random_state=42, 
        n_init=10
    )
    # labels_iniciais = kmeans_inicial.fit_predict(atributos)
    # mapa_inicial = labels_iniciais.reshape(H, W)

    scaler = StandardScaler()
    atributos_scaled = scaler.fit_transform(atributos)

    # Combinar características padronizadas com as posições ponderadas
    dados_finais = np.concatenate([atributos_scaled, coordenadas * peso_espacial], axis=1)
    animar_evolucao_kmeans(dados_finais, H=10, W=10, K=4)

    # kmeans = KMeans(n_clusters=K, random_state=42, n_init=10)
    # labels = kmeans.fit_predict(dados_finais)

    # for agent, label in zip(agents, labels):
    #     agent.cluster = int(label)

    # mapa_de_clusters = labels.reshape(H, W)
    # mascaras = [(mapa_de_clusters == i).astype(np.uint8) * 255 for i in range(K)]

    # plot_comparacao(mapa_inicial, mapa_de_clusters, K)

if __name__ == "__main__":
    main()

# Enviar para: wosleyarruda@uft.edu.br
# SWARM - Arthur Lima Duarte