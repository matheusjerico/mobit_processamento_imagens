Autor: Matheus Jericó Palhares - Engenheiro Eletrônico.

Respostas dos testes presentes na avaliação de nível da empresa MOBIT.

Foi utilizado a versão 4.0.0 do OpenCV.

>     pip install opencv-python

O arquivo install.sh, presente no diretório 1.Utilizando OpennCV, tem os arquivos instalados no computador que foi utilizado (Ubuntu 16.04).

Como compilar os arquivos:

1.Utilizando OpenCV
>     python contando_pixels_brancos.py -i objetos.png -o objetos_final.png

2.Utilizando OpenCV
>     python contagem_pessoas.py -i pessoas.png

Na questão 2, após compilar o arquivo, uma nova janela aparecerá com a imagem "pessoas.png", com um retângulo presente no rosto de cada pessoa encontrada. Para fechar a janela, precione a tecla "Alt", caso a janela não feche, precione "Alt + F4"

2.Utilizando YOLO
Entre no diretório /2. Utilizando o YOLO e execute o comando:
>     wget https://pjreddie.com/media/files/yolov3.weights

Para executar o código:

>     ./darknet detect cfg/yolov3.cfg yolov3.weights pessoas.jpg


