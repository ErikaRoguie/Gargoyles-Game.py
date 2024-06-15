class Game:
    def __init__(self):
        self.rooms = {
            'Castle': {'item': 'Artifact Piece 1', 'north': 'Park', 'south': 'Streets'},
            'Park': {'item': 'Artifact Piece 2', 'south': 'Castle', 'east': 'Rooftops'},
            'Streets': {'item': 'Artifact Piece 3', 'north': 'Castle', 'east': 'Rooftops'},
            'Rooftops': {'item': None, 'west': 'Park'}
        }
        self.player_location = 'Castle'
        self.player_inventory = []
        self.game_over = False

    def display_location(self):
        print(f"You are currently in {self.player_location}.")
        if self.rooms[self.player_location]['item']:
            print(f"There is an item here: {self.rooms[self.player_location]['item']}")

    def display_commands(self):
        print("Commands: move north, move south, move east, move west, get item")

    def get_command(self):
        return input("> ")

    def process_command(self, command):
        if command.startswith('move'):
            direction = command.split(' ')[1]
            if direction in self.rooms[self.player_location]:
                self.player_location = self.rooms[self.player_location][direction]
            else:
                print("You can't go that way.")
        elif command == 'get item':
            if self.rooms[self.player_location]['item']:
                self.player_inventory.append(self.rooms[self.player_location]['item'])
                self.rooms[self.player_location]['item'] = None
            else:
                print("There is no item here.")
        else:
            print("Invalid command.")

    def check_win_condition(self):
        if len(self.player_inventory) == 3 and self.player_location == 'Rooftops':
            print("You win!")
            self.game_over = True
        elif self.player_location == 'Rooftops':
            print("You lose!")
            self.game_over = True

    def play(self):
        while not self.game_over:
            self.display_location()
            self.display_commands()
            command = self.get_command()
            self.process_command(command)
            self.check_win_condition()

game = Game()
game.play()

def start_game():
    print("You are Goliath, the leader of the Manhattan Clan in Disney's Gargoyles.")
    print("Tonight, you face a new threat to your clan. What will you do first?")
    print("1. Patrol the city.")
    print("2. Stay at the castle.")
    choice = input("> ")

    if choice == "1":
        patrol_city()
    elif choice == "2":
        stay_castle()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        start_game()

def patrol_city():
    print("You decide to patrol the city. Suddenly, you spot a group of suspicious figures. What do you do?")
    print("1. Confront them.")
    print("2. Follow them secretly.")
    choice = input("> ")

    if choice == "1":
        confront= input("You confront the figures. They turn out to be thieves. What do you do?", "1. Fight them.", "2. Let them go.", "3. Talk to them.", "4. Arrest them.", "5. Follow them.", "6. Check them for weapons.") 
        confront()
    elif choice == "2":
        follow= input("You follow the figures secretly. They lead you to a crime scene. What do you do?", "1. Investigate the crime scene.", "2. Follow them further.", "3. Arrest them.",)
        follow()
    elif choice == "3":
        talk= input("You talk to the figures. They turn out to be Elisa Maza and Matt Bluestone returning from a mission. What do you do?", "1. Apologize.", "2. Ask them about the mission.", "3. Invite them to the castle.")
        talk()
    elif choice == "4":
        Arrest= input("You decide to arrest the figures. They turn out to not be thieves. What do you do?", "1. Let them go.","2. Talk to them.", "3. Become friends.")
        Arrest()
    else:
        print("Invalid choice. Please choose 1 or 2 or 3or 4.")
        patrol_city()

def stay_castle():
    print("You decide to stay at the castle. Suddenly, you hear a noise. What do you do?")
    print("1. Investigate the noise.")
    print("2. Ignore it.")
    choice = input("> ")

    if choice == "1":
        investigate= input("You investigate the noise. It turns out to be a group of thieves. What do you do?", "1. Fight them.", "2. Let them go.", "3. Talk to them.", "4. Arrest them.", "5. Follow them.", "6. Check them for weapons.")or input("You investigate the noise. It turns out to be Elisa Maza and Angela. What do you do?", "1. Apologize.", "2. Ask them about the noise.", "3. Invite them to the library.", "4. be romantic with Elisa.", "5. Ask Angela what she wants to do.", "6. have a clan meeting")
        investigate()
    elif choice == "2":
        ignore= input("You ignore the noise. It turns out to be nothing. What do you do?", "1. Go to sleep.", "2. Train.", "3. Read a book.", "4. Eat.", "5. Talk to your clan.", "6. Go to the city.")or input("You ignore the noise. It turns out to be the clan. What do you do?", "1. Have a clan meeting.", "2. Train.", "3. Read a book.", "4. Eat.", "5. Talk to your clan.", "6. Go to the city.")
        ignore()
    elif choice == "3":
        talk= input("You talk to the figures. They turn out to be Fox and baby Alexander. What do you do?", "1. Apologize.", "2. Ask them about the noise.", "3. Invite them to the library.", "4. Play with Alexander.", "5. Ask Fox about her day.", "6. Go to the city.")
        talk()
    else:
        print("Invalid choice. Please choose 1 or 2 or 3.")
        stay_castle()

# Add more functions for each choice


start_game()