import pytest
import GestorProyectosSimple as gps


# ---------------------------------------------------------
# PRUEBAS UNITARIAS DEL MÓDULO REPORTES
# ---------------------------------------------------------


def test_reporte_horas_por_tarea(monkeypatch, capsys):
    """Verifica que el reporte muestre el total de horas de cada tarea."""
    monkeypatch.setattr(gps, "main", lambda: None)

    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Alfa",
        "tareas": [
            {
                "nombre": "Diseño",
                "registros": [
                    {"empleado": "Carlos", "horas": 5.0},
                    {"empleado": "Ana", "horas": 3.0}
                ]
            }
        ]
    })

    # Opción 1 = Reporte de horas por tarea
    # Opción 3 = Volver
    entradas = ["1", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": entradas.pop(0))

    gps.menuReporte()

    salida = capsys.readouterr().out
    assert "===== HORAS POR TAREA =====" in salida
    assert "Proyecto: Proyecto Alfa" in salida
    assert "Tarea: Diseño" in salida
    assert "Total Horas: 8.0" in salida


def test_reporte_horas_por_proyecto(monkeypatch, capsys):
    """Verifica que el reporte sume las horas de todas las tareas de un proyecto."""
    monkeypatch.setattr(gps, "main", lambda: None)

    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Beta",
        "tareas": [
            {
                "nombre": "Frontend",
                "registros": [
                    {"empleado": "Luis", "horas": 4.0}
                ]
            },
            {
                "nombre": "Backend",
                "registros": [
                    {"empleado": "Marta", "horas": 6.5}
                ]
            }
        ]
    })

    # Opción 2 = Reporte de horas por proyecto
    # Opción 3 = Volver
    entradas = ["2", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": entradas.pop(0))

    gps.menuReporte()

    salida = capsys.readouterr().out
    assert "===== HORAS POR PROYECTO =====" in salida
    assert "Proyecto: Proyecto Beta" in salida
    assert "Total de horas trabajadas: 10.5" in salida


def test_reporte_sin_proyectos(monkeypatch, capsys):
    """Verifica el mensaje cuando no existen proyectos registrados."""
    monkeypatch.setattr(gps, "main", lambda: None)

    gps.proyectos.clear()

    entradas = ["1", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": entradas.pop(0))

    gps.menuReporte()

    salida = capsys.readouterr().out
    assert "No hay proyectos registrados" in salida


def test_reporte_proyecto_sin_tareas(monkeypatch, capsys):
    """Verifica que el reporte indique cuando un proyecto no tiene tareas."""
    monkeypatch.setattr(gps, "main", lambda: None)

    gps.proyectos.clear()
    gps.proyectos.append({
        "nombre": "Proyecto Vacío",
        "tareas": []
    })

    entradas = ["1", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": entradas.pop(0))

    gps.menuReporte()

    salida = capsys.readouterr().out
    assert "Proyecto: Proyecto Vacío" in salida
    assert "(Sin tareas)" in salida


def test_reporte_opcion_invalida(monkeypatch, capsys):
    """Verifica que el menú de reportes controle una opción incorrecta."""
    monkeypatch.setattr(gps, "main", lambda: None)

    entradas = ["99", "3"]
    monkeypatch.setattr("builtins.input", lambda prompt="": entradas.pop(0))

    gps.menuReporte()

    salida = capsys.readouterr().out
    assert "Opcion invalida" in salida
