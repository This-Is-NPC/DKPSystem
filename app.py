import io
import re
import pandas as pd
import streamlit as st
from datetime import datetime
import plotly.express as px
from bs4 import BeautifulSoup

def extract_dkp_info_from_html_bytes(file_bytes):
    """
    Extrai o valor de DKP e nome do player de um arquivo HTML em bytes
    
    Args:
        file_bytes (bytes): Conteúdo do arquivo HTML
    
    Returns:
        tuple: (nome do player, valor de DKP) ou None
    """
    try:
        soup = BeautifulSoup(file_bytes, 'html.parser')
        
        # Encontrar a tabela com a classe específica
        table = soup.find('table', class_='MuiTable-root css-14vjxg0')
        
        if table:
            # Encontrar todas as linhas da tabela
            rows = table.find_all('tr')
            
            player_dkp_data = []
            # Pular o cabeçalho e processar linhas de dados
            for row in rows[1:]:
                # Extrair colunas
                columns = row.find_all('td')
                if len(columns) >= 5:
                    player_name = columns[1].get_text(strip=True)
                    dkp_value = columns[4].get_text(strip=True)
                    player_dkp_data.append((
                        player_name, 
                        float(dkp_value.replace(',', '.'))
                    ))
            
            return player_dkp_data
        
        return None
    
    except Exception as e:
        st.error(f"Erro ao processar arquivo: {e}")
        return None

def parse_filename_datetime(filename):
    """
    Extrai data e hora do nome do arquivo no formato table_dkp_dd_mm_yyyy_hh_mm_ss.html
    
    Args:
        filename (str): Nome do arquivo
    
    Returns:
        datetime: Data extraída do nome do arquivo
    """
    match = re.search(r'table_dkp_(\d{2})_(\d{2})_(\d{4})_(\d{2})_(\d{2})_(\d{2})\.html', filename)
    if match:
        day, month, year, hour, minute, second = map(int, match.groups())
        return datetime(year, month, day, hour, minute, second)
    return None

def process_html_files(uploaded_files):
    """
    Processa arquivos HTML carregados
    
    Args:
        uploaded_files (list): Lista de arquivos carregados
    
    Returns:
        pd.DataFrame: DataFrame com dados processados
    """
    data = []
    
    for uploaded_file in uploaded_files:
        # Extrair informações de DKP
        player_dkp_info = extract_dkp_info_from_html_bytes(uploaded_file.getvalue())
        
        # Extrair datetime do nome do arquivo
        file_datetime = parse_filename_datetime(uploaded_file.name)
        
        if player_dkp_info and file_datetime:
            for player_name, dkp_value in player_dkp_info:
                data.append({
                    'datetime': file_datetime,
                    'dkp': dkp_value,
                    'player_name': player_name,
                    'filename': uploaded_file.name
                })
    
    return pd.DataFrame(data)

def main():
    st.title('Análise de DKP por Player')
    
    # Upload de múltiplos arquivos HTML
    uploaded_files = st.file_uploader(
        "Escolha os arquivos HTML", 
        type=['html'], 
        accept_multiple_files=True
    )
    
    if uploaded_files:
        # Processar arquivos
        df = process_html_files(uploaded_files)
        
        if not df.empty:
            # Gráfico do Plotly agora usa player_name como color
            fig = px.line(
                df.sort_values('datetime'), 
                x='datetime', 
                y='dkp', 
                color='player_name',
                hover_data=['filename'],
                title='Evolução do DKP por Player',
                labels={'datetime': 'Data', 'dkp': 'DKP', 'player_name': 'Player'}
            )
            
            st.plotly_chart(fig)
            
            # Tabela com dados
            st.dataframe(df)
        else:
            st.warning('Nenhum dado de DKP encontrado nos arquivos.')

if __name__ == '__main__':
    main()