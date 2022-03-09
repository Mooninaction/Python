''' 
Consigna: Crear un programa para calcular la nota final del estudiante en base a dos exámenes, los exámenes cuentan con un porcentaje distinto de la nota final
nota_1  cuenta como el 40% de la nota final
nota_2 cuenta como el 60% de la nota final

Aspectos a incluir en el entregable:
Tener en cuenta los temas vistos en la clase 1: números, print, input, variables, operaciones matemáticas, cadena de texto. 
Aspectos a tener en cuenta:
Los datos deben guardarse en variables y deben ser dinámicos por medio de input.
''' 
nota1= float(input("Ingrese la nota 1: "))
nota2= float(input("Ingrese la nota 2: "))

notas = (nota1*0.4) + (nota2*0.6)

print("La nota final es: " , notas)
