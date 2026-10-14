from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# 1. Utilizar uma lista para armazenar os níveis ou as mensagens do reservatório
niveis_reservatorio = [
    {"nivel": "Nível 1", "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": "Nível 2", "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": "Nível 3", "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": "Nível 4", "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": "Nível 5", "situacao": "Muito alto (alerta)", "cor": Fore.BLUE}
]

# 2. Criar uma função responsável por definir a cor da mensagem conforme o nível informado
def exibir_alerta(item):
    """Exibe no terminal a situação atual com a cor correspondente."""
    print(f"{item['cor']}{item['nivel']} Situação: {item['situacao']}{Style.RESET_ALL}")

# Função principal de simulação
def simular_reservatorio():
    print("--- SIMULAÇÃO DE MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ---\n")
    
    # Simula a leitura dos níveis do reservatório percorrendo a lista
    for dados in niveis_reservatorio:
        exibir_alerta(dados)
        
    print("\n--- Fim da simulação. Estilo do terminal restaurado. ---")

if __name__ == "__main__":
    simular_reservatorio()