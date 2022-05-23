import airportsdata
import geopy.distance
from fpdf import FPDF

distance = 11
dep = 'FAB'
arr = 'FAB'
arrname = 'Farnborough'
depname = 'Farnborough'


def distfinder():
	global distance
	global arr
	global arrname
	global depname

	depcords = airportsdata.load('IATA')[dep]
	depcords = depcords.pop('lat'), depcords.pop('lon')
	depname = airportsdata.load('IATA')[dep].pop('name')
	arr = input("Arrival code? ").upper()
	airports = airportsdata.load('IATA')
	arrivalfull = airports[arr]
	lat = arrivalfull.pop('lat')
	lon = arrivalfull.pop('lon')
	arrname = arrivalfull.pop('name')
	arrcords = (lat, lon)
	distance = geopy.distance.geodesic(depcords, arrcords).mi


def ticketcreate():
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size = 15)
	pdf.cell(200, 10, depname,
			ln = 1, align = 'C')
	pdf.cell(200, 10, arrname,
			ln = 2, align = 'C')
	pdf.output("original.pdf")


def farnborough():
	global dep
	dep = "FAB"
	distfinder()
	if distance > 1000:
		flightnumber = "DE3"
	else:
		flightnumber = "DE11"
	ticketcreate()
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def luton():
	global dep
	dep = "LTN"
	distfinder()
	if distance > 1000:
		flightnumber = "DE111"
	else:
		flightnumber = "DE101"
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def biggin():
	global dep
	dep = "BQH"
	distfinder()
	if distance > 1000:
		flightnumber = "DE51"
	else:
		flightnumber = "DE49"
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def teter():
	global dep
	dep = "TEB"
	distfinder()
	if distance > 1000:
		flightnumber = "DE301"
	else:
		flightnumber = "DE311"
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def hayward():
	global dep
	dep = "HWD"
	distfinder()
	if distance > 1000:
		flightnumber = "DE401"
	else:
		flightnumber = "DE411"
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def tash():
	global dep
	dep = "TAS"
	distfinder()
	if distance > 1000:
		flightnumber = "DE81"
	else:
		flightnumber = "N/A - No shorthaul out of Tashkent"
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def kansai():
	global dep
	dep = "KIX"
	distfinder()
	if distance > 1000:
		flightnumber = "261"
	else:
		flightnumber = "259"
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)


def douala():
	global dep
	dep = "DLA"
	distfinder()
	if distance > 1000:
		flightnumber = "DE701"
	else:
		flightnumber = "DE703"
	print(dep, "-", depname)
	print(arr, "-", arrname)
	print(flightnumber)
