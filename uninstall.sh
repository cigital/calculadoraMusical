#!/bin/sh 

echo -e "\nDesinstalando requisitos.."

sudo apt-get uninstall portaudio python-tkinter fluidsynth || sudo pacman -R portaudio tk && yay -R fluidsynth-git
pip uninstall -r ./requirements.txt  

echo -e "\nBorrando el directorio..."

sudo rm -rf entorno

echo -e "\nSe acabó la desinstalación"
