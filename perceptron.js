function somatorio(entradas, pesos) {
  if (entradas.length != pesos.length) {
    console.log(" As entradas e pesos não possuem a mesma quantidade.")
    return
  }

  let soma = 0
  for (let i = 0; i < entradas.length; i++) {
    soma += parseFloat(entradas[i]) * parseFloat(pesos[i])
  }
  return soma
}

function comparador(limiteAtivacao, soma) {
  return soma >= limiteAtivacao ? 1 : 0
}

function corrigir(entrada, peso, taxaAprendizado, saidaDesejada, saidaAtual) {
  const deltaPeso = taxaAprendizado * (saidaDesejada - saidaAtual) * entrada
  const novoPeso = peso + deltaPeso

  console.log(`deltaPeso = ${deltaPeso}`)

  return parseFloat(novoPeso).toFixed(2)
}
let entradas = []
let pesos = []

entradas.push([3, 1, 2])
entradas.push([2, 7, 3])
entradas.push([3, 9, 3])
entradas.push([2, 2, 2])
entradas.push([9, 3, 9])
entradas.push([7, 2, 7])
entradas.push([1, 3, 1])
console.log(`Entradas = ${entradas.join(",")}`)

pesos.push([1])
pesos.push([1])
pesos.push([1])
pesos.push([1])
pesos.push([1])
pesos.push([1])
pesos.push([1])

console.log(`Pesos = ${pesos.join(",")}`)

const saida = [1, 0, 0, 0, 0, 0]
const saidaFinal = [0, 0, 0, 0, 0, 0]

const taxaAprendizado = 0.9
const limiteAtivacao = 0.8

while (true) {
  let flag = 1
  console.log({ pesos })

  for (let coluna = 0; coluna < entradas[0].length; coluna++) {
    let aux = []
    for (let linha = 0; linha < entradas.length; linha++) {
      aux.push(entradas[linha][coluna])
    }

    const soma = somatorio(aux, pesos)
    console.log(`Somatoria = ${soma}`)

    const saidaAtual = comparador(limiteAtivacao, soma)
    saidaFinal[coluna] = saidaAtual

    if (saidaAtual != saida[coluna]) {
      console.log("\nAjustando...")

      for (let i = 0; i < pesos.length; i++) {
        pesos[i] = parseFloat(
          corrigir(
            entradas[i][coluna],
            pesos[i],
            taxaAprendizado,
            saida[coluna],
            saidaAtual
          )
        )
        console.log(`\n peso ${i} = ${pesos[i]}`)
      }
      flag = 0
      break
    }
  }
  if (flag == 1) break
}

console.log("\nFINAL => N")
console.log(`Pesos = ${pesos.join(",")}`)
console.log(saidaFinal.join(","))
