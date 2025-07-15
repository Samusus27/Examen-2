
import pyodbc


def espacios_invisibles(texto):
    return texto.strip()


def formatear_encabezado(texto):
    return texto.capitalize()


def valor_numerico(texto):
    return texto.isdigit()


def extraer_visible(texto):
    if "visible" in texto:
        return texto[texto.find("visible"):]
    return ""


def es_alfabetico(texto):
    return texto.isalpha()


def normalizar_lenguaje(texto):
    return texto.lower().strip()


def alternar_formato(texto):
    return texto.swapcase()


def posicion_dividir(texto):
    return texto.find("dividir")


def limpiar_residuos(texto):
    return texto.rstrip()


def recuperar_titulo(texto):
    return texto.strip().title()


conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=PCdeSamuel\\SQLEXPRESS;"
    "Database=Examen2;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
cursor.execute("SELECT texto, grupo_id FROM palabras")
registros = cursor.fetchall()

print("RESULTADOS DEL EJERCICIO 2:\n")

for texto, grupo_id in registros:
    if grupo_id == 1:
        resultado = espacios_invisibles(texto)
    elif grupo_id == 2:
        resultado = formatear_encabezado(texto)
    elif grupo_id == 3:
        resultado = valor_numerico(texto)
    elif grupo_id == 4:
        resultado = extraer_visible(texto)
    elif grupo_id == 5:
        resultado = es_alfabetico(texto)
    elif grupo_id == 6:
        resultado = normalizar_lenguaje(texto)
    elif grupo_id == 7:
        resultado = alternar_formato(texto)
    elif grupo_id == 8:
        resultado = posicion_dividir(texto)
    elif grupo_id == 9:
        resultado = limpiar_residuos(texto)
    elif grupo_id == 10:
        resultado = recuperar_titulo(texto)
    else:
        resultado = "Grupo no válido"

    print(f"Grupo {grupo_id} | Original: '{texto}' → Resultado: {resultado}")
