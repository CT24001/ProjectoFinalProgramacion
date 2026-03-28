Algoritmo GestordeProyectosSimple
	//Variables Globales
	Definir numEmpleados Como Entero
    Dimensionar  empleados[20]
	
	Definir numProyectos Como Entero
    Dimensionar  proyectos[20] 
	
	Definir tareaProyecto Como Entero
	Dimensionar tareaProyecto[20]
	
	Definir numTareas Como Entero
	Dimensionar tareas[20]
	numTareas <- 0
	
	Definir asignacionEmpleadoTarea Como Entero
	Dimensionar asignacionEmpleadoTarea[20]
	
	Definir horasAcumuladas Como Real
	Dimensionar horasAcumuladas[20]
	
	Para i <- 1 Hasta 20 Con Paso 1 Hacer
		horasAcumuladas[i] <- 0
		tareaProyecto[i] <- 0
		asignacionEmpleadoTarea[i] <- 0
		
	Fin Para
Repetir
		
	Escribir "=========================================="
    Escribir "           GESTOR DE PROYECTOS SIMPLE "
    Escribir "=========================================="
    Escribir ""
	
	Escribir "Menu:    "
	Escribir "1. Gestion de Empleados "
	Escribir "2. Gestion de Proyectos"
	Escribir "3. Gestion de Tareas"
	Escribir "4. Registros Horas"
	Escribir "5. Reporte"
	Escribir "6. Salir"
	
	Leer opcion
	
	
	Segun opcion Hacer
		1:
			MenuEmpleado(empleados,numEmpleados)
		2:
			MenuProyecto(proyectos, numProyectos)
		3:   
			MenuTareas(tareas, numTareas, proyectos, numProyectos, empleados, numEmpleados,asignacionEmpleadoTarea, tareaProyecto)
		4:
			MenuRegistroHoras(tareas, numTareas, horasAcumuladas)
		5:
			
		6:	
			Escribir "Saliendo del sistema"
		De Otro Modo:
			Escribir "Opcion no valida"
	Fin Segun
Hasta Que opcion = 6 
FinAlgoritmo


// Gestion de Empleados
SubProceso MenuEmpleado(empleados Por Referencia, numEmpleados Por Referencia)
	// Variables para el Menu de empleados
	Definir  opcionEmpleado Como Entero
	Definir nombre Como Caracter
	Escribir ""
	Escribir "Menu - Empleados"
    Escribir "1. Crear nuevo empleado"
	Escribir "2. Mostrar Empleados"
    Escribir "3. Volver"
	Leer  opcionEmpleado
	
	Segun opcionEmpleado Hacer
		1:
			Si numEmpleados = 20 Entonces
				Escribir "No se puede agregar mas empleados"
			SiNo
				Escribir "Ingresa el Nombre del Nuevo empleado"
				Leer nombre
				numEmpleados <- numEmpleados + 1
				empleados[numEmpleados] <- nombre
				Escribir "Empleado Agregado"
			Fin Si
			MenuEmpleado(empleados, numEmpleados)
		2: 
			Si numEmpleados = 0 Entonces
				Escribir "No hay empleados registrados"
			SiNo
				Escribir "Empleados Registrados"
				Para i <- 1 Hasta numEmpleados Con Paso 1 Hacer
					Escribir i ". " empleados[i]
				Fin Para
			Fin Si
			MenuEmpleado(empleados,numEmpleados)
		3:
			
		De Otro Modo:
			Escribir "Opcion no valida"
			MenuEmpleado(empleados,numEmpleados)
	Fin Segun
FinSubProceso

SubProceso MenuProyecto (proyectos Por Referencia , numProyectos Por Referencia)
	Definir opcionProyecto, idProyecto Como Entero
	Definir nombreProyecto Como Caracter
	Definir nuevaTarea Como Caracter
	
	Escribir " "
	Escribir  "Menu - Proyecto"
	Escribir "1. Crear un nuevo Projecto"
	Escribir "2. Listar todos los Proyectos"
	Escribir "3. Asociar tareas a Proyectos"
	Escribir "4. Volver"
	Leer opcionProyecto
	
	Segun opcionProyecto Hacer
		1:
			Si numProyectos = 20 Entonces
				Escribir "No se pueden agregar mas Proyectos"
			SiNo
				Escribir "Ingresa el Proyecto"
				Leer nombreProyecto
				numProyectos <- numProyectos + 1
				proyectos[numProyectos] <- nombreProyecto
				Escribir "Proyecto Agregado"
				MenuProyecto(proyectos, numProyectos)
			Fin Si
		2:
			Si numProyectos = 0 Entonces
				Escribir "No hay proyectos registrados"
			SiNo
				Escribir "Proyectos Registrados"
				Para i <- 1 Hasta numProyectos Con Paso 1 Hacer
					Escribir i ". " proyectos[i]
				Fin Para
			Fin Si
			MenuProyecto(proyectos, numProyectos)
		3:
			Si numProyectos = 0
				Escribir "No hay Proyectos"
			FinSi
			Escribir "Proyectos Disponibles "
			Para i <- 1 Hasta numProyectos Con Paso 1 Hacer
				Escribir i ". " proyectos[i]
			Fin Para
			Escribir "Selecciona numero de proyecto"
			Leer idProyecto
			
			Si idProyecto < 1 O idProyecto > numProyectos
				Escribir "Proyecto Invalido"
				MenuProyecto(proyectos, numProyectos)
			FinSi
			
		4:
			
		De Otro Modo:
			Escribir "Opcion no valida" 
			MenuProyecto(proyectos, numProyectos)
	Fin Segun
	
FinSubProceso

// Gestion de Tareas
SubProceso MenuTareas(tareas Por Referencia, numTareas Por Referencia, proyectos, numProyectos, empleados, numEmpleados, asignacionEmpleadoTarea Por Referencia, tareaProyecto Por Referencia)
	Definir opcionTarea, idProyectoSeleccionado, idEmpSeleccionado Como Entero
	Definir nombreTarea, responsable Como Caracter
	
	Escribir ""
	Escribir "--- Menu - Tareas ---"
	Escribir "1. Crear nueva tarea"
	Escribir "2. Mostrar todas las tareas"
	Escribir "3. Volver"
	Leer opcionTarea
	
	Segun opcionTarea Hacer
		1:
			Si numProyectos = 0 Entonces
				Escribir "Error: No existen proyectos para asignar tareas."
			SiNo
				Si numTareas = 20 Entonces
					Escribir "No se pueden agregar mas tareas (Limite alcanzado)"
				SiNo
					// 1. Selección de Proyecto
					Escribir "Selecciona el numero de proyecto para esta tarea:"
					Para i <- 1 Hasta numProyectos Con Paso 1 Hacer
						Escribir i ". " proyectos[i]
					Fin Para
					Leer idProyectoSeleccionado
					
					Si idProyectoSeleccionado < 1 O idProyectoSeleccionado > numProyectos Entonces
						Escribir "Proyecto Invalido"
					SiNo
						// 2. Datos de la Tarea
						Escribir "Ingresa el nombre de la nueva tarea:"
						Leer nombreTarea
						numTareas <- numTareas + 1
						tareas[numTareas] <- nombreTarea
						tareaProyecto[numTareas] <- idProyectoSeleccionado // Vínculo al proyecto
						
						// 3. Asignación de Empleado Responsable
						Si numEmpleados = 0 Entonces
							Escribir "Aviso: No hay empleados registrados. Tarea creada sin responsable."
							asignacionEmpleadoTarea[numTareas] <- 0
						SiNo
							Escribir "Selecciona el numero de empleado responsable:"
							Para j <- 1 Hasta numEmpleados Con Paso 1 Hacer
								Escribir j ". " empleados[j]
							Fin Para
							Leer idEmpSeleccionado
							
							Si idEmpSeleccionado > 0 Y idEmpSeleccionado <= numEmpleados Entonces
								asignacionEmpleadoTarea[numTareas] <- idEmpSeleccionado
								Escribir "Responsable asignado: ", empleados[idEmpSeleccionado]
							SiNo
								Escribir "ID invalido. Tarea queda sin responsable."
								asignacionEmpleadoTarea[numTareas] <- 0
							Fin Si
						Fin Si
						
						Escribir "Tarea Agregada Exitosamente"
					Fin Si
				Fin Si
			Fin Si
			MenuTareas(tareas, numTareas, proyectos, numProyectos, empleados, numEmpleados, asignacionEmpleadoTarea, tareaProyecto)
			
		2:
			Si numTareas = 0 Entonces
				Escribir "No hay tareas registradas"
			SiNo
				Escribir "--- Tareas Registradas ---"
				Para i <- 1 Hasta numTareas Con Paso 1 Hacer
					// Lógica para determinar el nombre del responsable
					Si asignacionEmpleadoTarea[i] = 0 Entonces
						responsable <- "Sin responsable"
					SiNo
						responsable <- empleados[asignacionEmpleadoTarea[i]]
					Fin Si
					
					// Mostramos Tarea + Proyecto asociado + Responsable
					Escribir i ". " tareas[i], " [Proyecto: ", proyectos[tareaProyecto[i]], "] - Responsable: ", responsable
				Fin Para
			Fin Si
			MenuTareas(tareas, numTareas, proyectos, numProyectos, empleados, numEmpleados, asignacionEmpleadoTarea, tareaProyecto)
			
		3:
			// No se llama a nada para que el SubProceso termine y regrese al Repetir del Algoritmo
		
			
		De Otro Modo:
			Escribir "Opcion no valida"
			MenuTareas(tareas, numTareas, proyectos, numProyectos, empleados, numEmpleados, asignacionEmpleadoTarea, tareaProyecto)
	Fin Segun
FinSubProceso


// Registro de Horas
SubProceso MenuRegistroHoras(tareas, numTareas, horasAcumuladas Por Referencia)
	Definir opcionRegistro, idTareaSeleccionada Como Entero
	Definir horasIngresadas Como Real
	
	Escribir ""
	Escribir "--- Menu - Registro de Horas ---"
	Escribir "1. Registrar horas en una tarea"
	Escribir "2. Volver"
	Leer opcionRegistro
	
	Segun opcionRegistro Hacer
		1:
			Si numTareas = 0 Entonces
				Escribir "Error: Debe crear tareas antes de registrar horas."
			SiNo
				Escribir "Selecciona el numero de la tarea:"
				Para i <- 1 Hasta numTareas Con Paso 1 Hacer
					Escribir i ". " tareas[i]
				Fin Para
				Leer idTareaSeleccionada
				
				Si idTareaSeleccionada < 1 O idTareaSeleccionada > numTareas Entonces
					Escribir "Tarea Invalida"
				SiNo
					Escribir "Ingresa las horas trabajadas hoy en esta tarea:"
					Leer horasIngresadas
					
					// VAlidación para evitar jornadas irreales (>24h)
					Si horasIngresadas > 0 Y horasIngresadas <= 24 Entonces
						horasAcumuladas[idTareaSeleccionada] <- horasAcumuladas[idTareaSeleccionada] + horasIngresadas
						Escribir "Horas registradas con exito. Total en esta tarea: ", horasAcumuladas[idTareaSeleccionada]
					SiNo
						Escribir "Error: La jornada diaria no puede ser negativa ni mayor a 24 horas."
					Fin Si
				Fin Si
			Fin Si
			MenuRegistroHoras(tareas, numTareas, horasAcumuladas)
		2:
		De Otro Modo:
			Escribir "Opcion no valida"
			MenuRegistroHoras(tareas, numTareas, horasAcumuladas)
	Fin Segun
FinSubProceso



