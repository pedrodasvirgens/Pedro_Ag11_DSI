# Auxiliador de controle de nível de água.


from colorama import Fore, Style, init

init(autoreset=True)

from colorama import Fore, Style, init

init(autoreset=True)

# Lista com os níveis de água do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for nivel in range(1, len(niveis) + 1):
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]

    print(cor + mensagem + Style.RESET_ALL)