class Input:
    #Create List of Commands
    def __init__(self):
        with open('input.txt', "r") as f:
            self.listOfCommands = [line.rstrip('\n') for line in f]
            
    #Return listOfCommands
    def __main__(self):
        return self.listOfCommands

class Submarine:
    def __init__(self):
        #Create variables for horizontal and vertical positioning
        self.horizontal_position = 0
        self.depth = 0
        
        #Get commands from input
        self.commands = Input().__main__()

        #Pull data from list of commands
        for command in self.commands:
            data = command.split(" ", 2)
            #Decrease Depth
            if data[0] == "up":
                self.depth += (int(data[1])* -1)
            #Increase Depth
            elif data[0] == "down":
                self.depth += int(data[1])
            #Increase Horizontal_position
            else:
                self.horizontal_position += int(data[1])
            
sub = Submarine()
print(f'P1 H: {sub.horizontal_position} D: {sub.depth}\n Product: {sub.horizontal_position * sub.depth}')




        
