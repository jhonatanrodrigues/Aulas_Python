import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect('tarefas.db')
cursor = conexao.cursor()

# Cria a tabela se ela não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente TEXT,
                    tarefa TEXT,
                    data TEXT,
                    horario TEXT,
                    descricao TEXT,
                    valor REAL,
                    telefone TEXT,
                    email TEXT)''')
conexao.commit()

# Função para buscar tarefas no banco de dados
def buscar_tarefa(tarefa=""):
    cursor.execute("SELECT * FROM tarefas WHERE tarefa LIKE ?", ('%' + tarefa + '%',))
    return cursor.fetchall()

# Função para atualizar o grid com a lista de tarefas
def atualizar_lista(cliente=""):
    for row in tree.get_children():
        tree.delete(row)
    tarefas = buscar_tarefa(cliente)
    for tarefa in tarefas:
        tree.insert("", "end", values=tarefa)

# Função para adicionar uma tarefa ao banco de dados
def adicionar_tarefa():
    def salvar_tarefa():
        cliente = entry_cliente.get()
        tarefa = entry_tarefa.get()
        data = entry_data.get()
        horario = entry_horario.get()
        descricao = entry_descricao.get()
        valor = entry_valor.get()
        telefone = entry_telefone.get()
        email = entry_email.get()

        if cliente and tarefa and data and horario and descricao and valor and telefone and email:
            cursor.execute("INSERT INTO tarefas (cliente, tarefa, data, horario, descricao, valor, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                           (cliente, tarefa, data, horario, descricao, valor, telefone, email))
            conexao.commit()
            atualizar_lista()
            janela_add.destroy()
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

  # Janela para adicionar tarefa
    janela_add = tk.Toplevel(root)
    janela_add.title("Adicionar Tarefa")

# Campos de entrada
    tk.Label(janela_add, text="Cliente").grid(row=0, column=0)
    entry_cliente = tk.Entry(janela_add)
    entry_cliente.grid(row=0, column=1)

    tk.Label(janela_add, text="Tarefa").grid(row=1, column=0)
    entry_tarefa = tk.Entry(janela_add)
    entry_tarefa.grid(row=1, column=1)

    tk.Label(janela_add, text="Data").grid(row=2, column=0)
    entry_data = tk.Entry(janela_add)
    entry_data.grid(row=2, column=1)

    tk.Label(janela_add, text="Horario").grid(row=3, column=0)
    entry_horario = tk.Entry(janela_add)
    entry_horario.grid(row=3, column=1)

    tk.Label(janela_add, text="Descrição").grid(row=4, column=0)
    entry_descricao = tk.Entry(janela_add)
    entry_descricao.grid(row=4, column=1)

    tk.Label(janela_add, text="Valor").grid(row=5, column=0)
    entry_valor = tk.Entry(janela_add)
    entry_valor.grid(row=5, column=1)

    tk.Label(janela_add, text="Telefone").grid(row=6, column=0)
    entry_telefone = tk.Entry(janela_add)
    entry_telefone.grid(row=6, column=1)

    tk.Label(janela_add, text="Email").grid(row=7, column=0)
    entry_email = tk.Entry(janela_add)
    entry_email.grid(row=7, column=1)

    # Botão para salvar o funcionário
    btn_salvar = tk.Button(janela_add, text="Salvar", command=salvar_tarefa)
    btn_salvar.grid(row=8, columnspan=2)

# Função para deletar uma tarefa do banco de dados
def deletar_tarefa():
    item_selecionado = tree.selection()
    if item_selecionado:
        tarefa = tree.item(item_selecionado)['values']
        cursor.execute("DELETE FROM tarefas WHERE id=?", (tarefa[0],))
        conexao.commit()
        atualizar_lista()
    else:
        messagebox.showerror("Erro", "Selecione uma tarefa para deletar.")

# Função para alterar uma tarefa
def alterar_tarefa():
    item_selecionado = tree.selection()
    if item_selecionado:
        tare = tree.item(item_selecionado)['values']

        def salvar_alteracao():
            cliente = entry_cliente.get()
            tarefa = entry_tarefa.get()
            data = entry_data.get()
            horario = entry_horario.get()
            descricao = entry_descricao.get()
            valor = entry_valor.get()
            telefone = entry_telefone.get()
            email = entry_email.get()

            cursor.execute("UPDATE tarefas SET cliente=?, tarefa=?, data=?, horario=?, descricao=?, valor=?, telefone=?, email=? WHERE id=?", 
                           (cliente, tarefa, data, horario, descricao, valor, telefone, email, tare[0]))
            conexao.commit()
            atualizar_lista()
            janela_editar.destroy()

        # Janela para editar tarefas
        janela_editar = tk.Toplevel(root)
        janela_editar.title("Alterar tarefa")

        # Campos de entrada
        tk.Label(janela_editar, text="Cliente").grid(row=0, column=0)
        entry_cliente = tk.Entry(janela_editar)
        entry_cliente.insert(0, tare[1])
        entry_cliente.grid(row=0, column=1)

        tk.Label(janela_editar, text="Tarefa").grid(row=1, column=0)
        entry_tarefa = tk.Entry(janela_editar)
        entry_tarefa.insert(0, tare[2])
        entry_tarefa.grid(row=1, column=1)

        tk.Label(janela_editar, text="Data").grid(row=2, column=0)
        entry_data = tk.Entry(janela_editar)
        entry_data.insert(0, tare[3])
        entry_data.grid(row=2, column=1)

        tk.Label(janela_editar, text="Horario").grid(row=3, column=0)
        entry_horario = tk.Entry(janela_editar)
        entry_horario.insert(0, tare[4])
        entry_horario.grid(row=3, column=1)

        tk.Label(janela_editar, text="Descrição").grid(row=4, column=0)
        entry_descricao = tk.Entry(janela_editar)
        entry_descricao.insert(0, tare[5])
        entry_descricao.grid(row=4, column=1)

        tk.Label(janela_editar, text="Valor").grid(row=5, column=0)
        entry_valor = tk.Entry(janela_editar)
        entry_valor.insert(0, tare[6])
        entry_valor.grid(row=5, column=1)

        tk.Label(janela_editar, text="Telefone").grid(row=6, column=0)
        entry_telefone = tk.Entry(janela_editar)
        entry_telefone.insert(0, tare[7])
        entry_telefone.grid(row=6, column=1)

        tk.Label(janela_editar, text="Email").grid(row=7, column=0)
        entry_email = tk.Entry(janela_editar)
        entry_email.insert(0, tare[8])
        entry_email.grid(row=7, column=1)

        # Botão para salvar alterações
        btn_salvar = tk.Button(janela_editar, text="Salvar", command=salvar_alteracao)
        btn_salvar.grid(row=8, columnspan=2)
    else:
        messagebox.showerror("Erro", "Selecione um funcionário para alterar.")



# Interface gráfica com Tkinter
root = tk.Tk()
root.title("CRUD de Cadastro de Tarefas")

# Campo de pesquisa
tk.Label(root, text="Pesquisar por Tarefa:").grid(row=0, column=0, padx=10, pady=10)
entry_pesquisa = tk.Entry(root)
entry_pesquisa.grid(row=0, column=1, padx=10, pady=10)
entry_pesquisa.bind("<KeyRelease>", lambda event: atualizar_lista(entry_pesquisa.get()))

# Botões
btn_adicionar = tk.Button(root, text="Adicionar", command=adicionar_tarefa)
btn_adicionar.grid(row=0, column=2, padx=10, pady=10)

btn_alterar = tk.Button(root, text="Alterar", command=alterar_tarefa)
btn_alterar.grid(row=0, column=3, padx=10, pady=10)

btn_deletar = tk.Button(root, text="Deletar", command=deletar_tarefa)
btn_deletar.grid(row=0, column=4, padx=10, pady=10)

btn_concluido = tk.Button(root, text="Concluido")
btn_concluido.grid(row=0, column=5, padx=10, pady=10)

# Grid (Treeview) para exibir a lista de funcionários
tree = ttk.Treeview(root, columns=("ID", "Cliente", "Tarefa", "Data", "Horario", "Descrição", "Valor", "Telefone", "Email"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Cliente", text="Cliente")
tree.heading("Tarefa", text="Tarefa")
tree.heading("Data", text="Data")
tree.heading("Horario", text="Horario")
tree.heading("Descrição", text="Descrição")
tree.heading("Valor", text="Valor")
tree.heading("Telefone", text="Telefone")
tree.heading("Email", text="Email")
tree.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

# Atualiza o grid inicialmente
atualizar_lista()

# Executa a interface
root.mainloop()

# Fechar a conexão com o banco de dados ao encerrar o programa
conexao.close()