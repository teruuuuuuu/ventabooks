from colorama import Fore, Style, Back
import msvcrt
import os
import random
import numpy
#crear arreglo
libros=numpy.empty([10,4],object)
#funciones de diseño
def printv(texto):
    print(f"{Fore.GREEN}{Fore.RESET}")
def printr(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{Style.RESET_ALL}{Fore.RESET}")
def limpiarpantalla():
    printv("<<Presione una tecla>>")
    msvcrt.getch()
    os.system("cls")
#funciones de arreglo
#validar codigo
#guardar
#buscar
#certificado sssssssssssss