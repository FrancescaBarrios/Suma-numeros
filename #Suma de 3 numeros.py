#Suma de 3 numeros 
import tkinter as tk

def suma():
    try:
        num1 = int(caja1.get())
        num2 = int(caja2.get())
        num3 = int(caja3.get())
        resultado = num1 + num2 + num3
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, ingrese números válidos.")
    
ventana= tk.Tk()
ventana.geometry("600x300") #izq para ancho y der para alto
ventana.title("Suma de 3 números")


etiqueta1=tk.Label(ventana, text="Ingrese el primer número:",font=("Arial", 14))
etiqueta1.grid(row=0, column=0, columnspan=2)
caja1=tk.Entry(ventana,font=("Arial", 14), bg="white", justify="center") 
caja1.grid(row=0, column=3, padx=10, pady=10, sticky="ew")


etiqueta2=tk.Label(ventana, text="Ingrese el segundo número:",font=("Arial", 14))
caja2=tk.Entry(ventana, font=("Arial", 14), bg="white", justify="center")
etiqueta2.grid(row=1, column=0, columnspan=2)
caja2.grid(row=1, column=3, padx=10, pady=10, sticky="ew")


etiqueta3=tk.Label(ventana, text="Ingrese el tercer número:",font=("Arial", 14) )
caja3=tk.Entry(ventana, font=("Arial", 14), bg="white",justify="center") 
etiqueta3.grid(row=2, column=0, columnspan=2)
caja3.grid(row=2, column=3, padx=10, pady=10, sticky="ew")

bonton1=tk.Button(ventana, text="Sumar", command=suma, font=("Arial", 14), bg="purple", fg="white")
bonton1.grid(row=5, column=2)

label_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 16))
label_resultado.grid(row=8, column=1) 

def limpiar():
    caja1.delete(0, tk.END)
    caja2.delete(0, tk.END)
    caja3.delete(0, tk.END)
    label_resultado.config(text="Resultado: ")

bonton2=tk.Button(ventana, text="limpiar", command= limpiar,  font=("Arial", 14), bg="red", fg="white")
bonton2.grid(row=5, column=3)

ventana.mainloop()