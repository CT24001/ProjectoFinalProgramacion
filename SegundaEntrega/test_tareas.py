import json
import pytest
import GestorProyectosSimple as gps


# ---------- PRUEBAS ESTRUCTURALES Y LÓGICA DE TAREAS ----------

def test_crear_tarea_estructura():
    # Limpiamos los proyectos para asegurar aislamiento
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": []
    })
    
    # Simular la creación de una tarea en la estructura de datos
    nueva_tarea = {
        "nombre": "Diseño UI",
        "registros": []
    }
    gps.proyectos[0]["tareas"].append(nueva_tarea)
    
    assert len(gps.proyectos[0]["tareas"]) == 1
    assert gps.proyectos[0]["tareas"][0]["nombre"] == "Diseño UI"
    assert gps.proyectos[0]["tareas"][0]["registros"] == []


def test_guardar_y_cargar_proyectos_con_tareas(tmp_path, monkeypatch):
    # Usar una ruta de archivo temporal para no afectar los datos de producción
    archivo = tmp_path / "proyectos.json"
    monkeypatch.setattr(gps, "ARCHIVO_PROYECTOS", str(archivo))
    
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [
            {
                "nombre": "Diseño UI",
                "registros": []
            }
        ]
    })
    
    # Guardar proyectos en el archivo temporal
    guardado_ok = gps.guardar_proyecto()
    assert guardado_ok is True
    assert archivo.exists()
    
    # Limpiar proyectos en memoria para verificar la carga correcta
    gps.proyectos.clear()
    
    # Cargar proyectos desde el archivo temporal
    gps.cargar_proyecto()
    assert len(gps.proyectos) == 1
    assert gps.proyectos[0]["nombre"] == "Proyecto Alfa"
    assert len(gps.proyectos[0]["tareas"]) == 1
    assert gps.proyectos[0]["tareas"][0]["nombre"] == "Diseño UI"


# ---------- PRUEBAS DEL MENÚ INTERACTIVO (GENTLEMEN'S INTERACTION MOCK) ----------

def test_menu_tarea_crear_exitosa(tmp_path, monkeypatch, capsys):
    archivo = tmp_path / "proyectos.json"
    monkeypatch.setattr(gps, "ARCHIVO_PROYECTOS", str(archivo))
    # Mockear main para que retorne directamente al salir del menú
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Beta",
        "tareas": []
    })
    
    # Entradas simuladas:
    # 1. Opción "1" (Crear nueva tarea)
    # 2. Proyecto "1" (Proyecto Beta, en el índice 0)
    # 3. Nombre de la tarea: "Completar Doc"
    # 4. Opción "3" (Volver / Salir del bucle recursivo)
    inputs = ["1", "1", "Completar Doc", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuTarea()
    
    # Verificar que la tarea se agregó correctamente
    assert len(gps.proyectos[0]["tareas"]) == 1
    assert gps.proyectos[0]["tareas"][0]["nombre"] == "Completar Doc"
    
    # Verificar salidas en consola
    captured = capsys.readouterr()
    assert "Tarea 'Completar Doc' agregada exitosamente" in captured.out


def test_menu_tarea_crear_indice_invalido(tmp_path, monkeypatch, capsys):
    archivo = tmp_path / "proyectos.json"
    monkeypatch.setattr(gps, "ARCHIVO_PROYECTOS", str(archivo))
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Beta",
        "tareas": []
    })
    
    # Selecciona opción 1, índice 5 (inválido porque solo hay 1 proyecto), y luego vuelve
    inputs = ["1", "5", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuTarea()
    
    captured = capsys.readouterr()
    assert "Índice no válido" in captured.out


def test_menu_tarea_crear_value_error(tmp_path, monkeypatch, capsys):
    archivo = tmp_path / "proyectos.json"
    monkeypatch.setattr(gps, "ARCHIVO_PROYECTOS", str(archivo))
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Beta",
        "tareas": []
    })
    
    # Selecciona opción 1, introduce "abc" (genera ValueError), y luego vuelve
    inputs = ["1", "abc", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuTarea()
    
    captured = capsys.readouterr()
    assert "Error: Ingrese solo números" in captured.out


def test_menu_tarea_sin_proyectos(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    
    # Limpiamos proyectos para que esté vacío
    gps.proyectos.clear()
    
    # Selecciona opción 1, y luego vuelve
    inputs = ["1", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuTarea()
    
    captured = capsys.readouterr()
    assert "No hay proyectos registrados" in captured.out


def test_menu_tarea_listar(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Gamma",
        "tareas": [
            {"nombre": "Tarea 1", "registros": []},
            {"nombre": "Tarea 2", "registros": []}
        ]
    })
    
    # Selecciona opción 2 (listar tareas) y luego vuelve
    inputs = ["2", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuTarea()
    
    captured = capsys.readouterr()
    assert "Proyecto: Proyecto Gamma" in captured.out
    assert "Tarea 1" in captured.out
    assert "Tarea 2" in captured.out


def test_menu_tarea_opcion_invalida(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    
    # Selecciona opción inválida y luego vuelve
    inputs = ["99", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuTarea()
    
    captured = capsys.readouterr()
    assert "Opción no válida" in captured.out
