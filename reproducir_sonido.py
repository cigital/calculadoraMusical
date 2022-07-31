from mingus.midi import fluidsynth
from time import sleep
import time
import random

fluidsynth.init("FluidR3_GM.sf2")
fluidsynth.set_instrument(1, 44)

def pianoSonido(tecla):
    for i in range(12):
        nota_cambiante = random.randint(0, 85)-int(tecla)
        if nota_cambiante < 0:
            nota_cambiante *= -1

        fluidsynth.play_Note(nota_cambiante, 1, nota_cambiante)
        time.sleep(1)

def para_sonido():
    fluidsynth.stop_everything()
