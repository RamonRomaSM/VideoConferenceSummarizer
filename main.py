import tkinter as Tk


def on_entry_click(event):
    if entry.get() == "URL de la reunión...":
        entry.delete(0, Tk.END)
        entry.configure(foreground="black")


def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "URL de la reunión...")
        entry.configure(foreground="gray")


def configurarVentana(ancho, alto):
    Tk_Width = ancho
    Tk_Height = alto + 200  # Para ponerlo un poco arriba

    x_Left = int(window.winfo_screenwidth() / 2 - Tk_Width / 2)
    y_Top = int(window.winfo_screenheight() / 2 - Tk_Height / 2)

    window.geometry("+{}+{}".format(x_Left, y_Top))
    window.minsize(ancho, alto)

def on_accept():
    print()
def on_cancel():
    print()



window = Tk.Tk()
configurarVentana(ancho=920, alto=320)

# Configuramos el entry
entry_width = 800
entry_height = 30
entry = Tk.Entry(window, width=entry_width, foreground="gray", font=('Arial', 14))
entry.insert(0, "URL de la reunión...")
entry.place(x=(920 - entry_width) // 2, y=(120 - entry_height) // 2, width=entry_width,
            height=entry_height)
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focus_out)

# Configuramos el checkbox
save_video_var = Tk.BooleanVar()
checkbox = Tk.Checkbutton(window, text="Guardar video", variable=save_video_var, font=('Arial', 14))
checkbox.place(x=(920 - entry_width) // 2, y=(220 - entry_height) // 2 + 20)

# Crear los botones Aceptar y Cancelar
button_width = 10

accept_button = Tk.Button(window, text="Aceptar", width=button_width, command=on_accept)
cancel_button = Tk.Button(window, text="Cancelar", width=button_width, command=on_cancel)

button_y = (320 - entry_height) // 2 + 90
accept_button.place(x=350, y=button_y)
cancel_button.place(x= 500, y=button_y)


window.mainloop()
