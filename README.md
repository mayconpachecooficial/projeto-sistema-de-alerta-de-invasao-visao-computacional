Tecnologias Utilizadas

OpenCV (cv2): Processamento de imagens e vídeos.
YOLO (You Only Look Once): Detecção de objetos em tempo real.
Winsound: Reprodução de sons no Windows.
Threading: Criação e gerenciamento de threads.


O que Foi Desenvolvido
Captura de Vídeo: Captura quadros de um vídeo (ex01.mp4).
Área de Interesse: Define uma região específica para monitoramento de invasores.
Detecção de Objetos: Usa YOLO para detectar pessoas no vídeo.
Verificação da Invasão: Destaca e exibe alerta se uma pessoa estiver na área de interesse.
Alerta Sonoro: Toca um som de alerta usando winsound em uma thread separada.
Exibição do Vídeo: Combina e exibe a imagem original com destaques de invasão em uma janela.
