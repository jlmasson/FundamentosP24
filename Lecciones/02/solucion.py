# Rúbrica:
# Petición y validación de variables (5 ptos)

# Ingreso de frase y llave. (1 pto)
frase = input("Ingrese mensaje a encriptar: ")

# Minúsculas y cadena limpia a los lados.
# Puede ser mayúscula, pero letras del alfabeto deben ser también mayúsculas
frase = frase.lower().strip() # (1 pto)
# Validar en caso de mensaje vacio (1 pto)
while len(frase) == 0:
	print("Mensaje no válido.")
	frase = input("Ingrese mensaje a encriptar: ")
	frase = frase.lower().strip()

# Pido el ingreso de llave.
llave = int(input("Ingrese llave: "))

# Validar que sea mayor a 0. (1 pto)
while llave <= 0:
	print("Llave no válida.")
	llave = int(input("Ingrese llave: "))

# Se procede a trabajar con una cadena de caracteres que sea el alfabeto
# Si es minúsculas, todo debe ser comparado en minúsculas.
# Si es mayúsculas, todo debe ser comparado en mayúsculas.
alfabeto = "abcdefghijklmnopqrstuvwxy" # (1 pto)
totalLetras = len(alfabeto)

encriptado = ""

# Algoritmo Principal (8 ptos) -> Puede variar la forma en que se lo resuelve
for caracter in frase:
	# Si el caracter se encuentra en la cadena, puedo obtener su índice.
	# Debo hacer esto porque la función index da error si el caracter no se encuentra en la cadena.
	# Si no se encuentra, no se hace nada y se lo concatena en la nueva cadena sin alteraciones
	# esto se da en el caso de hola12, 3 -> krod12, ya que 12 no esta en el alfabeto.
	if caracter in alfabeto:
		# Obtengo el índice del caracter 
		indiceCaracter = (alfabeto.index(caracter) + llave) % totalLetras
		caracter = alfabeto[indiceCaracter]
	encriptado += caracter

# Información por pantalla (2 ptos)
print("El mensaje encriptado es: %s" % encriptado)
