import tkinter as tk
from tkinter import messagebox

# Função Somar

def Somar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    soma = num1 + num2
    messagebox.showinfo("Resultado", f"Resultado da soma = {soma}")

def Subtrair():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    subtrair = num1 - num2
    messagebox.showinfo("Resultado", f"Resultado da soma = {subtrair}")

def Dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        dividir = num1 / num2
        messagebox.showinfo("Resultado", f"Resultado da soma = {dividir:.2f}")
    except:
        messagebox.showinfo("Erro", "Confira os números digitados")


def Multiplicar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    multiplicar = num1 * num2
    messagebox.showinfo("Resultado", f"Resultado da soma = {multiplicar}")


# Programa Principal
janela = tk.Tk()
janela.title("Calculos v.1.0")
janela.geometry("540x200")
janela.config(bg= "black")

label_num1 = tk.Label(janela, text="Digite o 1° número:", width=25, font=("Arial", 10, "bold"), fg="black", bg="gray")
label_num1.grid(column=0, row=0, padx=5, pady=5)
entry_num1 = tk.Entry(janela, width=29, font=("Arial", 10, "bold"), fg="black", bg="white")
entry_num1.grid(column=0, row=1, padx=5, pady=5)

label_num2 = tk.Label(janela, text="Digite o 2° número:", width=25, font=("Arial", 10, "bold"), fg="black", bg="gray")
label_num2.grid(column=1, row=0, padx=5, pady=5)
entry_num2 = tk.Entry(janela, width=29, font=("Arial", 10, "bold"), fg="black", bg="white")
entry_num2.grid(column=1, row=1, padx=5, pady=5)

button_adicao = tk.Button(janela, text="+", command= Somar, width=4, fg="white", bg="black")
button_adicao.grid(column=2, row=0, padx=5, pady=5)

button_subtrair = tk.Button(janela, text="-", command= Subtrair, width=4, fg="white", bg="black")
button_subtrair.grid(column=2, row=1, padx=5, pady=5)

button_dividir = tk.Button(janela, text="/", command= Dividir, width=4, fg="white", bg="black")
button_dividir.grid(column=4, row=0, padx=5, pady=5)

button_multiplicar = tk.Button(janela, text="*", command= Multiplicar, width=4, fg="white", bg="black")
button_multiplicar.grid(column=4, row=1, padx=5, pady=5)

janela.mainloop()
