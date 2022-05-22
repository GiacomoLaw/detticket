import airportsdata
import geopy.distance


def farnborough():
	dep = "FAB"
	depcords = (51.2757987976, -0.7763329744)
	arr = input("Arrival code? ").upper()
	airports = airportsdata.load('IATA')
	arrivalfull = airports[arr]
	lat = arrivalfull.pop('lat')
	lon = arrivalfull.pop('lon')
	arrcords = (lat, lon)
	distance = geopy.distance.geodesic(depcords, arrcords).mi
	if distance > 1000:
		flightnumber = "DE3"
	else:
		flightnumber = "DE11"
	print(dep, arr, flightnumber)

def luton():
	dep = "LTN"
	depcords = airportsdata.load('IATA')[dep]
	depcords = depcords.pop('lat'), depcords.pop('lon')
	arr = input("Arrival code? ").upper()
	airports = airportsdata.load('IATA')
	arrivalfull = airports[arr]
	lat = arrivalfull.pop('lat')
	lon = arrivalfull.pop('lon')
	arrcords = (lat, lon)
	distance = geopy.distance.geodesic(depcords, arrcords).mi
	if distance > 1000:
		flightnumber = "DE111"
	else:
		flightnumber = "DE101"
	print(dep, arr, flightnumber)

def biggin():
	dep = "BQH"
	depcords = airportsdata.load('IATA')[dep]
	depcords = depcords.pop('lat'), depcords.pop('lon')
	arr = input("Arrival code? ").upper()
	airports = airportsdata.load('IATA')
	arrivalfull = airports[arr]
	lat = arrivalfull.pop('lat')
	lon = arrivalfull.pop('lon')
	arrcords = (lat, lon)
	distance = geopy.distance.geodesic(depcords, arrcords).mi
	if distance > 1000:
		flightnumber = "DE51"
	else:
		flightnumber = "DE49"
	print(dep, arr, flightnumber)

def teter():
	dep = "TEB"
	depcords = airportsdata.load('IATA')[dep]
	depcords = depcords.pop('lat'), depcords.pop('lon')
	arr = input("Arrival code? ").upper()
	airports = airportsdata.load('IATA')
	arrivalfull = airports[arr]
	lat = arrivalfull.pop('lat')
	lon = arrivalfull.pop('lon')
	arrcords = (lat, lon)
	distance = geopy.distance.geodesic(depcords, arrcords).mi
	if distance > 1000:
		flightnumber = "DE301"
	else:
		flightnumber = "DE311"
	print(dep, arr, flightnumber)

def hayward():
	dep = "HWD"
	depcords = airportsdata.load('IATA')[dep]
	depcords = depcords.pop('lat'), depcords.pop('lon')
	arr = input("Arrival code? ").upper()
	airports = airportsdata.load('IATA')
	arrivalfull = airports[arr]
	lat = arrivalfull.pop('lat')
	lon = arrivalfull.pop('lon')
	arrcords = (lat, lon)
	distance = geopy.distance.geodesic(depcords, arrcords).mi
	if distance > 1000:
		flightnumber = "DE401"
	else:
		flightnumber = "DE411"
	print(dep, arr, flightnumber)

def tash():
	dep = "TAS"
	depcords = airportsdata.load('IATA')[dep]
	depcords = depcords.pop('lat'), depcords.pop('lon')
	arr = input("Arrival code? ").upper()
	airports = airportsdata.load('IATA')
	arrivalfull = airports[arr]
	lat = arrivalfull.pop('lat')
	lon = arrivalfull.pop('lon')
	arrcords = (lat, lon)
	distance = geopy.distance.geodesic(depcords, arrcords).mi
	if distance > 1000:
		flightnumber = "DE81"
	else:
		flightnumber = "N/A - No shorthaul out of Tashkent"
	print(dep, arr, flightnumber)

def kansai():
	dep = "KIX"
	depcords = airportsdata.load('IATA')[dep]
	depcords = depcords.pop('lat'), depcords.pop('lon')
	arr = input("Arrival code? ").upper()
	airports = airportsdata.load('IATA')
	arrivalfull = airports[arr]
	lat = arrivalfull.pop('lat')
	lon = arrivalfull.pop('lon')
	arrcords = (lat, lon)
	distance = geopy.distance.geodesic(depcords, arrcords).mi
	if distance > 1000:
		flightnumber = "261"
	else:
		flightnumber = "259"
	print(dep, arr, flightnumber)

def douala():
	dep = "DLA"
	depcords = airportsdata.load('IATA')[dep]
	depcords = depcords.pop('lat'), depcords.pop('lon')
	arr = input("Arrival code? ").upper()
	airports = airportsdata.load('IATA')
	arrivalfull = airports[arr]
	lat = arrivalfull.pop('lat')
	lon = arrivalfull.pop('lon')
	arrcords = (lat, lon)
	distance = geopy.distance.geodesic(depcords, arrcords).mi
	if distance > 1000:
		flightnumber = "DE701"
	else:
		flightnumber = "DE703"
	print(dep, arr, flightnumber)
