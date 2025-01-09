'''
1 - Entrar no site "https://pesqbrasil-pescadorprofissional.agro.gov.br/" e clicar no botão de login
2 - Clicar no campo CPF, digitar CPF e clicar no botão "continuar"
3 - Digitar a senha  e clicar no botão "entrar"
4 - Clicar no botão "Pescador Profissional" , clicar no botão "opcoes", clicar em "Imprimir Carteira"
5 - clicar no botão de download de PDF
'''

# AUTOMACAO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    # Desativar o pop-up de permissão de localização
    'profile.default_content_setting_values.geolocation': 2,
    # Não pedir permissão para fazer download
    'download.prompt_for_download': False,
    # Local padrão para armazenar downloads
    'download.default_directory': r'D:\estudos e projetos\Python\automacao01\bot-download-files\relatorios',
    # Não pedir permissão para fazer múltiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,
})


def baixar_carteira(cpf, senha):
    #entrando no site e clicando em "entrar"
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://pesqbrasil-pescadorprofissional.agro.gov.br/')
    sleep(3)
    botao_entrar = driver.find_element(By.XPATH, "//button[@type='submit']")
    botao_entrar.click()
    sleep(3)

    # Digitando cpf e clicando em "continuar"
    campo_cpf = driver.find_element(By.XPATH, "//input[@id='accountId']")
    campo_cpf.send_keys(cpf)
    botao_continuar = driver.find_element(By.XPATH, "//button[@id='enter-account-id']")
    botao_continuar.click()
    sleep(5)

    # Digitando senha e clicando em "entrar"
    campo_senha = driver.find_element(By.XPATH, "//input[@id='password']")
    campo_senha.send_keys(senha)
    botao_entrar2 = driver.find_element(By.XPATH, "//button[@id='submit-button']")
    botao_entrar2.click()
    sleep(5)

    # Acessando a carteirinha
    botao_menu = driver.find_element(By.XPATH, "//img[@alt='menu pescador ativo']")
    botao_menu.click()
    sleep(2)
    botao_opcoes = driver.find_element(By.XPATH, "//button[@title='Opções']")
    botao_opcoes.click()
    sleep(1)
    botao_carteira = driver.find_element(By.XPATH, "//div[@class='styles_cardLabel__UWTR_' and text()='IMPRIMIR CARTEIRINHA']")
    botao_carteira.click()
    sleep(4)

    # Baixando carteira em PDF
    import pyautogui
    for i in range(3):
        pyautogui.hotkey('shift', 'tab')

    pyautogui.press('enter')
    pyautogui.write('carteira_profissional')
    pyautogui.press('enter')
    print("\nCarteira baixada com sucesso!\n")
    driver.quit()





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
