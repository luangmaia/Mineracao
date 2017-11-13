import csv

def carregarDados(arquivo, arquivoEstados):
	estados = []

	with open(arquivoEstados, 'rb') as csvfile:
		linhas = csv.reader(csvfile)
		dados = list(linhas)

		i = 0
		for x in dados:
			estados.append(x[0])
			i += 1
	
	tabela = []

	with open(arquivo, 'rb') as csvfile:
		linhas = csv.reader(csvfile)
		dados = list(linhas)

		tabela = [0]

		tabela[0] = [0]*(len(estados)+1)

		tabela[0][0] = 'Planta'

		for i in range(len(estados)):
			tabela[0][i+1] = estados[i]

		ultimaPlanta = 'zzzzzzz'

		i = 0
		for x in dados:
			if 'var.' in x[0]:
				continue
			elif not ultimaPlanta in x[0]:
				ultimaPlanta = x[0]
				continue
			else:
				# ultimaPlanta = x[0]
				i += 1
				tabela.append([0])
				tabela[i] = [0]*(len(estados)+1)
			
			for y in x:
				if y not in estados:
					if not y is x[0]:
						continue
					
					tabela[i][0] = y
				else:
					tabela[i][estados.index(y)+1] = 1
	
	return tabela

tab = carregarDados('plants.data', 'states.data')
'''
for x in tab:
	print str(x)'''

with open("tabela.csv", "wb") as csvfile:
	writer = csv.writer(csvfile, delimiter=',', dialect='excel')
	writer.writerows(tab)