import webbrowser
from time import sleep
import random
import pyautogui as py

# FUNÇÃO PARA O CÁLCULO DAS COORDENADAS RELATIVAS
def calcular_coordenada_relativa(x_percentual, y_percentual):
    largura_tela, altura_tela = py.size()
    x = largura_tela * x_percentual
    y = altura_tela * y_percentual
    return (x, y)

# AUTOMACAO

def baixar_carteira(cpf, senha):
    # Abre o Google no navegador padrão
    url = "https://pesqbrasil-pescadorprofissional.agro.gov.br/"
    webbrowser.open(url)
    sleep(2)

    # Localiza e clica no botão de login com coordenadas relativas
    botao_entrar_posicao = calcular_coordenada_relativa(0.5, 0.3)  # Ajuste percentual conforme necessário
    py.click(botao_entrar_posicao)
    print("Botão clicado com sucesso! indo para a tela de CPF")
    sleep(3)

    # Fecha pop-up de permissão de localização (se existir)
    try:
        icone_localizacao = py.locateOnScreen('icon-local.png', confidence=0.8)
        if icone_localizacao:
            py.press('tab')
            py.press('enter')
            sleep(1)
    except: #py.ImageNotFoundException
        print("Ícone de localização não encontrado na tela. Proseguindo..")

    # Digita o CPF e clica em "continuar"
    py.write(cpf)
    botao_continuar_posicao = calcular_coordenada_relativa(0.5, 0.45)  # Ajuste percentual conforme necessário
    py.click(botao_continuar_posicao)
    print("Botão clicado com sucesso! indo para a tela de SENHA")
    sleep(3)

    # Digita a senha e clica em "entrar"
    py.write(senha)
    botao_entrar2_posicao = calcular_coordenada_relativa(0.5, 0.55)  # Ajuste percentual conforme necessário
    py.click(botao_entrar2_posicao)
    print("Botão clicado com sucesso! indo para a tela de MENU")
    sleep(4)

    # Acessando a carteirinha
    botao_menu_posicao = calcular_coordenada_relativa(0.5, 0.7)  # Ajuste percentual conforme necessário
    py.click(botao_menu_posicao)
    print("Botão clicado com sucesso! indo para a tela de OPCOES")
    sleep(2)

    botao_opcoes_posicao = calcular_coordenada_relativa(0.5, 0.75)  # Ajuste percentual conforme necessário
    py.click(botao_opcoes_posicao)
    print("Botão clicado com sucesso! indo para a tela de OPCOES")
    sleep(1)

    botao_imprimir_posicao = calcular_coordenada_relativa(0.5, 0.8)  # Ajuste percentual conforme necessário
    py.click(botao_imprimir_posicao)
    print("Botão clicado com sucesso! indo para a tela de IMPRIMIR CARTEIRA")
    sleep(8)

    botao_download_posicao = calcular_coordenada_relativa(0.5, 0.85)  # Ajuste percentual conforme necessário
    py.click(botao_download_posicao)
    print("Botão de download clicado!")
    sleep(3)

    comple1 = ''.join(str(random.randint(0, 9)) for _ in range(5))
    comple2 = ''.join(str(random.randint(1, 9)) for _ in range(5))
    py.write(f'carteira_profissional_{comple1}_{comple2}.pdf')
    py.press('enter')
    print("\nCarteira baixada com sucesso!\n")

# --------- INTERFACE GRAFICA ------------

import customtkinter as ctk

def buscar():
    text_cpf = entry_1.get()
    text_senha = entry_2.get()
    print(f"cpf: {text_cpf}")
    print(f"senha: {text_senha}")
    baixar_carteira("60155025333", "Milka2024@")

def exit():
    app.destroy()

app = ctk.CTk()
app.title("Bot | Buscador de RGP")

app.geometry("400x260")
app.grid_columnconfigure(0, weight=1)

# Título da interface
title_grid = ctk.CTkLabel(app, text="Buscador de RGP", font=("Helvetica", 20, "bold"))
title_grid.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

# Criando o Label e caixa CPF
label_1 = ctk.CTkLabel(app, text="CPF:")
label_1.grid(row=1, column=0, padx=20, pady=10, sticky="w")

entry_1 = ctk.CTkEntry(app, width=250)
entry_1.grid(row=1, column=1, padx=20, pady=10)

# Criando o Label e a caixa senha
label_2 = ctk.CTkLabel(app, text="SENHA:")
label_2.grid(row=2, column=0, padx=20, pady=10, sticky="w")

entry_2 = ctk.CTkEntry(app, width=250, show="*")
entry_2.grid(row=2, column=1, padx=20, pady=10)

# Criando o botão que chama a função buscar quando pressionado
button = ctk.CTkButton(app, text="BUSCAR CARTEIRINHA", command=buscar)
button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

# Botão sair
buttonExit = ctk.CTkButton(app, text="SAIR", command=exit, fg_color="red", hover_color="darkred")
buttonExit.grid(row=5, column=0, columnspan=2, padx=20, pady=0)

app.mainloop()
# --------- FIM INTERFACE GRAFICA ------------
