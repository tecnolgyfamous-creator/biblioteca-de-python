matriz_permisos = [
    ["ana_gomez", True, True, True],
    ["stolarSEA245", True, True, True],
    ["invitado_estudiante", True, False, False]
]

def verificar_permiso_matriz(nombre_usuario, accion_index):
    for fila in matriz_permisos:
        if fila[0] == nombre_usuario:
            return fila[accion_index]
    return False



def buscar_usuario_recursivo(lista, nombre_buscado, indice=0):
    if indice >= len(lista):
        return None
    
    if lista[indice]['usuario'] == nombre_buscado:
        return lista[indice]
    
    return buscar_usuario_recursivo(lista, nombre_buscado, indice + 1)