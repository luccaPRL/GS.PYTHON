
############# Professor esse codigo retrata a tela que tem na nossa panela, no codigo pode ver o nivel de bateria, modos de preparos e colocar um timer

# Todas as Variaveis
nivel_bateria = 100 
timer = 0 
modos = ["Fritar", "Cozinhar a Vapor", "Assar"]  
modo_selecionado = None 

# funcao para ver o quanto há de bateria
def verificar_bateria():
    print(f"\nNível de Bateria: {nivel_bateria}%")  

# funcao de configurar timer 
def configurar_timer():
    global timer
    entrada_valida = False
    while not entrada_valida:
        tempo_input = input("Defina o tempo de preparo (em minutos, máximo 99): ")
        if tempo_input.isdigit() and 0 < int(tempo_input) <= 99:
            timer = int(tempo_input)
            print(f"Timer configurado para {timer} minutos.")
            entrada_valida = True
        else:
            print("Por favor, insira um número válido entre 1 e 99.")

# funcao para selecionar o modo de preparo
def selecionar_modo():
    global modo_selecionado
    modo_selecionado = None
    while not modo_selecionado:
        print("\nModos disponíveis:")
        for i, modo in enumerate(modos, 1):
            print(f"{i}. {modo}")
        escolha = input("Escolha um modo de preparo (1, 2 ou 3): ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(modos):
            modo_selecionado = modos[int(escolha) - 1]
            print(f"Modo selecionado: {modo_selecionado}")
        else:
            print("Opção inválida. Tente novamente.")

# funcao que faz funcionar o "painel"
def começar():
    executando = True
    while executando:
        print("\n--- Painel SolarCooker ---")
        print("1. Verificar Nível de Bateria")
        print("2. Configurar Timer")
        print("3. Selecionar Modo de Preparo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            verificar_bateria()
        elif opcao == "2":
            configurar_timer()
        elif opcao == "3":
            selecionar_modo()
        elif opcao == "4":
            print("Encerrando o programa. Até mais!")
            executando = False
        else:
            print("Opção inválida. Tente novamente.")

# fazer o painel rodar
começar()