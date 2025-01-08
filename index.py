import customtkinter as ctk 

# --------- INTERFACE GRAFICA ------------
def buscar():
    text_1 = entry_1.get()  
    text_2 = entry_2.get()
    print(f"cpf: {text_1}")
    print(f"senha: {text_2}")
    
def exit():
    app.destroy()
     
# interface
app = ctk.CTk()
app.title("Bot | Buscador de RGP")

app.geometry("400x250")
app.grid_columnconfigure(0, weight=1)


# new

#titulo
title_grid = ctk.CTkLabel(app,text="Buscador de RGP",font=("Helvetica", 20, "bold"))
title_grid.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
# Criando o Label e caixa cpf
label_1 = ctk.CTkLabel(app, text="CPF:")
label_1.grid(row=1, column=0, padx=20, pady=10, sticky="w")

entry_1 = ctk.CTkEntry(app, width=250)
entry_1.grid(row=1, column=1, padx=20, pady=10)

# Criando o Label e a caixa senha
label_2 = ctk.CTkLabel(app, text="SENHA:")
label_2.grid(row=2, column=0, padx=20, pady=10, sticky="w")

entry_2 = ctk.CTkEntry(app, width=250)
entry_2.grid(row=2, column=1, padx=20, pady=10)

# Criando o botão que chama a função burcar quando pressionado
button = ctk.CTkButton(app, text="BUSCAR CARTEIRINHA", command=buscar)
button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)


# botoo sair
buttonExit = ctk.CTkButton(app, text="Exit", command=exit, fg_color="red")
buttonExit.grid(row=5, column=0, padx=20, pady=0,)

app.mainloop()
# --------- FIM INTERFACE GRAFICA ------------