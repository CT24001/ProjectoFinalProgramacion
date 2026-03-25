Algoritmo GestordeProyectosSimple
	//Variables Globales
	Definir numEmpleados Como Entero
    Dimensionar  empleados[20]
	
	Definir numProyectos Como Entero
    Dimensionar  proyectos[20] 
	
	
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
	Leer opcion
	
	
	Segun opcion Hacer
		1:
			MenuEmpleado(empleados,numEmpleados)
		2:
			MenuProyecto(proyectos, numProyectos)
		3:
			
		4:
			
		5:
			
		De Otro Modo:
			Escribir "Opcion no validad"
	Fin Segun
	
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
			GestordeProyectosSimple()
			
		De Otro Modo:
			Escribir "Opcion no validad"
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
			GestordeProyectosSimple()
		De Otro Modo:
			Escribir "Opcion no valida" 
			MenuProyecto(proyectos, numProyectos)
	Fin Segun
	
FinSubProceso


