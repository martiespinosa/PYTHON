import customtkinter as tk

def check_fullscreen(root):
    # Obtener el estado de la ventana
    state = root.wm_state()
    # Verificar si la ventana está en modo de pantalla completa
    return (state == 'zoomed')

def update_ui(root):
    # Verificar si la ventana está en modo de pantalla completa
    if check_fullscreen(root):
        # Si está en pantalla completa, mostrar algunas cosas
        label.configure(text="Estás en pantalla completa")
    else:
        # Si no está en pantalla completa, mostrar otras cosas
        label.configure(text="No estás en pantalla completa")
    # Programar la siguiente actualización de la interfaz de usuario
    root.after(1000, update_ui, root)

# Crear la ventana
root = tk.CTk()

# Crear una etiqueta vacía
label = tk.CTkLabel(root, text="")
label.pack()

# Actualizar la interfaz de usuario periódicamente
update_ui(root)

# Mostrar la ventana
root.mainloop()
