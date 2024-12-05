import os
import re
import pandas as pd
import streamlit as st
from datetime import datetime
import plotly.express as px
from bs4 import BeautifulSoup

def extract_dkp_from_html(file_path):
    """
    Extrai o valor de DKP de um arquivo HTML usando a classe específica do MUI
    
    Args:
        file_path (str): Caminho do arquivo HTML
    
    Returns:
        float: Valor de DKP extraído
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            
            # Encontrar a tabela com a classe específica
            table = soup.find('table', class_='MuiTable-root css-14vjxg0')
            
            if table:
                # Encontrar todas as linhas da tabela
                rows = table.find_all('tr')
                
                # Pular o cabeçalho e processar linhas de dados
                for row in rows[1:]:
                    # Extrair colunas
                    columns = row.find_all('td')
                    if len(columns) >= 5:
                        dkp_value = columns[4].get_text(strip=True)
                        return float(dkp_value.replace(',', '.'))
            
            return None
    
    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")
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

def process_html_files(directory):
    """
    Processa todos os arquivos HTML em um diretório
    
    Args:
        directory (str): Diretório contendo os arquivos HTML
    
    Returns:
        pd.DataFrame: DataFrame com dados processados
    """
    data = []
    
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            
            # Extrair DKP
            dkp_value = extract_dkp_from_html(filepath)
            
            # Extrair datetime do nome do arquivo
            file_datetime = parse_filename_datetime(filename)
            
            if dkp_value is not None and file_datetime is not None:
                data.append({
                    'datetime': file_datetime,
                    'dkp': dkp_value
                })
    
    return pd.DataFrame(data)

def main():
    st.title('Análise de DKP')
    
    # Seleção de diretório
    directory = st.text_input('C:\Projects\DKPSystem\pages')
    
    if directory and os.path.exists(directory):
        # Processar arquivos
        df = process_html_files(directory)
        
        if not df.empty:
            # Gráfico do Plotly
            fig = px.line(
                df.sort_values('datetime'), 
                x='datetime', 
                y='dkp', 
                title='Evolução do DKP ao Longo do Tempo',
                labels={'datetime': 'Data', 'dkp': 'DKP'}
            )
            
            st.plotly_chart(fig)
            
            # Tabela com dados
            st.dataframe(df)
        else:
            st.warning('Nenhum dado de DKP encontrado nos arquivos.')
    else:
        st.error('Diretório inválido')

if __name__ == '__main__':
    main()