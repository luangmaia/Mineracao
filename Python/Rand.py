import BaseHandle
import csv
from sklearn import metrics
import numpy

def main():
	tabela = BaseHandle.base2matrizSemNome('BasePorGenero.txt')
	vetorClimaEstados = getVetorClima()
	climasUnicos = []

	for elem in vetorClimaEstados:
		if not elem[0] in climasUnicos:
			climasUnicos.append(elem[0])
	
	climas = []
	climasAgrupamento = [0]*len(tabela)
	
	for elem in tabela:
		clima = getClima(elem, vetorClimaEstados, climasUnicos)

		if clima != 9999:
			climas.append(clima)
	
	print (climas)

	for i in range(len(climasUnicos)):
		with open(str(len(climasUnicos))+' Clusters com ID\cluster'+str(i)+'Kmeans.csv', 'r') as csvfile:
			linhas = csv.reader(csvfile, delimiter=',')
			dados = list(linhas)
		dados.pop(0)
		tab = dados

		for elem in tab:
			if elem:
				indice = int(elem.pop(0))

				clima = getClima(elem, vetorClimaEstados, climasUnicos)
				climasAgrupamento[indice] = clima
	
	print (climasAgrupamento)

	print ('Rand: ' + str(metrics.adjusted_rand_score(climas, climasAgrupamento)))

'''def getClimaAgrupamento(tab, vetorClimaEstados, climasUnicos):
	climas = vetorClimaEstados
	climasUnicos = climasUnicos

	cont = {}

	for linha in tab:
		for i in range(len(linha)):
			if int(linha[i]) == 1:
				aux = cont.keys()
				if climas[i][0] in aux:
					cont[climas[i][0]] += 1
				else:
					cont[climas[i][0]] = 1

	if not cont:
		return 9999

	chaves = list(cont.keys())
	maior = chaves[0]

	for elem in chaves:
		if cont[elem] > cont[maior]:
			maior = elem

	retorno = 0

	for i in range(len(climasUnicos)):
		if climasUnicos[i] == maior:
			retorno = i
			break

	return retorno'''

def getClima(linha, vetorClimaEstados, climasUnicos):
	climas = vetorClimaEstados
	climasUnicos = climasUnicos

	cont = {}

	for i in range(len(linha)):
		if int(linha[i]) == 1:
			aux = list(cont.keys())
			if climas[i][0] in aux:
				cont[climas[i][0]] += 1
			else:
				cont[climas[i][0]] = 1

	if not cont:
		return 9999

	chaves = list(cont.keys())
	maior = chaves[0]

	for elem in chaves:
		if cont[elem] > cont[maior]:
			maior = elem
	
	retorno = 0

	for i in range(len(climasUnicos)):
		if climasUnicos[i] == maior:
			retorno = i
			break

	return retorno

def getVetorClima():
	tabela = []

	with open('climas.data', 'r') as csvfile:
		linhas = csv.reader(csvfile, delimiter=',')
		dados = list(linhas)

	tabela = dados
	
	return tabela

if __name__ == "__main__":
	main()