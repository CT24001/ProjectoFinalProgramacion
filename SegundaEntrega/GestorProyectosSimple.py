from ast import Try
import json 
import os

# Variables globales
numEmpleados = 0
numProyectos = 0

# Arreglos
empleados = []
proyectos = []

# Archivos que almacenar la informacion de los empleados y 
# los proyectos de la empresa
ARCHIVO_EMPLEADOS = 'empleados.json'
ARCHIVO_PROYECTOS = 'proyectos.json'


def main():
    # Se cargan los datos de los empleados
    cargar_empleado()

    print("==========================================")
    print("        GESTOR DE PROYECTOS SIMPLE        ")
    print("==========================================\n")
    print("1. Gestion de Empleados")
    print("2. Gestion de Proyectos")
    print("3. Gestion de Tareas")
    print("4. Registro de Horas")
    print("5. Reporte")
    print("6. Salir")
    opcion = input("Seleccione una opcion\n")

    match opcion:
        case "1":
            menuEmpleado()
        case "2":
            menuProyecto()
    



# --------------------------
# Modulo de Empleados
#-------------------------

def menuEmpleado():
    print("\n Menu Empleados")
    print("1. Crear nuevo empleado")
    print("2. Mostrar empleados")
    print("3. Volver")
    opcion = input("Seleccione una opcion\n")

    match opcion:
        case "1":
            # Pidiendo la informacion del empleado
            id_empleado = input("Ingrese el ID del empleado\n")
            nombre = input("Ingrese nombre del empleado\n")
            
            # Se verifica si ya existe la Id ingresada 
            existe = any(emp['id']== id_empleado for emp in empleados)

            if existe:
                print("Ya existe esa ID \n")
                menuEmpleado()
                return
            
            # Se crea el diccionario a ocupar
            empleado = {
                "id": id_empleado,
                "nombre": nombre
            }
            # Agregando a la lista de los empleados
            empleados.append(empleado)

            if guardar_empleado():
                print("'Empleado agregado exitosamente")
            else:
                print("Fallo al guardar el empleado")
            menuEmpleado()

        case "2":
            if len(empleados) == 0:
                print("No hay empleados\n")
            else:
                print("\nEmpleados Registrados")
                for empleado in empleados:
                    print(empleado["id"],"-",empleado["nombre"])
                print(" ")
            menuEmpleado()
        case "3":
            main()
    



def guardar_empleado():
    try:
        with open(ARCHIVO_EMPLEADOS, 'w',encoding='utf-8') as f:
                json.dump(empleados,f,indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f'Error al guarda el empleado {e}')
        return False

def cargar_empleado():
    global empleados
    if os.path.exists(ARCHIVO_EMPLEADOS):
        try: 
            with open(ARCHIVO_EMPLEADOS, 'r', encoding='utf-8') as f:
                empleados = json.load(f)
        except Exception as e:
            print(f"Error al cargar los datos de los empleados {e}")
            empleados = []
    else:
        empleados = []



# --------------------------
# Modulo de Proyecto
#-------------------------

def menuProyecto():
    print("\n Menu Proyectos")
    print("1. Crear nuevo proyecto")
    print("2. Listar todos los proyectos")
    print("3. Volver")
    opcion = input("Seleccione una opcion\n")

    

    match opcion:
        case "1":
            nombre_proyecto = input("Ingrese el nombre del proyecto\n")

            proyecto = {
                "nombre": nombre_proyecto,
                "tareas": []
            }

            proyectos.append(proyecto)
            print("Proyecto creado\n")

            menuProyecto()
        case "2": 
            if len(proyectos) == 0:
                print("No hay proyectos registrados")
            else:
                print("\n Proyectos Registrados")
                for i, proyecto in enumerate(proyectos, start=1):
                    print(i, "-", proyecto["nombre"])
            menuProyecto()
        case "3":
            main()


main()
