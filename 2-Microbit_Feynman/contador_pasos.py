from microbit import *


# Inicializar el contador de pasos
pasos = 0


while True:
    # Detectar si el Micro:bit está siendo agitado
    if accelerometer.was_gesture("shake"):
        pasos += 1  # Incrementar el contador


    # Mostrar pasos al presionar botón A
    if button_a.is_pressed():
        display.scroll(str(pasos))


    # Reiniciar el contador al presionar botón B
    if button_b.is_pressed():
        pasos = 0
        display.show("R")  # Mostrar una "R" como confirmación
