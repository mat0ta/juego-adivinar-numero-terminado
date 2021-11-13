# Importamos las Bibiotecas
import random
from itertools import permutations

# Decalramos las variables
juegoTerminado = False

class juegoterminado():
    def __init__(self):
        self.tabla_puntuaciones = []
        self.nombre = str
        self.dificultad = 1
        self.intentos_permitidos = 20
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
    def iniciar_juego(self):
        numero = random.randint(1, self.numero_maximo + 1)
        numeroDado = input('Introcude un número del 1 al ' + str(self.numero_maximo) + ': ')
        while int(numeroDado) != int(numero):
            if int(numeroDado) < int(numero) and self.intentos_realizados < self.intentos_permitidos:
                self.intentos_realizados += 1
                print('--------------')
                print('| ' + str(self.intentos_realizados) + ' intentos |')
                print('--------------')
                numeroDado = input('Te has quedado corto. Inténtalo de nuevo: ')
            elif int(numeroDado) > int(numero) and self.intentos_realizados < self.intentos_permitidos:
                self.intentos_realizados += 1
                print('--------------')
                print('| ' + str(self.intentos_realizados) + ' intentos |')
                print('--------------')
                numeroDado = input('Te has pasado. Inténtalo de nuevo: ')
            elif self.intentos_realizados >= self.intentos_permitidos:
                return print('Has agotado todos tus intentos. Game over.')
        self.intentos_realizados += 1
        print('--------------------------------------------')
        print('¡Enhorabuena, lo has acertado en ' + str(self.intentos_realizados) + ' intento(s)!')
        print('--------------------------------------------')
        juegoTerminado = True
    def entrada_tabla(self):
        entrada = {
            'nombre': self.nombre,
            'intentos': self.intentos_realizados,
            'dificultad': self.dificultad,
        }
        self.tabla_puntuaciones.append(entrada)
    # def visualizar_tabla(self):
    #     print('-----------------------------------------------')
    #     for jugador in self.tabla_puntuaciones:
    #         print('| Nombre: ' + jugador['nombre'] + ' | Dificultad: ' + jugador['dificultad'] + ' | Intentos: ' + jugador['intentos'] + ' |')
    #     print('-----------------------------------------------')



a = juegoterminado()

def empezar():
    a.pedir_nombre(input('¿Cual es tu nombre?: '))
    a.perdir_dificultad(input('Elige una dificultad del 1 al 4: '))
    a.iniciar_juego()

empezar()