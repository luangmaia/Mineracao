import csv

def base2matrizComNome(base):
	tabela = []

	with open(base, 'r') as csvfile:
		linhas = csv.reader(csvfile, delimiter=',')
		dados = list(linhas)
	dados.pop(0)

	tabela = dados
	
	return tabela

def base2matrizSemNome(base):
	tabela = []

	with open(base, 'r') as csvfile:
		linhas = csv.reader(csvfile, delimiter=',')
		dados = list(linhas)
	dados.pop(0)

	for i in range(len(dados)):
		dados[i].pop(0)

	tabela = dados
	
	return tabela

def getEstados(base):
	tabela = []

	with open(base, 'r') as csvfile:
		linhas = csv.reader(csvfile, delimiter=',')
		dados = list(linhas)
	dados = dados.pop(0)

	dados.pop(0)

	tabela = dados
	
	return tabela

def getNomePlantas(base):
	tabela = []

	with open(base, 'r') as csvfile:
		linhas = csv.reader(csvfile, delimiter=',')
		dados = list(linhas)
	dados.pop(0)

	for i in range(len(dados)):
		dados[i] = dados[i].pop(0)

	tabela = dados
	
	return tabela