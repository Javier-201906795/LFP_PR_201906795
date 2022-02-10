#Librerias (Para abrir archivos)
from tkinter import filedialog, Tk

#Configuracion librerias explorador de archivos
def abrirarchivo():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Selecciona un archivo",
        initialdir =  "./",
        filetype = [
            ("Archivos LFP", "*.lfp"),
            ("Todos los archivos", "*.*")
        ]
    )



#Main program
if __name__ == "__main__":
    texto = abrirarchivo()
