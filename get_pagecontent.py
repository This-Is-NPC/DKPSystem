import pyautogui
import time
import pyperclip

def get_pagecontent():
    # Abre o navegador Edge sem usar um perfil específico
    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.typewrite('microsoft edge')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('alt', 'space')
    time.sleep(0.2)
    pyautogui.press('down', presses=5)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'l')

    # Acessa o site
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.typewrite('https://lootmanager.net/dashboard')
    pyautogui.press('enter')
    time.sleep(6)

    # Acessa o conteúdo da página
    pyautogui.hotkey('ctrl', 'shift', 'i')
    time.sleep(2)
    pyautogui.moveTo(1440, 130, duration=0.3)  # Move o mouse para a posição (x, y) 'duration' é o tempo em segundos para o movimento
    time.sleep(0.5)
    pyautogui.click(button='right')
    time.sleep(0.5)
    pyautogui.press('down', presses=3)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # Captura o conteúdo da área de transferência
    conteudo = pyperclip.paste()
    nome_arquivo = "page.html"

    # Fecha a página
    pyautogui.hotkey('ctrl', 'w')

    # Salva o conteúdo em um arquivo
    with open(f'pages/{nome_arquivo}', "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
