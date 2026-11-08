from usuario import usuario
from prestamo import Prestamo
from libros import mostrar_inventario, buscar_libro


def iniciar_sesion():
    print("=== SISTEMA DE BIBLIOTECA ===\n")
    print("INICIO DE SESIÓN")
    intentos = 3
    while intentos > 0:
        nombre = input("Usuario: ")
        clave = input("Contraseña: ")
        login = usuario(nombre, clave)
        conectado = login.autenticar_usuario()
        if conectado:
            return conectado
        intentos -= 1
        print(f"\n  Datos incorrectos. Te quedan {intentos} intentos.\n")
    print("Has superado el límite de intentos.")
    return None


def mostrar_menu():
    print("\n===== MENÚ =====")
    print("1. Visualizar inventario")
    print("2. Buscar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Salir")


if __name__ == "__main__":
    usuario_conectado = iniciar_sesion()

    if usuario_conectado:
        gestion_prestamo = Prestamo(usuario_conectado)
        opcion = ""

        while opcion != "5":
            mostrar_menu()
            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                mostrar_inventario()
            elif opcion == "2":
                buscar_libro(input("Título a buscar: "))
            elif opcion == "3":
                gestion_prestamo.realizar_prestamo(input("Título a prestar: "))
            elif opcion == "4":
                gestion_prestamo.devolver_libro(input("Título a devolver: "))
            elif opcion == "5":
                print("\nHasta pronto.")
            else:
                print("\nOpción no válida, intenta de nuevo.")