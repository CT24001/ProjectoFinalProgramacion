import json
import pytest
import GestorProyectosSimple as gps


# ---------- PRUEBAS DE LÓGICA DE NEGOCIO ----------

def test_agregar_horas_estructura():
    gps.empleados.clear()
    gps.proyectos.clear()
    
    gps.empleados.append({"id": "001", "nombre": "Carlos"})
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [
            {
                "nombre": "Desarrollo",
                "registros": []
            }
        ]
    })
    
    # Agregar un registro
    registro = {"empleado": "Carlos", "horas": 8.0}
    gps.proyectos[0]["tareas"][0]["registros"].append(registro)
    
    assert len(gps.proyectos[0]["tareas"][0]["registros"]) == 1
    assert gps.proyectos[0]["tareas"][0]["registros"][0]["empleado"] == "Carlos"
    assert gps.proyectos[0]["tareas"][0]["registros"][0]["horas"] == 8.0


def test_limite_24_horas_por_tarea():
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [
            {
                "nombre": "Desarrollo",
                "registros": [
                    {"empleado": "Carlos", "horas": 20.0}
                ]
            }
        ]
    })
    
    # Intentar agregar 5 horas adicionales a la misma tarea (20 + 5 = 25 > 24)
    horas_actuales = sum(r["horas"] for r in gps.proyectos[0]["tareas"][0]["registros"])
    intentando = 5.0
    
    # Validación de la regla de negocio
    assert horas_actuales + intentando > 24


def test_calculo_reporte_horas():
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Beta",
        "tareas": [
            {
                "nombre": "Frontend",
                "registros": [
                    {"empleado": "Ana", "horas": 5.0},
                    {"empleado": "Carlos", "horas": 7.5}
                ]
            },
            {
                "nombre": "Backend",
                "registros": [
                    {"empleado": "Ana", "horas": 8.0}
                ]
            }
        ]
    })
    
    # Calcular total de horas por tarea
    total_frontend = sum(r["horas"] for r in gps.proyectos[0]["tareas"][0]["registros"])
    total_backend = sum(r["horas"] for r in gps.proyectos[0]["tareas"][1]["registros"])
    
    assert total_frontend == 12.5
    assert total_backend == 8.0
    
    # Calcular total del proyecto
    total_proyecto = sum(
        sum(r["horas"] for r in t["registros"])
        for t in gps.proyectos[0]["tareas"]
    )
    assert total_proyecto == 20.5


# ---------- PRUEBAS DEL MENÚ REGISTRO DE HORAS ----------

def test_menu_registro_horas_faltan_datos(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.empleados.clear()
    gps.proyectos.clear()
    
    # Opción 1 (Cargar horas) y luego Opción 2 (Volver)
    inputs = ["1", "2"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuRegistroHoras()
    
    captured = capsys.readouterr()
    assert "Se requieren empleados y proyectos con tareas" in captured.out


def test_menu_registro_horas_exitoso(tmp_path, monkeypatch, capsys):
    archivo = tmp_path / "proyectos.json"
    monkeypatch.setattr(gps, "ARCHIVO_PROYECTOS", str(archivo))
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.empleados.clear()
    gps.empleados.append({"id": "1", "nombre": "Carlos"})
    
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [
            {
                "nombre": "Tarea 1",
                "registros": []
            }
        ]
    })
    
    # Inputs:
    # 1. Opción "1" (Cargar horas)
    # 2. Proyecto "1" (Proyecto Alfa)
    # 3. Tarea "1" (Tarea 1)
    # 4. Empleado "1" (Carlos)
    # 5. Horas "8"
    # 6. Opción "2" (Volver)
    inputs = ["1", "1", "1", "1", "8", "2"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuRegistroHoras()
    
    captured = capsys.readouterr()
    assert "Horas guardadas correctamente" in captured.out
    
    # Verificar almacenamiento
    assert len(gps.proyectos[0]["tareas"][0]["registros"]) == 1
    assert gps.proyectos[0]["tareas"][0]["registros"][0]["empleado"] == "Carlos"
    assert gps.proyectos[0]["tareas"][0]["registros"][0]["horas"] == 8.0


def test_menu_registro_horas_excede_limite(tmp_path, monkeypatch, capsys):
    archivo = tmp_path / "proyectos.json"
    monkeypatch.setattr(gps, "ARCHIVO_PROYECTOS", str(archivo))
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.empleados.clear()
    gps.empleados.append({"id": "1", "nombre": "Carlos"})
    
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [
            {
                "nombre": "Tarea 1",
                "registros": [
                    {"empleado": "Carlos", "horas": 20.0}
                ]
            }
        ]
    })
    
    # Intentar agregar 6 horas (20 + 6 = 26 > 24)
    inputs = ["1", "1", "1", "1", "6", "2"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuRegistroHoras()
    
    captured = capsys.readouterr()
    assert "Error: No se pueden asignar más de 24 horas a una tarea" in captured.out
    # Asegurar que no se guardó el registro excedente
    assert len(gps.proyectos[0]["tareas"][0]["registros"]) == 1


def test_menu_registro_horas_sin_tareas(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.empleados.clear()
    gps.empleados.append({"id": "1", "nombre": "Carlos"})
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [] # Sin tareas
    })
    
    inputs = ["1", "1", "2"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuRegistroHoras()
    
    captured = capsys.readouterr()
    assert "Este proyecto no tiene tareas" in captured.out


def test_menu_registro_horas_proyecto_invalido(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.empleados.clear()
    gps.empleados.append({"id": "1", "nombre": "Carlos"})
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [{"nombre": "Tarea 1", "registros": []}]
    })
    
    # Índice del proyecto "5" (fuera de rango)
    inputs = ["1", "5", "2"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuRegistroHoras()
    
    captured = capsys.readouterr()
    assert "Proyecto no válido" in captured.out


def test_menu_registro_horas_tarea_invalida(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.empleados.clear()
    gps.empleados.append({"id": "1", "nombre": "Carlos"})
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [{"nombre": "Tarea 1", "registros": []}]
    })
    
    # Tarea "5" (fuera de rango)
    inputs = ["1", "1", "5", "2"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuRegistroHoras()
    
    captured = capsys.readouterr()
    assert "Tarea no válida" in captured.out


def test_menu_registro_horas_empleado_invalido(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.empleados.clear()
    gps.empleados.append({"id": "1", "nombre": "Carlos"})
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [{"nombre": "Tarea 1", "registros": []}]
    })
    
    # Empleado "5" (fuera de rango)
    inputs = ["1", "1", "1", "5", "2"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuRegistroHoras()
    
    captured = capsys.readouterr()
    assert "Empleado no válido" in captured.out


# ---------- PRUEBAS DEL MENÚ REPORTES ----------

def test_menu_reporte_horas_por_tarea(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [
            {
                "nombre": "Tarea 1",
                "registros": [
                    {"empleado": "Carlos", "horas": 10.0}
                ]
            }
        ]
    })
    
    inputs = ["1", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuReporte()
    
    captured = capsys.readouterr()
    assert "===== HORAS POR TAREA =====" in captured.out
    assert "Proyecto: Proyecto Alfa" in captured.out
    assert "Tarea: Tarea 1" in captured.out
    assert "Total Horas: 10.0" in captured.out


def test_menu_reporte_horas_por_proyecto(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    
    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [
            {
                "nombre": "Tarea 1",
                "registros": [
                    {"empleado": "Carlos", "horas": 10.0}
                ]
            }
        ]
    })
    
    inputs = ["2", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuReporte()
    
    captured = capsys.readouterr()
    assert "===== HORAS POR PROYECTO =====" in captured.out
    assert "Proyecto: Proyecto Alfa" in captured.out
    assert "Total de horas trabajadas: 10.0" in captured.out


def test_menu_reporte_sin_proyectos(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    gps.proyectos.clear()
    
    inputs = ["1", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuReporte()
    
    captured = capsys.readouterr()
    assert "No hay proyectos registrados" in captured.out


def test_menu_reporte_opcion_invalida(monkeypatch, capsys):
    monkeypatch.setattr(gps, "main", lambda: None)
    
    inputs = ["99", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": inputs.pop(0))
    
    gps.menuReporte()
    
    captured = capsys.readouterr()
    assert "Opcion invalida" in captured.out
