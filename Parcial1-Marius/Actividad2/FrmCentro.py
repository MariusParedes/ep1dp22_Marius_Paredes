from distutils.command.config import config
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import bgcolor
from Propietario import Propietario

#variables globales



#creación interfaz grafica
formulario = tkinter.Tk()
formulario.geometry("1800x500")
formulario.config(bg="LightSkyBlue1")
formulario.title ("Registro de centro educativo privado")

#Creación de tabla
tabla = ttk.Treeview(formulario,columns=("columnanombre","columnadireccion","columnatelefono","columnadirector","columnaurl","columnahombres","columnamujeres","columnaidpropietario","columnanombrepropietario","columnatelefonopropietario"))
lista = []
#print("Carga de datos")
def cargarDatos():
    carga = Propietario()
    carga.codigo = int(txt_codigo.get())
    carga.nombre = txt_nombre.get()
    carga.direccion = txt_direccion.get()
    carga.telefono = txt_telefono.get()
    carga.director = txt_director.get()
    carga.url = txt_url.get()
    carga.cantH = int(txt_Chombre.get())
    carga.cantM = int(txt_Cmujer.get())
    carga.idPropiedad = int(txt_idPropietario.get())
    carga.nomPropiedad = txt_nombrePropietario.get()
    carga.telPropiedad = txt_telefonoPropietario.get()
    lista.append(carga)
    crearTabla()

def crearTabla():
    for fila in tabla.get_children():
        tabla.delete(fila)
    
    #tamaño de columnas
    tabla.column("#0",width=10, anchor=CENTER)
    #tabla.column("ccod", width=30)
    tabla.column("columnanombre", width=30, anchor=CENTER)
    tabla.column("columnadireccion",width=30,   anchor=CENTER)
    tabla.column("columnatelefono" , width=30,anchor=CENTER)
    tabla.column("columnadirector", width=30,anchor=CENTER)
    tabla.column("columnaurl", width=30,   anchor=CENTER)
    tabla.column("columnahombres", width=30,anchor=CENTER)
    tabla.column("columnamujeres", width=30,anchor=CENTER)
    tabla.column("columnaidpropietario", width=30, anchor=CENTER)
    tabla.column("columnanombrepropietario", width=30, anchor=CENTER)
    tabla.column("columnatelefonopropietario", width=30, anchor=CENTER )
    
    
    
    
    tabla.heading("#0", text="Codigo Centro" , anchor=CENTER)
    #tabla.heading("ccod", text="Codigo", anchor=CENTER)
    tabla.heading("columnanombre", text="Nombre" , anchor=CENTER)
    tabla.heading("columnadireccion", text= "Direccion", anchor=CENTER)
    tabla.heading("columnatelefono", text= "Telefono", anchor=CENTER)
    tabla.heading("columnadirector", text= "Director", anchor=CENTER)
    tabla.heading("columnaurl", text= "URL", anchor=CENTER)
    tabla.heading("columnahombres", text= "Cant Hombres", anchor=CENTER)
    tabla.heading("columnamujeres", text= "Cant Mujeres", anchor=CENTER)   
    tabla.heading("columnaidpropietario", text= "Id Propietario", anchor=CENTER)
    tabla.heading("columnanombrepropietario", text= "Nombre Propietario", anchor=CENTER)
    tabla.heading("columnatelefonopropietario", text= "Telefono Propietario", anchor=CENTER)
    
    for registro in lista:
        
        tabla.insert("",END, text=registro.codigo, values=(registro.nombre, registro.direccion, registro.telefono, registro.director, registro.url, registro.cantH, registro.cantM, registro.idPropiedad, registro.nomPropiedad, registro.telPropiedad) )
    tabla.place(y=180,width=1700)
    #tabla.pack(fill= tkinter.X)



#Crear objetos
lbl_formulario = tkinter.Label(formulario,text="FORMULARIO DE REGISTRO DEL PROPIETARIO EN CENTROS EDUCATIVOS PRIVADOS", font=("Arial",16))
lbl_formulario.pack()
#COL1
lbl_codigo=tkinter.Label(formulario, text="Codigo centro  ", bg="LightSkyBlue1", font=("Calibri",14))
#lbl_valor1.pack(padx=10)
lbl_codigo.place(x=10, y=50)
txt_codigo=tkinter.Entry(formulario,bg="snow", font=("Calibri" ,14))
txt_codigo.place(x=150, y=50)
#txt_valor1.pack(pady=10)

#cOL2
lbl_nombre=tkinter.Label(formulario, text="Nombre centro", bg="LightSkyBlue1", font=("Calibri",14))
#lbl_valor1.pack(padx=10)
lbl_nombre.place(x=400, y=50)
txt_nombre=tkinter.Entry(formulario,bg="snow", font=("Calibri" ,14))
txt_nombre.place(x=540, y=50)
#txt_valor1.pack(pady=10)

#COL3
lbl_direccion=tkinter.Label(formulario, text="Dirección centro", bg="LightSkyBlue1", font=("Calibri",14))
#lbl_valor1.pack(padx=10)
lbl_direccion.place(x=800, y=50)
txt_direccion=tkinter.Entry(formulario,bg="snow", font=("Calibri" ,14))
txt_direccion.place(x=950, y=50)
#txt_valor1.pack(pady=10)

#cOL4
lbl_telefono=tkinter.Label(formulario, text="Tel centro        ", bg="LightSkyBlue1", font=("Calibri",14))
#lbl_valor1.pack(padx=10)
lbl_telefono.place(x=1200, y=50)
txt_telefono=tkinter.Entry(formulario,bg="snow", font=("Calibri" ,14))
txt_telefono.place(x=1350, y=50)
#txt_valor1.pack(pady=10)

#cOL1 F2
lbl_director=tkinter.Label(formulario, text="Director centro", bg="LightSkyBlue1", font=("Calibri",14))
#lbl_valor1.pack(padx=10)
lbl_director.place(x=10, y=90)
txt_director=tkinter.Entry(formulario,bg="snow", font=("Calibri" ,14))
txt_director.place(x=150, y=90)
#txt_valor1.pack(pady=10)

#cOL2 F2
lbl_url=tkinter.Label(formulario, text="URL centro       ", bg="LightSkyBlue1", font=("Calibri",14))
#lbl_valor1.pack(padx=10)
lbl_url.place(x=400, y=90)
txt_url=tkinter.Entry(formulario,bg="snow", font=("Calibri" ,14))
txt_url.place(x=540, y=90)
#txt_valor1.pack(pady=10)

#COL3 F2
lbl_Chombre=tkinter.Label(formulario, text="Cant Hombres    ", bg="LightSkyBlue1", font=("Calibri",14))
#lbl_valor1.pack(padx=10)
lbl_Chombre.place(x=800, y=90)
txt_Chombre=tkinter.Entry(formulario,bg="snow", font=("Calibri" ,14))
txt_Chombre.place(x=950, y=90)
#txt_valor1.pack(pady=10)


#cOL4 F2
lbl_Cmujer=tkinter.Label(formulario, text="Cant Mujeres", bg="LightSkyBlue1", font=("Calibri",14))
#lbl_valor1.pack(padx=10)
lbl_Cmujer.place(x=1200, y=90)
txt_Cmujer=tkinter.Entry(formulario,bg="snow", font=("Calibri" ,14))
txt_Cmujer.place(x=1350, y=90)
#txt_valor1.pack(pady=10)



#cOL1 F3
lbl_idPropietario=tkinter.Label(formulario, text="Cod Propietario", bg="LightSkyBlue1", font=("Calibri",14))
#lbl_valor1.pack(padx=10)
lbl_idPropietario.place(x=10, y=130)
txt_idPropietario=tkinter.Entry(formulario,bg="snow", font=("Calibri" ,14))
txt_idPropietario.place(x=150, y=130)
#txt_valor1.pack(pady=10)

#cOL2 F3
lbl_nombrePropietario=tkinter.Label(formulario, text="Propietario      ", bg="LightSkyBlue1", font=("Calibri",14))
#lbl_valor1.pack(padx=10)
lbl_nombrePropietario.place(x=400, y=130)
txt_nombrePropietario=tkinter.Entry(formulario,bg="snow", font=("Calibri" ,14))
txt_nombrePropietario.place(x=540, y=130)
#txt_valor1.pack(pady=10)

#COL3 F3
lbl_telefonoPropietario=tkinter.Label(formulario, text="Tel Propietario   ", bg="LightSkyBlue1", font=("Calibri",14))
#lbl_valor1.pack(padx=10)
lbl_telefonoPropietario.place(x=800, y=130)
txt_telefonoPropietario=tkinter.Entry(formulario,bg="snow", font=("Calibri" ,14))
txt_telefonoPropietario.place(x=950, y=130)
#txt_valor1.pack(pady=10)



btn_guardar = tkinter.Button(formulario, text="Grabar en lista", bg="SpringGreen2",command=cargarDatos, width=50)
btn_guardar.place(x=1200, y=130)
#btn_promedio.pack(fill=tkinter.X, pady=8)





formulario.mainloop()