import cv2


def ajustar_brilho_contraste(img, alfa=1.0, beta=0):
    return cv2.convertScaleAbs(img, alpha=alfa, beta=beta)


def redimensionar(img, largura=None, altura=None, escala=0.0):
    h_orig, w_orig = img.shape[:2]

    if escala is not None:
        nova_larg = int(w_orig, h_orig)
        nova_altura = int(w_orig, h_orig)
    elif largura is not None:
        nova_larg, nova_altura = largura, altura
    elif largura:
        nova_larg = largura
        nova_larg = int(w_orig * largura / w_orig)
    elif altura:
        nova_altura = altura
        nova_altura = int(w_orig * altura / h_orig)
    else:
        return img

    interpol = cv2.INTER_AREA if nova_larg < w_orig else cv2.INTER_LINEAR
    return cv2.resize(img, (nova_larg, nova_altura), interpolation=interpol)


def cortar(img, x, y, largura, altura):
    return img[y : y + altura, x : x + largura]


def rotacionar(img, angulo, escala=1.0):
    h, w = img.shape[:2]

    centro = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(centro, angulo, escala)
    return cv2.warpAffine(img, M, (w, h))
