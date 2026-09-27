import cv2
import matplotlib.pyplot as plt

from funcoes.manipular_imagems import ajustar_brilho_contraste, cortar, redimensionar, rotacionar

# from funcoes.separar_cor import visualizar_canais, visualizar_hsv

# # Entendendo vetores
# imageColor = cv2.imread(r"./imagens/teste/cereja.jpeg", cv2.IMREAD_COLOR)
# imageBlack = cv2.imread(r"./imagens/teste/cereja.jpeg", cv2.IMREAD_GRAYSCALE)

# # print("-> Conteúdo numérico da imagem imageBlack.png (escala de cinza)")
# # print("Forma do vetor:", imageBlack.shape)
# # print("Primeiros 3x3 pixels:\n", imageBlack[:3, :3])

# # print("\n -- \n")

# # print("-> Conteúdo numérico da imagem imageColor.png (colorida)")
# # print("Forma do vetor:", imageColor.shape)
# # print("Primeiros 3x3 pixels (BGR):\n", imageColor[:3, :3, :])

# # Exibição de canais
# imageColor = cv2.imread(r"./camera/img/laranja.png")
# visualizar_hsv(imageColor, "imagens/resultados/hsv/img1.png")
# imageColor = cv2.imread(r"./camera/img/connor-ward.png")
# visualizar_hsv(imageColor, "imagens/resultados/hsv/img2.png")
# imageColor = cv2.imread(r"./camera/img/logos.png")
# visualizar_hsv(imageColor, "imagens/resultados/hsv/img3.png")

image = cv2.imread("camera/img/laranja.png")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_brilho = ajustar_brilho_contraste(image, alfa=1.3, beta=30)
# img_redium = redimensionar(image, escala=2.0)
img_corte = cortar(image, 100, 100, 800, 600)
img_rot = rotacionar(image, angulo=3.0)

plt.figure(figsize=(16, 10))

ax1 = plt.subplot(2, 3, 1)
ax1.imshow(cv2.cvtColor(img_brilho, cv2.COLOR_BGR2RGB))
ax1.set_title("Brilho/Contraste")
ax1.axis("off")

ax2 = plt.subplot(2, 3, 2)
ax2.imshow(cv2.cvtColor(img_rot, cv2.COLOR_BGR2RGB))
ax2.set_title("Rotacionada")
ax2.axis("off")

ax3 = plt.subplot(2, 3, 3)
ax3.imshow(cv2.cvtColor(img_corte, cv2.COLOR_BGR2RGB))
ax3.set_title("Cortada")
ax3.axis("off")

# ax4 = plt.subplot(2, 3, 4)
# ax4.plt.imshow(cv2.cvtColor(img_redium, cv2.COLOR_BGR2RGB))
# ax4.set_title("Redimensionada")
# ax4.axis("off")




