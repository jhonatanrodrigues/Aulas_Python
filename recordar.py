import tkinter as tk
from tkinter import messagebox
import BackRecordar as br

janela = tk.Tk()
janela.title('Recordar é Viver')
janela.geometry("500x300")

tamEntry = 55

label_nome = tk.Label(janela, text="Nome")
label_nome.grid(column=0, row=0, padx=10, pady=5)
entry_nome = tk.Entry(janela, width=tamEntry)
entry_nome.grid(column=1, row=0)

label_email = tk.Label(janela, text="E-mail")
label_email.grid(column=0, row=1, padx=10, pady=5)
entry_email = tk.Entry(janela, width=tamEntry)
entry_email.grid(column=1, row=1)

label_fone = tk.Label(janela, text="Telefone")
label_fone.grid(column=0, row=2, padx=10, pady=5)
entry_fone = tk.Entry(janela, width=tamEntry)
entry_fone.grid(column=1, row=2)

button_salvar = tk.Button(janela, text="Salvar", 
                          command=lambda: messagebox.showinfo("Salvo", br.save(entry_nome.get(),(entry_email.get()))))
button_salvar.grid(column=3, row=3, padx=5, pady=5)

janela.mainloop()