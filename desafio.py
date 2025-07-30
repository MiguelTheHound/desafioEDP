opcao = {
    "s": "solteiro",
    "c": "casado"
}

while True:
    escolha = input("Digite seu estado civil (s - solteiro / c - casado): ").lower()

    if escolha in opcao:
        estado_civil = opcao[escolha]
        if escolha == "s":
            valor = 350000
            print(f"Depósito : KZ {valor:.2f}\n")
            print(f"Estado civil: {estado_civil}")
        
        elif escolha == "c":
            familia = int(input("Digite o número de membros:"))
            valor = 350000
            if familia <= 3:
                valor = valor**2
                print(f"Depósito : KZ {valor:.2f}\n")
                print(f"Estado civil: {estado_civil}")
            
            elif familia >= 4:
                valor = float(valor**4)
                print(f"Depósito : KZ {valor:.2f}\n")
                print(f"Estado civil: {estado_civil}")


