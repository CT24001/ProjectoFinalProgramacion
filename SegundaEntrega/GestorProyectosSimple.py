# Gestor de Proyectos Simple
# Un proyecto tiene varias tareas asignadas a empleados. Los
# empleados pueden registrar las horas que trabajan en cada tarea.Se debe permitir
# calcular el total de horas por tarea o por proyecto.Evitar que un empleado registre
# jornadas irreales (por ejemplo, más de 24 horas en un día).

import json 
import os



# Listas donde se van a almacenar los datos de los empleados y proyectos
empleados = []
proyectos = []

# Archivos que va a almacenar la informacion de los empleados y 
# los proyectos de la empresa
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_EMPLEADOS = os.path.join(BASE_DIR, 'empleados.json')
ARCHIVO_PROYECTOS = os.path.join(BASE_DIR, 'proyectos.json')

def main():
    # Se cargan los datos de los empleados y los proyectos
    cargar_empleado()
    cargar_proyecto()

    print("==========================================")
    print("        GESTOR DE PROYECTOS SIMPLE        ")
    print("==========================================\n")
    print("1. Gestion de Empleados")
    print("2. Gestion de Proyectos")
    print("3. Gestion de Tareas")
    print("4. Registro de Horas")
    print("5. Reporte")
    print("6. Salir")
    print(" ")
    opcion = input("Seleccione una opcion\n")

    match opcion:
        case "1":
            menuEmpleado()
        case "2":
            menuProyecto()
        case "3":
            menuTarea()
        case "4":
            menuRegistroHoras()
        case "5":
            menuReporte()
        case '6':
            print("Hasta luego")
            exit() # Comando de python para salir del programa
        case _:
            print("Opcion no valida. Intente de nuevo")
            main()
    


# --------------------------
# Modulo de Empleados
#-------------------------

def menuEmpleado():
    print("\n Menu Empleados")
    print("1. Crear nuevo empleado")
    print("2. Mostrar empleados")
    print("3. Eliminar empleado")
    print("4. Volver")
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
            
            # Se crea el dicionario con los datos del empleado que se recibio
            empleado = {
                "id": id_empleado,
                "nombre": nombre
            }

            # Agregando a la lista de los empleados
            empleados.append(empleado)

            # Se llama a la funcion para poder guardar los datos en el archivo json
            if guardar_empleado():
                print("'Empleado agregado exitosamente")
            else:
                print("Fallo al guardar el empleado")
            menuEmpleado()

        case "2":
            # Se verifica si hay empleados 
            if len(empleados) == 0:
                print("No hay empleados\n")
            else:
                # Si hay empleado se recorre la lista con los datos de los empleados
                print("\nEmpleados Registrados")
                for empleado in empleados:
                    print(empleado["id"],"-",empleado["nombre"])
                print(" ")
            menuEmpleado()
        case "3":
            if len(empleados) == 0:
                print("No hay empleados\n")
            else:
                print("\n Empleados")
                for empleado in empleados:
                    print(empleado["id"],"-",empleado["nombre"])
                print(" ")
                try:
                    indice = int(input("\nIngrese el número del empleado a eliminar (0 para cancelar): "))
                    if indice == 0:
                        menuEmpleado()
                        return
                    if 1 <= indice <= len(empleados):
                        empleado_eliminado = empleados.pop(indice - 1)
                        if guardar_empleado():
                            print(f"Empleado '{empleado_eliminado['nombre']}' eliminado exitosamente")
                        else:
                            print(" Error al guardar los cambios")
                    else:
                        print("Número de empleado no válido")
                except ValueError:
                    print("Por favor, ingrese un número válido")

            menuEmpleado()
        case "4":
            main()
        case _:
            print("Opción no válida")
            menuEmpleado()

    



def guardar_empleado():
    # Esta funcion guarda la lista de empleados en el archivo JSON
    try:
        with open(ARCHIVO_EMPLEADOS, 'w',encoding='utf-8') as f:
                json.dump(empleados,f,indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f'Error al guarda el empleado {e}')
        return False

def cargar_empleado():
    # Esta funcion carga la lista de empleados del archivo JSON
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
    print("3. Eliminar proyecto")
    print("4. Volver")
    opcion = input("Seleccione una opcion\n")

    

    match opcion:
        case "1":
            # Se obtiene el nombre del proyecto
            nombre_proyecto = input("Ingrese el nombre del proyecto\n")

            # Verificar si ese proyecto ya existe o no
            existe = any(proy['nombre']== nombre_proyecto for proy in proyectos)
            if existe:
                print("Ya esta registrado ese proyecto \n")
                menuProyecto()
                return

            # Se crea el diccionario para guargar la info del proyecto 
            # ademas se crea un lista vacioa de tareas la cual va a almacenar 
            # la tareas de cada proyecto
            proyecto = {
                "nombre": nombre_proyecto,
                "tareas": []
            }

            proyectos.append(proyecto)
            # Guardar la informacion del proyecto en el archivo JSON
            if guardar_proyecto():
                print(f'Proyecto {nombre_proyecto} agregado exitosamente')
            else:
                print("No se puedo guardar el proyecto")
            menuProyecto()

        case "2": 
            # Verificar que hayan proyectos guardados y si es asi se mostraria todos los 
            #proyectos guardados
            if len(proyectos) == 0:
                print("No hay proyectos registrados")
            else:
                print("\n Proyectos Registrados")
                for i, proyecto in enumerate(proyectos, start=1):
                    print(i, "-", proyecto["nombre"])
            menuProyecto()
        case "3":
            if len(proyectos) == 0:
                print("No hay proyectos registrados")
            else:
                print("\n Proyectos ")
                for i, proyecto in enumerate(proyectos, start=1):
                    print(i, "-", proyecto["nombre"])
                try:
                    indice = int(input("\nIngrese el número del proyecto a eliminar (0 para cancelar): "))
                    if indice == 0:
                        menuProyecto()
                        return
                    if 1 <= indice <= len(proyectos):
                        proyecto_eliminado = proyectos.pop(indice - 1)
                        if guardar_proyecto():
                            print(f"✅ Proyecto '{proyecto_eliminado['nombre']}' eliminado exitosamente")
                        else:
                            print("Error al guardar los cambios")
                    else:
                        print("Número de proyecto no válido")
                except ValueError:
                    print(" Por favor, ingrese un número válido")
          
            menuProyecto()
        case "4":
            main()
        case _:
            print("Opción no válida")
            menuProyecto()

def guardar_proyecto():
    
    try:
        with open(ARCHIVO_PROYECTOS, 'w', encoding='utf-8') as f:
            json.dump(proyectos, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f'Error al guardar el proyecto: {e}')
        return False

def cargar_proyecto():
    
    global proyectos
    if os.path.exists(ARCHIVO_PROYECTOS):
        try:
            with open(ARCHIVO_PROYECTOS, 'r', encoding='utf-8') as f:
                proyectos = json.load(f)
            print(f"Se cargaron {len(proyectos)} proyectos")
        except Exception as e:
            print(f"Error al cargar los datos de los proyectos: {e}")
            proyectos = []
    else:
        print(" No existe archivo de proyectos")
        proyectos = []


# ------------------------
# Modulo Tareas
#-------------------------
def menuTarea():
    print("\n" + "="*40)
    print("        GESTIÓN DE TAREAS")
    print("="*40)
    print("1. Crear nueva tarea")
    print("2. Ver tareas por proyecto")
    print("3. Volver")
    opcion = input("Seleccione una opcion\n")

    match opcion:
        case "1":
            # Se verifica que existan proyectos 
            if not proyectos:
                print(" No hay proyectos registrados.")
            else:
                # Selección de Proyecto
                print("\n Proyectos")
                for i, p in enumerate(proyectos, start=1):
                    print(f"{i}. {p['nombre']}")
                
                try:
                    # Se solicita al usuario que el # de proyecto para agregar tarea 
                    p_idx = int(input("Seleccione el número del proyecto: ")) - 1
                    # Se verfica que # de proyecto se valido entonces se pide 
                    # el nombre de la tarea
                    if 0 <= p_idx < len(proyectos):
                        nombre_tarea = input("Nombre de la tarea: ")
                        
                        # Se inicializa con 'registros' vacío para las futuras horas
                        nueva_tarea = {
                            "nombre": nombre_tarea,
                            "registros": []
                        }
                        # Se agrega la tarea al proyecto selecionado
                        proyectos[p_idx]["tareas"].append(nueva_tarea)
                        
                        # Se guardan los datos en el archivo JSON
                        if guardar_proyecto():
                            print(f"✅ Tarea '{nombre_tarea}' agregada exitosamente.")
                    else:
                        print(" Índice no válido.")
                except ValueError:
                    print(" Error: Ingrese solo números.")
            menuTarea()

        case "2":
            print("\n--- Listado de Tareas ---")
            # Se recorre todos los proyectos y se verifica si tiene tareas o no para poder 
            # mostrarlas
            for p in proyectos:
                print(f"Proyecto: {p['nombre']}")
                if not p["tareas"]:
                    print("  (Sin tareas)")
                for t in p["tareas"]:
                    print(f"  - {t['nombre']}")
            menuTarea()

        case "3":
            main()
        case _:
            # Manejar cuando el usuario ingresa una opcion no válida
            print(" Opción no válida")
            menuTarea()

# ------------------------
# Modulo Registro de Horas
#-------------------------         
def menuRegistroHoras():
    print("\n" + "•"*40)
    print("       REGISTRO DE HORAS")
    print("•"*40)
    print("1. Cargar horas a una tarea")
    print("2. Volver")
    opcion = input("Seleccione una opcion\n")

    match opcion:
        case "1":
            # Verificar que existan empleados y proyectos para poder registrar horas
            if not empleados or not proyectos:
                print("⚠ Se requieren empleados y proyectos con tareas.")
            else:
                try:
                    # 1. Seleccionar Proyecto
                    print("\n--- Seleccione Proyecto ---")
                    for i, p in enumerate(proyectos, start=1):
                        print(f"{i}. {p['nombre']}")
                    p_idx = int(input("Número: ")) - 1

                    if 0 <= p_idx < len(proyectos):
                        # 2. Seleccionar Tarea
                        tareas = proyectos[p_idx]["tareas"]
                        # Se verifica que el proyecto tenga tareas
                        if not tareas:
                            print(" Este proyecto no tiene tareas.")
                        else:
                            print("\n--- Seleccione Tarea ---")
                            for i, t in enumerate(tareas, start=1):
                                print(f"{i}. {t['nombre']}")
                            t_idx = int(input("Número: ")) - 1
                            
                            # Se verfica que la tarea seleciona exista
                            if 0 <= t_idx < len(tareas):
                                # 3. Seleccionar Empleado
                                print("\n--- Seleccione Empleado ---")
                                for i, e in enumerate(empleados, start=1):
                                    print(f"{i}. {e['nombre']}")
                                e_idx = int(input("Número: ")) - 1

                                # Validar que el empleado exista
                                if 0 <= e_idx < len(empleados):
                                    # 4. Registrar Horas
                                    h = float(input(f"Horas de {empleados[e_idx]['nombre']}: "))
                                    
                                    # Calcular el total de hora 
                                    horas_actuales = sum(r["horas"] for r in proyectos[p_idx]["tareas"][t_idx]["registros"])
                                    if horas_actuales + h > 24:
                                        print(f"⚠ Error: No se pueden asignar más de 24 horas a una tarea. (Actuales: {horas_actuales}, Intentando agregar: {h})")
                                    else:
                                        # Se crea el registro de horas con su empleado correspondiente
                                        registro = {
                                            "empleado": empleados[e_idx]["nombre"],
                                            "horas": h
                                        }
                                        # Se agrega el registro a la tarea
                                        proyectos[p_idx]["tareas"][t_idx]["registros"].append(registro)
                                        
                                        # Se guarda los datos en el archivo JSON
                                        if guardar_proyecto():
                                            print("Horas guardadas correctamente.")
                                else: 
                                    print(" Empleado no válido.")
                            else: 
                                print(" Tarea no válida.")
                    else: 
                        print("Proyecto no válido.")
                except ValueError:
                    print(" Error: Entrada de datos incorrecta.")
            menuRegistroHoras()

        case "2":
            main()

        case _:
            print(" Opción no válida")
            menuRegistroHoras()

# ------------------------
# Modulo Reportes
#-------------------------
def menuReporte():
    print("\n" + "="*40)
    print("           REPORTES")
    print("="*40)
    print("1. Reporte de horas por tarea")
    print("2. Reporte de horas por proyecto")
    print("3. Volver")

    opcion = input("Seleccione una opcion\n")

    match opcion:

        case "1":
            print("\n===== HORAS POR TAREA =====")
            # Verificar si existen proyectos registrados
            if not proyectos:
                print("No hay proyectos registrados.")
            else:
                # Recorrre cada proyecto
                for proyecto in proyectos:

                    print(f"\nProyecto: {proyecto['nombre']}")
                    
                    # Verifica que el proyecto tenga tareas
                    if not proyecto["tareas"]:
                        print("  (Sin tareas)")
                    else:
                        # Se recorre cada tarea que tiene cada proyecto
                        for tarea in proyecto["tareas"]:
                            # Calcular el total de horas de la tarea sumando todos los registros
                            total_horas = 0

                            for registro in tarea["registros"]:
                                total_horas += registro["horas"]

                            # Se muestra todos los datos obtenidos 
                            print(f"  Tarea: {tarea['nombre']}")
                            print(f"  Total Horas: {total_horas}")

            menuReporte()

        case "2":
            print("\n===== HORAS POR PROYECTO =====")
            
            # Verificar si existen proyectos registrados
            if not proyectos:
                print("No hay proyectos registrados.")
            else:
                for proyecto in proyectos:

                     # Calcular el total de horas del proyecto sumando todas las tareas
                    total_proyecto = 0
                    #  Sumar horas de todas las tareas del proyecto
                    for tarea in proyecto["tareas"]:

                        for registro in tarea["registros"]:
                            total_proyecto += registro["horas"]

                     # Mostrar el resultado del proyecto
                    print(f"\nProyecto: {proyecto['nombre']}")
                    print(f"Total de horas trabajadas: {total_proyecto}")

            menuReporte()

        case "3":
            main()

        case _:
            print("Opcion invalida")
            menuReporte()


# ============================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================
if __name__ == "__main__":
    main()