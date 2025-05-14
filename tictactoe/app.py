from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

board = [""] * 9
current_player = "X"

def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] != "":
            return board[cond[0]]
    if "" not in board:
        return "Tie"
    return None

@app.route("/")
def index():
    winner = check_winner()
    return render_template("index.html", board=board, current_player=current_player, winner=winner)

@app.route("/move/<int:cell>")
def move(cell):
    global current_player
    if board[cell] == "" and not check_winner():
        board[cell] = current_player
        current_player = "O" if current_player == "X" else "X"
    return redirect(url_for('index'))

@app.route("/reset")
def reset():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
