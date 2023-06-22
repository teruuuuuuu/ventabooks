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
        print("1)Certificado criticas")
        print("2)Certificado detalle ventas")
        cert=int(input("Seleccione: "))
        if cert==1:
            f.printv("Certificado de criticas")
        elif cert==2:
            f.printv("Certificado detalle de ventas")
        else:
            f.printr("Opcion ni valida")
    else:
        f.printr("No valido")