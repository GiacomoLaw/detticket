from pick import pick
from lib.hub import *

title = "Ticket gen - from hub or not?"
options = ['Hub', 'Not', 'Exit']
option, index = pick(options, title)
print(option)
if option == "Hub":
	hubstart()
elif option == "Not":
	exit()
elif option == "Exit":
	exit()