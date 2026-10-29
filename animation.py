import numpy as np
import matplotlib
matplotlib.use('WebAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.cluster import KMeans
import warnings
from sklearn.exceptions import ConvergenceWarning

warnings.filterwarnings("ignore", category=ConvergenceWarning)


def animar_evolucao_kmeans(dados_finais, H, W, K):
    """
    Cria uma janela interativa mostrando a evolução K-Means passo a passo
    """
    frames = []
    prev_labels = None
    
    for i in range(1, 50):
        kmeans = KMeans(
            n_clusters=K, 
            max_iter=i, 
            n_init=1, 
            init='random', 
            random_state=42
        )
        labels = kmeans.fit_predict(dados_finais)
        frames.append(labels.reshape(H, W))

        # Algoritmo PARA se o k-means não mudar nada numa geração
        if prev_labels is not None and np.array_equal(labels, prev_labels):
            break
        prev_labels = labels

    fig, ax = plt.subplots(figsize=(8, 8))
    cmap = plt.get_cmap('tab10', K)
    
    im = ax.imshow(frames[0], cmap=cmap, origin='upper', interpolation='none')
    
    ax.set_xticks(np.arange(W))
    ax.set_yticks(np.arange(H))
    ax.grid(True, color='black', linewidth=0.5, linestyle='--')
    ax.set_xlabel('Posição X')
    ax.set_ylabel('Posição Y')
    
    cbar = fig.colorbar(im, ax=ax, ticks=range(K), shrink=0.8)
    cbar.ax.set_yticklabels([f'Cluster {i}' for i in range(K)])

    def update(frame_idx):
        im.set_array(frames[frame_idx])
        ax.set_title(f'Evolução K-Means\nIteração: {frame_idx + 1} de {len(frames)}', fontsize=14)
        return [im]

    ani = FuncAnimation(
        fig, update, frames=len(frames), 
        interval=800, blit=False, 
        repeat=True, repeat_delay=1000
    )
    
    plt.tight_layout()
    plt.show()