import pandas as pd
import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=PCdeSamuel\\SQLEXPRESS;"
    "Database=Examen2;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
cursor.execute("SELECT texto, grupo_id FROM palabras")
registros = cursor.fetchall()

palabras = ["LETRA", "LUZ", "RETO", "CLASE", "RADAR", "PYTHON"]

DIRECCIONES = {
    "derecha": (0, 1),
    "izquierda": (0, -1),
    "abajo": (1, 0),
    "arriba": (-1, 0),
}


class Ejercicio1:
    @staticmethod
    def buscar_palabra(matriz, palabra):
        filas = len(matriz)
        columnas = len(matriz[0])
        for i in range(filas):
            for j in range(columnas):
                for direccion, (dx, dy) in DIRECCIONES.items():
                    if Ejercicio1.buscar_ubicacion(matriz, palabra, i, j, dx, dy):
                        return (palabra, i, j, direccion)
        return (palabra, None, None, None)

    @staticmethod
    def buscar_ubicacion(matriz, palabra, x, y, dx, dy):
        for letra in palabra:
            if not (0 <= x < len(matriz) and 0 <= y < len(matriz[0])):
                return False
            celda = str(matriz[x][y]).strip().upper()
            if celda != letra:
                return False
            x += dx
            y += dy
        return True

    @staticmethod
    def ejecutar():
        df = pd.read_excel("Examen2.xlsx", sheet_name="Sopa", header=None)
        sopa_df = df.iloc[5:16, 0:15]
        sopa = sopa_df.fillna('').values.tolist()
        for i in range(len(sopa)):
            for j in range(len(sopa[i])):
                sopa[i][j] = str(sopa[i][j]).strip().upper()
        print("\nRESULTADOS DEL EJERCICIO 1:\n")
        for palabra in palabras:
            resultado = Ejercicio1.buscar_palabra(sopa, palabra)
            if resultado[1] is not None:
                print(
                    f"{resultado[0]}: ({resultado[1]+1}, {resultado[2]+1}) → Dirección: {resultado[3]}")
            else:
                print(f"{palabra} no encontrada")


class Ejercicio2:
    @staticmethod
    def animal_encerrado(texto):

        return texto.strip()

    @staticmethod
    def convertir_encabezado(texto):

        return texto.strip().upper()

    @staticmethod
    def valor_numerico(texto):

        return texto.strip().isdigit()

    @staticmethod
    def agua_clara(texto):

        partes = texto.strip().split()

        visibles = [palabra for palabra in partes if palabra.lower() in [
            "clara", "visible"]]
        return visibles[0] if visibles else ""

    @staticmethod
    def es_alfabetico(texto):

        return texto.strip().isalpha()

    @staticmethod
    def normalizar_lenguaje(texto):

        texto = texto.strip()
        if texto.lower().startswith("py"):
            return texto.lower()
        return texto

    @staticmethod
    def alternar_formato(texto):

        return texto.strip().swapcase()

    @staticmethod
    def posicion_dividir(texto):

        return texto.find("split")

    @staticmethod
    def limpiar_residuos(texto):

        return texto.rstrip()

    @staticmethod
    def recuperar_titulo(texto):

        return texto.strip().upper()

    @staticmethod
    def ejecutar(registros):
        print("\nRESULTADOS DEL EJERCICIO 2:\n")
        for texto, grupo_id in registros:
            resultado = None

            if grupo_id == 1 and "Gato" in texto:
                resultado = texto.strip()

            elif grupo_id == 4 and texto.strip().lower() == "python":
                resultado = texto.strip().upper()

            elif grupo_id == 2 and texto.strip() == "123":
                resultado = texto.strip().isdigit()

            elif grupo_id == 1 and "agua clara" in texto.lower():
                partes = texto.strip().split()
                visibles = [p for p in partes if p.lower() in [
                    "clara", "visible"]]
                resultado = visibles[0] if visibles else ""

            elif grupo_id == 2 and "123abc" in texto.lower():
                resultado = texto.strip().isalpha()

            elif grupo_id == 4 and texto.strip().lower().startswith("py"):
                resultado = texto.strip().lower()

            elif grupo_id == 1 and "cielo azul" in texto.lower():
                resultado = texto.strip().swapcase()

            elif grupo_id == 2 and "split" in texto.lower():
                resultado = texto.find("split")

            elif grupo_id == 2 and texto.endswith("    "):
                resultado = texto.rstrip()

            elif grupo_id == 5 and texto.strip().lower() == "final":
                resultado = texto.strip().upper()

            if resultado is not None:
                print(
                    f"Grupo {grupo_id} | Original: '{texto}' → Resultado: {resultado}")


class Menu:
    @staticmethod
    def iniciar():
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Ejecutar Ejercicio 1 (Sopa de letras)")
            print("2. Ejecutar Ejercicio 2 (Procesamiento de texto)")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                Ejercicio1.ejecutar()
            elif opcion == "2":
                Ejercicio2.ejecutar(registros)
            elif opcion == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    Menu.iniciar()
