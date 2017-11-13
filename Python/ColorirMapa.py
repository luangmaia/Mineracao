import gmplot

def criarMapa(nomeMapa, latitudes, longitudes, cor, porcentagens):

	gmap = gmplot.GoogleMapPlotter(50.8525354, -130.2167026, 3)

	for i in range(len(latitudes)):
		latitude = []
		longitude = []
		latitude.append(latitudes[i])
		longitude.append(longitudes[i])

		gmap.scatter(latitude, longitude, cor, size=150000*porcentagens[i], marker=False)

	gmap.draw(nomeMapa)