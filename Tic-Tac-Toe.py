import random
import time

class TicTacToe_grid:
    def __init__(self):
        self.grid: list[str] = [" "," "," ",
                                " "," "," ",
                                " "," "," "]
        self.player_symbol = ""
        self.ai_symbol = ""
    
    def make_grid(self):
        for i in range(3):  #Rows
            print(f"{self.grid[3*i]} | {self.grid[3*i+1]} | {self.grid[3*i+2]}")
            if i < 2:
                print("-----------")

    def get_indexes(self):
        indexes = [i for i in range(len(self.grid)) if self.grid[i] == " "]
        return indexes
    
    def symbol(self):
        while self.player_symbol not in ['X','O']:
            self.player_symbol = input("Please choose your symbol: X or O\n").upper()
            if self.player_symbol not in ['X','O']:
                print("Invalid Choice. Please choose again\n")
            if self.player_symbol == "X":
                self.ai_symbol = "O"
            else:
                self.ai_symbol = "X"
        return self.player_symbol, self.ai_symbol

    def update_grid(self, symbol: str, index: int):
        self.grid[index] = self.grid[index].replace(" ", f"{symbol}")

class TicTacToe_game:
    def __init__(self):
        self.turns: int = 0
        self.player_symbol: str = ""
        self.ai_symbol: str = ""
        self.play: bool = True
    
    def game_turns(self):
        print('\n')
        if self.turns % 2 == 0:
            print("Player turn")
        else:
            print("Ai turn")
        return self.turns

    def gameplay(self, indexes: list[int]):
        if self.turns % 2 == 0:
            grid_choice = int(input(f"Choose a grid to place symbol: {indexes}\n"))
            self.turns += 1
        else:
            grid_choice = random.choice(indexes)
            time.sleep(3)
            self.turns += 1
        return grid_choice

    def winner(self, grid: list[str]):
        if self.turns <= 9:
            for i in range(0, 9, 3):
                if grid[i] != " " and grid[i] == grid[i+1] == grid[i+2]:
                    print(f"{grid[i]} wins!")
                    return True
            for i in range(3):
                if grid[i] != " " and grid[i] == grid[i+3] == grid[i+6]:
                    print(f"{grid[i]} wins!")
                    return True
            if grid[0] != " " and grid[0] == grid[4] == grid[8]:
                print(f"{grid[4]} wins!")
                return True
            if grid[2] != " " and grid[2] == grid[4] == grid[6]:
                print(f"{grid[4]} wins!")
                return True
            elif self.turns == 9:
                print("It's a tie.\n")
            else:
                return False
            return True

    def play_again(self):
        again = str(input("\nDo you want to play Tic Tac Toe? Yes/No?\n"))
        if again.upper() == "YES":
            self.play = True
        else:
            self.play = False
        return self.play

            
tic_tac_toe = TicTacToe_grid()
game = TicTacToe_game()

while game.play_again():
    symbol = tic_tac_toe.symbol()
    while not game.winner(tic_tac_toe.grid):
        turns = game.game_turns()
        tic_tac_toe.make_grid()
        choices = tic_tac_toe.get_indexes()
        choice = game.gameplay(choices)
        if turns % 2 == 0:
            tic_tac_toe.update_grid(symbol=tic_tac_toe.player_symbol, index=choice)
        else:
            tic_tac_toe.update_grid(symbol=tic_tac_toe.ai_symbol, index=choice)