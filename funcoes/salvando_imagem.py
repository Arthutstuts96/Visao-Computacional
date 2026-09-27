import cv2
import os
import matplotlib.pyplot as plt
import zipfile


def salvar_jpg(img_bgr, caminho, qualidade = 95):
    """
    Salva a imagem em formato JPEG com a qualidade especificada
    JPEG: compressão com perda: quanto menor a qualidade, menor o arquivo,
    mas perde mais informação
    """

    params = [cv2.IMWRITE_JPEG_QUALITY, qualidade]
    cv2.imwrite(caminho, img_bgr, params)


def salvar_png(img_bgr, caminho, compressao=1):
    """
    Salva a imagem em formato PNG com a o nível de compressão especificado
    PNG: compressão sem perda: a qualidade nunca é reduzida,
    só o tempo de compressão e o tamanho do arquivo variam

    compressão é um inteiro entre 0 e 9, 0 sendo o mais rápido e 9 o mais lento
    """
    params = [cv2.IMWRITE_PNG_COMPRESSION, compressao]
    cv2.imwrite(caminho, img_bgr, params)


def tamanho_kb(caminho):
    """
    Retorna o tamanho em kb do arquivo especificado
    """
    if isinstance(caminho, (int, float)):
        return caminho / 1024
    
    return os.path.getsize(caminho) / 1024


def plotar_comparacao_jpeg(img_bgr, pasta, qualidade=(10, 50, 75, 95)):
    os.makedirs(pasta, exist_ok=True)
    n = len(qualidade)

    plt.figure(figsize=(4 * n, 5))
    plt.suptitle("Comparação de qualidade JPEG", fontsize=14)

    for i, q in enumerate(qualidade):
        caminho = os.path.join(pasta, f"jpeg_q{q:03d}.jpg")
        salvar_jpg(img_bgr, caminho, qualidade=q)
        kb = tamanho_kb(caminho)

        ax = plt.subplot(1, n, i + 1)
        ax.imshow(cv2.cvtColor(cv2.imread(caminho), cv2.COLOR_BGR2RGB))
        ax.set_title(f"Qualidade {q}\n{kb:.1f} KB")
        ax.axis("off")

    plt.tight_layout()
    plt.savefig("imagens/graficos/Comparacao_jpegs.png")


def plotar_comparacao_png(img_bgr, pasta, compressao=(1, 5, 7, 9)):
    os.makedirs(pasta, exist_ok=True)
    n = len(compressao)

    plt.figure(figsize=(4 * n, 5))
    plt.suptitle("Comparação de qualidade PNG", fontsize=14)

    for i, nivel in enumerate(compressao):
        caminho = os.path.join(pasta, f"png_q{nivel:03d}.png")
        salvar_png(img_bgr, caminho, compressao=nivel)
        kb = tamanho_kb(caminho)

        ax = plt.subplot(1, n, i + 1)
        ax.imshow(cv2.cvtColor(cv2.imread(caminho), cv2.COLOR_BGR2RGB))
        ax.set_title(f"Qualidade {nivel}\n{kb:.1f} KB")
        ax.axis("off")

    plt.tight_layout()
    plt.savefig("imagens/graficos/Comparacao_pngs.png")


def plotar_resumo_tamanhos(pasta):
    arquivos = sorted(
        [f for f in os.listdir(pasta) if f.endswith((".jpg", ".png"))],
        key=lambda f: os.path.getsize(os.path.join(pasta, f)),
    )
    nomes = [f.replace("_", "").replace(".jpg", " (JPEG)").replace
             (".png", " (PNG)") for f in arquivos]
    tamanhos = [tamanho_kb(os.path.getsize(os.path.join(pasta, f))) for f in arquivos]

    cores = ["steelblue" if f.endswith(".jpg") else "seagreen" for f in arquivos]

    plt.figure(figsize=(10, 5))
    barras = plt.barh(nomes, tamanhos)
    plt.xlabel("Tamanho em KB")
    plt.title("Tamanho dos arquivos salvos - JPEG vs PNG")

    for barra, kb in zip(barras, tamanhos):
        plt.text(barra.get_width() * 5, barra.get_y() + barra.get_height() / 2, f"{kb:.1f} KB", va='center')

    plt.tight_layout()
    plt.savefig("imagens/graficos/Comparacao_tamanho_imagens.png")