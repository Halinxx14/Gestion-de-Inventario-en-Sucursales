import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import time

from Clases.classMenu import MenuAplicacion
from Clases.classAdministrador import AdministradorSucursales


def mostrar_splash(root, administrador):
    splash=tk.Toplevel(root)
    splash.overrideredirect(True)

    imagen=Image.open("src/imagen/oxxo.png")
    imagen=imagen.resize((500, 300))

    img=ImageTk.PhotoImage(imagen)

    label=tk.Label(splash, image=img)
    label.image=img
    label.pack()

    # Barra de carga
    barra=ttk.Progressbar(splash,orient="horizontal",length=300,mode="determinate")
    barra.pack(pady=10)

    tk.Label(splash,text="Cargando sistema...",font=("Arial", 10)).pack()

    # Centrar ventana
    ancho=img.width()
    alto=img.height()

    x=(splash.winfo_screenwidth() // 2) - (ancho // 2)
    y=(splash.winfo_screenheight() // 2) - (alto // 2)

    splash.geometry(f"{ancho}x{alto+90}+{x}+{y}")

    # Animación de carga
    for i in range(101):
        barra["value"]=i
        splash.update()
        time.sleep(0.02)

    ruta_xml="src/config/inventario.xml"
    ruta_dtd="src/config/inventario.dtd"

    valido=administrador.validar_xml_dtd(ruta_xml,ruta_dtd)

    splash.destroy()

    return valido

if __name__ == "__main__":
    admin=AdministradorSucursales()
    ventana=tk.Tk()
    ventana.withdraw()
    valido=mostrar_splash(ventana, admin)

    if valido:

        admin.cargar_xml()
        ventana.deiconify()
        app=MenuAplicacion(ventana, admin)
        ventana.mainloop()

    else:

        messagebox.showerror("Error","El archivo XML no cumple con el DTD.")
        ventana.destroy()