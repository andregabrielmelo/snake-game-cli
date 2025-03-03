class Menu:
    def __init__(self):
        self.playing = False
        self.menu()

    def menu(self):
        self.displayMenu()
        choice: int = int(self.promptOption())

        match choice:
            case 1:
                self.startGame()
            case 2:
                self.showInstructions()
            case 3:
                print("Goodbye!")
                return
            case _:
                print("Invalid option, try again.")
                self.menu()

        
    def displayMenu(self) -> str:
        """Return menu options"""

        menu = "1. Start Game\n2. Instructions\n3. Quit"
        print(menu)
        return menu
    
    def promptOption(self, question="Option: ") -> any:
        while True:
            try:
                return input(f"{question}")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def startGame(self):
        """Start the game"""

        self.playing = True

    def showInstructions(self):
        instructions = "Eat. Grow. Repeat."
        print(instructions)

        while(self.promptOption("Click enter to return to menu...") != ""):
            continue
        
        self.menu()


