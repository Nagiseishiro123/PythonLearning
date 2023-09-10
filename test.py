
EMPTY = "-"
PLAYER = "X"
COMPUTER = "O"

def draw_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board):
    # row
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != EMPTY:
            return row[0]

    # col
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[col][0] != EMPTY for row in range(len(board))):
            return board[0][col]

    # main diag
    if all(board[i][i] == board[0][0] and board[i][i] != EMPTY for i in range(len(board))):
        return board[0][0]

    # 2nd diag
    if all(board[i][len(board)-1-i] == board[0][len(board)-1] and board[i][len(board)-1-i] != EMPTY for i in range(len(board))):
        return board[0][len(board)-1]

    # null
    return None

# init
def create_board():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    # Kiểm tra nếu trạng thái hiện tại là trạng thái kết thúc hoặc đã đạt đến độ sâu tối đa
    winner = check_win(board)
    if winner is not None:
        if winner == COMPUTER:
            return 1
        else:
            return -1
    elif not any(EMPTY in row for row in board):
        return 0

    # Nếu đang đánh giá cho máy tính
    if is_maximizing:
        best_score = -float("inf")
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == EMPTY:
                    board[row][col] = COMPUTER
                    score = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    # Nếu đang đánh giá cho người chơi
    else:
        best_score = float("inf")
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY
                    best_score = min(score, best_score)
        return best_score

# AI move
def computer_move(board):
    best_score = -float("inf")
    best_move = None
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                board[row][col] = COMPUTER
                score = minimax(board, 0, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    if best_move is not None:
        board[best_move[0]][best_move[1]] = COMPUTER

def play_caro():
    print("hello ae")
    board = create_board()
    current_player = PLAYER
    winner = None

    while True:
        draw_board(board)

        # win check
        winner = check_win(board)
        if winner is not None:
            if winner == PLAYER:
                print("You win")
            else:
                print("AI win")
            break

        # player move
        if current_player == PLAYER:
            while True:
                row = int(input("Input row: "))
                col = int(input("Input col: "))
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER
                    break
                else:
                    print("Ô này đã được đánh, vui lòng chọn ô khác.")

        # AI move
        elif current_player == COMPUTER:
            computer_move(board)

        # swap
        current_player = PLAYER if current_player == COMPUTER else COMPUTER

play_caro()

