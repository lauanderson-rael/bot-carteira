
### Modo headless - Selenium

Para executar o navegador no modo invisível, você deve configurar a opção de modo headless ao inicializar o driver. Aqui está um exemplo para ChromeDriver e FirefoxDriver:
-----------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

-- Configuração do Chrome no modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ativa o modo headless
chrome_options.add_argument("--disable-gpu")  # Necessário para Windows
chrome_options.add_argument("--window-size=1920,1080")  # Tamanho da janela virtual

-- Iniciar o driver
service = Service("caminho/para/chromedriver")  # Substitua pelo caminho do ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

-- Acessar um site
driver.get("https://www.google.com")
print(driver.title)

driver.quit()
-----------------

### Configurações para o Chrome
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    # Desativar o pop-up de permissão de localização
    'profile.default_content_setting_values.geolocation': 2,
})
