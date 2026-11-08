def buscar_usuario_recursivo(lista, nombre_buscado, indice=0):
    if indice >= len(lista):
        return None
    
    if lista[indice]['usuario'] == nombre_buscado:
        return lista[indice]
    return buscar_usuario_recursivo(lista, nombre_buscado, indice + 1)