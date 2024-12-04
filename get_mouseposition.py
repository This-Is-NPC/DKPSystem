import pyautogui
import time

try:
    while True:
        posicao_mouse = pyautogui.position()
        print(f"Posição do mouse: {posicao_mouse}", end="\r", flush=True)  # Atualiza na mesma linha
        time.sleep(0.1)  # Reduz a frequência da verificação
except KeyboardInterrupt:
    print("\nMonitoramento interrompido.")
