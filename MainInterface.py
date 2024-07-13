import tkinter
from tkinter import *
class MainInterface:
    global window
    global entry

    def on_entry_click(event):
        if entry.get() == "URL de la reunión...":
            entry.delete(0, tkinter.END)
            entry.configure(foreground="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, "URL de la reunión...")
            entry.configure(foreground="gray")

    def configurarVentana(ancho,alto):
        Tk_Width = ancho
        Tk_Height = alto + 200 #Para ponerlo un poco arriba

        x_Left = int(window.winfo_screenwidth() / 2 - Tk_Width / 2)
        y_Top = int(window.winfo_screenheight() / 2 - Tk_Height / 2)

        window.geometry("+{}+{}".format(x_Left, y_Top))
        window.minsize(ancho, alto)


    window = Tk()
    configurarVentana(ancho=920,alto=320)

    #Configuramos el entry
    entry_width = 800
    entry_height = 30
    entry = tkinter.Entry(window, width=entry_width, foreground="gray",font=('Arial', 14))
    entry.insert(0, "URL de la reunión...")
    entry.place(x=(920 - entry_width) // 2, y=(120 - entry_height) // 2, width=entry_width,
                height=entry_height)
    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focus_out)

    #Configuramos el checkbox
    save_video_var = tkinter.BooleanVar()
    checkbox = tkinter.Checkbutton(window, text="Guardar video", variable=save_video_var, font=('Arial', 14))
    checkbox.place(x=(920 - entry_width) // 2, y=(220 - entry_height) // 2 + 20)

    window.mainloop()

