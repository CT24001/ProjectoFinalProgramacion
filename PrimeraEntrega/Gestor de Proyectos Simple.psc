Algoritmo GestordeProyectosSimple
	
	Definir numEmpleados, numProyectos, numTareas, opcion, i Como Entero
	Definir empleados, proyectos, tareas Como Cadena
	Definir tareaProyecto, asignacionEmpleadoTarea Como Entero
	Definir horasAcumuladas Como Real
	
	Dimension empleados[20]
	Dimension proyectos[20]
	Dimension tareas[20]
	Dimension tareaProyecto[20]
	Dimension asignacionEmpleadoTarea[20]
	Dimension horasAcumuladas[20]
	
	numEmpleados <- 0
	numProyectos <- 0
	numTareas <- 0
	
	Para i <- 1 Hasta 20 Hacer
		horasAcumuladas[i] <- 0
		tareaProyecto[i] <- 0
		asignacionEmpleadoTarea[i] <- 0
	FinPara
	
	Repetir
		Escribir "=========================================="
		Escribir "        GESTOR DE PROYECTOS SIMPLE"
		Escribir "=========================================="
		Escribir ""
		Escribir "1. Gestion de Empleados"
		Escribir "2. Gestion de Proyectos"
		Escribir "3. Gestion de Tareas"
		Escribir "4. Registro de Horas"
		Escribir "5. Reporte"
		Escribir "6. Salir"
		Leer opcion
		
		Segun opcion Hacer
			1:
				MenuEmpleado(empleados, numEmpleados)
			2:
				MenuProyecto(proyectos, numProyectos)
			3:
				MenuTareas(tareas, numTareas, proyectos, numProyectos, empleados, numEmpleados, asignacionEmpleadoTarea, tareaProyecto)
			4:
				MenuRegistroHoras(tareas, numTareas, horasAcumuladas)
			5:
				Reporte(tareas, numTareas, proyectos, numProyectos, tareaProyecto, horasAcumuladas)
			6:
				Escribir "Saliendo del sistema..."
			De Otro Modo:
				Escribir "Opcion no valida"
		FinSegun
	Hasta Que opcion = 6
	
FinAlgoritmo



SubProceso MenuEmpleado(empleados Por Referencia, numEmpleados Por Referencia)
	
	Definir opcionEmpleado, i Como Entero
	Definir nombre Como Cadena
	
	Escribir ""
	Escribir "------ MENU DE EMPLEADOS ------"
	Escribir "1. Crear nuevo empleado"
	Escribir "2. Mostrar empleados"
	Escribir "3. Volver"
	Leer opcionEmpleado
	
	Segun opcionEmpleado Hacer
		1:
			Si numEmpleados = 20 Entonces
				Escribir "No se puede agregar mas empleados"
			SiNo
				Escribir "Ingresa el nombre del nuevo empleado:"
				Leer nombre
				numEmpleados <- numEmpleados + 1
				empleados[numEmpleados] <- nombre
				Escribir "Empleado agregado exitosamente"
			FinSi
			MenuEmpleado(empleados, numEmpleados)
			
		2:
			Si numEmpleados = 0 Entonces
				Escribir "No hay empleados registrados"
			SiNo
				Escribir "----- EMPLEADOS REGISTRADOS -----"
				Para i <- 1 Hasta numEmpleados Hacer
					Escribir i, ". ", empleados[i]
				FinPara
			FinSi
			MenuEmpleado(empleados, numEmpleados)
			
		3:
			
		De Otro Modo:
			Escribir "Opcion no valida"
			MenuEmpleado(empleados, numEmpleados)
	FinSegun
	
FinSubProceso



SubProceso MenuProyecto(proyectos Por Referencia, numProyectos Por Referencia)
	
	Definir opcionProyecto, i Como Entero
	Definir nombreProyecto Como Cadena
	
	Escribir ""
	Escribir "------ MENU DE PROYECTOS ------"
	Escribir "1. Crear nuevo proyecto"
	Escribir "2. Listar todos los proyectos"
	Escribir "3. Volver"
	Leer opcionProyecto
	
	Segun opcionProyecto Hacer
		1:
			Si numProyectos = 20 Entonces
				Escribir "No se pueden agregar mas proyectos"
			SiNo
				Escribir "Ingresa el nombre del proyecto:"
				Leer nombreProyecto
				numProyectos <- numProyectos + 1
				proyectos[numProyectos] <- nombreProyecto
				Escribir "Proyecto agregado exitosamente"
			FinSi
			MenuProyecto(proyectos, numProyectos)
			
		2:
			Si numProyectos = 0 Entonces
				Escribir "No hay proyectos registrados"
			SiNo
				Escribir "----- PROYECTOS REGISTRADOS -----"
				Para i <- 1 Hasta numProyectos Hacer
					Escribir i, ". ", proyectos[i]
				FinPara
			FinSi
			MenuProyecto(proyectos, numProyectos)
			
		3:
			
		De Otro Modo:
			Escribir "Opcion no valida"
			MenuProyecto(proyectos, numProyectos)
	FinSegun
	
FinSubProceso



SubProceso MenuTareas(tareas Por Referencia, numTareas Por Referencia, proyectos, numProyectos, empleados, numEmpleados, asignacionEmpleadoTarea Por Referencia, tareaProyecto Por Referencia)
	
	Definir opcionTarea, idProyectoSeleccionado, idEmpSeleccionado, i, j Como Entero
	Definir nombreTarea, responsable Como Cadena
	
	Escribir ""
	Escribir "------ MENU DE TAREAS ------"
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
					Escribir "No se pueden agregar mas tareas"
				SiNo
					Escribir "Selecciona el numero de proyecto para esta tarea:"
					Para i <- 1 Hasta numProyectos Hacer
						Escribir i, ". ", proyectos[i]
					FinPara
					Leer idProyectoSeleccionado
					
					Si idProyectoSeleccionado < 1 O idProyectoSeleccionado > numProyectos Entonces
						Escribir "Proyecto invalido"
					SiNo
						Escribir "Ingresa el nombre de la nueva tarea:"
						Leer nombreTarea
						
						numTareas <- numTareas + 1
						tareas[numTareas] <- nombreTarea
						tareaProyecto[numTareas] <- idProyectoSeleccionado
						
						Si numEmpleados = 0 Entonces
							Escribir "No hay empleados registrados. La tarea quedara sin responsable."
							asignacionEmpleadoTarea[numTareas] <- 0
						SiNo
							Escribir "Selecciona el numero del empleado responsable:"
							Para j <- 1 Hasta numEmpleados Hacer
								Escribir j, ". ", empleados[j]
							FinPara
							Leer idEmpSeleccionado
							
							Si idEmpSeleccionado >= 1 Y idEmpSeleccionado <= numEmpleados Entonces
								asignacionEmpleadoTarea[numTareas] <- idEmpSeleccionado
								Escribir "Responsable asignado: ", empleados[idEmpSeleccionado]
							SiNo
								asignacionEmpleadoTarea[numTareas] <- 0
								Escribir "ID invalido. La tarea queda sin responsable."
							FinSi
						FinSi
						
						Escribir "Tarea agregada exitosamente"
					FinSi
				FinSi
			FinSi
			MenuTareas(tareas, numTareas, proyectos, numProyectos, empleados, numEmpleados, asignacionEmpleadoTarea, tareaProyecto)
			
		2:
			Si numTareas = 0 Entonces
				Escribir "No hay tareas registradas"
			SiNo
				Escribir "----- TAREAS REGISTRADAS -----"
				Para i <- 1 Hasta numTareas Hacer
					Si asignacionEmpleadoTarea[i] = 0 Entonces
						responsable <- "Sin responsable"
					SiNo
						responsable <- empleados[asignacionEmpleadoTarea[i]]
					FinSi
					
					Escribir i, ". ", tareas[i], " [Proyecto: ", proyectos[tareaProyecto[i]], "] - Responsable: ", responsable
				FinPara
			FinSi
			MenuTareas(tareas, numTareas, proyectos, numProyectos, empleados, numEmpleados, asignacionEmpleadoTarea, tareaProyecto)
			
		3:
			
		De Otro Modo:
			Escribir "Opcion no valida"
			MenuTareas(tareas, numTareas, proyectos, numProyectos, empleados, numEmpleados, asignacionEmpleadoTarea, tareaProyecto)
	FinSegun
	
FinSubProceso



SubProceso MenuRegistroHoras(tareas, numTareas, horasAcumuladas Por Referencia)
	
	Definir opcionRegistro, idTareaSeleccionada, i Como Entero
	Definir horasIngresadas Como Real
	
	Escribir ""
	Escribir "------ MENU DE REGISTRO DE HORAS ------"
	Escribir "1. Registrar horas en una tarea"
	Escribir "2. Volver"
	Leer opcionRegistro
	
	Segun opcionRegistro Hacer
		1:
			Si numTareas = 0 Entonces
				Escribir "Error: Debe crear tareas antes de registrar horas."
			SiNo
				Escribir "Selecciona el numero de la tarea:"
				Para i <- 1 Hasta numTareas Hacer
					Escribir i, ". ", tareas[i]
				FinPara
				Leer idTareaSeleccionada
				
				Si idTareaSeleccionada < 1 O idTareaSeleccionada > numTareas Entonces
					Escribir "Tarea invalida"
				SiNo
					Escribir "Ingresa las horas trabajadas:"
					Leer horasIngresadas
					
					Si horasIngresadas > 0 Y horasIngresadas <= 24 Entonces
						horasAcumuladas[idTareaSeleccionada] <- horasAcumuladas[idTareaSeleccionada] + horasIngresadas
						Escribir "Horas registradas con exito. Total en esta tarea: ", horasAcumuladas[idTareaSeleccionada]
					SiNo
						Escribir "Error: La cantidad de horas debe estar entre 1 y 24."
					FinSi
				FinSi
			FinSi
			MenuRegistroHoras(tareas, numTareas, horasAcumuladas)
			
		2:
			
		De Otro Modo:
			Escribir "Opcion no valida"
			MenuRegistroHoras(tareas, numTareas, horasAcumuladas)
	FinSegun
	
FinSubProceso



SubProceso Reporte(tareas, numTareas, proyectos, numProyectos, tareaProyecto, horasAcumuladas)
	
	Definir opcionReporte, i, j Como Entero
	Definir totalProyecto Como Real
	
	Escribir ""
	Escribir "------ MENU DE REPORTES ------"
	Escribir "1. Total de horas trabajadas por tarea"
	Escribir "2. Total de horas trabajadas por proyecto"
	Escribir "3. Volver"
	Leer opcionReporte
	
	Segun opcionReporte Hacer
		1:
			Si numTareas = 0 Entonces
				Escribir "No hay tareas registradas."
			SiNo
				Escribir ""
				Escribir "===== REPORTE DE HORAS POR TAREA ====="
				Para i <- 1 Hasta numTareas Hacer
					Escribir "Tarea ", i, ": ", tareas[i], " -> Total horas: ", horasAcumuladas[i]
				FinPara
			FinSi
			Reporte(tareas, numTareas, proyectos, numProyectos, tareaProyecto, horasAcumuladas)
			
		2:
			Si numProyectos = 0 Entonces
				Escribir "No hay proyectos registrados."
			SiNo
				Escribir ""
				Escribir "===== REPORTE DE HORAS POR PROYECTO ====="
				
				Para i <- 1 Hasta numProyectos Hacer
					totalProyecto <- 0
					Escribir "Proyecto ", i, ": ", proyectos[i]
					
					Para j <- 1 Hasta numTareas Hacer
						Si tareaProyecto[j] = i Entonces
							Escribir "   Tarea: ", tareas[j], " -> Horas: ", horasAcumuladas[j]
							totalProyecto <- totalProyecto + horasAcumuladas[j]
						FinSi
					FinPara
					
					Escribir "   Total horas del proyecto: ", totalProyecto
					Escribir "--------------------------------------"
				FinPara
			FinSi
			Reporte(tareas, numTareas, proyectos, numProyectos, tareaProyecto, horasAcumuladas)
			
		3:
			
		De Otro Modo:
			Escribir "Opcion no valida"
			Reporte(tareas, numTareas, proyectos, numProyectos, tareaProyecto, horasAcumuladas)
	FinSegun
	
FinSubProceso