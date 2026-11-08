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

COLUMNAS = ["TITULO", "AUTOR", "GENERO", "STOCK"]
ANCHOS = [30, 22, 20, 5]

def crear_matriz():
    
    matriz = []
    for libro in inventario_libros:
        matriz.append([libro.titulo.strip().title(), libro.autor.title(), libro.genero, libro.stock])
    return matriz

def mostrar_inventario():
    
    matriz = crear_matriz()
    print("\n=== INVENTARIO DE LIBROS ===")

    encabezado = ""
    for j in range(len(COLUMNAS)):
        encabezado += f"{COLUMNAS[j]:{ANCHOS[j]}} "
    print(encabezado)
    print("-" * (sum(ANCHOS) + len(ANCHOS)))

    for fila in matriz:
        linea = ""
        for j in range(len(fila)):
            linea += f"{str(fila[j]):{ANCHOS[j]}} "
        print(linea)



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



