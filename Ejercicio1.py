import pandas as pd

# Lista de palabras a buscar
palabras = ["LETRA", "LUZ", "RETO", "CLASE", "RADAR", "PYTHON"]

# Aquí las direcciones que el programa toma para buscar las palabras.
DIRECCIONES = {
    "derecha": (0, 1),
    "izquierda": (0, -1),
    "abajo": (1, 0),
    "arriba": (-1, 0),
}

# Función que busca a lo largo de cada fila y columna las letras de cada palabra


def buscar_palabra(matriz, palabra):  # matriz representa a sopa
    # El len busca sobre cada fila y columna a lo largo de la sopa
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            for direccion, (dx, dy) in DIRECCIONES.items():
                # dx y dy significan las direcciones posibles dentro de la sopa, en cada eje
                if buscar_desde(matriz, palabra, i, j, dx, dy):
                    return (palabra, i, j, direccion)
    return (palabra, None, None, None)

# Aquí buscará desde cada columna y fila, cada posición


def buscar_desde(matriz, palabra, x, y, dx, dy):
    for letra in palabra:
        # Verifica que esté dentro de los límites de la sopa
        if not (0 <= x < len(matriz) and 0 <= y < len(matriz[0])):
            return False
        # El strip elimina espacios y el upper compara en mayúsculas.
        celda = str(matriz[x][y]).strip().upper()
        if celda != letra:
            return False
        x += dx
        y += dy
    return True


# Cargar el archivo Excel que contiene la sopa
df = pd.read_excel("Examen2.xlsx", sheet_name="Sopa", header=None)
sopa_df = df.iloc[5:16, 0:15]

# Convertimos esa sección del Excel en una matriz (lista de listas)
sopa = sopa_df.fillna('').values.tolist()

# Esta parte limpia cada letra de la sopa para que sean siempre mayúsculas y sin espacios
for i in range(len(sopa)):
    for j in range(len(sopa[i])):
        sopa[i][j] = str(sopa[i][j]).strip().upper()

# Búsqueda de palabras
print("RESULTADOS:\n")
for palabra in palabras:
    resultado = buscar_palabra(sopa, palabra)
    if resultado[1] is not None:
        # Si el sistema encuentra la palabra, imprime su ubicación
        print(f"{resultado[0]}: ({resultado[1]+1}, {resultado[2]+1})")
    else:
        # Si no la encuentra, lo indica
        print(f"{palabra} no encontrada")
