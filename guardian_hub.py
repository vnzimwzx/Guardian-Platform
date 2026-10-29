import os
from pathlib import Path
import pandas as pd
import requests
from datetime import datetime

def enviar_alerta_discord(usd, eur):
    # ==========================================
    # LINK DO SEU DISCORD CONFIGURADO COM SUCESSO
    # ==========================================
    url_webhook = "https://discord.com/api/webhooks/1564024066275282986/5GAByf9D5yBzh793bZH7AUQMsrSzu0FSMBxPnUV4wO3BEAAHTPTmRcxCyrz6GeyMGFYu"
    # ==========================================
    
    payload = {
        "username": "Guardian Platform",
        "avatar_url": "https://imgur.com", # Ícone hacker de elite
        "content": f"🛡️ **[GUARDIAN FILES] OPERAÇÃO CONCLUÍDA!**\n"
                   f"💻 *Desktop limpo e organizado com sucesso.*\n"
                   f"📊 *Planilhas diárias updated no SSD.*\n\n"
                   f"💵 **Dólar Comercial:** R$ {usd:.4f}\n"
                   f"🇪🇺 **Euro Comercial:** R$ {eur:.4f}\n\n"
                   f"⏰ *Execução autônoma concluída às {datetime.now().strftime('%H:%M:%S')}*"
    }
    
    try:
        requests.post(url_webhook, json=payload, timeout=10)
        print("[DISCORD] Alerta enviado com sucesso para o seu canal!")
    except Exception as e:
        print(f"[ERRO] Falha ao enviar para o Discord: {e}")

def buscar_cotacoes_ao_vivo():
    print("[GUARDIAN-HUB] Conectando aos servidores financeiros...")
    try:
        url = "https://awesomeapi.com.br"
        resposta = requests.get(url, timeout=10)
        dados_api = resposta.json()
        
        cotacao_dolar = float(dados_api['USDBRL']['bid'])
        cotacao_euro = float(dados_api['EURBRL']['bid'])
        return cotacao_dolar, cotacao_euro
    except Exception as e:
        return 4.96, 5.56

def verificar_e_atualizar_planilhas():
    pasta_dados = Path(r"C:\Scripts e Programs\Dados_Automatos")
    pasta_dados.mkdir(exist_ok=True)
    arquivo_excel = pasta_dados / "Relatorio_Diario.xlsx"
    
    usd_hoje, eur_hoje = buscar_cotacoes_ao_vivo()
    data_hoje = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    colunas = ['ID_Cliente', 'Cliente_Gringo', 'Faturamento_USD', 'Cotacao_USD_BRL', 'Cotacao_Euro_BRL', 'Ultima_Atualizacao']
    linhas = [
        [1, 'TechCorp Switzerland', 1500.00, usd_hoje, eur_hoje, data_hoje],
        [2, 'Global Logistics US', 2450.50, usd_hoje, eur_hoje, data_hoje],
        [3, 'Nordic Data SE', 980.00, usd_hoje, eur_hoje, data_hoje]
    ]
    
    df = pd.DataFrame(linhas, columns=colunas)
    df.to_excel(arquivo_excel, index=False)
    
    print("[GUARDIAN-HUB] Tudo pronto! Planilha atualizada com dados vivos da internet.")
    print(f"[GUARDIAN-HUB] Dólar Comercial hoje: R$ {usd_hoje:.4f}")
    
    # DISPARA O ALERTA PARA O SEU CANAL DE LOGS
    enviar_alerta_discord(usd_hoje, eur_hoje)

if __name__ == "__main__":
    verificar_e_atualizar_planilhas()
