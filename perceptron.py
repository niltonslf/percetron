import numpy as np

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

def main():
    """
    Método principal que recebe a entrada e os pesos iniciais,
    executa até chegar no resultado desejado ou no valor máximo
    de iterações.

    x           => Entrada
    w           => pesos
    saida       => Saídas desejadas
    saidaFinal  => Saídas atual
    mit         => Máximo de iterações
    it          => Quantidade de iterações
    n           => Taxa de aprendizado
    th          => Threshold (Limiar)
    """

    # Declaração de Variáveis
    x = np.array([[3,1,2],
                  [2,7,3],
                  [3,9,3],
                  [2,2,2],
                  [9,3,9],
                  [7,2,7],
                  [1,3,1]])
    w = np.zeros(len(x))
    saida = np.array([1,0,0])
    saidaFinal = np.array([0,0,0])
    mit = 500
    it = 0
    n = 0.1
    th = 0.5

    while True:
        it += 1
        print(w)
        for i in range(x.shape[1]):
            som = round(somatorio(x[:,i],w),2)
            print('Somatorio =',som)
            o = comparador(th, som) 
            saidaFinal[i] = o
            if o != saida[i]:
                print("\nAjustando...")
                w = corrigir(x[:,i], w, n, saida[i], o).round(2)
                break
        if (saidaFinal == saida).all():
            print("\nResultado encontrado com sucesso!!!")
            print("\nw =",w)
            print(saidaFinal)
            break
        elif it == mit:
            print("\nAtingido o número máximo de iterações!!!")
            print("Resultado não encontrado!!!")
            break

if __name__ == "__main__":
    main()