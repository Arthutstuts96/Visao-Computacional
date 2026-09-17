import cv2
import matplotlib.pyplot as plt

imagemColor = cv2.imread("camera/img/connor-ward.png")
img_rgb = cv2.cvtColor(imagemColor, cv2.COLOR_BGR2RGB)

# cv2.imshow("Mostrando a imagem", imagemColor)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img_rgb = cv2.imread("camera/img/bernie-almanzar.png", cv2.COLOR_BGR2RGB)

# plt.imshow(img_rgb)
# plt.title("Mostrando a imagem")
# plt.axis("off")
# plt.show()
fig, axes = plt.subplots(2, 3, figsize=(15, 5))

axes[0, 0].imshow(img_rgb)
axes[0, 0].set_title("Fig 1")

axes[0, 0].imshow(img_rgb)
axes[0, 1].set_title("Das")
axes[0, 1].axis("off")

plt.figure(figsize=(10,5))
axl = plt.subplot(2, 2, 1)
axl.imshow(img_rgb)
axl.set_title(f"Original {img_rgb.shape}")
axl('off')

plt.tight_layout()
plt.show()
