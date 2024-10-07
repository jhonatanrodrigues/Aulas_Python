import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

def Buscar():
    cep = entry_cep.get().strip()
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        
        if "erro" in dados:
            messagebox.showerror("Erro", "CEP não encontrado.")
        else:
            entry_lagradouro.delete(0,tk.END)
            entry_lagradouro.insert(0,dados['logradouro'])

            entry_bairro.delete(0,tk.END)
            entry_bairro.insert(0,dados['bairro'])

            entry_cidade.delete(0,tk.END)
            entry_cidade.insert(0,dados['localidade'])

            entry_estado.delete(0,tk.END)
            entry_estado.insert(0,dados['uf'])
            
    else:
        messagebox.showerror("Erro", "Erro na consulta ao ViaCEP.")
    
def imagem(url1, altura, largura):
    response = requests.get(url1)
    

    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img = img.resize((largura, altura), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)

        label_img.config(image=img_tk)
        label_img.image = img_tk
    else:
        print("Falha na imagem: ", response.status_code)

# Programa Principal
janela = tk.Tk()
janela.title("Correios v.1.0")
janela.geometry("600x250")
janela.config(bg= "black")


label_cep = tk.Label(janela, text="CEP", width=25, font=("Arial", 10, "bold"), fg="black", bg="gray")
label_cep.grid(column=0, row=0, padx=5, pady=5)

entry_cep = tk.Entry(janela, width=29, font=("Arial", 10, "bold"), fg="black", bg="white")
entry_cep.grid(column=1, row=0, padx=5, pady=5)

button_buscar = tk.Button(janela, text="Buscar", command= Buscar, width=4, fg="white", bg="black")
button_buscar.grid(column=3, row=0, padx=5, pady=5)


label_lagradouro = tk.Label(janela, text="Lagradouro", width=25, font=("Arial", 10, "bold"), fg="black", bg="gray")
label_lagradouro.grid(column=0, row=1, padx=5, pady=5)
entry_lagradouro = tk.Entry(janela, width=29, font=("Arial", 10, "bold"), fg="black", bg="white")
entry_lagradouro.grid(column=1, row=1, padx=5, pady=5)

label_bairro = tk.Label(janela, text="Bairro", width=25, font=("Arial", 10, "bold"), fg="black", bg="gray")
label_bairro.grid(column=0, row=2, padx=5, pady=5)
entry_bairro = tk.Entry(janela, width=29, font=("Arial", 10, "bold"), fg="black", bg="white")
entry_bairro.grid(column=1, row=2, padx=5, pady=5)

label_cidade = tk.Label(janela, text="Cidade", width=25, font=("Arial", 10, "bold"), fg="black", bg="gray")
label_cidade.grid(column=0, row=3, padx=5, pady=5)
entry_cidade = tk.Entry(janela, width=29, font=("Arial", 10, "bold"), fg="black", bg="white")
entry_cidade.grid(column=1, row=3, padx=5, pady=5)

label_estado = tk.Label(janela, text="Estado", width=25, font=("Arial", 10, "bold"), fg="black", bg="gray")
label_estado.grid(column=0, row=4, padx=5, pady=5)
entry_estado = tk.Entry(janela, width=29, font=("Arial", 10, "bold"), fg="black", bg="white")
entry_estado.grid(column=1, row=4, padx=5, pady=5)

label_img = tk.Label(janela)
label_img.grid(column=0, row=5, padx=5, pady=5)
url1= f"https://miro.medium.com/v2/resize:fit:1048/1*RpaJjaK0hdtXjgR4oDYgTQ.jpeg"
altura = 50
largura = 200

imagem(url1, altura, largura)

label_img = tk.Label(janela)
label_img.grid(column=1, row=5, padx=5, pady=5)
url1= f"https://miro.medium.com/v2/resize:fit:1048/1*RpaJjaK0hdtXjgR4oDYgTQ.jpeg"
altura = 50
largura = 200


imagem(url1, altura, largura)

janela.mainloop()