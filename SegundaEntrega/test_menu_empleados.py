# Se importa todas las librerias necesarias para las pruebas
import json
import pytest
import GestorProyectosSimple as gps


# ---------- PRUEBA GUARDAR EMPLEADOS ----------
def test_guardar_empleado(tmp_path, monkeypatch):

    # Crea una carpeta temporal 
    archivo = tmp_path / "empleados.json"

    monkeypatch.setattr(gps, "ARCHIVO_EMPLEADOS", str(archivo))

    # Se vacia los empleados existentes
    gps.empleados.clear()

    # Despues que se vacian los empleados se agrega el empleado
    gps.empleados.append({
        "id": "001",
        "nombre": "Carlos"
    })

    # Se guarda el resultado de la ejecucion de la funcion
    resultado = gps.guardar_empleado()

    # Verifica los diferentes procesos 
    assert resultado is True
    assert archivo.exists()


# ---------- PRUEBA DE CARGAR LOS DATOS DEL ARCHIVO JSON ----------
def test_cargar_empleado(tmp_path, monkeypatch):

    archivo = tmp_path / "empleados.json"

    # Se tiene datos fictisios 
    datos = [
        {
            "id": "001",
            "nombre": "Ana"
        }
    ]

    # Se crea el archivo json y se guardan los datos 
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f)

    monkeypatch.setattr(gps, "ARCHIVO_EMPLEADOS", str(archivo))

    # Se limpia la lista 
    gps.empleados.clear()

    # Se carga los datos del empleado
    gps.cargar_empleado()

    # Se comprueba que los datos fictisios se cargaron 
    assert gps.empleados[0]["id"] == "001"
    assert gps.empleados[0]["nombre"] == "Ana"


# ---------- PRUEBA DE VER SI EL ARCHIVO NO EXISTE ----------
def test_cargar_sin_archivo(tmp_path, monkeypatch):
    # Se tiene un archivo que no existe 
    archivo = tmp_path / "vacio.json"

    monkeypatch.setattr(gps, "ARCHIVO_EMPLEADOS", str(archivo))
    # Se limpia los dato y despues de ejecuta la funcion de guardar empleados 
    gps.empleados.clear()

    gps.cargar_empleado()

    # Dato que el archivo no existe no deberia haber nada cargado 
    assert len(gps.empleados) == 0


# ---------- ID DUPLICADA ----------
def test_id_repetida():

    gps.empleados.clear()

    gps.empleados.append({
        "id": "001",
        "nombre": "Luis"
    })

    # Se recorre todo los empleado y se busca el empleado requerido 
    existe = any(emp["id"] == "001" for emp in gps.empleados)

    # Se verfica si encontro el empleado
    assert existe is True


# ---------- PRUEBA DE ELIMINAR EMPLEADO----------
def test_eliminar_empleado():

    # Se limpia la lista y despues de agrega empleados
    gps.empleados.clear()

    gps.empleados.extend([
        {"id": "1", "nombre": "Juan"},
        {"id": "2", "nombre": "Pedro"}
    ])
    # Se elemina un usuario 
    eliminado = gps.empleados.pop(0)

    # Validar que el usuario fue eliminado y ver si solo queda un empleado registrado 
    assert eliminado["nombre"] == "Juan"
    assert len(gps.empleados) == 1