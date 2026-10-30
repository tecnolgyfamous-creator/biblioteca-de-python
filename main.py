from usuario import usuario
from prestamo import Prestamo
from libros import mostrar_inventario

if __name__ == "__main__":
    print("=== SISTEMA DE BIBLIOTECA ===\n")

   
    login = usuario("ana_gomez", "segura2026*")
    usuario_conectado = login.autenticar_usuario()

    if usuario_conectado:
        gestion_prestamo = Prestamo(usuario_conectado)

        # Se realiza el préstamo de un libro
        gestion_prestamo.realizar_prestamo("chupa el perro")

        # Se intenta pedir otro libro
        gestion_prestamo.realizar_prestamo("el señor de los anillos")

        # Devolución de un libro
        gestion_prestamo.devolver_libro("chupa el perro")

        # Ver cómo quedó el inventario al final
        print("\n")
        mostrar_inventario()