# 95.06_TP1
Trabajo práctico 1 -Teoría de Algoritmos I (75.29 / 95.06)  1C 2021

<Autores> Autores:
	
	Batallan, David Leonardo; 
	Flouret, Agustín Miguel; 
	Jadur, Luciano; 
	Milhas, Facundo; 
	de Vedia, Agustín Mariano.
</Autores>
  <Enunciado> Enunciado:
	
		Un servidor de videojuegos se alquila por horas. El contrato dura un tiempo fijo y permite utilizar en forma exclusiva el mismo por una cantidad
	contigua de horas una vez por semana. Por cada contrato que el dueño del servidor establece, se lleva un monto fijo de dinero. 
	Un monto variable monetario, uso por horas, del contrato se lo lleva la compañía de videojuegos que utilizan quienes juegan. 
	Por lo tanto al dueño del servidor le interesa tener la mayor cantidad de contratos posibles (sin importar la duración en horas de los mismos).

		El servidor funciona las 24hs. Recibe un conjunto de ofertas de contrato y debe seleccionar cuales aceptar. Cada contrato tiene un día y hora
	de inicio y un día y hora de fin. Durante ese lapso tendrán la exclusividad del servidor. Ese tiempo contiguo no puede durar más de 1 semana 
	(un contrato podría pedir por ejemplo 3 días completos pero nunca superar la semana).. Y esa fecha se repite todas las semanas. Los contratos
	aceptados no deben superponerse.

	Los siguientes son ejemplos de posibles contratos:

		Lunes de 16hs a Martes 1hs.
		Sabado de 10hs a Sábado 17hs
		Domingo de 22hs a Lunes 4hs
		Miércoles de 14hs a Miércoles a 15hs
		etc ...

	Actualmente lo que realizan es seleccionar primero los contratos de menor duración siempre que sean compatibles con los anteriores seleccionados. 
	Tienen dudas si esa es la mejor solución posible.

	Se pide:

		1. Explicar por qué la solución propuesta no es óptima

		2. Proponer una solución greedy que solucione el problema de forma óptima

		3. Determinar la complejidad temporal y espacial del problema

		4. Demostrar que la solución es óptima

		5. Programar la solución y presentar 2 ejemplos representativos para su ejecución y prueba

		6. Analizar justificando si la complejidad temporal y espacial de lo programado se condice con la obtenida en el punto 2
  
