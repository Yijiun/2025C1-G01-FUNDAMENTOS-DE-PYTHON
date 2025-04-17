"""
Autor: Yi Jiun Liu Lin
Fecha: 2025-04-16
Version: 0.1
Sistema de Gestión de Ventas que nos permita ingresar, almacenar y analizar datos de ventas.
"""

import os
from modulo import ingresar_ventas, guardar_ventas, analisis_venta
    

def limpiar_pantalla():
    """ Limpia la pantalla de la terminal en ejecucion """
    os.system('cls' if os.name =='nt' else 'clear')

def pausar():
    input('\nPresione Enter para continuar...')

#Menu Principal
def menu():
    ventas = []
    while True:
        print('\n---- Menu Principal----')
        print('1. Ingresar ventas de cursos UMCA')
        print('2. Guardar datos en un archivo CSV')
        print('3. Analizar las ventas')
        print('4. Salir')
        opcion = input('Ingrese una opcion: ')
        
        if opcion == "1":
            limpiar_pantalla()
            print('\n ---- Ingreso de Ventas de Cursos ----')
            ingresar_ventas(ventas)
            print(ventas)
            pausar()
        elif opcion == '2':
            limpiar_pantalla()
            print('\n ---- Guardar Ventas  en CSV----')
            guardar_ventas(ventas)
            pausar()
        elif opcion == '3':
            limpiar_pantalla()
            print('\n ---- Analisis de Ventas ----') 
            analisis_venta()
            pausar()
        elif opcion == '4':
            print('\n Gracias por usar el sistema. Hasta pronto!')
            pausar()
            break  # <- Cierro el sistema deteniendo el ciclo while
        else:
            print('Opcion no valida. Intente nuevamente una opcion.')
            pausar()

#Ejecucion del sistema si solo si el archivo es el main
if __name__=='__main__':
    print('Bienvenido al sistema de Gestion de Ventas')
    pausar()
    menu()
