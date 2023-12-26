def operacoes():
    def soma(aux = 0):
        valor = str(input("Insira um valor: "))
        aux = aux + float(valor)
        novo_valor = str(input('Insira um valor: '))
        aux = aux + float(novo_valor)
        print(aux)
    def subtracao(aux = 0): 
        valor = float(input("Insira um valor: "))
        aux = aux + valor
        novo_valor = float(input("Insira um valor: "))
        aux = aux - novo_valor
        print(aux)
    def multiplicacao(aux = 0):
        valor = float(input('Insira um valor: '))
        aux = aux + valor
        novo_valor = float(input('Insira um valor: '))
        aux = aux * novo_valor
        print(aux)
    def divisao(aux = 0):
        dividendo = float(input('Insira o valor a ser dividido: '))
        aux = aux + dividendo
        divisor = float(input('Insira o divisor: '))
        if divisor != 0:
            aux = aux / divisor
            print(aux)
        else:
            print("Não é possível dividir por zero.")
    def potenciacao():
        base = float(input('Insira o valor da base: '))
        exp = float(input('Insira o valor do expoente: '))
        print(base**exp)
    def radiciacao():
        radicando = float(input('Insira o valor para o radicando: '))
        raiz = float(input("Insira o valor da raíz: "))
        print(radicando ** 1 / raiz)
    def fatorial(i = 1):
        fator = int(input("Insira um valor: "))
        while (i <= fator):
            resp = fator * fatorial(i)
            i = i + 1
        print(resp)
    def log():
        logaritmando = float(input("Insira o valor para o logaritmando: "))
        base = float(input("Insira a base: "))
        logaritmo = base/(1/logaritmando) 
        print(logaritmo)
    def ln(): 
        logaritmando = float(input("Insira o valor para o logaritmando: "))
        logaritmo = 2.71828/(1/logaritmando) 
        print(logaritmo)
    def porcentagem():
        valor = float(input("Insira um valor: "))
        porcentagem = valor/100
        print(porcentagem,"%")