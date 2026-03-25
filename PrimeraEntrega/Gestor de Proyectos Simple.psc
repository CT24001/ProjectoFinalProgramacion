Algoritmo GestordeProyectosSimple
	//Variables Globales
	Definir numEmpleados Como Entero
    Dimensionar  empleados[20]
	
	
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
	Fin Segun
FinSubProceso




