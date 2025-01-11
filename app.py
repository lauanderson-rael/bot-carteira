'''
1 - Entrar no site "https://pesqbrasil-pescadorprofissional.agro.gov.br/" e clicar no botão de login
2 - Clicar no campo CPF, digitar CPF e clicar no botão "continuar"
3 - Digitar a senha  e clicar no botão "entrar"
4 - Clicar no botão "Pescador Profissional" , clicar no botão "opcoes", clicar em "Imprimir Carteira"
5 - clicar no botão de download de PDF
'''

import pyautogui as py
import webbrowser
from time import sleep
from os import system
import random
py.PAUSE = 0.5

# AUTOMACAO
def baixar_carteira(cpf, senha, resolucao):
    # Abre o Google no navegador padrão
    url = "https://pesqbrasil-pescadorprofissional.agro.gov.br/"
    webbrowser.open(url)
    sleep(2)

    # Localiza o botão na tela e clica nele
    botao_entrar = py.locateOnScreen(f'{resolucao}/btn1.png', confidence=0.8)
    if botao_entrar:
        botao_entrar_centro = py.center(botao_entrar) # Obtém as coordenadas do centro do botão
        py.click(botao_entrar_centro)
        sleep(3)
    else:
        print("Botão de 'entrar' nao encontrado")

    #fechar pop-up de permissão de localização
    try:
        icone_localizacao = py.locateOnScreen(f'{resolucao}/icon-local.png', confidence=0.8)
        if icone_localizacao:
            py.press('tab')
            py.press('enter')
            sleep(1)
    except: #
        print("\nÍcone de localização não encontrado na tela. Proseguindo...\n")

    # Digita o CPF e clicar em "continuar"
    py.write(cpf)
    py.press('tab')
    py.press('enter')
    sleep(3)

    # Digita a senha e clicar em "entrar"
    py.write(senha)
    py.press('tab')
    py.press('enter')
    sleep(3)

    # Acessando a carteirinha
    botao_menu = py.locateOnScreen(f'{resolucao}/btn4-img-pesc.png', confidence=0.8)
    if botao_menu:
        botao_menu_centro = py.center(botao_menu)
        py.click(botao_menu_centro)
        sleep(2)
    else:
        print("Botão de 'menu' nao encontrado")

    botao_opcoes = py.locateOnScreen(f'{resolucao}/btn5-img-opcoes.png', confidence=0.8)
    if botao_opcoes:
        botao_opcoes_centro = py.center(botao_opcoes)
        py.click(botao_opcoes_centro)
        sleep(1)
    else:
        print("Botão de 'opcoes' nao encontrado")

    botao_imprimir = py.locateOnScreen(f'{resolucao}/btn6-imprimir-cart.png', confidence=0.8)
    if botao_imprimir:
        botao_imprimir_centro = py.center(botao_imprimir)
        py.click(botao_imprimir_centro)
        sleep(5)
    else:
        print("Botão de 'imprimir' nao encontrado")

    botao_download = py.locateOnScreen(f'{resolucao}/btn7-download.png', confidence=0.8)
    if botao_download:
        botao_download_centro = py.center(botao_download)
        py.click(botao_download_centro)
        sleep(3)

        comple1 = ''.join(str(random.randint(0, 9)) for _ in range(5))
        comple2 = ''.join(str(random.randint(1, 9)) for _ in range(5))
        py.write(f'carteira_profissional_{comple1}_{comple2}.pdf')
        py.press('enter')
        print("\nCarteira baixada com sucesso!\n")

    else:
        print("Botão de 'download' nao encontrado")


# --------- INTERFACE GRAFICA ------------
import customtkinter as tk

def buscar():
    system('cls')
    cpf = entry_cpf.get()
    senha = entry_senha.get()
    res = combobox.get()

    if cpf == "" and senha == "" and res == "":
        print("Por favor, preencha todos os campos e selecione uma RESOLUÇÃO!")
    elif cpf == "" or senha == "" or res == "":
        print("Ops, Alguns campos estao vazios! Tente novamente.")
    else:
        print(f"Resolução selecionada: {res}")
        print(f"CPF: {cpf}")
        print(f"SENHA: {senha}")
        baixar_carteira(cpf, senha, res)

def exit():
    app.destroy()

def on_select(event):
    selected = combobox.get()
    print(f"Você selecionou: {selected}")
    return selected


app = tk.CTk()
app.title("Bot | Buscador de RGP")
app.geometry("400x280")
app.geometry("400x320")
app.grid_columnconfigure(0, weight=1)

# titulo da interface
title_grid = tk.CTkLabel(app,text="Buscador de RGP",font=("Helvetica", 20, "bold"))
title_grid.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

# Criando o Label e campo cpf
label_cpf = tk.CTkLabel(app, text="CPF:")
label_cpf.grid(row=1, column=0, padx=20, pady=10, sticky="w")

entry_cpf= tk.CTkEntry(app, width=250)
entry_cpf.grid(row=1, column=1, padx=20, pady=10)

# Criando o Label e a caixa senha
label_senha = tk.CTkLabel(app, text="SENHA:")
label_senha.grid(row=2, column=0, padx=20, pady=10, sticky="w")

entry_senha = tk.CTkEntry(app, width=250, show="*")
entry_senha.grid(row=2, column=1, padx=20, pady=10)

#  menu de seleção de resolucao
label_menu = tk.CTkLabel(app, text="SELECIONE A RESOLUÇÃO DE TELA DO COMPUTADOR:")
label_menu.grid(row=3, column=0, columnspan=2, padx=20, pady=0)

opcoes = ["1366x768", "1920X1080"]
combobox = tk.CTkComboBox(app, values=opcoes, state="readonly")
combobox.grid(row=4, column=0, columnspan=2, padx=20, pady=0)
combobox.bind("<<ComboboxSelected>>", on_select)

# Criando o botão BUSCAR CARTEIRINHA
button = tk.CTkButton(app, text="BUSCAR CARTEIRINHA", command=buscar)
button.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

# botao sair
buttonExit = tk.CTkButton(app, text="SAIR", command=exit, fg_color="red", hover_color="darkred")
buttonExit.grid(row=6, column=0, columnspan=2, padx=20, pady=0)

app.mainloop()
# --------- FIM INTERFACE GRAFICA ------------
