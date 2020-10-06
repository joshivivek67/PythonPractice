import random
class Gameboard:
    def __init__(self,lst):
        self.lst=lst
        
    def PrintBoard(self):
        print("  |  |  ")
        print("__ __ __ ")
        print(" "+self.lst[1]+"|"+self.lst[2]+" |"+self.lst[3]+"  ")
        print("__ __ __ ")
        print(" "+self.lst[4]+"|"+self.lst[5]+" |"+self.lst[6]+"  ")
        print("__ __ __ ")
        print(" "+self.lst[7]+"|"+self.lst[8]+" |"+self.lst[9]+"  ")
        print("__ __ __ ")
        print("  |  |  ")
    
    def UpdateBoard(self,player,marker):
        self.marker=marker
        position=int(input('{} Choose your position: (1-9) '.format(player)))
        while True:
            if position in [1,2,3,4,5,6,7,8,9] and self.lst[position]==" ":
                self.lst[position]= marker
                break
            else:
                print("Position already filled,choose another position")
                position=int(input("enter other position: "))
                
    def CheckWin(self,mark):
        return ((self.lst[7] == mark and self.lst[8] == mark and self.lst[9] == mark) or # across the top
                (self.lst[4] == mark and self.lst[5] == mark and self.lst[6] == mark) or # across the middle
                (self.lst[1] == mark and self.lst[2] == mark and self.lst[3] == mark) or # across the bottom
                (self.lst[7] == mark and self.lst[4] == mark and self.lst[1] == mark) or # down the middle
                (self.lst[8] == mark and self.lst[5] == mark and self.lst[2] == mark) or # down the middle
                (self.lst[9] == mark and self.lst[6] == mark and self.lst[3] == mark) or # down the right side
                (self.lst[7] == mark and self.lst[5] == mark and self.lst[3] == mark) or # diagonal
                (self.lst[9] == mark and self.lst[5] == mark and self.lst[1] == mark)) # diagonal
    
    def BoardFull(self):
        if " " not in self.lst:
            return True
        else:
            return False
        
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')    

class Player:
    def __init__(self,name1,name2):
        self.name1=name1
        self.name2=name2
        
    def GoFirst(self):
        data={self.name1:0,self.name2:1}
        turn=random.randint(0,1)
        for name, num in data.items():
            if num==turn:
                print(name+" will go first")
                return name
            
    def SymbolSelector(self):
        symbols= ["X", "O"]
        symbol1=input("{} Please choose x or o: ".format(self.name1)).upper()
        print(self.name1+" gets "+symbol1)
        symbol2=[x for x in symbols if x != symbol1][0]
        print(self.name2+" gets "+symbol2)
        return {self.name1:symbol1,self.name2:symbol2}
    
print('Welcome to Tic Tac Toe!')
while True:
    theBoard=[" "]*10
    player1Name=input("Enter player1 name: ")
    player2Name=input("Enter player2 name: ")
    players=Player(player1Name,player2Name)
    symbolDict=players.SymbolSelector()
    print(symbolDict)
    turnFirst=players.GoFirst()
    board=Gameboard(theBoard)
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turnFirst == player1Name:
            board.PrintBoard()
            board.UpdateBoard(player1Name,symbolDict[player1Name])
            board.PrintBoard()
            
            if board.CheckWin(symbolDict[player1Name]):
                print('{} Congratulations! You have won the game!'.format(player1Name))
                game_on = False
            else:
                if board.BoardFull():
                    print('The game is a draw!')
                    break
                else:
                    turnFirst = player2Name
                
        else:
            print(symbolDict[player2Name])
            board.UpdateBoard(player2Name,symbolDict[player2Name])
            board.PrintBoard()
            
            if board.CheckWin(symbolDict[player2Name]):
                print('{} Congratulations! You have won the game!'.format(player2Name))
                game_on = False
            else:
                if board.BoardFull():
                    print('The game is a draw!')
                    break
                else:
                    turnFirst = player1Name

            
                
    if not replay():
        break
