import tkinter as tk
from hash_table import HashTable

def insert_button_clicked():
    key = int(key_entry.get())
    value = value_entry.get()
    hash_table.insert(key, value)
    result_label.config(text="Inserido: Chave {} com Valor '{}'".format(key, value))

def search_button_clicked():
    key = int(search_key_entry.get())
    result = hash_table.search(key)
    result_label.config(text="Resultado da busca: {}".format(result))

# Cria a instância da tabela hash
hash_table = HashTable(10)

# Cria a janela principal
root = tk.Tk()
root.title("Tabela Hash com Tkinter")

# Cria elementos da interface
key_label = tk.Label(root, text="Chave:")
key_label.pack()
key_entry = tk.Entry(root)
key_entry.pack()

value_label = tk.Label(root, text="Valor:")
value_label.pack()
value_entry = tk.Entry(root)
value_entry.pack()

insert_button = tk.Button(root, text="Inserir", command=insert_button_clicked)
insert_button.pack()

search_key_label = tk.Label(root, text="Chave de Busca:")
search_key_label.pack()
search_key_entry = tk.Entry(root)
search_key_entry.pack()

search_button = tk.Button(root, text="Buscar", command=search_button_clicked)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
