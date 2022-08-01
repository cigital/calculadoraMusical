![Banner](https://github.com/cigital/calculadoraMusical/blob/main/screenshots/banner.png)

# 🎵 Calculadora Musical 🎵 
Este proyecto sirve para reproducir sonidos con los resultados de la calculadora mediante MIDI, 
puedes cambiar de instrumento e velocidad si lo deseas.

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
Puedes elegir entre "FluidR3_GM.sf2" o "freepats-general-midi.sf2", cambia en la linea de 5 en "reproducir_sonido.py" al que quieras.

En "calculadora.py" esta comentado el boton PI, si quieres este boton, descomenta las lineas 24, 102 y 281-290.

Puedes probar los instrumentos ejecutando el archivo "reproducir_instrumento.py"

```python
python3 reproducir_instrumento.py
```

Para tener otro instrumento cambia en la linea 6 en el archivo "reproducir_sonido.py" el valor 44 por el numero de instrumento que deseas, los numeros de instrumentos validos estan ![aquí](htt  ips://soundprogramming.net/file-formats/general-midi-instrument-list/ ). 

Y en el archivo "calculadora.py" cambia en la linea 200 el numero 84 por el numero de teclas maximas que tenga tu instrumento.

Los instrumentos [ 0 - 8 ] su maximo es 96

Los instrumentos [ 9 - 16 ] su maximo es 115

Los instrumentos [ 17 - 24 ] su maximo es 96

Los instrumentos [ 25 - 32 ] su maximo es 115 

Los instrumentos [ 33 - 40 ] su maximo es 72 

Los instrumentos [ 41 - 48 ] su maximo es 84

Los instrumentos [ 49 - 56 ] su maximo es 84

Los instrumentos [ 57 - 64 ] su maximo es 84

Los instrumentos [ 65 - 72 ] su maximo es 72

Los instrumentos [ 73 - 80 ] su maximo es 115

Los instrumentos [ 81 - 88 ] su maximo es 115

Los instrumentos [ 89 - 96 ] su maximo es 96

Los instrumentos [ 97 - 104 ] su maximo es 96

Los instrumentos [ 105 - 112 ] su maximo es 115

Los instrumentos [ 113 - 119 ] su maximo es 96 

Los instrumentos [ 120 - 127 ] su maximo es 115

## Aclaración
No funciona con numero muy pequeños.

## Referencias
![Mingus doc](https://bspaans.github.io/python-mingus/index.html)

![Midi instruments]( https://soundprogramming.net/file-formats/general-midi-instrument-list/)

![Plantilla de calculadora](https://github.com/programiz/Calculator)
