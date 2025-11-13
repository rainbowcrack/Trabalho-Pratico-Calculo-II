import os
import platform

# ============================================================
#  Cores ANSI
# ============================================================
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
WHITE = "\033[97m"

# ============================================================
#  ASCII LOGO - FRAJOLAMATH 
# ============================================================
LOGO = f"""{MAGENTA}
                                                                             ____                                   
    ,---,.                                       ,--,                      ,'  , `.               ___     ,---,     
  ,'  .' |                                     ,--.'|                   ,-+-,.' _ |             ,--.'|_ ,--.' |     
,---.'   |  __  ,-.                .--.  ,---. |  | :                ,-+-. ;   , ||             |  | :,'|  |  :     
|   |   .',' ,'/ /|              .--,`| '   ,'\:  : '               ,--.'|'   |  ;|             :  : ' ::  :  :     
:   :  :  '  | |' | ,--.--.      |  |. /   /   |  ' |     ,--.--.  |   |  ,', |  ':  ,--.--.  .;__,'  / :  |  |,--. 
:   |  |-,|  |   ,'/       \\     '--`_.   ; ,. :'  | |    /       \\ |   | /  | |  || /       \\ |  |   |  |  :  '   | 
|   :  ;/|'  :  / .--.  .-. |    ,--,'|'   | |: :|  | :   .--.  .-. |'   | :  | :  |,.--.  .-. |:__,'| :  |  |   /' : 
|   |   .'|  | '   \\__\\/ : . .    |  | '   | .; :'  : |__  \\__\\/ : . .;   . |  ; |--'  \\__\\/ : . .  '  : |__'  :  | | | 
'   :  '  ;  : |   ," .--.; |    :  | |   :    |  | '.'| ," .--.; ||   : |  | ,     ," .--.; |  |  | '.'|  |  ' | : 
|   |  |  |  , ;  /  /  ,.  |  __|  : '\\   \\  /;  :    ;/  /  ,.  ||   : '  |/     /  /  ,.  |  ;  :    ;|  :  :_:,' 
|   :  \\   ---'  ;  :   .'   \\.'__/\_: | `----' |  ,   /;  :   .'   \\;   | |`-'     ;  :   .'   \\ |  ,   /|  | ,'     
|   | ,'         |  ,     .-./   :    :         ---`-' |  ,     .-./   ;/         |  ,     .-./  ---`-' `--''       
`----'            `--`---'    \\   \\  /                  `--`---'   '---'           `--`---'                         
                               `--`-'                                                                               
{RESET}"""

# ============================================================
#  ASCII FRAJOLA 
# ============================================================
FRAJOLA = f"""{CYAN}
                / ,            
          /\\  \\|/  /\\         
          |\\\\_;=._//|         
           \\."   "./          
           //^\\ /^\\\\          
    .'``",/ |0| |0| \\,"``'.   
   /   ,  `'\\.---./'`  ,   \\  
  /`  /`\\,."(     )".,/`\\  `\\ 
  /`     ( '.'-.-'.' )     `\\ 
  /"`     "._  :  _."     `"\ 
   `/.'`"=.,_``=``_,.="`'.\\`  
             )   (             
{RESET}"""

# ============================================================
#  Cabeçalho principal
# ============================================================
def cabecalho():
    os.system("cls" if platform.system() == "Windows" else "clear")
    print(LOGO)
    print(FRAJOLA)
    print(f"{BOLD}{YELLOW}{'='*70}{RESET}")
    print(f"{BOLD}{CYAN}🐾 FRAJOLAMATH - INTEGRADOR FRAÇÕES PARCIAIS{RESET}")
    print(f"{BOLD}{YELLOW}{'='*70}{RESET}")

# ============================================================
#  Menu principal
# ============================================================
def menu():
    cabecalho()
    print(f"\n{CYAN}Integrantes: Any Gabriela, Guilherme Pinheiro, Izabel Chaves, Matheus Rossi e Rafael Colares")
    print(f"{YELLOW}Cálculo II - Trabalho Prático, Prof.a: Claudia Tavares\n")
    print(f"{BOLD}{MAGENTA}Escolha o tipo de integral (caso):{RESET}\n")
    print(f"{GREEN}[1]{RESET} Caso 1 → ∫ (A*x + B) / ((x - x1)*(x - x2)) dx")
    print(f"{GREEN}[2]{RESET} Caso 2 → ∫ (A*x + B) / (a*x² + b*x + c) dx")
    print(f"{GREEN}[3]{RESET} Caso 3 → ∫ (A*x + B) / ((x² + x1)*(x² + x2)) dx")
    print(f"{GREEN}[4]{RESET} Caso 4 → ∫ (A*x² + B*x + C) / ((x - a)*(x² + b)) dx")
    print(f"{RED}[0]{RESET} Sair")
    print(f"{CYAN}{'='*70}{RESET}")
    escolha = input(f"{BOLD}Digite o número do caso desejado:{RESET} ")
    return escolha.strip()

# ============================================================
#  Execução dos casos
# ============================================================
def executar_caso(escolha):
    pasta = f"caso{escolha}"
    arquivo = f"integrar-{escolha}.py"
    caminho = os.path.join(pasta, arquivo)

    if not os.path.exists(caminho):
        print(f"\n{RED}Arquivo '{caminho}' não encontrado.{RESET}")
        return

    print(f"\n{BOLD}{YELLOW}{'='*70}{RESET}")
    print(f"{BOLD}{MAGENTA}EXECUTANDO CASO {escolha}:{RESET} {arquivo}")
    print(f"{YELLOW}{'='*70}{RESET}")

    comando = f"python \"{caminho}\"" if platform.system() == "Windows" else f"python3 \"{caminho}\""
    os.system(comando)

# ============================================================
#  Programa principal
# ============================================================
if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "0":
            print(f"\n{GREEN}Encerrando o FrajolaMath... Até logo!{RESET}\n")
            break
        elif opcao in {"1", "2", "3", "4"}:
            executar_caso(opcao)
            input(f"\n{CYAN}Pressione ENTER para voltar ao menu principal...{RESET}")
        else:
            print(f"\n{RED}Opção inválida. Tente novamente.{RESET}\n")
