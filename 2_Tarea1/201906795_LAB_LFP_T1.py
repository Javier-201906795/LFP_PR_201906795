#Librerias (Para abrir archivos)
from tkinter import filedialog, Tk

################################################################
#Configuracion librerias explorador de archivos
def abrirarchivo():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Selecciona un archivo",
        #accede a la carpeta donde esta el archivo py
        initialdir =  "./",
        #tipo de archivo que puede seleccionar
        filetype = [
            ("Archivos LFP", "*.lfp"),
            ("Todos los archivos", "*.*")
        ]
    )

    #Leer archivo
    if archivo is None:
        print("No se selecciono ningun archivo" + "\n")
        return None
    else:
        #Devolver Texto del archivo
        txt = archivo.read()
        archivo.close()
        return txt
################################################################
#Quitar espacios vacios Y devuelve una lista con los codigos Ascii
def elementosascii(texto):
    textosinespacios = []
    for a in texto:
        if a == '\n' or a == ' ':
            pass
        else:
            #temp =[ord(a),a]
            textosinespacios.append(ord(a))
    return textosinespacios
################################################################
def elementosasciienrango(listado,RangIni,RangFin):
    #Evalua si el elemento esta en el rango especificado
    contador = 0
    for c in listado:
        if int(c) >= int(RangIni) and int(c) <= int(RangFin):
            #cuenta los elementos 
            contador += 1
    return contador
################################################################
#Main program
if __name__ == "__main__":
    #cargar el archivo lfp con el texto a inspeccionar
    texto = abrirarchivo()

    #inspeccionarmos si existe algun texto
    if texto is not None:
        #si tiene mas de 0 caracteres
        if (len(texto)>0):
            print(texto)
            print("################################")
            #Quitar espacios vacios y devuelve un listado ascii
            listadoascii = elementosascii(texto)
            print(listadoascii)
            #Evalua cuantos son  letras Mayusculas
            Mayusculas = elementosasciienrango(listadoascii,97,122)
            #Evalua cuantos son  letras Minusculas
            Minusculas = elementosasciienrango(listadoascii,65,90)
            #Evalua cuantos son  digitos
            #Evalua cuantos son  simbolos

            print("Mayusculas: ", Mayusculas, "\nMinusculas: ", Minusculas)
            
            
        else:
            print("Error T2: No hay texto en el archivo seleccionado")
    else:
        print("Error T1: No se puede procesar \n")

    
