import numpy as np

def main():

    # Read bingo draws
    draws = [int(x) for x in input().split(",")]
    # Dictionary {draw: position}
    positions = {draws[i]: i for i in range(len(draws))}

    # Read bingo boards
    boards = []
    while True:
        try:
            input()
            board = []
            # Boards are 5x5
            for _ in range(5):
                board.append([int(x) for x in input().split()])
            boards.append(np.array(board))
        except Exception:
            break

    # Compute the winning turn of each board
    win_turn = []
    # N is for numbers that are never drawned
    N = len(draws) + 1
    for board in boards:
        # Replace each value in the board by the turn it is drawn
        board = np.vectorize(lambda x: positions.get(x, N))(board)
        # The winning turn of a row/column is the maximum turn in it
        # The winning turn of a board is the minimum winning turn among rows/columns
        win_turn.append(min(board.max(axis=0).min(), board.max(axis=1).min()))

    # Find the board that wins first
    winning_board = boards[np.argmin(win_turn)]
    winning_turn = np.min(win_turn)
    # Compute score by keeping only unmarked numbers on the board
    f = lambda x: x if positions.get(x, N) > winning_turn else 0
    # The score is the sum of unmarked number times the last number drawn
    p1 = np.vectorize(f)(winning_board).sum() * draws[winning_turn]

    # Find the board that wins last
    losing_board = boards[np.argmax(win_turn)]
    losing_turn= np.max(win_turn)
    # Compute score by keeping only unmarked numbers on the board
    f = lambda x: x if positions.get(x, N) > losing_turn else 0
    # The score is the sum of unmarked number times the last number drawn
    p2 = np.vectorize(f)(losing_board).sum() * draws[losing_turn]

    return p1, p2

p1, p2 = main()
print("Puzzle answer, part 1:", p1)
print("Puzzle answer, part 2:", p2)
