# Automação de Sistemas e Processos com Python

### Desafio:

# Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa.
# O seu trabalho, como analista, é enviar um e-mail para ele, assim que começar a trabalhar, com o total gasto, 
# a quantidade de produtos compradas e o preço médio dos produtos.

# E-mail do seu chefe: para o nosso exercício, coloque um e-mail seu como sendo o e-mail do seu chefe<br>
# Link de acesso ao sistema da empresa: https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema

# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado





import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.hotkey("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(5)


x, y = pyautogui.position()
print(f"Posição do Mouse  X: {x}, Y: {y}")
time.sleep(1)

pyautogui.click(x=629, y=392)
pyautogui.write("Samir Laoune")
pyautogui.press("tab")
pyautogui.write("senha")

x, y = pyautogui.position()
print(f"Posição do Mouse  X: {x}, Y: {y}")
time.sleep(1)

pyautogui.click(x= 629, y=537)
time.sleep(5)

x, y = pyautogui.position()
print(f"Posição do Mouse  X: {x}, Y: {y}")
time.sleep(5)

pyautogui.click(x= 493, y=474)
time.sleep(5)

x, y = pyautogui.position()
print(f"Posição do Mouse  X: {x}, Y: {y}")
time.sleep(5)

pyautogui.click(x= 555, y=427)



# importar a base de dados.

import pandas as pd

tabela = pd.read_csv(r"C:\Users\Samir\Downloads\Compras.csv", sep = ";")
print(tabela)

total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)

    
    # Enviar email

import pyperclip

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")
time.sleep(10)

x, y = pyautogui.position()
print(f"Posição do Mouse  X: {x}, Y: {y}")
time.sleep(5)

pyautogui.click(x=87, y=211)
pyautogui.write("samirsk8team45@gmail.com")   # email do destinatário.
time.sleep(3)
pyautogui.press("tab")

pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
time.sleep(3)

pyautogui.press("tab")

texto = f"""
Prezados,
Segue o relatório de compras:

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida, responder esse e-mail.
Att., Samir Laoune.
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")


# pyautogui.click - as posições do mouse vai depender da resolução da tela.
# base de dados está no primeiro link.
# time.sleep - usar conforme o tempo de resposta do carregamento da página.



