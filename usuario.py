from busqueda_usuario import buscar_usuario_recursivo



def cargar_usuarios_desde_txt(nombre_archivo="usuario.txt"):
    lista_usuarios = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                return lista_usuarios
            
            for linea in lineas[1:]:
                linea = linea.strip()
                if not linea:
                    continue
                
                partes = linea.split("|")
                if len(partes) == 3:
                    usuario_dict = {
                        "usuario": partes[0],
                        "contraseña": partes[1],
                        "nombre": partes[2]
                    }
                    lista_usuarios.append(usuario_dict)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    
    return lista_usuarios

class usuario:
    def __init__(self, usuario, contraseÑa):
        self.usuario = usuario
        self.contraseÑa = contraseÑa

    def autenticar_usuario(self):
        lista_usuarios = cargar_usuarios_desde_txt()
        
        u = buscar_usuario_recursivo(lista_usuarios, self.usuario)
        if u and u['contraseña'] == self.contraseÑa:
            mostrar_bienvenida(u)
            return u
        return []


def mostrar_bienvenida(u):
    print()
    print(f" ¡Bienvenido Biblioteca, {u['nombre']}!")