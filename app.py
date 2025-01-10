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

# AUTOMACAO

def baixar_carteira(cpf, senha):
    # Abre o Google no navegador padrão
    url = "https://pesqbrasil-pescadorprofissional.agro.gov.br/"
    webbrowser.open(url)
    sleep(2)

    # Localiza o botão na tela e clica nele
    botao_entrar = py.locateOnScreen('btn1.png', confidence=0.8)
    if botao_entrar:
        botao_entrar_centro = py.center(botao_entrar) # Obtém as coordenadas do centro do botão
        py.click(botao_entrar_centro)
        print("Botão clicado com sucesso! indo para a tela de CPF")
        sleep(3)

    #fechar pop-up de permissão de localização (se existir)
    try:
        icone_localizacao = py.locateOnScreen('icon-local.png', confidence=0.8)
        if icone_localizacao:
            py.press('tab')
            py.press('enter')
            sleep(1)
    except py.ImageNotFoundException:
        print("Ícone de localização não encontrado na tela. Proseguindo..")

    # Digita o CPF e clicar em "continuar"
    py.write(cpf)
    botao_continuar = py.locateOnScreen('btn2.png', confidence=0.8)
    if botao_continuar:
        botao_continuar_centro = py.center(botao_continuar)
        py.click(botao_continuar_centro)
        print("Botão clicado com sucesso! indo para a tela de SENHA")
        sleep(3)

    # Digita a senha e clicar em "entrar"
    py.write(senha)
    botao_entrar2 = py.locateOnScreen('btn3.png', confidence=0.8)
    if botao_entrar2:
        botao_entrar2_centro = py.center(botao_entrar2)
        py.click(botao_entrar2_centro)
        print("Botão clicado com sucesso! indo para a tela de MENU")
        sleep(4)

    # Acessando a carteirinha
    botao_menu = py.locateOnScreen('btn4-img-pesc.png', confidence=0.8)
    if botao_menu:
        botao_menu_centro = py.center(botao_menu)
        py.click(botao_menu_centro)
        print("Botão clicado com sucesso! indo para a tela de OPCOES")
        sleep(2)

    botao_opcoes = py.locateOnScreen('btn5-img-opcoes.png', confidence=0.8)
    if botao_opcoes:
        botao_opcoes_centro = py.center(botao_opcoes)
        py.click(botao_opcoes_centro)
        print("Botão clicado com sucesso! indo para a tela de OPCOES")
        sleep(1)

    botao_imprimir = py.locateOnScreen('btn6-imprimir-cart.png', confidence=0.8)
    if botao_imprimir:
        botao_imprimir_centro = py.center(botao_imprimir)
        py.click(botao_imprimir_centro)
        print("Botão clicado com sucesso! indo para a tela de IMPRIMIR CARTEIRA")
        sleep(3)

    botao_download = py.locateOnScreen('btn7-download.png', confidence=0.8)
    if botao_download:
        botao_download_centro = py.center(botao_download)
        py.click(botao_download_centro)
        print("Botão de dowload clicado!")
        sleep(3)

        py.write('carteira_profissional.pdf')
        py.press('enter')
        print("\nCarteira baixada com sucesso!\n")


# --------- INTERFACE GRAFICA ------------
import customtkinter as ctk

def buscar():
    text_cpf = entry_1.get()
    text_senha = entry_2.get()
    print(f"cpf: {text_cpf}")
    print(f"senha: {text_senha}")
    baixar_carteira(text_cpf, text_senha)

def exit():
    app.destroy()

app = ctk.CTk()
app.title("Bot | Buscador de RGP")

app.geometry("400x260")
app.grid_columnconfigure(0, weight=1)

# titulo da interface
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

entry_2 = ctk.CTkEntry(app, width=250, show="*")
entry_2.grid(row=2, column=1, padx=20, pady=10)

# Criando o botão que chama a função burcar quando pressionado
button = ctk.CTkButton(app, text="BUSCAR CARTEIRINHA", command=buscar)
button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

# botao sair
buttonExit = ctk.CTkButton(app, text="SAIR", command=exit, fg_color="red", hover_color="darkred")
buttonExit.grid(row=5, column=0, columnspan=2, padx=20, pady=0)

app.mainloop()
# --------- FIM INTERFACE GRAFICA ------------
