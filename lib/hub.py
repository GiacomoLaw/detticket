from pick import pick
from .hubdepart import *


def hubstart():
	title = "Departure airport hub?"
	options = ['Yes', 'No']
	option, index = pick(options, title)
	print(option)
	if option == "Yes":
		hublaunch()
	elif option == "No":
		nonbase()
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
