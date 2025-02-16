
board = [[],
         [],
         [],
         [],
         [],
         [],
         [],
         [],
         []]

def generate_domains(board):
    domains = {
    }
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                domains[(i, j)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return(domains)

def game_over(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return True
    return False

def input_numbers(board):
    for i in range(9):
        board[i] = input('>').split()
    return board

def domain_customization(domains, board):
    neighbours = [[(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)],
                  [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)],
                  [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)],
                  [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)],
                  [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)],
                  [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)],
                  [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)],
                  [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)],
                  [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)],]
    for index in domains:
        for neighbour in neighbours:
            if index in neighbour:
                for i in neighbour:
                    if board[i[0]][i[1]] in domains[index]:
                        domains[index].remove(board[i[0]][i[1]])
                break
            
        i = index[0]
        j = index[1]
        for x in range(9):
            if board[x][j] in domains[(index)]:
                domains[index].remove(board[x][j])
        for y in range(9):
            if board[i][y] in domains[(index)]:
                domains[index].remove(board[i][y])
    return domains
        
def add_values(board, domains):
    for index in domains:
        if len(domains[index]) == 1:
            board[index[0]][index[1]] = domains[index][0]
    return(board)




board = input_numbers(board)
domains = generate_domains(board)
while game_over(board):
    domains = domain_customization(domains, board)
    board = add_values(board, domains)

for i in board:
    for j in i:
        print(j,sep='',end=' ')
    print()
