import csv
from geopy.geocoders import Nominatim

def main():
	abbr2state = getListAbbr2State()
	qtdeEstados = len(abbr2state)
	coordEstados = []
	geolocator = Nominatim()

	for i in range(qtdeEstados):
		print(abbr2state[i][1])
		location = geolocator.geocode(abbr2state[i][1])
		print (location.address)
		coord = [location.latitude, location.longitude]
		coordEstados.append(coord)
	
	with open("coord.data", "w") as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerows(coordEstados)

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

if __name__ == "__main__":
	main()