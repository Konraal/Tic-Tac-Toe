
def player_move(moves :list, current_player :str) -> list:

    while True:
        while True:
            try:
                x :int= int(input("X position (1-3): "))
                if 1 <= x <= 3:
                    x-=1
                    break
                else:
                    print("Give number in range 1-3.")
            except ValueError:
                print("Use only integers from range 1-3.")

        while True:
            try:
                y :int = int(input("Y position (1-3): "))
                if 1 <= y <= 3:
                    y-=1
                    break
                else:
                    print("Give number in range 1-3.")
            except ValueError:
                print("Use only integers from range 1-3.")

        if moves[x][y] != "X" and moves[x][y] != "O":
            moves[x][y] = current_player
            return moves
        else:
            print("This field is taken, choose a different one.")

def update_board(moves) -> str:

    board = (f" {moves[0][0]} | {moves[0][1]} | {moves[0][2]}  \n"
             f"-----------\n"
             f" {moves[1][0]} | {moves[1][1]} | {moves[1][2]}  \n"
             f"-----------\n"
             f" {moves[2][0]} | {moves[2][1]} | {moves[2][2]} \n")
    return board

def game_result(moves :list, current_player :str) -> bool:

    for x in range(3):
        if all(moves[x][y] == current_player for y in range(3)):
            return "win"
    for y in range(3):
        if all(moves[x][y] == current_player for x in range(3)):
            return "win"

    if all(moves[i][i] == current_player for i in range(3)):
        return "win"

    if all(moves[i][2-i] == current_player for i in range(3)):
        return "win"
    all_taken = all(cell in ["X", "O"] for row in moves for cell in row)
    if all_taken:
        return 'draw'

    return 'continue'

def main()-> None:
    print("Welcome  to simple tic, tac, toe game!")
    game_on :bool = True
    current_player :str = "X"
    moves :list = [[' ',' ',' ' ],[' ',' ',' '],[' ',' ',' ']]

    while game_on:
        moves :list = player_move(moves,current_player)
        print(update_board(moves))
        result = game_result(moves,current_player)

        if result == "win":
            print(f"Congratulations {current_player}, you win!")
            game_on = False
        elif result == "draw":
            print("Draw!")
            game_on = False

        current_player = 'O' if current_player == 'X' else 'X'



if __name__ == '__main__':
    main()