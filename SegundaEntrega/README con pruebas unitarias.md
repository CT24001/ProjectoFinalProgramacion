# Gestor de Proyectos Simple

## Descripción

Gestor de Proyectos Simple es una aplicación desarrollada en Python que permite administrar empleados, proyectos, tareas y el registro de horas trabajadas dentro de una organización.

El sistema utiliza archivos JSON para almacenar la información, permitiendo mantener los datos guardados incluso después de cerrar la aplicación.

---

## Objetivo del Proyecto

Desarrollar una aplicación de consola que permita gestionar empleados, proyectos y tareas, registrando las horas trabajadas y generando reportes que faciliten el control y seguimiento de las actividades realizadas.

---

## Funcionalidades

### Gestión de Empleados
- Crear empleados.
- Mostrar empleados registrados.
- Eliminar empleados.
- Validación de IDs duplicados.

### Gestión de Proyectos
- Crear proyectos.
- Mostrar proyectos registrados.
- Eliminar proyectos.
- Validación de proyectos repetidos.

### Gestión de Tareas
- Crear tareas asociadas a proyectos.
- Mostrar tareas por proyecto.

### Registro de Horas
- Registrar horas trabajadas por empleados.
- Asociar horas a tareas específicas.
- Validación para evitar registrar más de 24 horas en una tarea.

### Reportes
- Reporte de horas por tarea.
- Reporte de horas por proyecto.
- Cálculo automático de horas acumuladas.

---

## Tecnologías Utilizadas

- Python 3
- JSON
- Pytest
- Visual Studio Code
- Git
- GitHub

---

## Pruebas Unitarias

### Instalación de Pytest

```bash
python -m pip install pytest
```

### Ejecutar Todas las Pruebas

```bash
python -m pytest -v
```

### Ejecutar Únicamente las Pruebas del Módulo de Reportes

```bash
python -m pytest test_reportes.py -v
```

### Casos de Prueba Implementados

- Generación correcta del reporte de horas por tarea.
- Generación correcta del reporte de horas por proyecto.
- Comportamiento cuando no existen proyectos registrados.
- Validación de opciones inválidas del menú.
- Cálculo correcto del total de horas por proyecto.

---

## Integrantes

- Jehosua Abdiel Cañas Tijerino
- Néstor Armando Chinchilla Fuentes
- Ronnie Odir Portillo Consuegra
