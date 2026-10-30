import customtkinter as ctk
import usuario 
from customtkinter import CTkMessagebox


ctk.set_widget_scaling(1.5)
ctk.set_appearance_mode("Light")
ventana = ctk.CTk()
ventana.geometry ("600x800")

bienvenida = ctk.CTkLabel(ventana , text=" biblioidat", font= ("helvetica", 24 , "bold")  )

bienvenida.pack(side = "top" , anchor="w", padx=20, pady=20)
ventana.title("BIBLIOIDAT")

container = ctk.CTkFrame(ventana)
container.place(relx=0.5, rely=0.5, anchor="center")

usuario_label = ctk.CTkLabel(container, text="USUARIO", font=("arial" , 15 ))
usuario_label.grid (row=0 ,column=0 , padx=10 , pady= 10, sticky="w" )


usuario_caja = ctk.CTkEntry(container, width=200 , font=("arial" , 12))
usuario_caja.grid(  row=0,column=1 , padx=10, pady=10)


contraseña= ctk.CTkLabel(container , text="CONTRASEÑA", font=("arial" , 15 ))
contraseña.grid (row=1 ,column=0 , padx=10 , pady= 10, sticky="w" )

contraseña_caja = ctk.CTkEntry(container, width=200 , font=("arial" , 12))
contraseña_caja.grid(  row=1,column=1 , padx=10, pady=10)

def verificar_login():
        login= usuario.usuario(usuario_caja.get() ,contraseña_caja.get() )
        login.autenticar_usuario()
        print()

boton_entrar = ctk.CTkButton( container, text="Entrar", font=("arial", 14, "bold"), width=15, fg_color="#1C1D59", text_color="white" ,command=verificar_login)
boton_entrar.grid(row=2, column=0, columnspan=2, pady=20)


    
ventana.mainloop()