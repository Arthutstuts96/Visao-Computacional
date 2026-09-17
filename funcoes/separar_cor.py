import cv2
import matplotlib.pyplot as plt

# — FUNÇÃO: separar canais RGB —
def separar_canais_rgb(img_bgr):
    """
    Separa os 3 canais de uma imagem BGR.
    Retorna (vermelho, verde, azul) como arrays 2D (escala de cinza).
    Nota: no OpenCV a ordem é BGR, então [:,:,0]=Azul, [:,:,2]=Vermelho.
    """
    # img[:, :, 0] = primeiro canal = Azul   (Blue)
    # img[:, :, 1] = segundo canal  = Verde  (Green)
    # img[:, :, 2] = terceiro canal = Vermelho (Red)
    azul     = img_bgr[:, :, 0]
    verde    = img_bgr[:, :, 1]
    vermelho = img_bgr[:, :, 2]
    return vermelho, verde, azul

# — FUNÇÃO: visualizar canais —
def visualizar_canais(img_bgr, caminho):
    """Plota a imagem original e seus 3 canais R, G, B lado a lado."""
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    r, g, b = separar_canais_rgb(img_bgr)

    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    axes[0].imshow(img_rgb);         axes[0].set_title("Original (RGB)")
    axes[1].imshow(r, cmap="gray");  axes[1].set_title("Canal R (Vermelho)")
    axes[2].imshow(g, cmap="gray");  axes[2].set_title("Canal G (Verde)")
    axes[3].imshow(b, cmap="gray");  axes[3].set_title("Canal B (Azul)")
    for ax in axes: ax.axis("off")
    plt.tight_layout()
    plt.savefig(caminho)

# - FUNÇÃO: visualizar canais HSV -
def visualizar_hsv(img_bgr, caminho):
    """
    Converte a imagem de BGR para HSV e plota os 3 canais separados
    """
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    # img_bgr = cv2.cvtColor(img_bgr, cv2.COLOR_GRAY2BGR)

    # Dividimos o array 3D em 3 arrays 2D
    h, s, v = cv2.split(img_hsv)

    fig, axes = plt.subplots(1, 4, figsize=(25, 30))
    axes[0].imshow(h); axes[0].set_title("Original RGB")
    axes[1].imshow(h, cmap="hsv"); axes[1].set_title("Canal H (Hue)")
    axes[2].imshow(h, cmap="gray"); axes[2].set_title("Canal S (Saturation)")
    axes[3].imshow(h, cmap="gray"); axes[3].set_title("Canal V (Value/Brilho)")
    for ax in axes: ax.axis("off")
    plt.tight_layout()
    plt.savefig(caminho)