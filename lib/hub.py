from pick import pick
from .hubdepart import *
from .hubarrival import *


def hubstart():
	title = "Departure airport hub?"
	options = ['Yes', 'Arrival hub', 'Exit']
	option, index = pick(options, title)
	print(option)
	if option == "Yes":
		hublaunch()
	elif option == "Arrival hub":
		arrhub()
	elif option == "Exit":
		exit()


def hublaunch():
	title = "Hub origin"
	options = ['Farnborough', 'Luton', 'Biggin', 'Teterboro', 'Hayward', 'Tashkent', 'Kansai', 'Douala']
	option, index = pick(options, title)
	print(option)
	if option == "Farnborough":
		farnborough()
	elif option == "Luton":
		luton()
	elif option == "Biggin":
		biggin()
	elif option == "Teterboro":
		teter()
	elif option == "Hayward":
		hayward()
	elif option == "Tashkent":
		tash()
	elif option == "Kansai":
		kansai()
	elif option == "Douala":
		douala()


def arrhub():
	title = "Hub to"
	options = ['Farnborough', 'Luton', 'Biggin', 'Teterboro', 'Hayward', 'Tashkent', 'Kansai', 'Douala']
	option, index = pick(options, title)
	print(option)
	if option == "Farnborough":
		farnborougharr()
	elif option == "Luton":
		lutonarr()
	elif option == "Biggin":
		bigginarr()
	elif option == "Teterboro":
		teterarr()
	elif option == "Hayward":
		haywardarr()
	elif option == "Tashkent":
		tasharr()
	elif option == "Kansai":
		kansaiarr()
	elif option == "Douala":
		doualaarr()
