import unicodedata


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
    libros("luna de pluton", "dross", "ciencia ficcion", 5),
    libros("el señor de los anillos", "tolkien", "fantasia", 6),
    libros("ojos de plata", "scott cawton", "terror", 8),
    libros("yo cambio", "jeanpaul", "drama", 9),
    libros("cien años de soledad", "gabriel garcia marquez", "realismo magico", 4),
    libros("1984", "george orwell", "ciencia ficcion", 7),
    libros("don quijote de la mancha", "miguel de cervantes", "aventura", 3),
    libros("harry potter y la piedra filosofal", "j.k. rowling", "fantasia", 8),
    libros("fahrenheit 451", "ray bradbury", "ciencia ficcion", 5),
    libros("el resplandor", "stephen king", "terror", 4),
    libros("orgullo y prejuicio", "jane austen", "romance", 6),
    libros("el principito", "antoine de saint-exupery", "fabula", 7),
    libros("crimen y castigo", "fiodor dostoyevski", "drama", 3),
    libros("los juegos del hambre", "suzanne collins", "ciencia ficcion", 6),
    libros("dracula", "bram stoker", "terror", 4),
    libros("el codigo da vinci", "dan brown", "suspenso", 5),
    libros("la sombra del viento", "carlos ruiz zafon", "misterio", 6),
    libros("el hobbit", "j.r.r. tolkien", "fantasia", 7),
    libros("matar a un ruiseñor", "harper lee", "drama", 4),
    libros("el retrato de dorian gray", "oscar wilde", "terror", 3),
    libros("dune", "frank herbert", "ciencia ficcion", 5),
    libros("los pilares de la tierra", "ken follett", "historica", 4),
    libros("it", "stephen king", "terror", 6),
    libros("rayuela", "julio cortazar", "ficcion", 3),
    libros("la metamorfosis", "franz kafka", "drama", 5),
    libros("el alquimista", "paulo coelho", "aventura", 7),
    libros("el nombre del viento", "patrick rothfuss", "fantasia", 4),
    libros("un mundo feliz", "aldous huxley", "ciencia ficcion", 6),
    libros("el psicoanalista", "john katzenbach", "suspenso", 5),
    libros("cumbres borrascosas", "emily bronte", "romance", 3),
    libros("los miserables", "victor hugo", "drama", 4),
    libros("la llamada de cthulhu", "h.p. lovecraft", "terror", 6),
    libros("cronica de una muerte anunciada", "gabriel garcia marquez", "drama", 5),
    libros("el perfume", "patrick suskind", "suspenso", 4),
    libros("juego de tronos", "george r.r. martin", "fantasia", 7),
    libros("yo antes de ti", "jojo moyes", "romance", 5),
    libros("la chica del tren", "paula hawkins", "suspenso", 4),
    libros("el extranjero", "albert camus", "filosofia", 3),
    libros("dr. jekyll y mr. hyde", "robert louis stevenson", "terror", 5),
    libros("el guardian entre el centeno", "j.d. salinger", "drama", 4),
    libros("la isla del tesoro", "robert louis stevenson", "aventura", 6),
    libros("neuromante", "william gibson", "ciencia ficcion", 3),
    libros("el cuento de la criada", "margaret atwood", "ciencia ficcion", 5),
    libros("la tregua", "mario benedetti", "romance", 4),
    libros("entrevista con el vampiro", "anne rice", "terror", 3),
    libros("el monje que vendio su ferrari", "robin sharma", "autoayuda", 6),
    libros("la vuelta al mundo en 80 dias", "julio verne", "aventura", 5),
    libros("el padrino", "mario puzo", "crimen", 4),
    libros("las ventajas de ser invisible", "stephen chbosky", "drama", 6),
    libros("carrie", "stephen king", "terror", 4),
    libros("el gato negro", "edgar allan poe", "terror", 5),
    libros("frankenstein", "mary shelley", "terror", 6),
    libros("la odisea", "homero", "mitologia", 4),
    libros("la iliada", "homero", "mitologia", 5),
    libros("el tunel", "ernesto sabato", "drama", 3),
    libros("pedro paramo", "juan rulfo", "realismo magico", 4),
    libros("la casa de los espiritus", "isabel allende", "realismo magico", 5),
    libros("el silmarillion", "j.r.r. tolkien", "fantasia", 3),
    libros("ready player one", "ernest cline", "ciencia ficcion", 6),
    libros("los renglones torcidos de dios", "torcuato luca de tena", "suspenso", 4),
    libros("veronika decide morir", "paulo coelho", "drama", 5),
    libros("el lobo estepario", "hermann hesse", "filosofia", 3),
    libros("demian", "hermann hesse", "filosofia", 4),
    libros("siddhartha", "hermann hesse", "filosofia", 5),
    libros("la naranja mecanica", "anthony burgess", "ciencia ficcion", 4),
    libros("la ladrona de libros", "markus zusak", "historica", 6),
    libros("el diario de ana frank", "ana frank", "biografia", 5),
    libros("el arte de la guerra", "sun tzu", "estrategia", 7),
    libros("el principe", "nicolas maquiavelo", "politica", 4),
    libros("la republica", "platon", "filosofia", 3),
    libros("meditaciones", "marco aurelio", "filosofia", 6),
    libros("el viejo y el mar", "ernest hemingway", "aventura", 5),
    libros("por quien doblan las campanas", "ernest hemingway", "belica", 3),
    libros("adios a las armas", "ernest hemingway", "romance", 4),
    libros("el gran gatsby", "f. scott fitzgerald", "drama", 5),
    libros("las uvas de la ira", "john steinbeck", "drama", 3),
    libros("de ratones y hombres", "john steinbeck", "drama", 4),
    libros("al este del eden", "john steinbeck", "drama", 4),
    libros("la peste", "albert camus", "drama", 3),
    libros("el mito de sisifo", "albert camus", "filosofia", 2),
    libros("el jugador", "fiodor dostoyevski", "drama", 4),
    libros("los hermanos karamazov", "fiodor dostoyevski", "drama", 3),
    libros("el idiota", "fiodor dostoyevski", "drama", 4),
    libros("anna karenina", "leon tolstoi", "romance", 3),
    libros("guerra y paz", "leon tolstoi", "historica", 2),
    libros("la muerte de ivan ilich", "leon tolstoi", "drama", 4),
    libros("el fantasma de canterville", "oscar wilde", "comedia", 6),
    libros("la importancia de llamarse ernesto", "oscar wilde", "comedia", 3),
    libros("sin noticias de gurb", "eduardo mendoza", "comedia", 4),
    libros("buenos presagios", "terry pratchett y neil gaiman", "comedia", 5),
    libros("guia del autoestopista galactico", "douglas adams", "comedia", 6),
    libros("el mundo de sofia", "jostein gaarder", "filosofia", 4),
    libros("la historia interminable", "michael ende", "fantasia", 5),
    libros("momo", "michael ende", "fantasia", 5),
    libros("coraline", "neil gaiman", "terror", 6),
    libros("american gods", "neil gaiman", "fantasia", 4),
    libros("la catedral del mar", "ildefonso falcones", "historica", 5),
    libros("los siete maridos de evelyn hugo", "taylor jenkins reid", "romance", 6),
    libros("el psicoanalista en apuros", "john katzenbach", "suspenso", 3),
]

COLUMNAS = ["TITULO", "AUTOR", "GENERO", "STOCK"]
ANCHOS = [30, 22, 20, 5]


# ---------------- Consola ----------------
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
        if libro.titulo.strip().lower() == titulo_buscado.strip().lower():
            print("\n libro encontrado")
            libro.mostrar_info()
            encontrado = True
            break
    if not encontrado:
        print(f"\n El libro '{titulo_buscado}' no esta disponible")


# ---------------- Búsqueda y Registro ----------------
def _norm(texto):
    t = unicodedata.normalize("NFD", texto.lower().strip())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def filtrar_libros(texto, genero=None):
    t = _norm(texto)
    g = _norm(genero) if genero else None
    return [
        l for l in inventario_libros
        if (t in _norm(l.titulo) or t in _norm(l.autor))
        and (g is None or _norm(l.genero) == g)
    ]


def generos():
    return sorted({l.genero for l in inventario_libros})


def registrar_libro(titulo, autor, genero, stock):
    """Agrega un libro nuevo directamente a la lista inventario_libros."""
    t = titulo.strip().lower()
    a = autor.strip().lower()
    g = genero.strip().lower()
    if any(_norm(l.titulo) == _norm(t) for l in inventario_libros):
        return False
    inventario_libros.append(libros(t, a, g, stock))
    return True


# ---------------- Préstamos ----------------
prestamos_activos = {}


def _clave(usuario, libro):
    return (usuario, libro.titulo.strip().lower())


def prestar_libro(libro, usuario):
    if libro.stock <= 0:
        return False
    libro.stock -= 1
    k = _clave(usuario, libro)
    prestamos_activos[k] = prestamos_activos.get(k, 0) + 1
    return True


def devolver_libro(libro, usuario):
    k = _clave(usuario, libro)
    if prestamos_activos.get(k, 0) <= 0:
        return False
    libro.stock += 1
    prestamos_activos[k] -= 1
    if prestamos_activos[k] == 0:
        del prestamos_activos[k]
    return True


def cantidad_prestada(libro, usuario):
    return prestamos_activos.get(_clave(usuario, libro), 0)