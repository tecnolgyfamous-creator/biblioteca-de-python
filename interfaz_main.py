import customtkinter as ctk
import usuario
import libros
from PIL import Image

class ventanaMain(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("BIBLIOIDAT")
      
        self.geometry("1000x800")

        #empecemos
        self.marco_lateral=ctk.CTkFrame(self, width=200, corner_radius=0)
        self.marco_lateral.pack(side="left", fill="y")

        self.logo = ctk.CTkLabel(self.marco_lateral, text="BIBLIOIDAT", font=("Helvetica", 20, "bold"))
        self.logo.pack(padx=20, pady=30)

        self.marco_contenido = ctk.CTkFrame(self)
        self.marco_contenido.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        self.btn_libros = ctk.CTkButton(self.marco_lateral, text="Libros", fg_color="transparent", command=self.mostrar_libros)
        self.btn_libros.pack(padx=20, pady=10, fill="x")
        

         
    def mostrar_libros(self):
            for widget in self.marco_contenido.winfo_children():
             widget.destroy()

            imagen_pil = Image.open("Libro_icono.jpg")
            Libro_icono = ctk.CTkImage(light_image=imagen_pil, dark_image=imagen_pil, size=(24, 24))

            for libro in libros.inventario_libros:
                
               
                tarjeta = ctk.CTkFrame(self.marco_contenido, fg_color=("gray85", "gray20"))
                tarjeta.pack(fill="x", padx=10, pady=5)

                lbl_imagen = ctk.CTkLabel(tarjeta, text="", image=Libro_icono)
                lbl_imagen.pack(side="left", padx=10, pady=10)

                texto_libro = f"{libro.titulo.title()} - {libro.autor.title()}"
                lbl_titulo = ctk.CTkLabel(tarjeta, text=texto_libro, font=("Helvetica", 14, "bold"))
                lbl_titulo.pack(side="left", padx=15, pady=10)

                lbl_stock = ctk.CTkLabel(tarjeta, text=f"Stock: {libro.stock}", font=("Helvetica", 12))
                lbl_stock.pack(side="right", padx=15, pady=10)

        
            
            

if __name__ == "__main__":
    app = ventanaMain()  
    app.mainloop()      