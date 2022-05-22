import airportsdata
import geopy.distance

distance = 11
dep = 'FAB'
arr = 'FAB'
depname = 'Farnborough'


def distfinder():
	global distance
	global dep
	global depname
	global arrname

	depcords = airportsdata.load('IATA')[arr]
	depcords = depcords.pop('lat'), depcords.pop('lon')
	dep = input("Departure code? ").upper()
	airports = airportsdata.load('IATA')
	arrivalfull = airports[dep]
	lat = arrivalfull.pop('lat')
	lon = arrivalfull.pop('lon')
	depname = arrivalfull.pop('name')
	arrname = airportsdata.load('IATA')[arr].pop('name')
	arrcords = (lat, lon)
	distance = geopy.distance.geodesic(depcords, arrcords).mi


def farnborougharr():
	global arr
	arr = "FAB"
	distfinder()
	if distance > 1000:
		flightnumber = "DE3"
	else:
		flightnumber = "DE11"
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def lutonarr():
	global arr
	arr = "LTN"
	distfinder()
	if distance > 1000:
		flightnumber = "DE111"
	else:
		flightnumber = "DE101"
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def bigginarr():
	global arr
	arr = "BQH"
	distfinder()
	if distance > 1000:
		flightnumber = "DE51"
	else:
		flightnumber = "DE49"
	print(dep, arr, flightnumber)
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def teterarr():
	global arr
	arr = "TEB"
	distfinder()
	if distance > 1000:
		flightnumber = "DE301"
	else:
		flightnumber = "DE311"
	print(dep, arr, flightnumber)
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def haywardarr():
	global arr
	arr = "HWD"
	distfinder()
	if distance > 1000:
		flightnumber = "DE401"
	else:
		flightnumber = "DE411"
	print(dep, arr, flightnumber)
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def tasharr():
	global arr
	arr = "TAS"
	distfinder()
	if distance > 1000:
		flightnumber = "DE81"
	else:
		flightnumber = "N/A - No shorthaul out of Tashkent"
	print(dep, arr, flightnumber)
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def kansaiarr():
	global arr
	arr = "KIX"
	distfinder()
	if distance > 1000:
		flightnumber = "261"
	else:
		flightnumber = "259"
	print(dep, arr, flightnumber)
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def doualaarr():
	global arr
	arr = "DLA"
	distfinder()
	if distance > 1000:
		flightnumber = "DE701"
	else:
		flightnumber = "DE703"
	print(dep, arr, flightnumber)
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)
