import numpy as np
import random as rd

# Definición de función: 2 ptos
def distribuye(n, m, q, total):
    # Se crea una matriz llena de ceros
    region = np.zeros((n, m), int)
    # Se crea una variable acumuladora que mantendrá el total de elementos
    # permitidos. Nótese en la condición del while, que el máximo posible
    # está dado por: maxPosible = n * m * q, puesto que q es la cantidad máxima 
    # de tortugas que pueden existir por cada celda. 
    suma = 0
    while total > 0 and suma < n * m * q:
        
        # Uso correcto de números aleatorios: 2 ptos
        
        # Se generan indices aleatorios para la fila y columna
        f = rd.randint(0, n - 1)
        c = rd.randint(0, m - 1)
        
        # Se genera la cantidad aleatoria de tortugas para la celda.
        totalCelda = rd.randint(1, q)
        
        # Control de casillas: 3 ptos
        
        # Se obtiene el valor actual de la celda, no importa si es 0, o ya
        # tenga una valor mayor a 0
        temp = region[f, c]
        
        # Condición que permite acumular q tortugas como máximo en la celda.
        # Por ejemplo, considérese q = 5. Al inicio, todas las celdas están en 0, 
        # entonces si totalCelda en la primera vez es 2, la celda se actualiza a ese valor
        # Supongamos que de nuevo se vuelve a generar la misma posición aleatoria, y el valor
        # de totalCelda es 3, como el anterior junto con el nuevo valor generado es menor o igual
        # al maximo, se procede a actualizar. Pero si en vez de 3 hubiera sido 4, entonces 2 + 4 <= 5
        # lo cual es falso, y la celda no se la actualiza.
        if temp + totalCelda <= q:
            region[f, c] = temp + totalCelda
            # Se resta al total la cantidad de tortugas usadas.
            total -= totalCelda
            # Se acumula el total de tortugas utilizadas que puede ser menor que el total puesto como
            # máximo. Por ejemplo: distribuye(2, 2, 1, 6). Tiene como n = m = 2 y q = 1, por ende, el
            # máximo permitido por la matriz es 4, pero la cantidad máxima de tortugas es 6. 
            # De ser así el lazo se rompe, puesto que ya colocó la cantidad de tortugas máxima permitida
            # en la matriz, que es diferente al total de tortugas que se requiere.
            suma += totalCelda
            
            # Puede darse el caso que se haya excedido al momento de haber generado la cantidad de tortugas
            # para esa celda, por eso, se procede a quitar el excedente.
            if total < 0:
                region[f, c] += total
                suma -= total
                total -= total
    # Resultado final considerando el total: 3 ptos
    return region

region = distribuye(2, 2, 1, 6)
print(region)

region = distribuye(4, 6, 5, 20)
print(region)
