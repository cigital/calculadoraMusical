#!/bin/sh 

echo "Instalando virtualenv..."

pip install -q virtualenv

echo -e "\nCreando el directorio..."

mkdir entorno

echo -e "\nCreando el entorno..."

python3 -m virtualenv entorno -q
source entorno/bin/activate 

echo -e "\nInstalando requisitos.."

sudo apt-get install portaudio python-tkinter fluidsynth || sudo pacman -S portaudio tk && yay -S fluidsynth-git

pip install -r ./requirements.txt -q 

echo -e "\nSe acabó la instalación"
