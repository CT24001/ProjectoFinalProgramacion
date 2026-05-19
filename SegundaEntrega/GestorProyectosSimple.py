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
            if not proyectos:
                print("⚠ No hay proyectos registrados.")
            else:
                # Selección de Proyecto
                for i, p in enumerate(proyectos, start=1):
                    print(f"{i}. {p['nombre']}")
                
                try:
                    p_idx = int(input("Seleccione el número del proyecto: ")) - 1
                    if 0 <= p_idx < len(proyectos):
                        nombre_tarea = input("Nombre de la tarea: ")
                        
                        # Se inicializa con 'registros' vacío para las futuras horas
                        nueva_tarea = {
                            "nombre": nombre_tarea,
                            "registros": []
                        }
                        proyectos[p_idx]["tareas"].append(nueva_tarea)
                        
                        if guardar_proyecto():
                            print(f"✅ Tarea '{nombre_tarea}' agregada exitosamente.")
                    else:
                        print("⚠ Índice no válido.")
                except ValueError:
                    print("⚠ Error: Ingrese solo números.")
            menuTarea()

        case "2":
            print("\n--- Listado de Tareas ---")
            for p in proyectos:
                print(f"Proyecto: {p['nombre']}")
                if not p["tareas"]:
                    print("  (Sin tareas)")
                for t in p["tareas"]:
                    print(f"  - {t['nombre']}")
            menuTarea()

        case "3":
            main()

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
                        if not tareas:
                            print("⚠ Este proyecto no tiene tareas.")
                        else:
                            print("\n--- Seleccione Tarea ---")
                            for i, t in enumerate(tareas, start=1):
                                print(f"{i}. {t['nombre']}")
                            t_idx = int(input("Número: ")) - 1

                            if 0 <= t_idx < len(tareas):
                                # 3. Seleccionar Empleado
                                print("\n--- Seleccione Empleado ---")
                                for i, e in enumerate(empleados, start=1):
                                    print(f"{i}. {e['nombre']}")
                                e_idx = int(input("Número: ")) - 1

                                if 0 <= e_idx < len(empleados):
                                    # 4. Registrar Horas
                                    h = float(input(f"Horas de {empleados[e_idx]['nombre']}: "))

                                    horas_actuales = sum(r["horas"] for r in proyectos[p_idx]["tareas"][t_idx]["registros"])
                                    if horas_actuales + h > 24:
                                        print(f"⚠ Error: No se pueden asignar más de 24 horas a una tarea. (Actuales: {horas_actuales}, Intentando agregar: {h})")
                                    else:
                                        registro = {
                                            "empleado": empleados[e_idx]["nombre"],
                                            "horas": h
                                        }
                                        proyectos[p_idx]["tareas"][t_idx]["registros"].append(registro)
                                        
                                        if guardar_proyecto():
                                            print("✅ Horas guardadas correctamente.")
                                else: 
                                    print("⚠ Empleado no válido.")
                            else: 
                                print("⚠ Tarea no válida.")
                    else: 
                        print("⚠ Proyecto no válido.")
                except ValueError:
                    print("⚠ Error: Entrada de datos incorrecta.")
            menuRegistroHoras()

        case "2":
            main()

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

            if not proyectos:
                print("No hay proyectos registrados.")
            else:
                for proyecto in proyectos:

                    print(f"\nProyecto: {proyecto['nombre']}")

                    if not proyecto["tareas"]:
                        print("  (Sin tareas)")
                    else:
                        for tarea in proyecto["tareas"]:

                            total_horas = 0

                            for registro in tarea["registros"]:
                                total_horas += registro["horas"]

                            print(f"  Tarea: {tarea['nombre']}")
                            print(f"  Total Horas: {total_horas}")

            menuReporte()

        case "2":
            print("\n===== HORAS POR PROYECTO =====")

            if not proyectos:
                print("No hay proyectos registrados.")
            else:
                for proyecto in proyectos:

                    total_proyecto = 0

                    for tarea in proyecto["tareas"]:

                        for registro in tarea["registros"]:
                            total_proyecto += registro["horas"]

                    print(f"\nProyecto: {proyecto['nombre']}")
                    print(f"Total de horas trabajadas: {total_proyecto}")

            menuReporte()

        case "3":
            main()

        case _:
            print("Opcion invalida")
            menuReporte()

if __name__ == "__main__":
    main()