import tkinter as tk
import string
import random

letters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

def gerar_senha():
    password, pool = [], []
    size = int(size_entry.get())

    if var1 == 1:
        pool.append(letters)
    if var2:
        pool.append(digits)
    if var3:
        pool.append(symbols)

    for i in range(size):
        kind = random.choice((pool))
        password.append(random.choice(kind))

    password = ''.join(password)
    password_label = tk.Label(root, text=password, font=("Arial, 14"))
    password_label.grid(row=6, column=0, padx=5, columnspan=2)

root = tk.Tk()
root.title("Gerador de Senhas 1.0")
var1, var2, var3 = tk.IntVar(), tk.IntVar(), tk.IntVar()

text_label = tk.Label(root, text='Configure sua senha', font=("Arial, 14"))
text_label.grid(row=0, column=0, padx=5, columnspan=2)

letters_label = tk.Checkbutton(root, text='Letras',variable=var1, font=("Arial, 12"))
letters_label.grid(sticky="W", row=1, column=0, padx=5)

numbers_label = tk.Checkbutton(root, text='Números',variable=var2, font=("Arial, 12"))
numbers_label.grid(sticky="W",row=2, column=0, padx=5)

symbols_label = tk.Checkbutton(root, text='Símbolos',variable=var3, font=("Arial, 12"))
symbols_label.grid(sticky="W",row=3, column=0, padx=5)

size_label = tk.Label(root, text='Tamanho', font=("Arial, 12"))
size_label.grid(sticky="W",row=4, column=0)

def only_numbers(char):
    return char.isdigit()
validation = root.register(only_numbers)

size_entry = tk.Entry(root, font=("Arial, 12"), validate="key", validatecommand=(validation, '%S'))
size_entry.grid(sticky="W",row=4, column=1, padx=(0, 10))

my_button = tk.Button(root, text="Gerar senha", font=("Arial, 14"), bg= "green3", width = 10, command=lambda:gerar_senha())
my_button.grid(row=5, column=0, columnspan=3, pady=20)

root.mainloop()
