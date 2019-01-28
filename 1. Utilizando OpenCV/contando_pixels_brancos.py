# -*- coding: utf-8 -*-
"""
Contagens de objetos brancos
 
    python contando_pixels_brancos.py -i [imagefile] -o [imagefile]
 
@autor: Matheus Jericó
"""
 
# Import packages
import numpy as np
import argparse
import imutils
import cv2
  
# construindo passagem de parâmetros
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="nome do arquivo de imagem de entrada")
ap.add_argument("-o", "--output", required=True,
    help="nome do arquivo de imagem de saida")
args = vars(ap.parse_args())
  
# contagem de objetos
counter = {}
 
# carregar imagem
image_orig = cv2.imread(args["image"])
height_orig, width_orig = image_orig.shape[:2]
 
# imagem de saída com contorno
image_contours = image_orig.copy()
 
# detecção da cor branca
color = 'white'

# copiar imagem original
image_to_process = image_orig.copy()

# inicialização da contagem
counter[color] = 0

# inverter cores da imagem
image_to_process = (255-image_to_process)
lower = np.array([ 50,  50,  40])
upper = np.array([100, 120,  80])

# encontrar as cores dentro do limite especificado acima
image_mask = cv2.inRange(image_to_process, lower, upper)
# aplicar mascara
image_res = cv2.bitwise_and(image_to_process, image_to_process, mask = image_mask)

# carregar imagem, convertê-la em tons de cinza e, levemente, borrá-la
image_gray = cv2.cvtColor(image_res, cv2.COLOR_BGR2GRAY)
image_gray = cv2.GaussianBlur(image_gray, (5, 5), 0)

# realize a detecção de bordas e, em seguida, realize uma dilatação + erosão para fechar as lacunas entre as bordas do objeto
image_edged = cv2.Canny(image_gray, 50, 100)
image_edged = cv2.dilate(image_edged, None, iterations=1)
image_edged = cv2.erode(image_edged, None, iterations=1)

# encontrar contornos no mapa de borda
contours,hierarchy = cv2.findContours(image_edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# loop sobre os contornos individualmente
for c in contours:
     
    # se o contorno não for suficientemente grande, ignore-o
    if (cv2.contourArea(c) < 5):
        continue
     
    # computar o casco convexo do contado
    hull = cv2.convexHull(c)

    if color == 'white':
        # printar contorno em cor verde
        cv2.drawContours(image_contours,[hull],0,(0,255,0),1)

    counter[color] += 1


# Print o número de objetos de cor branca
print("{} objetos brancos".format(counter[color]))
 
# Imagem de saída
cv2.imwrite(args["output"],image_contours)
