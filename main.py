import schedule
import time
from get_pagecontent import get_pagecontent

# Agende o script para rodar a cada 1 minuto
schedule.every(1).hour.do(get_pagecontent)

# Print só pra indicar que o código iniciou
print('Start')

# Mantém o programa rodando para verificar os agendamentos
while True:
    schedule.run_pending()
    time.sleep(1)
