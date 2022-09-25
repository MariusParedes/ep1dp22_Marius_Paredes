from cProfile import label
import tkinter
from turtle import bgcolor, left

ventana = tkinter.Tk()
ventana.geometry("400x700")
ventana.title("Actividad 1 - Marius Paredes")
ventana.config(bg="sky blue")


lbl_titulo=tkinter.Label(ventana, text = "INGRESO DE VALORES", bg="dodger blue",font="Arial 12")
lbl_titulo.pack()

lbl_valor1 = tkinter.Label(ventana,text="Valor 1", bg="Skyblue3",font="Arial 12")
lbl_valor1.pack(fill=tkinter.X, pady=8)
txt_valor1 = tkinter.Entry(ventana, font="Arial 16")
txt_valor1.pack(fill=tkinter.X , padx=20)


lbl_valor2 = tkinter.Label(ventana,text="Valor 2", bg="Skyblue3",font="Arial 12")
lbl_valor2.pack(fill=tkinter.X, pady=8)
txt_valor2 = tkinter.Entry(ventana, font="Arial 16")
txt_valor2.pack(fill=tkinter.X , padx=20)


lbl_valor3 = tkinter.Label(ventana,text="Valor 3", bg="Skyblue3",font="Arial 12")
lbl_valor3.pack(fill=tkinter.X, pady=8)
txt_valor3 = tkinter.Entry(ventana, font="Arial 16")
txt_valor3.pack(fill=tkinter.X , padx=20)


lbl_valor4 = tkinter.Label(ventana,text="Valor 4", bg="Skyblue3",font="Arial 12")
lbl_valor4.pack(fill=tkinter.X, pady=8)
txt_valor4 = tkinter.Entry(ventana, font="Arial 16")
txt_valor4.pack(fill=tkinter.X , padx=20)


lbl_valor5 = tkinter.Label(ventana,text="Valor 5", bg="Skyblue3",font="Arial 12")
lbl_valor5.pack(fill=tkinter.X, pady=8)

txt_valor5 = tkinter.Entry(ventana, font="Arial 16")
txt_valor5.pack(fill=tkinter.X, padx=20)




def valores():
    v1 = float(txt_valor1.get())
    v2 = float(txt_valor2.get())
    v3 = float(txt_valor3.get())
    v4 = float(txt_valor4.get())
    v5 = float(txt_valor5.get())
    suma = v1+v2+v3+v4+v5
    promedio = suma /5
    lbl_resultado["text"]='El promedio es: ',promedio
    
    #Calculo del mayor
    if v1 > v2 and v1 > v3 and v1 > v4 and v1 > v5:
        lbl_mayor["text"]= "El mayor número ingresado es: ",v1
    if v2 > v1 and v2 > v3 and v2 > v4 and v2 > v5:
        lbl_mayor["text"]= "El mayor número ingresado es: ",v2
    if v3 > v2 and v3 > v1 and v3 > v4 and v3 > v5:
        lbl_mayor["text"]= "El mayor número ingresado es: ",v3
    if v4 > v2 and v4 > v3 and v4 > v1 and v4 > v5:
        lbl_mayor["text"]= "El mayor número ingresado es: ",v4
    if v5 > v2 and v5 > v3 and v5 > v4 and v5 > v1:
        lbl_mayor["text"]= "El mayor número ingresado es: ",v5
    if v1 == v2 or v1 == v3 or v1 == v4 or v1 == v5 or v2 == v3 or v2 == v4 or v2 == v5 or v3 == v4 or v3 == v5 or v4 == v5:
        lbl_mayor["text"]= "No se pudo establecer el mayor porque hay duplicados"

    #multiplo
    multiplo = v1*v5
    if suma > multiplo:
        lbl_comparacion["text"]= "La suma es mayor al multiplo"
    elif suma == multiplo:
        lbl_comparacion["text"]= "La suma es igual al multiplo"
    elif suma < multiplo:
        lbl_comparacion["text"]= "La suma es menor al multiplo"


btn_promedio = tkinter.Button(ventana, text="Calcular", command=valores, bg="SpringGreen2", font="ArialBlack 16", fg="White")
btn_promedio.pack(fill=tkinter.X, pady=20, padx=20)



#Zona de resultados

lbl_zonaresultados = tkinter.Label(ventana,text="Zona de resultados",bg="IndianRed1",font="Arial 12")
lbl_zonaresultados.pack(pady=20)


lbl_resultado=tkinter.Label(ventana, text="Promedio", bg="sky blue")
lbl_resultado.pack(fill=tkinter.X, pady=15)

lbl_mayor = tkinter.Label(ventana, text="Número Mayor", bg="sky blue")
lbl_mayor.pack(fill=tkinter.X,pady=15)

lbl_comparacion = tkinter.Label(ventana, text="Comparar si la suma es mayor igual o menor que el multiplo",bg="sky blue")
lbl_comparacion.pack(fill=tkinter.X,pady=15)





ventana.mainloop()