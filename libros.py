#modulo hecho por erick cabrera si lo demas ta mal nose este modulo es echo por mi xd
class libros:
    def __init__(self, titulo, autor, genero, stock):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.stock = stock

    def mostrar_info(self):
        print(f"Título: {self.titulo} Autor: {self.autor} Género: {self.genero} Stock: {self.stock}")

inventario_libros = [

    libros("chupa el perro", "german garmendia", "comedia", 2),
    libros("luna de pluton ", "dross", "ciencia ficcion", 5),
    libros("el señor de los anillos", "tolkien", "fantasia", 6),
    libros("ojos de plata", "scott cawton", "terror", 8),
    libros("yo cambio","jeanpaul","drama",9),

 ]

COLUMNAS = ["TITULO", "GENERO", "STOCK"]

def crear_matriz():
    """Extrae los datos de inventario_libros y arma la matriz dinámicamente."""
    matriz = []
    for libro in inventario_libros:
        matriz.append([libro.titulo.strip(), libro.genero, libro.stock])
    return matriz

def mostrar_matriz():
    """Muestra la matriz formateada en la consola."""
    matriz = crear_matriz()
    print("\n=== MATRIZ DE LIBROS ===")
    print(f"{COLUMNAS[0]:30} {COLUMNAS[1]:20} {COLUMNAS[2]}")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            ancho = 30 if j == 0 else 20 if j == 1 else 0
            print(f"{str(matriz[i][j]):{ancho}}", end=" ")
        print()

def buscar_libro(titulo_buscado):
        encontrado = False
        for libro in inventario_libros:
            if libro.titulo.lower() == titulo_buscado.lower():
                print("\n libro encontrado")
                libro.mostrar_info()
                encontrado = True
                break
        if not encontrado:
         print(f"\n El libro '{titulo_buscado}' no esta disponible")

def mostrar_inventario():
    print("\ninventario:")
    for libro in inventario_libros:
        libro.mostrar_info()


