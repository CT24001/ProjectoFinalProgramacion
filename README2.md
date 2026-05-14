# Gestor de Proyectos Simple

## Descripción
Gestor de Proyectos Simple es una aplicación desarrollada en Python que permite administrar empleados, proyectos, tareas y el registro de horas trabajadas dentro de una empresa.

El sistema utiliza archivos JSON para almacenar la información, permitiendo mantener los datos guardados incluso después de cerrar el programa.

---

# Funcionalidades

## 1. Gestión de Empleados
- Crear empleados
- Mostrar empleados registrados
- Validación de IDs duplicados

## 2. Gestión de Proyectos
- Crear proyectos
- Mostrar proyectos registrados
- Validación de proyectos repetidos

## 3. Gestión de Tareas
- Crear tareas asociadas a proyectos
- Mostrar tareas por proyecto

## 4. Registro de Horas
- Registrar horas trabajadas por empleados
- Asociar horas a tareas específicas

## 5. Reportes
- Reporte de horas por tarea
- Reporte de horas por proyecto

---

# Tecnologías Utilizadas

- Python
- JSON
- Visual Studio Code

---

# Estructura del Proyecto

```text
GestorProyectos/
│
├── main.py
├── empleados.json
├── proyectos.json
└── README.md
```

---

# Archivos JSON

## empleados.json
Almacena la información de los empleados.

Ejemplo:

```json
[
    {
        "id": "12345",
        "nombre": "Juan Perez"
    }
]
```

---

## proyectos.json
Almacena proyectos, tareas y registros de horas.

Ejemplo:

```json
[
    {
        "nombre": "Sistema Web",
        "tareas": [
            {
                "nombre": "Login",
                "registros": [
                    {
                        "empleado": "Juan Perez",
                        "horas": 5
                    }
                ]
            }
        ]
    }
]
```

---

# Cómo Ejecutar el Proyecto

## 1. Instalar Python

Verificar instalación:

```bash
python --version
```

---

## 2. Ejecutar el programa

Desde la terminal:

```bash
python main.py
```

---

# Menú Principal

```text
1. Gestión de Empleados
2. Gestión de Proyectos
3. Gestión de Tareas
4. Registro de Horas
5. Reporte
6. Salir
```

---

# Objetivo del Proyecto

El objetivo principal del proyecto es aplicar conceptos básicos de programación en Python como:

- Funciones
- Listas y diccionarios
- Archivos JSON
- Validaciones
- Modularización
- Menús interactivos

---

# Integrantes

 - Jehosua Abdiel Cañas Tijerino
 - Néstor Armando Chinchilla Fuentes 
 - Ronnie Odir Portillo Consuegra

---

# Estado del Proyecto

Proyecto académico en desarrollo.