import os
import shutil
from pathlib import Path

# Destino fixo monitorado pelo robô
caminho_pasta = Path(r"C:\Users\Administrator\Desktop")

print("[ROBÓ] Iniciando a varredura avançada do Desktop, Antôny...")

# Lista de pastas que o próprio robô cria (para ele não tentar entrar nelas e criar um loop)
pastas_do_sistema = ['ZIP', 'PY', 'RAR', 'PNG', 'XLSX', 'PDF', 'TXT', 'DOCX', 'DADOS_AUTOMATOS']

# 1ª ETAPA: Varrer subpastas bagunçadas de clientes e trazer os arquivos para fora
for item in caminho_pasta.iterdir():
    if item.is_dir() and item.name.upper() not in pastas_do_sistema:
        print(f"[RECONHECIMENTO] Pasta de cliente encontrada: '{item.name}'. Sugando arquivos...")
        
        # Entra na pasta do cliente e move todos os arquivos para a Área de Trabalho principal
        for sub_item in item.rglob('*'):
            if sub_item.is_file():
                try:
                    # Se o arquivo já existir no Desktop, adiciona um contador para não sobrescrever
                    destino_temporario = caminho_pasta / sub_item.name
                    if destino_temporario.exists():
                        destino_temporario = caminho_pasta / f"cliente_{sub_item.stem}_{int(os.path.getmtime(sub_item))}{sub_item.suffix}"
                    
                    shutil.move(str(sub_item), str(destino_temporario))
                except Exception as e:
                    print(f"[AVISO] Erro ao extrair arquivo {sub_item.name}: {e}")
        
        # Após esvaziar a pasta do cliente, deleta a pasta vazia para limpar o Desktop
        try:
            shutil.rmtree(str(item))
            print(f"[SUCESSO] Pasta '{item.name}' limpa e removida.")
        except Exception as e:
            print(f"[AVISO] Não foi possível remover a pasta vazia '{item.name}': {e}")

# 2ª ETAPA: Passar o rodo geral e organizar todos os arquivos nas pastas maiúsculas
for arquivo in caminho_pasta.iterdir():
    if arquivo.is_file() and arquivo.suffix:
        nome_pasta = arquivo.suffix.replace('.', '').upper()
        pasta_destino = caminho_pasta / nome_pasta
        
        pasta_destino.mkdir(exist_ok=True)
        
        try:
            shutil.move(str(arquivo), str(pasta_destino / arquivo.name))
            print(f"Organizado: {arquivo.name} -> Pasta {nome_pasta}")
        except Exception as e:
            print(f"[ERRO] Não foi possível mover {arquivo.name}: {e}")

print("[ROBÓ] Varredura avançada concluída com sucesso!")
