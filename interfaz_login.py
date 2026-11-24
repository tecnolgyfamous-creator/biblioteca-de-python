import os
import sys
import customtkinter as ctk
from PIL import Image, ImageOps
import usuario
import interfaz_main

RUTA_ICONO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Libro_icono.jpg")

# ---------- Colores simples ----------
FONDO = "#F4F5F6"
SUPERFICIE = "#FFFFFF"
TINTA = "#1E242B"
TINTA_SUAVE = "#5F6B76"
LINEA = "#D6DCE2"
BARRA = "#232F3E"
BARRA_SUAVE = "#B8C4CE"
ACENTO = "#E2A03F"
ACENTO_HOVER = "#CF8E2E"
ROJO = "#B83B2B"

if sys.platform.startswith("win"):
    FUENTE = "Segoe UI"
elif sys.platform == "darwin":
    FUENTE = "Helvetica Neue"
else:
    FUENTE = "DejaVu Sans"


def fuente(tam=13, negrita=False):
    return (FUENTE, tam, "bold") if negrita else (FUENTE, tam)


def icono_blanco(tam):
    """Convierte Libro_icono.jpg a blanco con fondo transparente."""
    gris = ImageOps.invert(Image.open(RUTA_ICONO).convert("L"))
    bbox = gris.getbbox()
    if bbox:
        gris = gris.crop(bbox)
    img = Image.new("RGBA", gris.size, (255, 255, 255, 255))
    img.putalpha(gris)
    return ctk.CTkImage(light_image=img, dark_image=img, size=tam)


ctk.set_widget_scaling(1.0)
ctk.set_appearance_mode("light")

ventana = ctk.CTk()
ventana.title("Biblioidat")
ventana.resizable(False, False)
ventana.configure(fg_color=FONDO)

ANCHO, ALTO = 880, 540
x = (ventana.winfo_screenwidth() - ANCHO) // 2
y = (ventana.winfo_screenheight() - ALTO) // 2
ventana.geometry(f"{ANCHO}x{ALTO}+{x}+{y}")

ventana.grid_columnconfigure(0, weight=5, uniform="c")
ventana.grid_columnconfigure(1, weight=6, uniform="c")
ventana.grid_rowconfigure(0, weight=1)

# ---------- Panel izquierdo ----------
izq = ctk.CTkFrame(ventana, fg_color=BARRA, corner_radius=0)
izq.grid(row=0, column=0, sticky="nsew")

ctk.CTkLabel(izq, text="", image=icono_blanco((56, 56))).place(x=40, y=44)
ctk.CTkLabel(
    izq,
    text="Biblioidat",
    font=fuente(24, True),
    text_color="#FFFFFF",
    anchor="w",
).place(x=40, rely=0.50, anchor="sw")
ctk.CTkLabel(
    izq,
    text="Busca, presta, devuelve y registra libros\nen un solo lugar.",
    font=fuente(13),
    text_color=BARRA_SUAVE,
    justify="left",
    anchor="w",
).place(x=40, rely=0.54)

# ---------- Panel derecho ----------
der = ctk.CTkFrame(ventana, fg_color=FONDO, corner_radius=0)
der.grid(row=0, column=1, sticky="nsew")

form = ctk.CTkFrame(der, fg_color="transparent")
form.place(relx=0.5, rely=0.5, anchor="center")

ctk.CTkLabel(
    form,
    text="Iniciar sesión",
    font=fuente(20, True),
    text_color=TINTA,
    anchor="w",
).pack(fill="x")
ctk.CTkLabel(
    form,
    text="Ingresa con tu usuario de la biblioteca.",
    font=fuente(13),
    text_color=TINTA_SUAVE,
    anchor="w",
).pack(fill="x", pady=(2, 22))


def campo(texto, **kw):
    ctk.CTkLabel(
        form,
        text=texto,
        font=fuente(12, True),
        text_color=TINTA,
        anchor="w",
    ).pack(fill="x", pady=(0, 4))
    caja = ctk.CTkEntry(
        form,
        width=310,
        height=40,
        corner_radius=8,
        border_width=1,
        border_color=LINEA,
        fg_color=SUPERFICIE,
        text_color=TINTA,
        font=fuente(13),
        **kw,
    )
    caja.pack(pady=(0, 14))
    return caja


usuario_caja = campo("Usuario")
contraseña_caja = campo("Contraseña", show="•")


def alternar_clave():
    contraseña_caja.configure(show="" if ver_clave.get() else "•")


ver_clave = ctk.CTkCheckBox(
    form,
    text="Mostrar contraseña",
    font=fuente(12),
    text_color=TINTA_SUAVE,
    fg_color=BARRA,
    hover_color=BARRA,
    border_color=LINEA,
    checkbox_width=18,
    checkbox_height=18,
    command=alternar_clave,
)
ver_clave.pack(anchor="w", pady=(0, 14))

mensaje = ctk.CTkLabel(
    form,
    text="",
    font=fuente(12),
    text_color=ROJO,
    anchor="w",
    wraplength=310,
    justify="left",
)
mensaje.pack(fill="x", pady=(0, 8))

intentos = 3


def verificar_login(event=None):
    global intentos
    login = usuario.usuario(usuario_caja.get(), contraseña_caja.get())
    login_data = login.autenticar_usuario()

    if login_data:
        ventana.destroy()
        app = interfaz_main.ventanaMain(login_data)
        app.mainloop()
        return

    intentos -= 1
    contraseña_caja.delete(0, "end")
    if intentos > 0:
        mensaje.configure(
            text=f"Usuario o contraseña incorrectos. Te quedan {intentos} intento(s)."
        )
    else:
        mensaje.configure(
            text="Superaste el límite de intentos. Se cerrará la aplicación."
        )
        boton_entrar.configure(state="disabled")
        ventana.after(2000, ventana.destroy)


boton_entrar = ctk.CTkButton(
    form,
    text="Entrar",
    width=310,
    height=42,
    corner_radius=8,
    font=fuente(13, True),
    fg_color=ACENTO,
    hover_color=ACENTO_HOVER,
    text_color=TINTA,
    command=verificar_login,
)
boton_entrar.pack()

usuario_caja.bind("<Return>", lambda e: contraseña_caja.focus())
contraseña_caja.bind("<Return>", verificar_login)
usuario_caja.focus()

ventana.mainloop()