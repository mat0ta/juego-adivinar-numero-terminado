# Importamos las Bibiotecas
import random
from itertools import permutations

class juegoterminado():
    def __init__(self):
        self.tabla_puntuaciones = []
        self.dificultad = 1
        self.intentos_permitidos = 10
        self.intentos_realizados = 0
    def  perdir_dificultad(self, nivel):
        while not nivel.isdigit():
            nivel = input('Introduzca un número válido: ')
        while int(nivel) < 1 or int(nivel) > 4:
            nivel = input('Introduzca un número válido: ')
        self.dificultad = int(nivel)
        print('Dificultad seleccionada: ' + str(self.dificultad))

a = juegoterminado()
a.perdir_dificultad(input('Elige el nivel de dificultad entre 1 y 4: '))