#  Gestor de Proyectos Simple

##  Descripción

El **Gestor de Proyectos Simple** es una aplicación desarrollada en pseudocódigo (compatible con PSeInt) que permite administrar:

- Empleados  
- Proyectos  
- Tareas  
- Registro de horas trabajadas  
- Generación de reportes  

Este sistema simula un entorno básico de gestión de proyectos donde se pueden asignar tareas a empleados y registrar el tiempo trabajado.

---

##  Objetivo

El objetivo del sistema es:

- Organizar tareas dentro de proyectos  
- Asignar responsables a cada tarea  
- Registrar horas trabajadas  
- Generar reportes de productividad  

---

##  Funcionalidades

###  Gestión de Empleados
- Crear nuevos empleados  
- Listar empleados registrados  

###  Gestión de Proyectos
- Crear nuevos proyectos  
- Listar proyectos existentes  

###  Gestión de Tareas
- Crear tareas asociadas a un proyecto  
- Asignar un empleado responsable  
- Visualizar todas las tareas con:
  - Proyecto asociado  
  - Responsable  

###  Registro de Horas
- Registrar horas trabajadas por tarea  
- Validación de horas (máximo 24 por día)  

###  Reportes

####  Reporte por tarea
- Muestra el total de horas trabajadas en cada tarea  

####  Reporte por proyecto
- Muestra:
  - Tareas pertenecientes a cada proyecto  
  - Horas trabajadas por tarea  
  - Total de horas por proyecto  

---

##  Estructura del Sistema

El sistema utiliza arreglos para almacenar la información:

- empleados[20]
- proyectos[20]
- tareas[20]
- tareaProyecto[20]
- asignacionEmpleadoTarea[20]
- horasAcumuladas[20]

Cada índice representa una relación entre entidades.

---

##  Flujo del Programa

1. Menú principal  
2. Selección de módulo  
3. Ejecución de operaciones  
4. Retorno al menú principal  
5. Salida del sistema  

---

##  Menú Principal

1. Gestion de Empleados
2. Gestion de Proyectos
3. Gestion de Tareas
4. Registro de Horas
5. Reporte
6. Salir

---

##  Consideraciones

- Límite máximo de registros: 20  
- No utiliza base de datos (todo es en memoria)  
- Validación básica de entradas  

---

##  Autor

 - Jehosua Abdiel Cañas Tijerino
 - Néstor Armando Chinchilla Fuentes 
 - Ronnie Odir Portillo Consuegra

Ingeniería en Desarrollo de Software  
Universidad de El Salvador  

---

##  Año

2026
