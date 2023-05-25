import tkinter as tk
from tkinter import messagebox

# ゲームの状態を表す変数
current_player = "O"  # 現在のプレイヤー（"O"または"X"）
game_board = [["", "", ""],
              ["", "", ""],
              ["", "", ""]]

# プレイヤーがマスをクリックしたときの処理
def cell_click(row, col):
    global current_player, game_board
    
    # 既にマスが埋まっている場合は処理しない
    if game_board[row][col] != "":
        return
    
    # マスを現在のプレイヤーで埋める
    game_board[row][col] = current_player
    
    # マスの表示を更新する
    buttons[row][col].configure(text=current_player)
    
    # 勝敗判定を行う
    if check_winner(current_player):
        messagebox.showinfo("勝者", f"{current_player}の勝ちです！")
        reset_game()
    elif check_draw():
        messagebox.showinfo("引き分け", "引き分けです。")
        reset_game()
    else:
        # プレイヤーを交代する
        current_player = "X" if current_player == "O" else "O"

# 勝利条件をチェックする関数
def check_winner(player):
    # 横のラインをチェック
    for row in range(3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] == player:
            return True
    
    # 縦のラインをチェック
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] == player:
            return True
    
    # 対角線をチェック
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == player:
        return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0] == player:
        return True
    
    return False

# 引き分けをチェックする関数
def check_draw():
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == "":
                return False
    return True

# ゲームをリセットする関数
def reset_game():
    global current_player, game_board
    current_player = "O"
    game_board = [["", "", ""],
                  ["", "", ""],
                  ["", "", ""]]
    for row in range(3):
        for col in range(3):
            buttons[row][col].configure(text="")

# メインウィンドウを作成
window = tk.Tk()
window.title("丸罰ゲーム")

# ボタンを作成
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text="", width=10, height=        5, command=lambda r=row, c=col: cell_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# ゲームをリセットするボタン
reset_button = tk.Button(window, text="リセット", command=reset_game)
reset_button.grid(row=3, columnspan=3)

# メインループを開始
window.mainloop()
