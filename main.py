import cv2  # Importa a biblioteca OpenCV para processamento de imagens
from ultralytics import YOLO  # Importa o modelo YOLO (You Only Look Once) para detecção de objetos
import winsound  # Importa o módulo winsound para reproduzir sons no Windows
import threading  # Importa o módulo threading para criar e gerenciar threads

video = cv2.VideoCapture('ex01.mp4')  # Cria um objeto VideoCapture para ler o vídeo 'ex01.mp4' ou 'ex02.mp4' 
cv2.namedWindow('img', cv2.WINDOW_NORMAL)  # Cria uma janela chamada 'img'
modelo = YOLO('yolov8n.pt')  # Carrega o modelo YOLO pré-treinado 'yolov8n.pt'

area = [100,190, 1150,700]  # Coordenadas da área de interesse (retângulo verde)

alarmeCtl = False  # Variável de controle para o alarme (inicialmente desligado)

def alarme():  # Função para reproduzir o som do alarme
    global alarmeCtl  # Acessa a variável alarmeCtl no escopo global
    for _ in range(7):  # Loop para reproduzir o som 7 vezes
        winsound.Beep(2500,100)  # Reproduz um som de 2500 Hz por 100 milissegundos

    alarmeCtl = False  # Desliga o alarme após reproduzir o som

while True:  # Loop infinito para processar cada quadro do vídeo
    check,img = video.read()  # Lê um quadro do vídeo
    img = cv2.resize(img,(1270,720))  # Redimensiona o quadro para 1270x720 pixels
    img2 = img.copy()  # Cria uma cópia da imagem original
    cv2.rectangle(img2,(area[0],area[1]),(area[2],area[3]),(0,255,0),-1)  # Desenha um retângulo verde na área de interesse

    resultado = modelo(img)  # Executa a detecção de objetos no quadro usando o modelo YOLO

    for objetos in resultado:  # Itera sobre os objetos detectados
        obj = objetos.boxes  # Obtém as caixas delimitadoras (bounding boxes) dos objetos
        for dados in obj:  # Itera sobre as caixas delimitadoras
            x,y,w,h = dados.xyxy[0]  # Obtém as coordenadas x, y, largura e altura da caixa delimitadora
            x,y,w,h = int(x),int(y),int(w),int(h)  # Converte para inteiros
            cls = int(dados.cls[0])  # Obtém a classe do objeto detectado
            cx,cy = (x+w)//2, (y+h)//2  # Calcula as coordenadas do centro da caixa delimitadora
            if cls ==0:  # Verifica se a classe é 0 (pessoa)
                cv2.rectangle(img, (x, y), (w, h), (255, 0, 0), 5)  # Desenha um retângulo vermelho ao redor da pessoa

                if cx >=area[0] and cx <=area[2] and cy>=area[1] and cy <=area[3]:  # Verifica se a pessoa está dentro da área de interesse
                    cv2.rectangle(img2, (area[0], area[1]), (area[2], area[3]), (0, 0, 255), -1)  # Desenha um retângulo vermelho na área de interesse
                    cv2.rectangle(img,(100,30),(470,80),(0,0,255),-1)  # Desenha um retângulo vermelho para exibir o texto
                    cv2.putText(img,'INVASOR DETECTADO',(105,65),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)  # Exibe o texto "INVASOR DETECTADO"
                    if not alarmeCtl:  # Verifica se o alarme não está ligado
                        alarmeCtl = True  # Liga o alarme
                        threading.Thread(target=alarme).start()  # Inicia uma nova thread para reproduzir o som do alarme

    imgFinal = cv2.addWeighted(img2,0.5,img,0.5,0)  # Combina a imagem original com a imagem da área de interesse
    cv2.resizeWindow('img', 640, 360)  # Redimensiona a janela para 640x360 pixels
    cv2.imshow('img',imgFinal)  # Exibe a imagem final
    cv2.waitKey(1)  # Aguarda 1 milissegundo para processar eventos da janela
