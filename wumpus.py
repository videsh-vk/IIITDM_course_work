class World:
    def __init__(self):
        self.world = [[(i,j) for i in range(4)] for j in range(4)]
        self.player_position = (0,0)
        self.wumpus_position = (2,0)
        self.arrows = 1
        self.pits = [(0,2),(2,2),(3,3)]
        self.GOLD_GRABBED = False
        
        #sensor information
        self.senses = {
            (0,0):None,
            (0,1):["BREEZE"],
            (0,2):None,
            (0,3):["BREEZE"],
            (1,0):["STENCH"],
            (1,1):None,
            (1,2):["BREEZE"],
            (1,3):None,
            (2,0):None,
            (2,1):["GLITTER","BREEZE","GOLD"],
            (2,2):None,
            (2,3):["BREEZE"],
            (3,0):["STENCH"],
            (3,1):None,
            (3,2):["BREEZE"],
            (3,3):None
        }
        self.facing = 'e'
    
    
    def move(self,curr,direc):
        if direc=='w':
            self.facing = direc
            return (curr[0]-1,curr[1])
        elif direc=='e':
            self.facing = direc
            return (curr[0]+1,curr[1])
        elif direc=='s':
            self.facing = direc
            return (curr[0]+1,curr[1])
        else:
            self.facing = direc
            return (curr[0]+1,curr[1])
        
    def shoot(self):
        curr = self.player_position
        facing = self.facing
        while True:
            arrow_pos = self.move(curr,facing)
            if arrow_pos == self.wumpus_position:
                self.arrows = 0
                self.wumpus_position = (-2,-2)
                return 1
            elif arrow_pos[0] not in range(4) or arrow_pos[1] not in range(4):
                self.arrows = 0
                return 0
    
    def play(self):
        print("Welcome to wumpus world!!")
        while True:
            if self.player_position == (0,0) and self.GOLD_GRABBED:
                print("You won")
                return
            
            if self.player_position in self.pits:
                print("You fell into pit and died")
                return
            elif self.player_position == self.wumpus_position:
                print("Wumpus ate you and you died")
                return
            else:
                print(f"Your current position: {self.player_position}")
                print(f"Senses in current position: {self.senses[self.player_position]}")
                
                option = input("Press 1 to move and Press 2 to perform action: ")
                if option == "1":
                    direction = input("Press the direction you want to move: ")
                    self.player_position = self.move(self.player_position,direction)
                else:
                    action = input("Press G to grab and S to shoot: ")
                    if action == "G":
                        if "GLITTER" not in self.senses[self.player_position]:
                            print("Nothing to grab")
                        else:
                            print("You got the gold, get out of cave")
                            self.GOLD_GRABBED = True
                    else:
                        if self.arrows == 0:
                            print("You have no arrows to shoot")
                        else:
                            result = self.shoot()
                            if result==1:
                                print("You killed the wumpus")
                            else:
                                print("Your arrow hitted the wall")

world = World()
world.play()