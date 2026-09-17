import cv2
import matplotlib.pyplot as plt

from funcoes.separar_cor import visualizar_canais, visualizar_hsv

# Entendendo vetores
imageColor = cv2.imread(r"./imagens/teste/cereja.jpeg", cv2.IMREAD_COLOR)
imageBlack = cv2.imread(r"./imagens/teste/cereja.jpeg", cv2.IMREAD_GRAYSCALE)

# print("-> Conteúdo numérico da imagem imageBlack.png (escala de cinza)")
# print("Forma do vetor:", imageBlack.shape)
# print("Primeiros 3x3 pixels:\n", imageBlack[:3, :3])

# print("\n -- \n")

# print("-> Conteúdo numérico da imagem imageColor.png (colorida)")
# print("Forma do vetor:", imageColor.shape)
# print("Primeiros 3x3 pixels (BGR):\n", imageColor[:3, :3, :])

# Exibição de canais
imageColor = cv2.imread(r"./camera/img/laranja.png")
visualizar_hsv(imageColor, "imagens/resultados/hsv/img1.png")
imageColor = cv2.imread(r"./camera/img/GuardaSol.png")
visualizar_hsv(imageColor, "imagens/resultados/hsv/img2.png")
imageColor = cv2.imread(r"./camera/img/logos.png")
visualizar_hsv(imageColor, "imagens/resultados/hsv/img3.png")
