# Rúbrica:
# Petición de variables (5 ptos)

# Pido los valores correspondientes.
numeroCuenta = input("Número de cuenta: ")
tipoCuenta = input("Tipo de cuenta (aho/cte): ")
cedula = input("Cédula: ")
dolares = int(input("Valor a depositar: "))

# Algoritmo Principal (5 ptos)
# Obtengo la cantidad de billetes de $ 50.
total50 = dolares // 50
# Procedo a manipular la diferencia, es decir el módulo
# Por ejemplo, si tengo $ 77, la división entera, da 1,
# el residuo es 27.
diferencia = dolares % 50
# Con este residuo procedo a calcular la cantidad de
# billetes de $ 20.
total20 = diferencia // 20
# Luego procedo a calcular el nuevo residuo.
# Por ejemplo, sabiendo que diferencia = 27, total20 = 1
# y el residuo es ahora 7, mismo que será el nuevo valor
# de la variable diferencia
diferencia = diferencia % 20
# Luego procedo a manipular ese residuo, para obtener
# la cantidad de billetes de $ 10.
# No importa que la división entera de un valor de 0
# Es lo que se busca
total10 = diferencia // 10
# Se hace lo mismo para los demás billetes
diferencia = diferencia % 10
total5 = diferencia // 5
total1 = diferencia % 5

# Lista
billetes = [total50, total20, total10, total5, total1]

if (tipoCuenta == "aho"):
	tipoCuenta = "Ahorros"
elif (tipoCuenta == "cte"):
	tipoCuenta = "Corriente"

# Información por pantalla (5 ptos)
print("Cédula del cliente:", cedula)
print("Número de cuenta:", numeroCuenta)
print("Tipo de cuenta:", tipoCuenta)
print("Cantidad depositada:", dolares)
print("Equivalentes [50, 20, 10, 5, 1]:", billetes)