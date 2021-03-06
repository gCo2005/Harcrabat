"""
Database.py
NewScript
Contains all the data for the game
"""


from colorama import Fore, Back, init, Style


### CONSTANTS ###


ENV_CLEANUP_FACTOR = 50
ENV_INCONSISTENCY = 1.01
ENV_CLUSTER_SIZE = 5
COLLECT_DELAY = 0 #### 60
MOVE_DELAY = 0 #### 5
HARVEST_SIZE = 4
UNCOMMON_RESOURCE_THRESHOLD = 75
RARE_RESOURCE_THRESHOLD = 16
PRINT_SEPARATER = "print('-----------------------------------------------')"


### LISTS ###


ITEMS = [] #### Fill in
#### BIOMES = []
ENVIRONMENTS = ["Woodlands", "Plains", "Grasslands", "Waterlands", "Rockylands"] #### Change to object in main
BIOME_WEIGHTS = [60, 20, 5, 1]
RESOURCE_WEIGHTS = [60, 35, 5]


### DICTS ###


COMMANDS = {
	"help": "View the command list",
	"exit": "Exit the program",
	"start": "Start the game",
	"controls": "View the controls"
	}
KEY_BINDINGS = {
	b"w": ("self.Player.turn('North')", "Turn to the north"),
	b"s": ("self.Player.turn('South')", "Turn to the south"),
	b"a": ("self.Player.turn('West')", "Turn to the west"),
	b"d": ("self.Player.turn('East')", "Turn to the east"),
	b" ": ("self.Player.move()", "Move forward"),
	b"j": ("self.Player.collect()", "Collect resources"),
	b"k": ("self.Player.attack()", "Attack with current weapon"),
	b"q": ("self.Player.describe_surroundings()", "Give detailed location information"),
	b"e": ("self.Player.look()", "Reveal the square ahead"),
	b"h": ("self.Player.list_inv()", "View your inventory"),
	b"`": ("self.command_input()", "Pause game"),
	b"l": ("self.Player.craft(self.items)", "Craft an item")
	}
PRINT_COLORS = {
	"Critical": Fore.RED,
	"Legendary": Fore.BLUE,
	"Rare": Fore.CYAN,
	"Uncommon": Fore.GREEN,
	"Common": "",
	"Reset": Style.RESET_ALL,
	}
