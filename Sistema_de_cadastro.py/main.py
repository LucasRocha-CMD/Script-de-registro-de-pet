import tkinter as tk
from tkinter import ttk, messagebox
from cachorro import Cachorro
from gato import Gato

animais = []

def cadastrar_animal():
    nome = entry_nome.get().strip()
    idade = entry_idade.get().strip()
    tipo = combo_tipo.get()
    porte_raca = entry_porte_raca.get().strip()

    if not nome:
        messagebox.showerror("Erro", "O nome não pode estar vazio.")
        return
    if not idade.isdigit():
        messagebox.showerror("Erro", "A idade deve ser um número.")
        return
    if tipo not in ["Cachorro", "Gato"]:
        messagebox.showerror("Erro", "Selecione um tipo válido de animal.")
        return
    if not porte_raca:
        messagebox.showerror("Erro", "O porte ou raça não pode estar vazio.")
        return

    idade = int(idade)

    if tipo == "Cachorro":
        animal = Cachorro(nome, idade, porte_raca)
    elif tipo == "Gato":
        animal = Gato(nome, idade, porte_raca)
    
    animais.append(animal)
    listar_animais()
    
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_porte_raca.delete(0, tk.END)

    messagebox.showinfo("Animal cadastrado com sucesso!")

def listar_animais():
    for widget in lista_frame.winfo_children():
        widget.destroy()
    for animal in animais:
        label = tk.Label(lista_frame, text=animal.mostrar(), anchor='w', padx=10, pady=2)
        label.pack(fill='x')

app = tk.Tk()
app.title("Sistema de Cadastro de Animais")

# Tabs
tab_control = ttk.Notebook(app)
tab_cadastro = ttk.Frame(tab_control)
tab_lista = ttk.Frame(tab_control)
tab_control.add(tab_cadastro, text="Cadastro")
tab_control.add(tab_lista, text="Lista de Animais")
tab_control.pack(expand=1, fill="both")

# Cadastro Tab
tk.Label(tab_cadastro, text="Nome:").pack(pady=2)
entry_nome = tk.Entry(tab_cadastro)
entry_nome.pack(pady=2, fill='x')

tk.Label(tab_cadastro, text="Idade:").pack(pady=2)
entry_idade = tk.Entry(tab_cadastro)
entry_idade.pack(pady=2, fill='x')

tk.Label(tab_cadastro, text="Tipo:").pack(pady=2)
combo_tipo = ttk.Combobox(tab_cadastro, values=["Cachorro", "Gato"])
combo_tipo.pack(pady=2, fill='x')

tk.Label(tab_cadastro, text="Porte (para Cachorro) ou Raça (para Gato):").pack(pady=2)
entry_porte_raca = tk.Entry(tab_cadastro)
entry_porte_raca.pack(pady=2, fill='x')

btn_cadastrar = tk.Button(tab_cadastro, text="Cadastrar", command=cadastrar_animal)
btn_cadastrar.pack(pady=10)

# Lista Tab
lista_frame = tk.Frame(tab_lista)
lista_frame.pack(fill="both", expand=True)

listar_animais()

app.mainloop()
