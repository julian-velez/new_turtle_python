# Importa todas las funciones del módulo turtle (para dibujar gráficos)
from turtle import *

# Importa funciones para trabajar con colores en formato HSV
from colorsys import *

# Acelera la animación del dibujo (reduce el tiempo de actualización)
tracer(200)

# Cambia el color de fondo de la ventana a negro
bgcolor('black')

# Oculta el cursor de la tortuga para que solo se vea el dibujo
hideturtle()

# Define el grosor del lápiz con el que se dibuja
pensize(2)

# Bucle principal que se ejecuta 750 veces
# Controla el crecimiento de la figura
for i in range(750):

    # Cambia el color en cada iteración usando HSV
    # i/750 hace un degradado de colores tipo arcoíris
    color(hsv_to_rgb(i / 750, 1, 1)) 

    # Segundo bucle que se repite 5 veces en cada iteración
    # Sirve para crear la forma repetitiva del patrón
    for j in range(5):

        # Mueve la tortuga hacia adelante
        # La distancia aumenta con i para que la figura crezca
        forward(i * 0.5)

        # Gira a la izquierda un ángulo específico
        # Este ángulo crea un patrón geométrico interesante
        left(160.2456)

        # Luego gira un poco a la derecha
        # Esto cambia la dirección del patrón
        right(30)

        # Dibuja un arco de círculo
        # El tamaño del círculo también crece con i
        circle(i * 0.20, 70)

# Mantiene la ventana abierta cuando termina el dibujo
done()
