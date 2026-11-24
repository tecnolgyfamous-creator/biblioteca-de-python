import os
import sys
import customtkinter as ctk
from PIL import Image, ImageOps
import libros

RUTA_ICONO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Libro_icono.jpg")

# ---------- Paleta y colores por género ----------
FONDO = "#F2F4F3"
SUPERFICIE = "#FFFFFF"
TINTA = "#16282D"
TINTA_SUAVE = "#66777B"
LINEA = "#DCE3E2"
PETROLEO = "#12353F"
PETROLEO_2 = "#1E4B58"
AZAFRAN = "#E2A03F"
AZAFRAN_HOVER = "#CF8E2E"
ROJO = "#B4452F"
VERDE = "#2F7A5B"

COLORES_GENERO = [
    "#C0583B", "#3F7CAC", "#6B8F4E", "#8E5A9B", "#D19A2A",
    "#2F8F83", "#B24A6B", "#5B6C9D", "#8A7A5C", "#4C8C6A",
]

TODOS = "Todos los géneros"
LIMITE_INICIAL = 25

if sys.platform.startswith("win"):
    FUENTE = "Segoe UI"
elif sys.platform == "darwin":
    FUENTE = "Helvetica Neue"
else:
    FUENTE = "DejaVu Sans"


def fuente(tam=13, negrita=False):
    return (FUENTE, tam, "bold") if negrita else (FUENTE, tam)


def color_genero(genero):
    """Elige un color fijo de la paleta según el texto del género."""
    return COLORES_GENERO[sum(ord(c) for c in genero.lower()) % len(COLORES_GENERO)]


def icono_blanco(tam):
    """Convierte Libro_icono.jpg a blanco con fondo transparente."""
    gris = ImageOps.invert(Image.open(RUTA_ICONO).convert("L"))
    bbox = gris.getbbox()
    if bbox:
        gris = gris.crop(bbox)
    img = Image.new("RGBA", gris.size, (255, 255, 255, 255))
    img.putalpha(gris)
    return ctk.CTkImage(light_image=img, dark_image=img, size=tam)


class ventanaMain(ctk.CTk):
    def __init__(self, usuario_dict=None):
        super().__init__()
        ctk.set_appearance_mode("light")
        self.usuario = usuario_dict
        self.title("Biblioidat")
        self.geometry("1160x740")
        self.minsize(940, 600)
        self.configure(fg_color=FONDO)

        self.vista = "libros"
        self.mostrar_todo = False
        self._job_busqueda = None
        self._job_toast = None

        self._crear_barra_lateral()
        self._crear_contenido()
        self.cambiar_vista("libros")

    def _crear_barra_lateral(self):
        lateral = ctk.CTkFrame(self, width=230, corner_radius=0, fg_color=PETROLEO)
        lateral.pack(side="left", fill="y")
        lateral.pack_propagate(False)

        marca = ctk.CTkFrame(lateral, fg_color="transparent")
        marca.pack(fill="x", padx=22, pady=(28, 28))
        ctk.CTkLabel(marca, text="", image=icono_blanco((28, 28))).pack(side="left")
        ctk.CTkLabel(
            marca,
            text="Biblioidat",
            font=fuente(18, True),
            text_color="#FFFFFF",
        ).pack(side="left", padx=10)

        self.botones_menu = {}
        opciones = (
            ("libros", "Catálogo"),
            ("prestar", "Prestar"),
            ("devolver", "Devolver"),
            ("registrar", "Registrar"),
        )
        for clave, texto in opciones:
            btn = ctk.CTkButton(
                lateral,
                text=texto,
                anchor="w",
                height=42,
                corner_radius=8,
                fg_color="transparent",
                hover_color=PETROLEO_2,
                text_color="#FFFFFF",
                font=fuente(14),
                command=lambda c=clave: self.cambiar_vista(c),
            )
            btn.pack(fill="x", padx=14, pady=2)
            self.botones_menu[clave] = btn

        # Tarjeta de usuario en la parte inferior
        perfil = ctk.CTkFrame(lateral, fg_color=PETROLEO_2, corner_radius=12)
        perfil.pack(side="bottom", fill="x", padx=14, pady=18)
        nombre = self.usuario["nombre"].strip().title() if self.usuario else "Invitado"
        ctk.CTkLabel(
            perfil,
            text=nombre[0].upper(),
            width=36,
            height=36,
            corner_radius=18,
            fg_color=AZAFRAN,
            text_color=TINTA,
            font=fuente(15, True),
        ).pack(side="left", padx=(10, 8), pady=10)
        ctk.CTkLabel(
            perfil,
            text=nombre,
            font=fuente(12, True),
            text_color="#FFFFFF",
            wraplength=130,
            justify="left",
        ).pack(side="left", padx=(0, 8))

    def _crear_contenido(self):
        self.contenido = ctk.CTkFrame(self, fg_color="transparent")
        self.contenido.pack(side="right", fill="both", expand=True, padx=30, pady=(24, 14))

        self.lbl_titulo = ctk.CTkLabel(
            self.contenido, text="", font=fuente(22, True), text_color=TINTA, anchor="w"
        )
        self.lbl_titulo.pack(fill="x")

        self.lbl_sub = ctk.CTkLabel(
            self.contenido, text="", font=fuente(13), text_color=TINTA_SUAVE, anchor="w"
        )
        self.lbl_sub.pack(fill="x", pady=(2, 14))

        barra = ctk.CTkFrame(self.contenido, fg_color="transparent")
        barra.pack(fill="x", pady=(0, 12))
        self.barra = barra

        self.caja_buscar = ctk.CTkEntry(
            barra,
            height=40,
            corner_radius=8,
            border_width=1,
            border_color=LINEA,
            fg_color=SUPERFICIE,
            text_color=TINTA,
            font=fuente(13),
            placeholder_text="Buscar por título o autor",
            placeholder_text_color=TINTA_SUAVE,
        )
        self.caja_buscar.pack(side="left", fill="x", expand=True)
        self.caja_buscar.bind("<KeyRelease>", self._buscar_al_escribir)

        self.filtro_genero = ctk.CTkOptionMenu(
            barra,
            height=40,
            width=195,
            corner_radius=8,
            font=fuente(13),
            dropdown_font=fuente(13),
            fg_color=SUPERFICIE,
            button_color=LINEA,
            button_hover_color="#CBD4D2",
            text_color=TINTA,
            dropdown_fg_color=SUPERFICIE,
            dropdown_text_color=TINTA,
            dropdown_hover_color=FONDO,
            values=[TODOS],
            command=lambda _: self._cambiar_filtro(),
        )
        self.filtro_genero.pack(side="left", padx=(10, 0))

        self.lista = ctk.CTkScrollableFrame(
            self.contenido,
            fg_color="transparent",
            scrollbar_button_color=LINEA,
            scrollbar_button_hover_color=TINTA_SUAVE,
        )
        self.lista.pack(fill="both", expand=True)

        self._crear_form_registro()

        self.aviso = ctk.CTkLabel(
            self,
            text="",
            font=fuente(13, True),
            corner_radius=10,
            height=40,
            fg_color=TINTA,
            text_color="#FFFFFF",
        )

    def _crear_form_registro(self):
        self.form = ctk.CTkFrame(
            self.contenido,
            fg_color=SUPERFICIE,
            corner_radius=12,
            border_width=1,
            border_color=LINEA,
        )
        estilo = dict(
            width=380,
            height=40,
            corner_radius=8,
            border_width=1,
            border_color=LINEA,
            fg_color=FONDO,
            text_color=TINTA,
            font=fuente(13),
        )

        self.in_titulo = ctk.CTkEntry(self.form, **estilo)
        self.in_autor = ctk.CTkEntry(self.form, **estilo)
        self.in_genero = ctk.CTkComboBox(
            self.form,
            values=[],
            button_color=LINEA,
            button_hover_color="#CBD4D2",
            dropdown_font=fuente(13),
            **estilo,
        )
        self.in_stock = ctk.CTkEntry(self.form, **{**estilo, "width": 120})
        self.in_stock.bind("<Return>", lambda e: self.guardar_libro())

        campos = (
            ("Título", self.in_titulo),
            ("Autor", self.in_autor),
            ("Género (elige uno o escribe uno nuevo)", self.in_genero),
            ("Cantidad de copias", self.in_stock),
        )
        for i, (texto, widget) in enumerate(campos):
            ctk.CTkLabel(
                self.form, text=texto, font=fuente(13, True), text_color=TINTA, anchor="w"
            ).grid(
                row=i * 2,
                column=0,
                sticky="w",
                padx=26,
                pady=(22 if i == 0 else 12, 4),
            )
            widget.grid(row=i * 2 + 1, column=0, sticky="w", padx=26)

        ctk.CTkButton(
            self.form,
            text="Guardar",
            width=130,
            height=40,
            corner_radius=8,
            font=fuente(13, True),
            fg_color=AZAFRAN,
            hover_color=AZAFRAN_HOVER,
            text_color=TINTA,
            command=self.guardar_libro,
        ).grid(row=8, column=0, sticky="w", padx=26, pady=24)

    def _limpiar_form(self):
        for entrada in (self.in_titulo, self.in_autor, self.in_stock):
            entrada.delete(0, "end")
        self.in_stock.insert(0, "1")
        self.in_genero.configure(values=[g.title() for g in libros.generos()])
        self.in_genero.set("")

    def _nombre_usuario(self):
        return self.usuario["usuario"] if self.usuario else "invitado"

    def cambiar_vista(self, vista):
        self.vista = vista
        self.mostrar_todo = False
        titulos = {
            "libros": "Catálogo",
            "prestar": "Prestar un libro",
            "devolver": "Devolver un libro",
            "registrar": "Registrar un libro",
        }
        self.lbl_titulo.configure(text=titulos[vista])

        for clave, btn in self.botones_menu.items():
            activa = clave == vista
            btn.configure(
                fg_color=PETROLEO_2 if activa else "transparent",
                font=fuente(14, activa),
            )

        if vista == "registrar":
            self.barra.pack_forget()
            self.lista.pack_forget()
            self.form.pack(fill="x")
            self.lbl_sub.configure(text="Agrega un libro nuevo al inventario")
            self._limpiar_form()
            return

        self.form.pack_forget()
        self.barra.pack(fill="x", pady=(0, 12))
        self.lista.pack(fill="both", expand=True)
        self.caja_buscar.delete(0, "end")

        valores = [TODOS] + [g.title() for g in libros.generos()]
        self.filtro_genero.configure(values=valores)
        self.filtro_genero.set(TODOS)
        self.refrescar()

    def _cambiar_filtro(self):
        self.mostrar_todo = False
        self.refrescar()

    def _buscar_al_escribir(self, _evento=None):
        self.mostrar_todo = False
        if self._job_busqueda:
            self.after_cancel(self._job_busqueda)
        self._job_busqueda = self.after(180, self.refrescar)

    def _activar_mostrar_todos(self):
        self.mostrar_todo = True
        self.refrescar()

    def refrescar(self):
        genero = self.filtro_genero.get()
        genero = None if genero == TODOS else genero
        lista = libros.filtrar_libros(self.caja_buscar.get(), genero)
        usuario = self._nombre_usuario()

        if self.vista == "devolver":
            lista = [l for l in lista if libros.cantidad_prestada(l, usuario) > 0]
            total = sum(libros.cantidad_prestada(l, usuario) for l in lista)
            sub = (
                f"Tienes {total} libro(s) prestado(s)"
                if lista
                else "Aquí aparecen los libros que tienes prestados"
            )
        elif self.vista == "prestar":
            disp = sum(1 for l in lista if l.stock > 0)
            sub = f"{disp} de {len(lista)} títulos con copias disponibles"
        else:
            copias = sum(l.stock for l in lista)
            sub = f"{len(lista)} títulos y {copias} copias en el inventario"

        self.lbl_sub.configure(text=sub)
        self.mostrar_libros(lista)

    def mostrar_libros(self, lista):
        for w in self.lista.winfo_children():
            w.destroy()

        if not lista:
            texto = self.caja_buscar.get().strip()
            if self.vista == "devolver" and not texto:
                msg = "No tienes libros prestados.\nVe a Prestar para elegir uno."
            elif texto:
                msg = f'Ningún libro coincide con "{texto}".\nPrueba con otro título o autor.'
            else:
                msg = "No hay libros en este género."
            ctk.CTkLabel(
                self.lista, text=msg, font=fuente(14), text_color=TINTA_SUAVE, justify="center"
            ).pack(pady=55)
            return

        visibles = lista if self.mostrar_todo else lista[:LIMITE_INICIAL]
        usuario = self._nombre_usuario()
        for libro in visibles:
            self._crear_fila(libro, usuario)

        if len(lista) > LIMITE_INICIAL and not self.mostrar_todo:
            pie = ctk.CTkFrame(self.lista, fg_color="transparent")
            pie.pack(pady=12)
            ctk.CTkLabel(
                pie,
                text=f"Mostrando {LIMITE_INICIAL} de {len(lista)} libros",
                font=fuente(12),
                text_color=TINTA_SUAVE,
            ).pack(side="left", padx=(0, 12))
            ctk.CTkButton(
                pie,
                text=f"Mostrar todos ({len(lista)})",
                height=30,
                corner_radius=8,
                font=fuente(12, True),
                fg_color=SUPERFICIE,
                hover_color=LINEA,
                text_color=TINTA,
                border_width=1,
                border_color=LINEA,
                command=self._activar_mostrar_todos,
            ).pack(side="left")

    def _crear_fila(self, libro, usuario):
        color = color_genero(libro.genero)
        fila = ctk.CTkFrame(
            self.lista,
            height=60,
            fg_color=SUPERFICIE,
            corner_radius=10,
            border_width=1,
            border_color=LINEA,
        )
        fila.pack(fill="x", pady=4, padx=(0, 6))
        fila.grid_propagate(False)
        fila.grid_columnconfigure(1, weight=1)
        fila.grid_rowconfigure(0, weight=1)

        # Lomo del libro según el género
        ctk.CTkFrame(fila, width=6, corner_radius=3, fg_color=color).grid(
            row=0, column=0, sticky="ns", padx=(12, 12), pady=9
        )

        # Título arriba y autor + género abajo
        texto = ctk.CTkFrame(fila, fg_color="transparent")
        texto.grid(row=0, column=1, sticky="w", pady=6)

        ctk.CTkLabel(
            texto,
            text=libro.titulo.strip().title(),
            font=fuente(13, True),
            text_color=TINTA,
            anchor="w",
        ).pack(anchor="w")

        sub = ctk.CTkFrame(texto, fg_color="transparent")
        sub.pack(anchor="w")
        ctk.CTkLabel(
            sub, text=libro.autor.title(), font=fuente(12), text_color=TINTA_SUAVE
        ).pack(side="left")
        ctk.CTkLabel(
            sub, text=f"   {libro.genero.title()}", font=fuente(12, True), text_color=color
        ).pack(side="left")

        if self.vista == "devolver":
            n = libros.cantidad_prestada(libro, usuario)
            txt, col = f"{n} prestado(s)", PETROLEO_2
        elif libro.stock <= 0:
            txt, col = "Agotado", ROJO
        else:
            txt, col = f"{libro.stock} disponible(s)", VERDE

        ctk.CTkLabel(
            fila,
            text=f"  {txt}  ",
            font=fuente(12, True),
            text_color=col,
            fg_color=FONDO,
            corner_radius=10,
            height=24,
        ).grid(row=0, column=2, padx=12)

        if self.vista == "prestar":
            ctk.CTkButton(
                fila,
                text="Prestar",
                width=94,
                height=30,
                corner_radius=8,
                font=fuente(12, True),
                fg_color=AZAFRAN,
                hover_color=AZAFRAN_HOVER,
                text_color=TINTA,
                text_color_disabled="#FFFFFF",
                state="normal" if libro.stock > 0 else "disabled",
                command=lambda l=libro: self.prestar(l),
            ).grid(row=0, column=3, padx=(0, 12))
        elif self.vista == "devolver":
            ctk.CTkButton(
                fila,
                text="Devolver",
                width=94,
                height=30,
                corner_radius=8,
                font=fuente(12, True),
                fg_color=PETROLEO,
                hover_color=PETROLEO_2,
                text_color="#FFFFFF",
                command=lambda l=libro: self.devolver(l),
            ).grid(row=0, column=3, padx=(0, 12))

    def avisar(self, texto, error=False):
        if self._job_toast:
            self.after_cancel(self._job_toast)
        self.aviso.configure(text=f"   {texto}   ", fg_color=ROJO if error else TINTA)
        self.aviso.place(relx=0.58, rely=0.97, anchor="s")
        self.aviso.lift()
        self._job_toast = self.after(2800, self.aviso.place_forget)

    def guardar_libro(self):
        titulo = self.in_titulo.get().strip()
        autor = self.in_autor.get().strip()
        genero = self.in_genero.get().strip()
        try:
            stock = int(self.in_stock.get())
        except ValueError:
            stock = 0

        if not titulo or not autor or not genero:
            self.avisar("Completa título, autor y género", error=True)
        elif stock <= 0:
            self.avisar("La cantidad debe ser un número mayor a 0", error=True)
        elif not libros.registrar_libro(titulo, autor, genero, stock):
            self.avisar("Ese libro ya está en el catálogo", error=True)
        else:
            self.avisar(f'Guardaste "{titulo.title()}"')
            self._limpiar_form()

    def prestar(self, libro):
        if libros.prestar_libro(libro, self._nombre_usuario()):
            self.avisar(f'Prestaste "{libro.titulo.strip().title()}". Quedan {libro.stock}')
        else:
            self.avisar("No quedan copias de este libro", error=True)
        self.refrescar()

    def devolver(self, libro):
        if libros.devolver_libro(libro, self._nombre_usuario()):
            self.avisar(f'Devolviste "{libro.titulo.strip().title()}". Stock: {libro.stock}')
        else:
            self.avisar("No tienes este libro prestado", error=True)
        self.refrescar()


if __name__ == "__main__":
    app = ventanaMain()
    app.mainloop()