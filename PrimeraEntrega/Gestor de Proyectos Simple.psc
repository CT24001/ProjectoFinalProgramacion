Algoritmo GestordeProyectosSimple
	
	// Variables Globales 
	Definir numEmpleados, numProyectos, numTareas, opcion, i, numeroElmentos Como Entero
	Definir empleados, proyectos, tareas Como Cadena
	Definir tareaProyecto, asignacionEmpleadoTarea Como Entero
	Definir horasAcumuladas Como Real
	
	// Areglos Globales para el gestor como maximo 20 elementos cada uno
	Dimension empleados[20]
	Dimension proyectos[20]
	Dimension tareas[20]
	Dimension tareaProyecto[20]
	Dimension asignacionEmpleadoTarea[20]
	Dimension horasAcumuladas[20]
	
	// Inicializando las variables 
	numEmpleados <- 0
	numProyectos <- 0
	numTareas <- 0
	numeroElmentos <- 20
	
	// Se inicializa los arreglos con valor de 0
	Para i <- 1 Hasta 20 Hacer
		horasAcumuladas[i] <- 0
		tareaProyecto[i] <- 0
		asignacionEmpleadoTarea[i] <- 0
	FinPara
	
	// Menu principal el corazon del programa
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
				MenuRegistroHoras(tareas, numTareas, horasAcumuladas, tareaProyecto, numProyectos, proyectos)
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
	// Variables locales para el menu Empleado 
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
			// Se compureba de que no haya mas de 20 empleados guardado
			Si numEmpleados = 20 Entonces
				Escribir "No se puede agregar mas empleados"
			SiNo
				Escribir "Ingresa el nombre del nuevo empleado:"
				Leer nombre
				numEmpleados <- numEmpleados + 1
				// Se guarda el nombre de empleado en el arreglo correpodiente 
				empleados[numEmpleados] <- nombre
				Escribir "Empleado agregado exitosamente"
			FinSi
			// Se muestra de nuevo el menu empleado
			MenuEmpleado(empleados, numEmpleados)
			
		2:
			// Se compureba de que haya empleados registrados
			Si numEmpleados = 0 Entonces
				Escribir "No hay empleados registrados"
			SiNo
				// Se recorre todo el arreglo para mostrar a todos los empleados 
				Escribir "----- EMPLEADOS REGISTRADOS -----"
				Para i <- 1 Hasta numEmpleados Hacer
					Escribir i, ". ", empleados[i]
				FinPara
			FinSi
			// Se muestra de nuevo el menu empleado
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
				// Agregar un nuevo proyecto al arreglo proyecto
				numProyectos <- numProyectos + 1
				proyectos[numProyectos] <- nombreProyecto
				Escribir "Proyecto agregado exitosamente"
			FinSi
			MenuProyecto(proyectos, numProyectos)
			
		2:
			Si numProyectos = 0 Entonces
				Escribir "No hay proyectos registrados"
			SiNo
				//mostrar el arreglo de proyectos 
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
					// Primero se selecciona el numero de proyecto al que se le quiere agregar la tarea
					Escribir "Selecciona el numero de proyecto para esta tarea:"
					Para i <- 1 Hasta numProyectos Hacer
						Escribir i, ". ", proyectos[i]
					FinPara
					Leer idProyectoSeleccionado
					
					// Verificando que el # proyecto selecciona exista 
					Si idProyectoSeleccionado < 1 O idProyectoSeleccionado > numProyectos Entonces
						Escribir "Proyecto invalido"
					SiNo
						
						Escribir "Ingresa el nombre de la nueva tarea:"
						Leer nombreTarea
						
						numTareas <- numTareas + 1
						// Se guarda el nombre de la tarea
						tareas[numTareas] <- nombreTarea
						// Se guarda a que proyecto pertene la tarea 
						tareaProyecto[numTareas] <- idProyectoSeleccionado
						
						// Se asigna responsable de la tarea, primero se verifica que haya empleados registrados 
						Si numEmpleados = 0 Entonces
							Escribir "No hay empleados registrados. La tarea quedara sin responsable."
							asignacionEmpleadoTarea[numTareas] <- 0
						SiNo
							// Se muestra la lista de empleados 
							Escribir "Selecciona el numero del empleado responsable:"
							Para j <- 1 Hasta numEmpleados Hacer
								Escribir j, ". ", empleados[j]
							FinPara
							Leer idEmpSeleccionado
							
							// Verificando que el empleados selecciona exista 
							Si idEmpSeleccionado >= 1 Y idEmpSeleccionado <= numEmpleados Entonces
								// Se guarda el id de empleado que va a hacer responsable de la tarea
								asignacionEmpleadoTarea[numTareas] <- idEmpSeleccionado
								// Se muestra el nombre del empleado responsable
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
			// Verificando que haya tareas registradas 
			Si numTareas = 0 Entonces
				Escribir "No hay tareas registradas"
			SiNo
				// Mostrando las tareas registradas 
				Escribir "----- TAREAS REGISTRADAS -----"
				Para i <- 1 Hasta numTareas Hacer
					
					Si asignacionEmpleadoTarea[i] = 0 Entonces
						responsable <- "Sin responsable"
					SiNo
						responsable <- empleados[asignacionEmpleadoTarea[i]]
					FinSi
					// Aqui se muestra la tareas y al projecto que le pertenece y quien es responsable de dicha tarea
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



SubProceso MenuRegistroHoras(tareas, numTareas, horasAcumuladas Por Referencia, tareaProyecto, numProyectos, proyectos)
	
	Definir opcionRegistro, idTareaSeleccionada, i, idProyectoActual Como Entero
	Definir horasIngresadas, totalProyecto Como Real
	
	Escribir ""
	Escribir "------ MENU DE REGISTRO DE HORAS ------"
	Escribir "1. Registrar horas en una tarea"
	Escribir "2. Volver"
	Leer opcionRegistro
	
	Segun opcionRegistro Hacer
		1:
			// Verificando que haya tareas
			Si numTareas = 0 Entonces
				Escribir "Error: Debe crear tareas antes de registrar horas."
			SiNo
				// Se muestran todas las tareas registradas
				Escribir "Selecciona el numero de la tarea:"
				Para i <- 1 Hasta numTareas Hacer
					Escribir i, ". ", tareas[i]
				FinPara
				Leer idTareaSeleccionada
				
				// Verificando que la tarea seleccionada exista
				Si idTareaSeleccionada < 1 O idTareaSeleccionada > numTareas Entonces
					Escribir "Tarea invalida"
				SiNo
					Escribir "Ingresa las horas trabajadas:"
					Leer horasIngresadas
					
					// Validando que las horas ingresadas sean mayores a 0
					Si horasIngresadas > 0 Entonces
						idProyectoActual <- tareaProyecto[idTareaSeleccionada]
						totalProyecto <- 0
						
						// Sumar las horas actuales de todas las tareas del mismo proyecto
						Para i <- 1 Hasta numTareas Hacer
							Si tareaProyecto[i] = idProyectoActual Entonces
								totalProyecto <- totalProyecto + horasAcumuladas[i]
							FinSi
						FinPara
						
						// Validar que el proyecto no exceda 24 horas
						Si totalProyecto + horasIngresadas <= 24 Entonces
							horasAcumuladas[idTareaSeleccionada] <- horasAcumuladas[idTareaSeleccionada] + horasIngresadas
							Escribir "Horas registradas con exito."
							Escribir "Total acumulado del proyecto: ", totalProyecto + horasIngresadas
						SiNo
							Escribir "Error: No se puede exceder 24 horas acumuladas por dia en el proyecto."
							Escribir "Horas actuales del proyecto: ", totalProyecto
						FinSi
					SiNo
						Escribir "Error: La cantidad de horas debe ser mayor que 0."
					FinSi
				FinSi
			FinSi
			MenuRegistroHoras(tareas, numTareas, horasAcumuladas, tareaProyecto, numProyectos, proyectos)
			
		2:
			
		De Otro Modo:
			Escribir "Opcion no valida"
			MenuRegistroHoras(tareas, numTareas, horasAcumuladas, tareaProyecto, numProyectos, proyectos)
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
				// Se recorre todo el arreglo tareas para mostrar todas las tareas con su total de horas
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
				
				// Se recorre todo el arreglo de proyectos para mostrar los proyectos
				Para i <- 1 Hasta numProyectos Hacer
					totalProyecto <- 0
					Escribir "Proyecto ", i, ": ", proyectos[i]
					// Recorre todas las tareas existente 
					Para j <- 1 Hasta numTareas Hacer
						// Verifica si dicha tarea pertenece al proyecto
						Si tareaProyecto[j] = i Entonces
							// Aqui se muestra la tarea con sus horas
							Escribir "   Tarea: ", tareas[j], " -> Horas: ", horasAcumuladas[j]
							// Aqui se va acumulando las horas de cada tarea para al final mostrar las horas totales por proyecto
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