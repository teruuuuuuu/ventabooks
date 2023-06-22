from colorama import Fore, Style, Back
import msvcrt
import os
import random
import numpy
#crear arreglo
libros=numpy.empty([10,4],object)
#funciones de diseño
def printv(texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}{Style.RESET_ALL}{Fore.RESET}")
def printr(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{Style.RESET_ALL}{Fore.RESET}")
def titulo(texto):
    print("--------------")
    print(f"{texto.upper()}")
    print("--------------")
def limpiarpantalla():
    printv("<<Presione una tecla>>")
    msvcrt.getch()
    os.system("cls")
#funciones de arreglo

#validar codigo
def validar(c):
    for i in range(10):
        if libros[i,0]==c:
            return i
    return -1     
#guardar
def guardar(c,t,a,p):
    if None in libros:
        if validar(c)>0:
            if len(t)>=4:
                if p>=0:
                    if len(a)>=10:
                        for i in range(10):
                            if libros[i,0]==None:
                                libros[i,0]=c
                                libros[i,1]=t
                                libros[i,2]=a
                                libros[i,3]=p
                                printv(f"Libro {t} registrado")
                                break
                    else:
                        printr("El autor debe tener a lo menos 10 caracteres")
                else:
                    printr("El precio debe ser mayor o igual a 0")
            else:
                printr("El titulo debe de tener a lo menos 4 caracteres")
        else:
            printr("El codiga ya esta registrado") 
    else:
        printr("No hay espacio disponible")                                       
#buscar
#certificados
critticas=[]
critticas.append("Borges es mejor")
critticas.append("1 de 10 nada recomendable")
critticas.append("Una obra maestra")
critticas.append("El primero me gusto mas")
critticas.append("Primer comentario")
critticas.append("Segundo comentario")
critticas.append("Busco novia")
critticas.append("Hoy estoy muy triste porque nadie se suscribio a mi canal :c")
critticas.append("Que interfaz mas mala cambienmela")
critticas.append("Me dio sueño")
def certificados(c):
    posicion=validar(c)
    if posicion>0:
        print(f"""{Fore.BLUE}
        -----------------------------
        CRITICAS {libros[posicion,1]}
        -----------------------------
        TITULO   {libros[posicion,2]}
        -----------------------------
        CRITICA 1: {critticas[random.randint(0,10)]}
        CRITICA 2: {critticas[random.randint(0,10)]}
        CRITICA 3: {critticas[random.randint(0,10)]}
        {Fore.RESET}""")
    else:
        printr("Codigo no encontrado")    
