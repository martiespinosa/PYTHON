import customtkinter as ctk
from PIL import Image, ImageTk

# Crear la ventana principal
window = ctk.CTk()
window.geometry("300x300")

# Crear el marco principal
frame = ctk.CTkFrame(window)
frame.pack()

# Mensaje de abajo
mensaje1 = ctk.CTkLabel(frame, text="Mensaje de abajo")
mensaje1.place(relx=0.3, rely=0.1)

# Cargar la imagen de fondo del marco
image = Image.open(r"C:\Users\MARTI\Desktop\PYTHON\INTERFACES GRÁFICAS\Diseño sin título.png")

# Aplicar una máscara de opacidad a la imagen
alpha = 0.5  # Valor entre 0 y 1
image = image.convert("RGBA")
data = image.getdata()
new_data = []
for item in data:
    new_data.append((item[0], item[1], item[2], int(alpha * 255)))
image.putdata(new_data)

# Crear una instancia de ImageTk para mostrar la imagen en el marco
background_image = ImageTk.PhotoImage(image)

# Crear una etiqueta para mostrar la imagen en el marco
label = ctk.CTkLabel(frame, image=background_image)
label.place(relx=0, rely=0)

# Establecer el tamaño del marco para que se ajuste a la imagen
frame.configure(width=image.width, height=image.height)

# Mensaje de arriba
mensaje2 = ctk.CTkLabel(frame, text="Mensaje de arriba")
mensaje2.place(relx=0.5, rely=0.8)

# Ejecutar el bucle principal de la aplicación
window.mainloop()
