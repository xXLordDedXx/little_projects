class TicTacToe_grid:
    def __init__(self):
        self.grid: list[str] = [" 0 "," 1 "," 2 ",
                                " 3 "," 4 "," 5 ",
                                " 6 "," 7 "," 8 "]
    
    def make_grid(self):
        print('\n')
        for i in range(3):  #Rows
            print(f"{self.grid[3*i]} | {self.grid[3*i+1]} | {self.grid[3*i+2]}")
            if i < 2:
                print("----x-----x----")


TicTacToe_grid().make_grid()