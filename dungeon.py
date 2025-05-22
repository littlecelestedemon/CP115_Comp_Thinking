class Player():
    def __init__(self):
        self.inventory = []
        self.alive = True
        self.has_won = False



def room_001_event():
    if 'some really gross cheese' in player.inventory:
        choice = input('Give cheese to skeleton?')
        if choice == 'yes':
            print('you give the skeleton some cheese.')
            print('he becomes your friend.')
            player.has_won == True
    else:    
        pass
    return

def room_002_event():
    pass

def room_003_event():
    pass

def room_004_event():
    global player
    print("You see some gross moldy cheese.")
    choice = input('Eat the cheese, take the cheese, or leave?')
    if choice == 'eat':
        print('you eat the moldy cheese and die.')
        player.alive = False
    elif choice == 'take':
        player.inventory.append('some really gross cheese')
    else:
        pass
    return

class Room():
    def __init__(self, raw_string):
        lines = raw_string.split('\n')
        self.id = lines[0]
        self.exits = lines[-1]
        self.room_text = "\n".join(lines[1:-1])

    def visit(self):
        print(self.room_text)
        event_dict[self.id]()

    def move(self):
        choices = {}
        print("There are rooms to the following directions:")
        
        for item in self.exits.split(','):
            item_direction, item_id = item.split(':')
            print(item_direction)
            choices[item_direction] = item_id
            
        decision = input( "Where do you want to go?" )
        return choices[decision]

player = Player()

file = open('map_01.txt')
rooms_raw_text = file.read().split('%%%%%')

rooms = [Room(text.strip()) for text in rooms_raw_text]
event_dict = {
    'room_001':room_001_event,
    'room_002':room_002_event,
    'room_003':room_003_event,
    'room_004':room_004_event
    }
id_dict = {item.id:item for item in rooms}

current_room = rooms[0]

while player.alive and not player.has_won:
    current_room.visit()
    if player.alive and not player.has_won:
        new_room_id = current_room.move()
        current_room = id_dict[new_room_id]

if player.has_won:
    print("Yay, you win")
if not player.alive:
    print("You died in the dungeon")


