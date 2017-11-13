'''-----------------------------------------------------------------------------------------------------------------------------------------------------

É necessário passar como parâmetro o número de clusters

-----------------------------------------------------------------------------------------------------------------------------------------------------'''

import kmeansExample
import ColorirMapa
import csv
import sys
from geopy.geocoders import Nominatim

def main():
	abbr2state = getListAbbr2State()
	qtdeEstados = len(abbr2state)
	coordEstados = []
	'''geolocator = Nominatim()

	for i in range(qtdeEstados):
		print(abbr2state[i][1])
		location = geolocator.geocode(abbr2state[i][1])
		print (location.address)
		coord = [location.latitude, location.longitude]
		coordEstados.append(coord)'''
	
	coordEstados = getCoordEstados()
	
	'''for i in range(8,13):
		print('kmeans com ' + str(i))
		kmeansExample.main(i)
		colorir(i, abbr2state, qtdeEstados, coordEstados)'''
	qtdeClusters = int(sys.argv[1])
	kmeansExample.main(qtdeClusters)
	colorir(qtdeClusters, abbr2state, qtdeEstados, coordEstados)

def colorir(numClusters, abbr2state, qtdeEstados, coordEstados):

	for i in range(numClusters):
		porcentagens = [0]*qtdeEstados
		tabela = []
		nome = "cluster" + str(i) + "Kmeans.csv"
		nomeMapa = 'total' + str(numClusters) + 'MapaCluster' + str(i) + '.html'

		with open(nome, 'r') as csvfile:
			linhas = csv.reader(csvfile, delimiter=',')
			dados = list(linhas)
		estados = dados.pop(0)
		tabela = dados

		latitude = [0]*qtdeEstados
		longitude = [0]*qtdeEstados

		for elem in tabela:
			if elem:
				#print (elem)
				for j in range(len(elem)):
					if int(elem[j]) == 1:
						latitude[j] = float(coordEstados[j][0])
						longitude[j] = float(coordEstados[j][1])
						porcentagens[j] += 1/len(tabela)

		ColorirMapa.criarMapa(nomeMapa, latitude, longitude, '#FF0000', porcentagens)
	
def getListAbbr2State():
	tabela = []

	with open('states.data', 'r') as csvfile:
		linhas = csv.reader(csvfile, delimiter=',')
		dados = list(linhas)
	abbr = dados

	with open('abbr2state.data', 'r') as csvfile:
		linhas = csv.reader(csvfile, delimiter=',')
		dados = list(linhas)
	estados = dados

	if len(abbr) == len(estados):
		for i in range(len(abbr)):
			elem = [abbr[i][0], estados[i][0]]
			tabela.append(elem)

	return tabela

def getCoordEstados():
	dados = []
	with open('coord.data', 'r') as csvfile:
		linhas = csv.reader(csvfile, delimiter=',')
		dados = list(linhas)
	
	return dados

if __name__ == "__main__":
	main()