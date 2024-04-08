'''
nombre: Jerónimo
apellido: Córdoba
---
Clase 1: Tarea
---
Enunciado:
UTN TECHNOLOGIES
UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, 
que promete revolucionar el mercado.

Las posibles aplicaciones son las siguientes:
Inteligencia artificial (IA),
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)
Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

Los datos requeridos son los siguientes:
A) Los datos a ingresar por cada empleado encuestado son:
    nombre del empleado
    edad (no menor a 18)
    género (Masculino - Femenino - Otro)
    tecnologia (IA, RV/RA, IOT)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
    Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
    Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
    Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
'''

contador_masculino = 0; mayor_masculino = 0; nombre_mayor_masculino = 0; 
contador_NO_IA = 0; tecnologia_masculino = 0; contador_IOT_AI = 0; 
tecnologías = ["IA", "RV/RA", "IOT"]; generos = ["Masculino", "Femenino", "Otro"]; encuestas = []; 

for i in range(10):
    nombre = input("Ingrese su nombre: ").capitalize()
    
    while True:
        edad = int(input("Ingrese si edad: "))
        if edad >= 18:
            break
        print("La edad debe ser al menos 18. Inténtalo de nuevo.")
    
    while True:
        genero = str(input("Ingrese su genero (Masculino, Femenino, Otro): "))
        if genero in generos:
            break
        print("El genero debe ser (Masculino, Femenino, Otro). Inténtalo de nuevo.")
    
    while True:
        tecnologia = str(input("Ingrese su tecnologia (IA, RV/RA, IOT): "))
        if tecnologia in tecnologías:
            break
        print("La tecnologia debe ser (IA, RV/RA, IOT). Inténtalo de nuevo.")
    
    encuestas.append([nombre, edad, genero, tecnologia]) #nombre = 0, edad = 1, genero = 2, tecnologia = 3
        
for encuesta in encuestas:
    nombre = encuesta[0] #Usar "encuesta[0]" para acceder al primer dato append
    edad = encuesta[1] #Usar "encuesta[1]" para acceder al dato de la edad en el append
    genero = encuesta[2] #Usar "encuesta[2]" para acceder al dato del sexo en el append
    tecnologia = encuesta[3] #Usar "encuesta[3]" para acceder al dato de la tecnologia en el append
    
    if genero == "Masculino" and (tecnologia == "IA" or tecnologia == "IOT") and 25 <= edad <= 50:
        contador_masculino += 1
    if genero != "Femenino" or 33 <= edad <= 40:
        contador_NO_IA += 1
    if genero == "Masculino" and edad > mayor_masculino:
        mayor_masculino = edad
    nombre_tecnologia_mayor_masculino = (nombre, tecnologia)

porcentaje = (contador_NO_IA / 10) * 100

print("Cantidad de empleados de género masculino que votaron por IOT o IA, con edad entre 25 y 50 años inclusive:", contador_masculino)
print("Porcentaje de empleados que no votaron por IA, siempre que su género no sea Femenino o su edad esté entre 33 y 40:", porcentaje,"%")
print("Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género:", nombre_tecnologia_mayor_masculino[0], "-", nombre_tecnologia_mayor_masculino[1])