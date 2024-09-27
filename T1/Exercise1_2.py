result = 0
number = 1

n_iteraciones = 0
#
# OPCION 1
#
while number < 100:      # Condición desde 1 al 100.
    n_iteraciones = n_iteraciones + 1
    if number % 2 == 0:           # Condición de Par.
        result = result + number        # Suma de los valores que son pares. (que cumple la condicion de arriba)
    else:                         # si no se cumple la condición de Par 
        None                            # No hace nada
    number = number + 1           # incrementa en 1 el valor de number.

print("Sum of even numbers (Method 1):", result, " con N iteraciones: ",n_iteraciones)

#
# OPCION 2
# 
result = 2
number = 4
n_iteraciones = 0

while number < 100:
    n_iteraciones = n_iteraciones + 1
    result = result + number
    number = number + 2

print("Sum of even numbers (Method 2):", result, " con N iteraciones: ",n_iteraciones)

############
# OPCION 3 #
############

numero_salida = 99
result = 0
n_iteraciones = 0

for number in range(0, numero_salida + 1,2):
    #print(" Valores de number",number)
    n_iteraciones = n_iteraciones + 1
    result += number

print("Sum of even numbers (Method 3):", result, " con N iteraciones: ",n_iteraciones)


# Del 1 al 100.
# 
# number          --> result = result + number.
# 0 es par ? - si --> 0
# 1 es par - no
# 2 es par ? - si --> 0 + 2
# 3 es par ? - no
# 4 es par ? - si --> 0 + 2 + 4
# 101 - salir del prgroama y mostrar el resultado.

##
# X = si (y%2 == 0) siendo Y = [1..100]
# 
##
