from permisos import buscar_usuario_recursivo

""" lista """

lista_usuarios = [
    {"usuario": "ana_gomez", "contraseña": "segura2026*", "nombre": "ana gomez"},
    {"usuario": "stolarSEA245", "contraseña": "clave1234", "nombre": "Stolar Sirlupú Enrique Arturo"},
    {"usuario": "JimenezPJL123", "contraseña": "password987", "nombre": "Jimenez Prada Jorge Luis "},
    {"usuario": "luzmarina", "contraseña": "admin#2026", "nombre": "luz marina"},
    {"usuario": "matin", "contraseña": "clave3546", "nombre": "martin rios salazar"}
]

class usuario:
    def __init__(self, usuario, contraseÑa):
            self.usuario = usuario
            self.contraseÑa = contraseÑa

    

class usuario:
    def __init__(self, usuario, contraseÑa):
        self.usuario = usuario
        self.contraseÑa = contraseÑa

    def autenticar_usuario(self):
        print("INICIO DE SESIÓN")
        intentos = 3
        while intentos > 0:
            u = buscar_usuario_recursivo(lista_usuarios, self.usuario)

            if u and u['contraseña'] == self.contraseÑa:
                mostrar_bienvenida(u)
                return u
            
            intentos -= 1
            print(f"\n  Datos incorrectos. Te quedan {intentos} intentos.\n")

        print("Has superado el limite de intentos.")
        return []


def mostrar_bienvenida(u):
    print()
    print(f" ¡Bienvenido Bliblioteca, {u["nombre"]}!")