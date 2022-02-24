from tkinter import filedialog, Tk, Label, Button

def mensaje():
    print("mensaje")
    ventana = Tk()
    ventana.geometry("400x280")
    ventana.title("LFP_PR_201906795.py[2]")
    
    lbl = Label(ventana,text="Ingresar un archivo .data")
    lbl.pack()



if __name__ == "__main__":

    ventana = Tk()
    ventana.geometry("400x280")
    ventana.title("LFP_PR_201906795.py")
    
    lbl = Label(ventana,text="Ingresar un archivo .data")
    lbl.pack()

    btn = Button(ventana,text="Subir archivo .data", command=mensaje)
    btn.pack()

    ventana.mainloop()