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
        while not nivel.isdigit() and 1 >= nivel <= 4:
            nivel = input('Introduzca un número válido: ')
        self.dificultad = nivel

