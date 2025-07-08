from random import randrange

FINISH_FAILURE=-1
FINISH_SUCCESS=1
NOT_FINISH=0
#function that fets a board and a location and returns a list of all possible digits for this location
def options(board:list,loc:tuple)->list:
    posibble_dig=[1,2,3,4,5,6,7,8,9]
    #checks the row
    if (board[loc[0]][loc[1]]!=-1):
        return []
    for dig in board[loc[0]]:
        if (dig!=-1 and dig in posibble_dig):
            posibble_dig.remove(dig)
    #checks the column
    for i in range(9):
        dig=board[i][loc[1]]
        if (dig!=-1 and dig in posibble_dig):
            posibble_dig.remove(dig)
    square_row=(loc[0]//3)*3
    square_column=(loc[1]//3)*3
    #checks the 3x3 table
    for i in range(square_row,square_row+3,1):
        for j in range(square_column,square_column+3,1):
            dig=board[i][j]
            if (dig!=-1 and dig in posibble_dig):
                posibble_dig.remove(dig)
    if(len(posibble_dig)==0):
        return None
    return posibble_dig

#The function gets a board and returns a board where every empty space is replaced with a list of possible options for that location.
def possible_digits(board:list)->list:
    new_board=[]
    for i in range(9):
        new_board.append([])
        for j in range(9):
            new_board[i].append([])
            if(board[i][j]!=-1):
                continue
            else:
                option_lst=options(board,(i,j))
                if(option_lst!=[]):
                    new_board[i][j]=option_lst
                else:
                    new_board[i][j].append(None)
    return new_board

#function that gets a Sudoku board, an options board, and a position where there is only one possible option.
#The function updates both boards and checks that the board is legal.
def board_update_and_check(board:list,possibilities:list,loc:tuple)->tuple:
    board[loc[0]][loc[1]]=possibilities[loc[0]][loc[1]][0]
    possibilities=possible_digits(board)
    for i in range(9):
        for j in range(9):
            if (possibilities[i][j]==None):
                return False,board,possibilities
    return True,board,possibilities

#The function gets a board and an options board, updates both boards as much as possible, and returns accordingly.
def one_stage(board:list,possibilities:list)->tuple:
    min_length,length=10,0
    is_legal,finish=True,False
    while(not finish):
        finish=True
        for i in range(9):
            for j in range(9):
                cur_cordinates=i,j
                length=len(possibilities[i][j])
                if(length==1):
                    is_legal,board,possibilities=board_update_and_check(board,possibilities,cur_cordinates)
                    if(not is_legal):
                        return FINISH_FAILURE,None
                    finish=False
                    break
                elif(length>1):
                    if(length<min_length):
                        min_length=length
                        min_cordinates=cur_cordinates
            if(not finish):
                min_length=10
                break
    if(min_length>0 and min_length!=10):
        return NOT_FINISH,min_cordinates
    else:
        return FINISH_SUCCESS,None

#The function gets a board and an options board and attempts to fill the board according to the rules.
#the function will allow the user to choose one of the options for the location with the minimum number of possibilities.
def fill_board(board:list,possibilities:list):
    finish = False
    while(not finish):
        finish=True
        method,loc=one_stage(board,possibilities)
        possibilities=possible_digits(board)
        if (method==NOT_FINISH):
            pos_lst = possibilities[loc[0]][loc[1]]
            finish=False
            while(not finish):
                print("Choose one number from:",pos_lst,"for the location:",loc)
                choice=int(input("Your choice: "))
                if choice in pos_lst:
                    possibilities[loc[0]][loc[1]]=[choice]
                    finish=True
            finish=False
    if(method==FINISH_FAILURE):
        return FINISH_FAILURE
    else:
        return FINISH_SUCCESS

#function that עקאד a board and returns a board with random values.
def create_random_board(board:list)->list:
    #resets the Sudoku and builds the list of positions
    board.clear()
    loc_list=[(r,c) for r in range(9) for c in range(9)]
    for i in range(9):
        board.append([])
        for j in range(9):
            board[i].append(-1)
    n=randrange(10,20)
    for i in range(n):
        k=randrange(1,len(loc_list))
        r,c=loc_list[k-1]
        loc_list.remove(loc_list[k-1])
        finish=False
        while (not finish):
            dig=randrange(1,9)
            if (dig in options(board,(r,c))):
                board[r][c]=dig
                finish=True
    return board

#function that gets a Soduko board and printing it
def print_board(board:list):
    for i in range(9):
        for j in range(9):
            if board[i][j]==-1:
                board[i][j]=' '
            board[i][j]=str(board[i][j])
    print('-----------------')
    for i in range(9):
        row='|'.join(board[i])
        print(row)
        print('-----------------')
#function that checks whether the given board is valid in terms of duplicates.
def is_legit(board:list)->bool:
    counters=[0 for i in range(10)]
    for i in range(9):
        #checks the rows
        for dig in board[i]:
            if dig!=-1:
                counters[dig]+=1
        for j in counters:
            if j>1:
                return False
        counters = [0 for i in range(10)]
        #checks the columns
        for j in range(9):
            if board[j][i]!=-1:
                counters[board[j][i]]+=1
        for j in counters:
            if j>1:
                return False
        counters = [0 for i in range(10)]
    #checks the 3x3 tables
    square_row, square_col = 0, 0
    for t in range(9):
        for i in range(square_row, square_row + 3, 1):
            for j in range(square_col, square_col + 3, 1):
                if board[i][j]!=-1:
                    counters[board[i][j]]+=1
        for j in counters:
            if j>1:
                return False
        counters = [0 for i in range(10)]
        if square_row<6:
            square_row+=3
        else:
            square_row=0
            square_col+=3
    return True

#The function will take a board and a file name and print the board to the file.
def print_board_to_file(board:list,file_name:str):
    f = open(file_name, "a")
    if(not is_legit(board)):
        f.write("Board is not legit\n")
    elif (fill_board(board, possible_digits(board)) == FINISH_SUCCESS):
        for i in range(9):
            for j in range(9):
                board[i][j]=str(board[i][j])
        f.write("Here is the solved board!\n")
        f.write('-----------------\n')
        for i in range(9):
            row='|'.join(board[i])
            f.write(row)
            f.write("\n-----------------\n")
    else:
        f.write("Board is unsolvable\n")
    f.close()

#*********************main*************************
soduko1=[[5,3,-1,-1,7,-1,-1,-1,-1],
 [6,-1,-1,-1,-1,-1,1,-1,-1],
 [-1,-1,9,-1,-1,-1,-1,6,-1],
 [-1,-1,-1,-1,6,-1,-1,-1,3],
 [-1,-1,-1,8,-1,3,-1,-1,1],
 [-1,-1,-1,-1,-1,-1,-1,-1,-1],
 [-1,6,-1,-1,-1,-1,-1,-1,-1],
 [-1,-1,-1,-1,1,-1,-1,-1,-1],
 [-1,-1,-1,-1,8,-1,-1,-1,9]]
soduko2=[[5,3,4,6,7,8,9,1,2],
 [6,7,2,1,9,5,3,4,8],
 [1,9,8,3,4,2,5,6,7],
 [8,5,9,7,6,1,4,2,3],
 [4,2,6,8,5,3,7,9,1],
 [7,1,3,9,2,4,8,5,6],
 [9,6,1,5,3,7,2,8,4],
 [2,8,7,4,1,9,6,3,5],
 [3,4,5,2,8,6,1,7,9]]
soduko3=[[5,1,6,8,4,9,7,3,2],
 [3,-1,7,6,-1,5,-1,-1,-1],
 [8,-1,9,7,-1,-1,-1,6,5],
 [1,3,5,-1,6,-1,9,-1,7],
 [4,7,2,5,9,1,-1,-1,6],
 [9,6,8,3,7,-1,-1,5,-1],
 [2,5,3,1,8,6,-1,7,4],
 [6,8,4,2,-1,7,5,-1,-1],
 [7,9,1,-1,5,-1,6,-1,8]]
soduko4=[[5,3,4,6,7,8,9,1,2],
 [6,7,2,1,9,5,3,4,9],
 [1,9,8,3,4,2,5,6,7],
 [8,5,9,7,6,1,4,2,3],
 [4,2,6,8,5,3,7,9,1],
 [7,1,3,9,2,4,8,5,6],
 [9,6,1,5,3,7,2,8,4],
 [2,8,7,4,1,9,6,3,5],
 [3,4,5,2,8,6,1,7,9]]
soduko5=[[5,3,4,6,7,8,9,1,2],
 [6,7,2,1,9,5,3,4,8],
 [1,9,8,3,4,2,5,6,7],
 [-1,-1,-1,7,6,1,4,2,3],
 [-1,-1,-1,8,5,3,7,9,1],
 [-1,-1,-1,9,2,4,8,5,6],
 [-1,-1,-1,-1,3,7,2,8,4],
 [-1,-1,-1,-1,1,9,6,3,5],
 [-1,-1,-1,-1,8,6,1,7,9]]
f=open("solved_soduko","w")
print_board_to_file(soduko1,"solved_soduko")
print_board_to_file(soduko2,"solved_soduko")
print_board_to_file(soduko3,"solved_soduko")
print_board_to_file(soduko4,"solved_soduko")
print_board_to_file(soduko5,"solved_soduko")
print_board_to_file(create_random_board([]),"solved_soduko")
f.close()