from mingus.midi import fluidsynth
from time import sleep
import time
import random

fluidsynth.init("FluidR3_GM.sf2")

# Reproduce una nota especifica durante 5 segundos
def reproducir_nota_especifica():
    numero_de_instrumento = int(input("El numero de tu instrumento: "))

    fluidsynth.set_instrument(1, numero_de_instrumento)
    tecla = input("La nota que quieres reproducir, en numero, ej: 4 | ")
    for i in range(5):
        fluidsynth.play_Note(int(tecla), 1, 100)
        time.sleep(1)

# Reproduce todas las notas del intrumento
def reproducir_todas_las_notas():
    numero_de_instrumento = int(input("El numero de tu instrumento: "))

    for n in range(numero_de_instrumento, 127):
        fluidsynth.set_instrument(1, n)
        for i in range(116):
            fluidsynth.play_Note(i, 1, 120)
            print(f"Estoy por el instrumento {n} y la nota {i}")
            time.sleep(0.25)

desicion = int(input("Reproducir una nota especifica -> 1 \nReproducir todas las notas -> 2 \nQue quieres hacer: "))

match desicion:
    case 1:
        reproducir_nota_especifica()
    case 2:
        reproducir_todas_las_notas()
    case other:
        print("Desición invalida")
