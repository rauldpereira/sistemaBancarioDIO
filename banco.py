menu = """

1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  match opcao:
    case "1":
      valor = float(input("Informe o valor do depósito: "))
      if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
      else:
        print("Valor Inválido.")

    case "2":
      print("Saque")
      valor = float(input("Informe o valor do saque: "))
      if valor > saldo:
        print("Saldo Insuficiente")
      elif valor > limite:
        print("Limite de saque excedido.")
      elif numero_saques >= LIMITE_SAQUES:
        print("Número máximo de saques excedido.")
      elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
      else:
        print("Valor de saque inválido.")

    case "3":
      print("Extrato:")
      print(extrato if extrato else "Não foram realizadas movimentações.")
      print("---------------------------------")
      print(f"\nSaldo: R$ {saldo:.2f}")

    case "4":
      print("Saindo...")
      break

    case _:
      print(
          "Operação Inválida, por favor selecione novamente a operação desejada"
      )
