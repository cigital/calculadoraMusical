![Banner](https://github.com/cigital/calculadoraMusical/blob/main/images/banner.png)

# 🎵 Calculadora Musical 🎵 
![Github](https://img.shields.io/github/last-commit/cigital/calculadoraMusical)
![Github](https://img.shields.io/github/license/cigital/calculadoraMusical)

Este proyecto sirve para reproducir sonidos con los resultados de la calculadora mediante MIDI, 
puedes cambiar de instrumento e velocidad si lo deseas.

!! ADVERTENCIA, esto solo esta probado en Arch Linux !!

## Instalación
Clona el repositorio al entorno y muevelo al directorio entorno:
```bash
git clone https://github.com/cigital/calculadora-musical && cd calculadora-musical
```

Dale permisos de ejecución al archivo de instalación y desinstalación

```bash
chmod +x ./install.sh ./uninstall.sh 
```
Ejecuta el archivo install.sh

```bash
./install.sh
```

## Como usar
Entra en el entorno

```bash
source entorno/bin/activate
```

Ejecuta el archivo calculadora.py

```python
python3 calculadora.py
```

## Configurar
Puedes elegir entre "FluidR3_GM.sf2" o "freepats-general-midi.sf2", cambiando en la linea de 5 en "reproducir_sonido.py" al que quieras.

En "calculadora.py" esta comentado el boton PI, si quieres este boton, descomenta las lineas 24, 102 y 281-290.

Puedes probar los instrumentos ejecutando "reproducir_instrumento.py"

```python
python3 reproducir_instrumento.py
```

Para tener otro instrumento cambia en la linea 6 en el archivo "reproducir_sonido.py" el valor 44 por el numero de instrumento que deseas, los numeros de instrumentos validos estan [aquí](https://soundprogramming.net/file-formats/general-midi-instrument-list/ ). 

Y en el archivo "calculadora.py" cambia en la linea 200 el numero 84 por la nota maxima que tenga tu instrumento.

Notas maximas intrumentos:

Nota 72 --> [ 33 - 40 ] , [ 65 - 72 ]

Nota 84 --> [ 41 - 48 ] , [ 49 - 56 ] , [ 57 - 64 ]

Nota 96 --> [ 0 - 8 ] , [ 17 - 24 ] , [ 89 - 104 ] , [ 113 - 119 ]

Nota 115 --> [ 9 - 16 ] , [ 25 - 32 ] , [ 73 - 88 ] , [ 105 - 112 ] ,[ 120 - 127 ]

## Aclaración
El progama no funciona con numero muy pequeños.

## Referencias
[Mingus doc](https://bspaans.github.io/python-mingus/index.html) | [Midi instruments]( https://soundprogramming.net/file-formats/general-midi-instrument-list/) | [Plantilla de calculadora](https://github.com/programiz/Calculator)
