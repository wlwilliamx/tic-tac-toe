# 玩家下棋
def player_play():
    global board, EMPTY
    for i in range(9):
        print(" ", end='')
        if board[i] == PLAYER:
            print("X ", end='')
        elif board[i] == COMPUTER:
            print("O ", end='')
        else:
            print("  ", end='')
        if (i + 1) % 3 != 0:
            print("|", end='')
        elif i != 8:
            print("\n-----------")
    print("\nPlease choose your next :")
    p = int(input())
    if board[p-1] != 0:
        print("That square is not empty, please choose again")
        player_play()
        return
    board[p-1] = PLAYER
    EMPTY = EMPTY - 1


# 判断游戏是否结束
def is_end():
    if EMPTY == 0:
        return True
    ans = utility()
    if ans != 0:
        return True
    else:
        return False


# 输出游戏结果
def result():
    winner = utility()
    if winner == PLAYER:
        print("\nYou win !!!")
    elif winner == COMPUTER:
        print("\nThe computer win")
    else:
        print("\nDraw")


# 效用函数
def utility():
    if board[0] == board[4] and board[0] == board[8]:
        return board[0]
    if board[2] == board[4] and board[2] == board[6]:
        return board[2]
    for i in range(0, 9, 3):
        if board[i] == board[i+1] and board[i] == board[i+2]:
            return board[i]
    for i in range(3):
        if board[i] == board[i + 3] and board[i] == board[i + 6]:
            return board[i]
    return 0


# 搜索 MIN 的最佳选择（极小值）
def min_val(alpha, beta):
    global board, EMPTY
    if is_end():
        return utility()
    parent = code()
    if parent in record:
        return record[parent][1]
    v = INF
    step = 0
    for i in range(9):
        if board[i] == 0:
            board[i] = PLAYER
            EMPTY = EMPTY - 1
            m = max_val(alpha, beta)
            if m < v:
                v = m
                step = i
            board[i] = 0
            EMPTY = EMPTY + 1
            if v <= alpha:
                record[parent] = [step, v]
                return v
            beta = min(beta, v)
    record[parent] = [step, v]
    return v


# 搜索 MAX 的最佳选择（极大值）
def max_val(alpha, beta):
    global board, EMPTY
    if is_end():
        return utility()
    parent = code()
    if parent in record:
        return record[parent][1]
    v = -INF
    step = 0
    for i in range(9):
        if board[i] == 0:
            board[i] = COMPUTER
            EMPTY = EMPTY - 1
            m = min_val(alpha, beta)
            if m > v:
                v = m
                step = i
            board[i] = 0
            EMPTY = EMPTY + 1
            if v >= beta:
                record[parent] = [step, v]
                return v
            alpha = max(alpha, v)
    record[parent] = [step, v]
    return v


# 基于极小极大算法采用 α-β 剪枝
def alpha_beta_search():
    max_val(-INF, INF)
    return record[code()][0]


# 电脑下棋
def computer_play():
    global board, EMPTY
    v = alpha_beta_search()
    print("The computer choose", v+1, "\n")
    board[v] = COMPUTER
    EMPTY = EMPTY - 1


# 将棋盘转换成 ID
def code():
    v = 0
    for i in board:
        v = v * 10 + i
    return v


# player is -1, computer is 1
PLAYER = -1
COMPUTER = 1
board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]
EMPTY = 9  # 棋盘上空格子的数量
INF = 1e9
record = {}  # 记录已经遍历过的状态，并将他的下一步和其效用值绑定存储
print("\nYou are 'X', the computer is 'O'\nYou have to enter a num[1~9] to put your chess")
print("Do you want to start first ? (y/n)")
while True:
    c = input()
    if c == "y" or c == "Y":
        break
    elif c == "n" or c == "N":
        computer_play()
        break
    else:
        print("Input error, Please enter again")
while not is_end():
    player_play()
    if is_end():
        break
    else:
        computer_play()
result()
