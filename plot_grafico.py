import time

from matplotlib import pyplot as plt
import numpy as np


def plot_comparacao(mapa_inicial, mapa_final, K):
    """
    Gera um gráfico comparativo de dois tabuleiros de clusters 10x10.
    
    Parâmetros:
    - mapa_inicial: Array 2D (10, 10) dos clusters iniciais (fragmentados).
    - mapa_final: Array 2D (10, 10) dos clusters finais (organizados espacialmente).
    - K: Número de clusters (inteiro).
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)
    
    cmap = plt.get_cmap('tab10', K)
    fig.suptitle(f'Comparação de Agrupamento de Agentes (K={K}, 10x10 Grid)', fontsize=16, fontweight='bold')

    # --- Configuração do Subplot 1: Inicial ---
    im1 = axes[0].imshow(mapa_inicial, cmap=cmap, origin='upper', interpolation='none')
    axes[0].set_title('Clusters Iniciais\n(Apenas Atributos Puros)', fontsize=12)
    axes[0].set_xlabel('Posição X')
    axes[0].set_ylabel('Posição Y')
    axes[0].set_xticks(np.arange(10))
    axes[0].set_yticks(np.arange(10))
    axes[0].grid(True, color='black', linewidth=0.5, linestyle='--')

    # --- Configuração do Subplot 2: Final ---
    im2 = axes[1].imshow(mapa_final, cmap=cmap, origin='upper', interpolation='none')
    axes[1].set_title('Clusters Finais\n(Atributos Normalizados + Espaço)', fontsize=12)
    axes[1].set_xlabel('Posição X')
    axes[1].set_ylabel('Posição Y')
    axes[1].set_xticks(np.arange(10))
    axes[1].set_yticks(np.arange(10))
    axes[1].grid(True, color='black', linewidth=0.5, linestyle='--')

    cbar = fig.colorbar(im2, ax=axes, ticks=range(K), shrink=0.8, location='right', pad=0.03)
    cbar.ax.set_yticklabels([f'Cluster {i}' for i in range(K)])
    cbar.ax.set_title('Cluster ID', fontsize=10, pad=10)

    plt.savefig(f'comparacao_clusters_melhorada_{time.time()}.png', dpi=300)
