import funciones as f
while True:
    f.limpiarpantalla()
    f.printv("SISTEMA VENTABOOKS")
    f.printv("------------------")
    print("1)Guardar")
    print("2)Buscar")
    print("3)Certificados")
    print("0)Salir")
    opcion=int(input("Seleccione: "))
    if opcion==0:
        f.printv("Adios")
        break
    elif opcion==1:
        f.printv("Guardar")
    elif opcion==2:
        f.printv("Buscar")
    elif opcion==3:
        f.printv("Certificados")
    else:
        f.printr("No valido")