import random
start=[]
white=[]
black=[]
score = [0,0]
for x in range(100):
    print("\nRound",x+1)
    for i in range(8):
        for j in range(8):
            start.append([i,j])
    random.shuffle(start)
    white = start[0]
    white[0] += 1
    white[1] += 1

    black = start[10]
    black[0] += 1
    black[1] += 1
    start=[]

    print("The white Rook is in row:",white[0]," and column:",white[1])
    while white != black:
        print("The black Bishop is now in row:",black[0]," and column:",black[1])
        print("It's white's turn, imput target row and column:")
        row=int(input())
        col=int(input())
        while (white[0] == row and white[1] == col) or (white[0] != row and white[1] != col) or (0>=row or row>=9) or (0>=col or col>=9):
            print("Illegal move, imput new target row and column")
            row=int(input())
            col=int(input())
        white[0] = row
        white[1] = col
        if  white == black :
            score[0] += 1 
            print("White won !")
            break
        print("The white Rook is in row:",white[0]," and column:",white[1])
        print("It's black's turn, imput target row and column")
        row=int(input())
        col=int(input())
        rowsplit=abs(black[0]-row)
        colsplit=abs(black[1]-col)
        while rowsplit != colsplit or black[0] == row or (0>=row or row>=9) or (0>=col or col>=9):
            print("Illegal move, imput new target row and column")
            row=int(input())
            col=int(input())
            rowsplit=abs(black[0]-row)
            colsplit=abs(black[1]-col)
        black[0] = row
        black[1] = col
        if  white == black :
            score[1] += 1 
            print("Black won !")
print("The score is  White:",score[0],"-",score[1],"Black")
print("White won!") if score[0] > score[1] else print("It's a tie.") if score[0] == score[1] else print("Black won!")
#
print("\n New Game, Board size is now 7x7")
white=[]
black=[]
score = [0,0]
for x in range(100):
    print("\nRound",x+1)
    for i in range(7):
        for j in range(7):
            start.append([i,j])
    random.shuffle(start)
    white = start[0]
    white[0] += 1
    white[1] += 1
    black = start[10]
    black[0] += 1
    black[1] += 1
    start=[]
    print("The white Rook is in row:",white[0]," and column:",white[1])
    while white != black:
        print("The black Bishop is now in row:",black[0]," and column:",black[1])
        print("It's white's turn, imput target row and column:")
        row=int(input())
        col=int(input())
        while (white[0] == row and white[1] == col) or (white[0] != row and white[1] != col) or (0>=row or row>=8) or (0>=col or col>=8):
            print("Illegal move, imput new target row and column")
            row=int(input())
            col=int(input())
        white[0] = row
        white[1] = col
        if  white == black :
            score[0] += 1 
            print("White won !")
            break
        print("The white Rook is in row:",white[0]," and column:",white[1])
        print("It's black's turn, imput target row and column")
        row=int(input())
        col=int(input())
        rowsplit=abs(black[0]-row)
        colsplit=abs(black[1]-col)
        while rowsplit != colsplit or black[0] == row or (0>=row or row>=8) or (0>=col or col>=8):
            print("Illegal move, imput new target row and column")
            row=int(input())
            col=int(input())
            rowsplit=abs(black[0]-row)
            colsplit=abs(black[1]-col)
        black[0] = row
        black[1] = col
        if  white == black :
            score[1] += 1 
            print("Black won !")
print("The score is  White:",score[0],"-",score[1],"Black")
print("White won!") if score[0] > score[1] else print("It's a tie.") if score[0] == score[1] else print("Black won!")
#
print("\n New Game, Board size is now 7x8")
white=[]
black=[]
score = [0,0]
for x in range(100):
    print("\nRound",x+1)
    for i in range(7):
        for j in range(8):
            start.append([i,j])
    random.shuffle(start)
    white = start[0]
    white[0] += 1
    white[1] += 1
    black = start[10]
    black[0] += 1
    black[1] += 1
    start=[]
    print("The white Rook is in row:",white[0]," and column:",white[1])
    while white != black:
        print("The black Bishop is now in row:",black[0]," and column:",black[1])
        print("It's white's turn, imput target row and column:")
        row=int(input())
        col=int(input())
        while (white[0] == row and white[1] == col) or (white[0] != row and white[1] != col) or (0>=row or row>=8) or (0>=col or col>=9):
            print("Illegal move, imput new target row and column")
            row=int(input())
            col=int(input())
        white[0] = row
        white[1] = col
        if  white == black :
            score[0] += 1 
            print("White won !")
            break
        print("The white Rook is in row:",white[0]," and column:",white[1])
        print("It's black's turn, imput target row and column")
        row=int(input())
        col=int(input())
        rowsplit=abs(black[0]-row)
        colsplit=abs(black[1]-col)
        while rowsplit != colsplit or black[0] == row or (0>=row or row>=8) or (0>=col or col>=9):
            print("Illegal move, imput new target row and column")
            row=int(input())
            col=int(input())
            rowsplit=abs(black[0]-row)
            colsplit=abs(black[1]-col)
        black[0] = row
        black[1] = col
        if  white == black :
            score[1] += 1 
            print("Black won !")
print("The score is  White:",score[0],"-",score[1],"Black")
print("White won!") if score[0] > score[1] else print("It's a tie.") if score[0] == score[1] else print("Black won!")
