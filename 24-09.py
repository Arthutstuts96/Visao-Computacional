import cv2

from funcoes.histograma import *
from funcoes.salvando_imagem import *

# caminho_imagem = "camera/img/cachorros.jpeg"
# image = cv2.imread(str(caminho_imagem))
# if image is None:
#     raise FileNotFoundError(f"Não foi possível carregar a imagem: {caminho_imagem}")

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray_corr = clahe_pb(gray)
# plotar_comparacao_pb(gray, gray_corr)

# color_corr = clahe_colorido(image)
# plotar_comparacao_colorida(image, color_corr)

imagem = cv2.imread("camera/img/cachorros.jpeg")

PASTA_SAIDA = "imagens/resultados/png_vs_jpg"

plotar_comparacao_jpeg(imagem, PASTA_SAIDA, qualidade=(10, 50, 75, 95))
plotar_comparacao_png(imagem, PASTA_SAIDA, compressao=(0, 3, 6, 9))
plotar_resumo_tamanhos(PASTA_SAIDA)

with zipfile.ZipFile("imagens/resultados/teste.zip", "w", compression=zipfile.ZIP_DEFLATED) as zip_ref:
    zip_ref.write("camera/img/cereja.png")