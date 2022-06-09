# Declaramos una variable
calificacion = input("Intruduce tu calificación de la AZ-900: ")

calificacion = int(calificacion)
# Preguntamos si la calificación es menor a 700 
if calificacion < 700 :
    print("Vees, por no estudiar") #Si es menor a 700 muestra esto 

elif calificacion > 1000:
    print("Mientes, no puedes sacar más de mil")
else :
    print("Felicidades, pasa por tu certificado") #Si no se cumple el if anteriro pasa a esta linea
    

edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas puebla")
elif edad > 100 : 
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")
# EN PYTHON NO HAY SWITCH CASE