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
            existe = any(proy['nombre']== nombre_proyecto for proy in proyectos)
            
            if existe:
                print("Ya esta registrado ese proyecto \n")
                menuProyecto()
                return

            proyecto = {
                "nombre": nombre_proyecto,
                "tareas": []
            }

            proyectos.append(proyecto)
            if guardar_proyecto():
                print(f'Proyecto {nombre_proyecto} agregado exitosamente')
            else:
                print("No se puedo guardar el proyecto")
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
            print(f"✅ Se cargaron {len(proyectos)} proyectos")
        except Exception as e:
            print(f"Error al cargar los datos de los proyectos: {e}")
            proyectos = []
    else:
        print("📋 No existe archivo de proyectos")
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
                                    registro = {
                                        "empleado": empleados[e_idx]["nombre"],
                                        "horas": h
                                    }
                                    proyectos[p_idx]["tareas"][t_idx]["registros"].append(registro)
                                    
                                    if guardar_proyecto():
                                        print("✅ Horas guardadas correctamente.")
                                else: print("⚠ Empleado no válido.")
                            else: print("⚠ Tarea no válida.")
                    else: print("⚠ Proyecto no válido.")
                except ValueError:
                    print("⚠ Error: Entrada de datos incorrecta.")
            menuRegistroHoras()

        case "2":
            main()

if __name__ == "__main__":
    main()