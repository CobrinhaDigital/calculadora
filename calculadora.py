def selecionarOperacao(aux = 0):
    operacao = int(input("Digite o número relacionado à operação que deseja realizar: \n 1) Soma \n 2) Subtração \n 3) Multiplicação \n 4) Divisão \n 5) Potenciação \n 6) Raíz quadrada \n\n Resp => "))
    while (operacao <= 6):
        match operacao:
            case 1:
                soma()
            case 2:
                valor = float(input("Insira um valor: "))
                aux = aux + valor
                novo_valor = float(input("Insira um valor: "))
                aux = aux - novo_valor
                print(aux)
            case 3: 
                valor = float(input('Insira um valor: '))
                aux = aux + valor
                novo_valor = float(input('Insira um valor: '))
                aux = aux * novo_valor
                print(aux)
            case 4: 
                dividendo = float(input('Insira um valor: '))
                aux = aux + dividendo
                divisor = float(input('Insira um valor: '))
                if novo_valor != 0:
                    aux = aux / divisor
                    print(aux)
                else:
                    print("Não é possível dividir por zero.")
            case 5: 
                base = float(input('Insira um valor: '))
                exp = float(input('Insira o valor do expoente: '))
                print(base**exp)
            case 6: 
                radicando = float(input('Insira um valor: '))
                raiz = float(input("Insira o valor da raíz: "))
                print(radicando ** 1 / raiz)

    def soma(): 
        valor = str(input("Insira um valor: "))
        aux = aux + float(valor)
        novo_valor = str(input('Insira um valor: '))
        aux = aux + float(novo_valor)
        print(aux)

selecionarOperacao()