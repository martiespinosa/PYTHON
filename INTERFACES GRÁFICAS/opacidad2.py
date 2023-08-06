import customtkinter as ctk

window = ctk.CTk()
window.geometry("300x300")

frame= ctk.CTkFrame(window)
frame.pack()

mensaje_de_abajo = ctk.CTkLabel(frame, text="¡Mensaje en segundo plano!")
mensaje_de_abajo.pack()

window.attributes('-alpha', 0.5)

mensaje_primario = ctk.CTkLabel(window, text="¡Mensaje en primer plano!")
mensaje_primario.pack()

window.mainloop()
