import airportsdata
import geopy.distance


def distfinder():
	global distance
	global arr

	depcords = airportsdata.load('IATA')[dep]
	depcords = depcords.pop('lat'), depcords.pop('lon')
	arr = input("Arrival code? ").upper()
	airports = airportsdata.load('IATA')
	arrivalfull = airports[arr]
	lat = arrivalfull.pop('lat')
	lon = arrivalfull.pop('lon')
	arrcords = (lat, lon)
	distance = geopy.distance.geodesic(depcords, arrcords).mi

def farnborough():
	global dep
	dep = "FAB"
	distfinder()
	if distance > 1000:
		flightnumber = "DE3"
	else:
		flightnumber = "DE11"
	print(dep, arr, flightnumber)

def luton():
	global dep
	dep = "LTN"
	distfinder()
	if distance > 1000:
		flightnumber = "DE111"
	else:
		flightnumber = "DE101"
	print(dep, arr, flightnumber)

def biggin():
	global dep
	dep = "BQH"
	distfinder()
	if distance > 1000:
		flightnumber = "DE51"
	else:
		flightnumber = "DE49"
	print(dep, arr, flightnumber)

def teter():
	global dep
	dep = "TEB"
	distfinder()
	if distance > 1000:
		flightnumber = "DE301"
	else:
		flightnumber = "DE311"
	print(dep, arr, flightnumber)

def hayward():
	global dep
	dep = "HWD"
	distfinder()
	if distance > 1000:
		flightnumber = "DE401"
	else:
		flightnumber = "DE411"
	print(dep, arr, flightnumber)

def tash():
	global dep
	dep = "TAS"
	distfinder()
	if distance > 1000:
		flightnumber = "DE81"
	else:
		flightnumber = "N/A - No shorthaul out of Tashkent"
	print(dep, arr, flightnumber)

def kansai():
	global dep
	dep = "KIX"
	distfinder()
	if distance > 1000:
		flightnumber = "261"
	else:
		flightnumber = "259"
	print(dep, arr, flightnumber)

def douala():
	global dep
	dep = "DLA"
	distfinder()
	if distance > 1000:
		flightnumber = "DE701"
	else:
		flightnumber = "DE703"
	print(dep, arr, flightnumber)
