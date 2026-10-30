from libros import inventario_libros
from usuario import lista_usuarios, usuario

class Prestamo:
    def __init__(self, usuario_dict):
        self.usuario = usuario_dict

    def realizar_prestamo(self, titulo_buscado):
        encontrado = False
        
        for libro in inventario_libros:
            if libro.titulo.lower() == titulo_buscado.lower():
                encontrado = True
                
                if libro.stock > 0:
                    libro.stock -= 1  
                    print("         ¡PRÉSTAMO EXITOSO!")
                    print(f" Usuario: {self.usuario['nombre']}")
                    print(f" Libro:   {libro.titulo}")
                    print(f" Quedan:  {libro.stock} copia(s)")
                else:
                    print(f"\n Lo sentimos, no quedan copias de '{libro.titulo}'.")
                break

        if not encontrado:
            print(f"\n El libro '{titulo_buscado}' no existe en el inventario.")

    def devolver_libro(self, titulo_buscado):
        encontrado = False
        for libro in inventario_libros:
            if libro.titulo.lower() == titulo_buscado.lower():
                encontrado = True
                libro.stock += 1
                print("        ¡DEVOLUCIÓN EXITOSA!")
                print(f" Usuario: {self.usuario['nombre']}")
                print(f" Libro:   {libro.titulo}")
                print(f" Stock actual: {libro.stock}")
                break

        if not encontrado:
            print(f"\n El libro '{titulo_buscado}' no pertenece al inventario.")