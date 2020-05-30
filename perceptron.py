def somatorio(xn, wn):
    if len(xn) != len(wn):
        print("A quantidade de entrada não bate")
        exit(0)
    soma = 0
    for i in range(len(xn)):
        soma += xn[i]*wn[i]
    return soma


def comparador(th, soma):
    if(soma >= th):  # th ?
        return 1
    else:
        return 0


def corrigir(x, w, n, t, o):
    # t => saida desejda
    # o => saida atual
    # n => taxa de aprendizado
    dw = n*(t-o)*x
    wi = w+dw  # ?
    print('dw =', dw)
    #print('w1 =',wi)
    return wi


x = []
x.append([3, 1, 2])
x.append([2, 7, 3])
x.append([3, 9, 3])
x.append([2, 2, 2])
x.append([9, 3, 9])
x.append([7, 2, 7])
x.append([1, 3, 1])
print('x =', x)


[
    [3, 1, 2],
    [2, 7, 3],
    [3, 9, 3],
    [2, 2, 2],
    [9, 3, 9],
    [7, 2, 7],
    [1, 3, 1],
]


w = []
w.append(1)
w.append(1)
w.append(1)
w.append(1)
w.append(1)
w.append(1)
w.append(1)
print('w =', w)

saida = [1, 0, 0, 0, 0, 0]

saidaFinal = [0, 0, 0, 0, 0, 0]

n = 0.9
th = 0.8

while(True):
    flag = 1
    print(w)
    for i in range(len(x[0])):
        aux = []
        for j in range(len(x)):
            aux.append(x[j][i])

        som = round(somatorio(aux, w), 2)
        print('Somatorio =', som)
        o = comparador(th, som)
        saidaFinal[i] = o
        if o != saida[i]:
            print("\nAjustando...")
            for j in range(len(w)):
                w[j] = round(corrigir(x[j][i], w[j], n, saida[i], o), 2)
                print('w'+str(j)+'=', w[j])
            flag = 0
            break
    if flag == 1:
        break

print("\nw =", w)
print(saidaFinal)
