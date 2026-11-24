import libros


class Prestamo:
    def __init__(self, usuario_dict):
        self.usuario = usuario_dict

    def _buscar(self, titulo):
        for libro in libros.inventario_libros:
            if libro.titulo.strip().lower() == titulo.strip().lower():
                return libro
        return None

    def realizar_prestamo(self, titulo_buscado):
        libro = self._buscar(titulo_buscado)
        if not libro:
            print(f"\n El libro '{titulo_buscado}' no existe en el inventario.")
        elif libros.prestar_libro(libro, self.usuario["usuario"]):
            libros.guardar_inventario_txt()
            print("         ¡PRÉSTAMO EXITOSO!")
            print(f" Usuario: {self.usuario['nombre']}")
            print(f" Libro:   {libro.titulo}")
            print(f" Quedan:  {libro.stock} copia(s)")
        else:
            print(f"\n Lo sentimos, no quedan copias de '{libro.titulo}'.")

    def devolver_libro(self, titulo_buscado):
        libro = self._buscar(titulo_buscado)
        if not libro:
            print(f"\n El libro '{titulo_buscado}' no pertenece al inventario.")
        elif libros.devolver_libro(libro, self.usuario["usuario"]):
            libros.guardar_inventario_txt()
            print("        ¡DEVOLUCIÓN EXITOSA!")
            print(f" Usuario: {self.usuario['nombre']}")
            print(f" Libro:   {libro.titulo}")
            print(f" Stock actual: {libro.stock}")
        else:
            print("\n No tienes ese libro prestado.")
