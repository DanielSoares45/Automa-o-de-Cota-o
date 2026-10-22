import requests
import pyautogui
import time

# 1. Buscar dados da API de moedas
url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
response = requests.get(url)
dados = response.json()

dolar = dados['USDBRL']['bid']
euro = dados['EURBRL']['bid']

relatorio = f"""--- Relatorio de Cotacao ---
Dolar: R$ {dolar}
Euro: R$ {euro}
Automacao concluida com sucesso!"""

# 2. Automação de Interface (RPA)
print("A automação vai começar. Não mexa no mouse!")
time.sleep(3) # Tempo para você minimizar o VS Code, se quiser

# Abre o menu iniciar, digita notepad e aperta enter
pyautogui.press('win')
time.sleep(1)
pyautogui.write('notepad')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

# Digita o relatório no Bloco de Notas
pyautogui.write(relatorio, interval=0.05)