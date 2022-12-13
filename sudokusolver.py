from typing import Tuple, List
def get_block_num(sudoku:List[List[int]],pos:Tuple[int, int]) -> int:
    a=(pos[0]-1)//3
    b=(pos[1]-1)//3
    return a*3+b+1

def get_position_inside_block(sudoku:List[List[int]],pos:Tuple[int, int]) -> int:
       a=(pos[0]-1)%3  
       b=(pos[1]-1)%3
       return (a)*3+b+1
def get_block(sudoku:List[List[int]], x: int) -> List[int]:
    a=(x-1)//3
    b=a*3
    c=(x-1)%3
    lst=[]
    e=c*3  
    for i in range(b,b+3):
        for j in range(e,e+3):
            lst.append(sudoku[i][j])
    return lst

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
    a=[]
    for j in range (0,9):
        a.append(sudoku[i-1][j])
    return a

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
    a=[]
    for j in range (0,9):
        a.append(sudoku[j][x-1])
    return a

def findfirst_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
    for i in range(8,-1,-1):
        for j in range(0,9):
            if(sudoku[j][i]==0):
                return((j+1,i+1))
    
    return((-1,-1))

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
    for i in range(0,9):
        for j in range(0,9):
            if(sudoku[i][j]==0):
                return((i+1,j+1))
    
    return((-1,-1))

def valid_list(lst: List[int])-> bool:
    freq=[0,0,0,0,0,0,0,0,0,0]
    for i in range (0,9):
        a=lst[i]
        freq[a]+=1 
    for i in range(1,10):
        if(freq[i]>1):
            return False
    return True 

def valid_sudoku(sudoku:List[List[int]])-> bool:
    for i in range(0,9):
        flag=valid_list(sudoku[i])
    a=[]
    for i in range(0,9):
        for j in range(0,9):
            a.append(sudoku[j][i])
    flag=valid_list(a)
    for x in range(1,10):
        a1=(x-1)//3
        b=a1*3
        c=(x-1)%3
        lst=[]
        e=c*3
        for i in range(b,b+3):
            for j in range(e,e+3):
                lst.append(sudoku[i][j])
        flag=valid_list(lst)
    return flag

def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
    a=[]
    for i in range(1,10):
        b=get_row(sudoku,pos[0])
        c=get_column(sudoku,pos[1])
        x=get_block_num(sudoku,pos)
        d=get_block(sudoku,x)
        if((i not in b) and (i not in c) and (i not in d)):
            a.append(i)
    return a
def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
    a=pos[0]
    b=pos[1]
    sudoku[a-1][b-1]=num
    return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
    a=pos[0]
    b=pos[1]
    sudoku[a-1][b-1]=0
    return sudoku 

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
    # """ This is the main Sudoku solver. This function solves the given incomplete Sudoku and returns 
    # true as well as the solved sudoku if the Sudoku can be solved i.e. after filling all the empty positions the Sudoku remains valid.
    # It return them in a tuple i.e. `(True, solved_sudoku)`.

    # However, if the sudoku cannot be solved, it returns False and the same sudoku that given to solve i.e. `(False, original_sudoku)`
    # """
    # your code goes here

    # to complete this function, you may define any number of helper functions.
    # However, we would be only calling this function to check correctness.

    # return (False, sudoku)
  
    a=findfirst_unassigned_position(sudoku)
    i=a[0]
    j=a[1]
    if(i==-1 and j==-1):
        return (True,sudoku)
    b=get_candidates(sudoku,a)
    b.sort(reverse=True)
    for k in b:
        make_move(sudoku,a,k)
        flag,sudoku=sudoku_solver(sudoku)
        if(flag):
            return (True,sudoku)
        else:
            undo_move(sudoku,a)
    return (False,sudoku)

def input_sudoku() -> List[List[int]]:
    sudoku= list()
    for _ in range(9):
        row = list(map(int, input().rstrip(" ").split(" ")))
        sudoku.append(row)
    return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end = " ")
        print()
def in_lab_component(sudoku: List[List[int]]):
    print("Testcases for In Lab evaluation")
    print("Get Block Number:")
    print(get_block_num(sudoku,(4,4)))
    print(get_block_num(sudoku,(7,2)))
    print(get_block_num(sudoku,(2,6)))
    print("Get Block:")
    print(get_block(sudoku,3))
    print(get_block(sudoku,5))
    print(get_block(sudoku,9))
    print("Get Row:")
    print(get_row(sudoku,3))
    print(get_row(sudoku,5))
    print(get_row(sudoku,9))

if __name__ == "__main__":

    # Input the sudoku from stdin
    sudoku = input_sudoku()

    # Try to solve the sudoku
    possible, sudoku = sudoku_solver(sudoku)

    # The following line is for the in-lab component
    in_lab_component(sudoku)
    # Show the result of the same to your TA to get your code evaulated

    # Check if it could be solved
    if possible:
        print("Found a valid solution for the given sudoku :)")
        print_sudoku(sudoku)

    else:
        print("The given sudoku cannot be solved :(")
        print_sudoku(sudoku)