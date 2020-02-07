# IN PROGRESS

green='\033[1;92m'
white='\033[1;97m'
yellow='\033[1;93m'
reset='\033[0m'

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items=[]
        self.branchtable={}
        self.branchtable[GET] = self.get_item
        self.branchtable[DROP] = self.drop_item
    def get_item(self, item):
      self.items.append(item)
    def drop_item(self, item):
      self.items.remove(item)
    def __repr__(self):
        return f'\n{repr(self.name)} \n{repr(self.description)}\n'

#----------------------------------------------------------------

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.branchtable={}
        self.branchtable[GET] = self.get_item
        self.branchtable[DROP] = self.drop_item
    def get_item(self, item):
      self.backpack.append(item)
    def drop_item(self, item):
      self.backpack.remove(item)


#----------------------------------------------------------------

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f'{yellow}{repr(self.name)}{reset} \n{repr(self.description)}'

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].items = [Item("Ring", "An old, tarnished ring.")]
room['foyer'].items = [Item("Porcelain Figure", "A porcelain figurine in the likeness of a strange creature...")]
room['overlook'].items = [Item("Turtle Shell", "This empty turtle shell has strange markings carved into it.")]
room['narrow'].items = [Item("Sword", "An iron sword orange with rust... or blood?")]
room['treasure'].items = ["Book", "A moldering book with a plain, black cover and written in a foreign language."]

Jamie = Player("Jamie",room["outside"])
current_location = None
Jamie.backpack = []

print('Choose a direction (n,s,e, or w), look around (l), pick up an item you find (p), drop an item (d), or quit the game by pressing q!\n')
playing = True
while playing:
  for key, value in room.items():
      # print(value.name)
    if value.name==Jamie.location.name:
       print(value)
       current_location = value
  move=input(f"\nWhat do you want to do, {Jamie.name}?\n")
  if move == "n":
      if Jamie.location.n_to == None:
        print("\nWe can't go there!")
      else:
        Jamie.location = Jamie.location.n_to
  if move == "s":
      if Jamie.location.s_to == None:
        print("\nWe can't go there!")
      else:
        Jamie.location = Jamie.location.s_to
        print
  if move == "e":
      if Jamie.location.e_to == None:
        print("\nWe can't go there!")
      else:
        Jamie.location = Jamie.location.e_to
  if move == "w":
      if Jamie.location.w_to == None:
        print("\nWe can't go there!")
      else:
        Jamie.location = Jamie.location.w_to
  if move == "q":
      print(f"\n {green}Hark Triton{reset}, hark! Bellow, bid our father the Sea King rise from the depths full fowl in his fury! Black waves teeming with salt foam to smother this young mouth with pungent slime. To choke ye, engorging your organs til’ ye turn blue and bloated with bilge and brine and can scream no more only when he, crowned in cockle shells with slitherin’ tentacle tail and steaming beard take up his fell befitted arm, his coral tyne trident screeches banshee-like in the tempest and plunges right through yer gullet bursting ye -- a bulging blacker no more, but a blasted bloody film now and nothing for the harpies and the souls of dead sailors to peck and claw and feed upon only to be lapped up and swallowed by the infinite waters of the Dread Emperor himself. Forgotten to any man, to any time, forgotten to any god or devil, forgotten even to the sea, for any stuff for part of {Jamie.name}, even any scantling of your soul is {Jamie.name} no more, but is now itself the sea!")
      playing=False
  if move == "l":
     print("\nYou carefully look around...\n")
     print("You find: \n")
     itemName=[i.name for i in Jamie.location.items]
     itemDescription=[i.description for i in Jamie.location.items]
     print(itemName, itemDescription)
  if move == "p":
    if len(Jamie.location.items) > 0:
      selectable=[]
      for item in Jamie.location.items:
        selectable.append(item)
      selection=input("\nThis might be useful. Type in its name to collect it...\n")
      if selection:
        for item in selectable:
            if selection==item.name:
              Jamie.get_item(item)
              Jamie.location.drop_item(item)
              print(f"\nYou put the {selection} in your backpack.\n")
    else:
      print("\nYou don't see anything in here.\n")
  if move=="d":
    if len(Jamie.backpack) > 0:
      print("\nHere's what's in your backpack: \n", Jamie.backpack)
      selectable=[]
      for item in Jamie.backpack:
        selectable.append(item)
      selection=input("\nYour backpack is getting heavy. Choose an item to leave behind...")
      if selection:
        for item in selectable:
            if selection==item.name:
              Jamie.drop_item(item)
              Jamie.location.get_item(item)
              print(f"\nYou take the {selection} out of your backpack and leave it here.\n")
    else:
      print("\n There's nothing in your backpack right now.\n")

      








