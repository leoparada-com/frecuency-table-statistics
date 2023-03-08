# El siguiente script corresponde una actividad incial para profesores de matematica que se inician en la programacion con Python. El script realiza lo siguiente:

# Crea un conjunto de números aleatorios
# Determina el dominio 
# Contabiliza cuántos hay de cada uno 
# Crea una tabla de frecuencia
# Construye un histograma

# [1] ---------------------------------------------------------------------------
def generar_numeros_aleatorios(minimo, maximo, cantidad):
    import random                  # Importa el módulo random para generar números aleatorios. 
    numeros = []                   # Crea una lista vacía para almacenar los números aleatorios.
    for i in range(cantidad):      # Itera tantas veces como el valor indicado por la variable "cantidad".
        numeros.append(random.randint(minimo, maximo)) # Agrega un número aleatorio único al conjunto.
    return numeros                 # Devuelve el conjunto de números aleatorios únicos generados.


# [2] ----------------------------------------------------------------------------
def determinar_dominio(lista):    
    conjunto = set(lista)          # Convertir la lista en un conjunto (set) para obtener los valores únicos
    return sorted(list(conjunto))  # Convertir el conjunto de vuelta en una lista ordenada y devolverla


# [3] ----------------------------------------------------------------------------
def contabilizar(lista):
    # Obtener la lista de valores únicos usando la función determinar_dominio   
    valores_unicos = determinar_dominio(lista)     
    conteo         = {} # Inicializar un diccionario vacío para contar la cantidad de cada valor
    # Iterar sobre la lista de valores únicos y contar la cantidad de cada valor en la lista original

    for valor in valores_unicos:
        cantidad      = lista.count(valor)
        conteo[valor] = cantidad
    
    return conteo # Devolver el diccionario con el conteo de cada valor

# [4] ----------------------------------------------------------------------------
def print_dict_as_table(dictionary):
    from prettytable import PrettyTable
    table = PrettyTable(['x', 'f'])
    for key, value in dictionary.items():
        table.add_row([key, value])
    print(table)


# [5] ----------------------------------------------------------------------------
def plot_histogram(dictionary):
    import matplotlib.pyplot as plt
    x = list(dictionary.keys())
    y = list(dictionary.values())
    plt.bar(x, y)
    plt.xlabel('eje de valores')
    plt.ylabel('eje de frecuencias')
    plt.title('Histograma')
    save_path = 'histogram.png'
    plt.savefig(save_path)


#  ----------------------------------------------------------------------------
#  COMIENZA EL PROGRAMA
#  ----------------------------------------------------------------------------
#lista   = [1,2,3,2,3,4,5,3,2,3,4,5,6]
lista            = generar_numeros_aleatorios(1,6,20)
tabla_frecuencia = contabilizar(lista)

print('El set de datos es el siguiente:')
print(lista)
print()
print('La tabla de frecuencia es la siguiente:')
#print(tabla_frecuencia)
print_dict_as_table(tabla_frecuencia)
plot_histogram(tabla_frecuencia)


#  ----------------------------------------------------------------------------
#  FIN DEL PROGRAMA
#  ----------------------------------------------------------------------------

