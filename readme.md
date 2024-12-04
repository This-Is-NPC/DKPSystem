# Sistema de Controle de Distribuição de DKP

## Visão Geral

Este repositório contém um sistema baseado em Python para gerenciar e distribuir Pontos de Morte de Dragão (DKP) para uma guilda ou grupo de raid.

## Pré-requisitos

- Python 3.8+
- pip
- Suporte a ambiente virtual

## Instruções de Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/This-Is-NPC/DKPSystem.git
cd controle-distribuicao-dkp
```

### 2. Criar Ambiente Virtual

```bash
python -m venv venv
```

### 3. Ativar Ambiente Virtual

- No Windows:
```bash
.\venv\Scripts\activate
```

- No macOS/Linux:
```bash
source venv/bin/activate
```

### 4. Instalar Dependências

```bash
pip install -r requirements.txt
```
## Executando a Aplicação

```bash
python main.py
```

## Funcionalidades

- Logs históricos de pontos

## Observações

- Requer sessão ativa no Lootmanager
- Pyautogui usado para interação web
- Mouse/teclado podem ficar temporariamente inativos durante a execução do script

## Solução de Problemas

- Certifique-se de estar logado no Lootmanager antes de executar
- Verifique a conectividade com a internet
- Confirme as versões do Python e das dependências

## Contribuindo

1. Faça um fork do repositório
2. Crie sua branch de feature (`git checkout -b feature/NovoRecurso`)
3. Commit suas alterações (`git commit -m 'Adicionar NovoRecurso'`)
4. Envie para a branch (`git push origin feature/NovoRecurso`)
5. Abra um Pull Request