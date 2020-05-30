import numpy as np
import sys

def somatorio(xn, wn):
    """
    Método responsável em realizar o somatorio da multiplicação
    da entrada com os pesos para então retornar.

    :param xn: Vetor de entradas
    :param wn: Vetor de pesos

    :return: O somatorio da multiplicação das entradas pelo pesos
    """
    if len(xn) != len(wn):
        print("A quantidade de entrada não bate")
        exit(0)
    return (xn * wn).sum()

def comparador(th, soma):
    """
    Método responsável em validar se o a soma está acima do limiar.

    :param th: Limiar de ativação do neurônio (Threshold)
    :param soma: Resultado do somatorio

    :return: 1 se a soma é maior/igual que o limiar, senão 0
    """
    return 1 if soma >= th else 0

def corrigir(x, w, n, t, o):
    """
    Método responsável pelo cálculo de correção dos pesos,
    fazendo com que os pesos convirja para o resultado ideal.

    :param x: Vetor de entradas
    :param w: Vetor de pesos
    :param n: Taxa de aprendizado
    :param t: Saída desejada
    :param o: Saída atual

    :return: Vetor dos novos pesos
    """
    dw = n*(t-o)*x
    wi = w+dw 
    print('dw =', dw)
    return wi

def main(filename="entradas", n=0.5, th=0.8, mit=500):
    """
    Método principal que recebe a entrada e os pesos iniciais,
    executa até chegar no resultado desejado ou no valor máximo
    de iterações.

    x           => Entradas
    w           => pesos
    saida       => Saídas desejadas
    saidaFinal  => Saídas atual
    mit         => Máximo de iterações
    it          => Quantidade de iterações
    n           => Taxa de aprendizado
    th          => Threshold (Limiar)

    :param filename: Nome do arquivo contendo os valores das entradas e saída
    :param n: Taxa de aprendizado
    :param th: Threshold (Limiar)
    :param mit: Máximo de iterações
    """

    # Tratamento de abertura do arquivo
    try:
        valores = np.loadtxt(filename, delimiter=',').T
    except:
        print(filename, "- Arquivo ou diretório não encontrado")
        exit(1)
    
    # Declaração de Variáveis
    x = valores[:-1]
    w = np.zeros(len(x))
    saida = valores[-1]
    saidaFinal = np.zeros(len(saida))
    it = 0

    while True:
        it += 1
        print(w)
        for i in range(x.shape[1]):
            som = round(somatorio(x[:,i],w),4)
            print('Somatorio =',som)
            o = comparador(th, som) 
            saidaFinal[i] = o
            if o != saida[i]:
                print("\nAjustando...")
                w = corrigir(x[:,i], w, n, saida[i], o).round(4)
                break
        if (saidaFinal == saida).all():
            print("\nResultado encontrado com sucesso!!!")
            print("\nw =",w)
            print("Saida =", saidaFinal)
            print("Iterações =", it)
            break
        elif it == mit:
            print("\nAtingido o número máximo de iterações!!!")
            print("Resultado não encontrado!!!")
            break


if __name__ == "__main__":
    help = """
    Uso: python3 perceptron.py ARQUIVO [OPÇÕES]

    Realiza a execução de uma rede neural perceptron a partir das
    entradas e saída escrito em um arquivo.

    O argumento do ARQUIVO é obrigatorio.

    Se OPÇÕES não for especificado é atribuido os valores padrão,
    que são:
        n   - Taxa de aprendizado = 0.5
        th  - Threshold (Limiar) = 0.8
        mit - Máximo de iterações = 500

    Argumentos OPÇÕES:
        -n FLOAT      seta a taxa de aprendizado
        -t FLOAT      seta o limiar (Threshold)
        -m INT        seta o máximo de iterações

    Exemplos:
        python3 perceptron.py entradas
        python3 perceptron.py entradas -n 0.5
        python3 perceptron.py entradas -t 0.8
        python3 perceptron.py entradas -m 500
        python3 perceptron.py entradas -n 0.5 -t 0.8 -m 500
    """

    n=0.5
    th=0.8
    mit=500

    try:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':       
            print(help)
            exit(0)
        else:
            filename = sys.argv[1]

        for i in range(2,len(sys.argv),2):
            if '-n' == sys.argv[i]:
                try:
                    n = float(sys.argv[i+1])
                except:
                    print(help)
                    print('ERROR! Valor incorreto ou vazio para o\
                    \nargumento -n (taxa de aprendizado)')
                    exit(1)
            elif '-t' == sys.argv[i]:
                try:
                    th = float(sys.argv[i+1])
                except:
                    print(help)
                    print("ERROR!\nValor incorreto ou vazio para o\
                    \nargumento -t (limiar [Threshold])")
                    exit(1)
            elif '-m' == sys.argv[i]:
                try:
                    mit = int(sys.argv[i+1])
                except:
                    print(help)
                    print("ERROR!\nValor incorreto ou vazio para o\
                    \nargumento -m (Máximo de iterações)")
                    exit(1)
            else:
                print(help)
                print("Argumento Inválido!!!")
                exit(1)
    except IndexError:
        print("Não são suficientes os argumentos fornecidos!\
                \n\nUso: python3 perceptron.py ARQUIVO [OPÇÃO]")
        exit(1)

    print(n, th, mit)
    main(filename=filename, n=n, th=th, mit=mit)