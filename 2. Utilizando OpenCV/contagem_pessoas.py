"""
Contagens de objetos brancos
 
    python contagem_pessoas.py -i pessoas.png
 
@autor: Matheus Jericó
"""


import cv2
import argparse
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="nome do arquivo de imagem de entrada")
args = vars(ap.parse_args())
  
# criando haar cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Lê imagem
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detecta faces na imagem
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Encontrei {0} pessoas, reconhecendo a face!".format(len(faces)))

# Colocando retângulos na face.
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)

print("Encontrei {0} pessoas, reconhecendo a face!".format(len(faces)))
