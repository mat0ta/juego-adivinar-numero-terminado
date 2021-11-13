# Importamos las Bibiotecas
import random
from itertools import permutations

class juegoterminado():
    def __init__(self):
        self.tabla_puntuaciones = []
        self.nombre = str
        self.dificultad = 1
        self.intentos_permitidos = 10
        self.intentos_realizados = 0
        self.numero_maximo = 100
    def pedir_nombre(self, nombre):
        self.nombre = str(nombre)
    def perdir_dificultad(self, nivel):
        while not nivel.isdigit():
            nivel = input('Introduzca un número válido: ')
        while int(nivel) < 1 or int(nivel) > 4:
            nivel = input('Introduzca un número válido: ')
        self.dificultad = int(nivel)
        self.numero_maximo = 100 ** int(self.dificultad)
        print('Dificultad seleccionada: ' + str(self.dificultad))
    def iniciar_juego(self, numero):
        numeroDado = input('Introcude un número del 1 al ' + str(self.numero_maximo))



a = juegoterminado()