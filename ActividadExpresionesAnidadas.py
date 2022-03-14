'''A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable que almacene si se cumplen TODAS las siguientes condiciones, 
encadenando operadores lógicos en una sola línea:
NOMBRE sea diferente de cuatro asteriscos “****”
EDAD sea mayor que 10 y a su vez menor que 18
Que la longitud de NOMBRE sea mayor o igual a 3 pero a la vez menor que 10
EDAD multiplicada por 4 sea mayor que 40
'''

nombre= input("Ingrese su nombre ")
edad=int(input("Ingrese su edad "))

validacion= (nombre !="****") and ( edad > 10 and edad <18) and (len(nombre) >= 3 and len(nombre) < 10) and (edad * 4 > 40)
print(validacion)