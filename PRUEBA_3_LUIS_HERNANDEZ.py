alumno = []


def preguntar():
    print("Elegir una opcion escribir solo el numero")
    print("1.- Grabar")
    print("1.- buscar")
    print("3.- Imprimr")
    print("4.- Salir")
    try:
        pregunta = int(input())
        if pregunta == 1 or pregunta == 2 or pregunta == 3 or pregunta == 4:
            return pregunta
        else:
            print("Opcion invalida")
            return preguntar()
    except ValueError:
        print("Ingrese solo numeros ")
        return preguntar()


def grabar():
    print("Ingrese los solicitados ")
    while True:
        rut = input("Rut")
        if len(rut) == 0:
            print("Rut no debe estar vacio")
        elif len(rut) == 10:
            break
        else:
            print("Rut debe tener 10 carateres")
    while True:
        nombre = input("Nombre: ")
        if len(nombre) == 0:
            print("nombre no puede estar vacio")
        elif len(nombre) >= 2 and len(nombre) <= 12:
            break
        else:
            print("Nombre debe tener entre 2 y 12 caracteres")
    while True:
        apellido = input("Apellido")
        if len(apellido) == 0:
            print("Apellido no purde estar vacio")
        else:
            break
    while True:
        fecha_de_nacimiento = input("fecha de nacimineto")
        if len(fecha_de_nacimiento) == 0:
            print("La fecha  no pude estar vacio")
        else:
            break
    while True:
        carrera = input("carrera")
        if len(carrera) == 0:
            print("carrera no puede estar vacio")
            break
    while True:
        asignatura = input("Asignatura")
        if len(asignatura) == 0:
            print("asignatura no pude estar vacio")
        else:
            break
    while True:
        try:
            promedio = float(input("Nota: "))
            if promedio >= 1.0 and promedio <= 7.0:
                break
            else:
                print("nota debe ser entre 1 y 7")
        except ValueError:
            print("Ingrese solo numeros")
    while True:
        num_lista = input("Numero de lista")
        if len(num_lista) == 0:
            print("numero de lista no puede estar vacio")
        else:
            break
    alumnos.append([rut, nombre, apellido, fecha_de_nacimiento,
                   carrera, asignatura, promedio, num_lista])
    print("alumno Agregado")
    return rut


def buscar():
    if len(alumnos) == 0:
        print("No existe Alumno ")
    else:
        while True:
            rut = input("RUT")
            if len(rut) == 0:
                print("RUT no puede estar vacio")
            elif len(rut) == 10:
                break
            else:
                print("Su RUT debe tener 10 caracteres")
        for alumno in alumnos:
            if alumno[0] == rut:
                print("RUT: " + alumno[0])
                print("NOMBRE: " + alumno[1])
                print("APELLIDO: " + alumno[2])
                print("FECHA DE NACIMIENTO" + alumno[3])
                print("CARRERA" + alumno[4])
                print("ASIGNATURA" + alumno[5])
                print("PROMEDIO" + str(alumno[6]))
                print("NUMERO DE LISTA" + alumno[7])
                return rut
            else:
                print("ALUMNO NO ENCONTRADO")


def imprimir(rut=None):
    if len(alumnos) == 0:
        print("NO HAY ALUMNOS ")
    elif rut is not None:
        respuesta = input("DESEA UAR EL RUT AGREGADO ANTERIORMENTE? S/N: ")
        if respuesta == "S" or respuesta == "s":
            for alumno in alumnos:
                if alumno[0] == rut:
                    nombre = alumno[1]
                    apellido = alumno[2]
                    carrera = alumno[4]
                    asignatura = alumno[5]
                    promedio = alumno[6]
        elif respuesta == "N" or respuesta == "n":
            print("BUSQUE EL RUT DEL ALUMNO")
            rut = buscar()
            for alumno in alumnos:
                if alumno[0] == rut:
                    nombre = alumno[1]
                    apellido = alumno[2]
                    carrera = alumno[4]
                    asignatura = alumno[5]
                    promedio = alumno[6]
        else:
            print("OPCION NO VALIDA")
            return
        menu = """Eliga una opcion escribiendo solo el numero
        1. CERTIFICADO DE ALUMNO REGULAR 
        2. CERTIFICADO DE NOTAS 
        3. CERTIFICADO DE MATRICULA
        4. SALIR"""
        print(menu)
        while True:
            try:
                pregunta = int(input())
                if pregunta == 1 or pregunta == 2 or pregunta == 3 or pregunta == 4:
                    break
                else:
                    print("OPCION NO VALIDA")
            except ValueError:
                print("ELIJA UNA OPCION VALIDA")
        if pregunta == 1:
            print("CERTIFICADO DE ALUMNO REGULAR ")
            print(f"RUT: {rut}")
            print(f"NOMBRE: {nombre}", end=" ")
            print(f"APELLIDO: {apellido}")
            print(f"CARRERA: {carrera}")
        elif pregunta == 2:
            print("CERTIFICADO DE NOTAS ")
            print(f"RTU: {rut}")
            print(f"NOMBRE: {nombre}", end=" ")
            print(f"APELLIDO: {apellido}")
            print(f"ASIGNATURA: {asignatura}")
            print(f"PROMEDIO: {promedio}")
        elif pregunta == 3:
            print("CERTIFICADO DE MATRICULA")
            print(f"RUT: {rut}")
            print(f"NOMBRE: {nombre}", end=" ")
            print(f"APELLIDO: {apellido}")
            print(f"CARRERA: {carrera}")
        elif pregunta == 4:
            print("RETORNNDO AL MENU PRINCIPAL")
            return
        elif rut is None:
            print("NO EXIXTE EL RUT")


def salir():
    print("PROGRAMA FINALIZADO")
    exit()


def main():
    print("BIENVENIDO")
    rut = None
    while True:
        pregunta = preguntar()
        if pregunta == 1:
            rut = grabar()
        elif pregunta == 2:
            rut = buscar()
        elif pregunta == 3:
            imprimir(rut)
        elif pregunta == 4:
            salir()


if __name__ == '__main__':
    main()
