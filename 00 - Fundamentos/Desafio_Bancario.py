menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_DIARIO_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_str_d = input("Digite o valor do depósito: ").strip().replace(',', '.')
        try:
          valor = float(valor_str_d)
          if valor > 0:
              saldo += valor
              extrato += f"+ Deposito: R$ {valor:.2f}\n"
          else:
            print("Operação Inválida. O valor deverá ser maior que zero.")
        except ValueError:
            print("Operação inválida. Por favor, digite um número válido.")

    elif opcao == "s":
        valor_str_s = input("Digite o valor do saque: ").strip().replace(',', '.')
        try:
            valor = float(valor_str_s)
            if valor <= 0:
                print("Operação Inválida. O valor deverá ser maior que zero.")
            else:
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = numero_saques >= LIMITE_DIARIO_SAQUES
                if excedeu_saldo:
                    print("Operação falhou! Você não tem saldo suficiente.")
                elif excedeu_limite:
                    print("Operação falhou! O valor do saque excede o limite.")
                elif excedeu_saques:
                    print("Operação falhou! Número máximo de saques excedido.")
                else:
                    saldo -= valor
                    extrato += f"- Saque: R$ {valor:.2f}\n"
                    numero_saques += 1
        except ValueError:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Tente novamente.")