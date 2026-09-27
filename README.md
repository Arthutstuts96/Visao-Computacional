# Visão Computacional

Neste repositório estão diversas funções e testes de manipulação de imagens, de modo a reutilizar as mesmas para práticas de visão computacional. Atualizado semanalmente a cada nova aula da disciplina.

## Ambiente

- Linux Mint
- VSCode
- Python v3.12.3
    - OpenCV
    - Numpy
    - Pillow
    - Zipfile

## Estrutura de pastas

- `funcoes`: Guarda diversas funções para manipulação das imagens, como de histograma, separação de canais em RGB/HSV, e salvar imagens em formatos diferentes
- `imagens`: Resultados das manipulações de imagens no geral, ou imagens criadas pelo programa
    - `graficos`: Gráficos plotados via matplotlib
    - `resultados`: Resultados gerais 
        - `histograma`: Resultados do histograma
        - `hsv`: Resultado da separação de canais HSV
        - `png_vs_jpg`: Resultado das diferentes compressões de imagem JPG e PNG
    - `screenshots`: Capturas de telas tiradas com a câmera aberta (`cv2`)
- `entrada`: Imagens e vídeos disponibilizadas para serem utilizadas de entrada para os algoritmos
    - `img`: Imagens
    - `vídeos`: Vídeos