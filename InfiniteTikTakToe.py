import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Infinite Tic Tac Toe")



current_player = "X"
buttons = []


def on_button_click(button):
    if button.cget("text") != "":
        messagebox.showerror("Invalid Move", "Nice try... pick somewhere else")
        root.focus_force()
        return
    global current_player
    if current_player == "X":
        button.config(fg="red")
    else:
        button.config(fg="blue")
    button.config(text=current_player)
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    make_infinite(button)
    check_for_wins()

# button definitions, TL = top left, TM = top middle, TR = top right; etc.
TL = tk.Button(root, text= "", width=10, height=7, command=lambda: on_button_click(TL))
TL.grid(row=0, column=0)
TM = tk.Button(root, text= "", width=10, height=7, command=lambda: on_button_click(TM))
TM.grid(row=0, column=1)
TR = tk.Button(root, text= "", width=10, height=7, command=lambda: on_button_click(TR))
TR.grid(row=0, column=2)
ML = tk.Button(root, text= "", width=10, height=7, command=lambda: on_button_click(ML))
ML.grid(row=1, column=0)
MM = tk.Button(root, text= "", width=10, height=7, command=lambda: on_button_click(MM))
MM.grid(row=1, column=1)
MR = tk.Button(root, text= "", width=10, height=7, command=lambda: on_button_click(MR))
MR.grid(row=1, column=2)
BL = tk.Button(root, text= "", width=10, height=7, command=lambda: on_button_click(BL))
BL.grid(row=2, column=0)
BM = tk.Button(root, text= "", width=10, height=7, command=lambda: on_button_click(BM))
BM.grid(row=2, column=1)
BR = tk.Button(root, text= "", width=10, height=7, command=lambda: on_button_click(BR))
BR.grid(row=2, column=2)


# remove oldest x or o from board and replace with empty string
def make_infinite(button):
    
    if len(buttons) == 5:
        Button_to_gray = buttons[4]
        Button_to_gray.config(fg="gray")
        buttons.insert(0, button)
    elif len(buttons) < 6:
        buttons.insert(0, button)
        return
    else:
        Button_to_remove = buttons[5]
        Button_to_gray = buttons[4]
        Button_to_remove.config(text="",fg="black" )
        Button_to_gray.config(fg="gray")
        buttons.insert(0, button)
        return

# check for wins
def check_for_wins():
    # get text of buttons
    TLT = TL.cget("text")
    TMT = TM.cget("text")
    TRT = TR.cget("text")
    MLT = ML.cget("text")
    MMT = MM.cget("text")
    MRT = MR.cget("text")
    BLT = BL.cget("text")
    BMT = BM.cget("text")
    BRT = BR.cget("text")
    # check for horizontal wins
    if TLT == TMT == TRT and TLT != "":
        winner = TLT
    elif MLT == MMT == MRT and MLT != "":
        winner = MLT
    elif BLT == BMT == BRT and BLT != "":
        winner = BLT
    # check for vertical wins
    elif TLT == MLT == BLT and TLT != "":
        winner = TLT
    elif TMT == MMT == BMT and TMT != "":
        winner = TMT
    elif TRT == MRT == BRT and TRT != "":
        winner = TRT
    # check for diagonal wins
    elif TLT == MMT == BRT and TLT != "":
        winner = TLT
    elif TRT == MMT == BLT and TRT != "":
        winner = TRT
    else:
        winner = None

    if winner:
        response = messagebox.askquestion("Game Over", f"{winner} Wins! Play again?")
        if response == 'yes':
            reset_game()
        else:
            root.quit()

def reset_game():
    global current_player
    current_player = "X"
    TL.config(text="")
    TM.config(text="")
    TR.config(text="")
    ML.config(text="")
    MM.config(text="")
    MR.config(text="")
    BL.config(text="")
    BM.config(text="")
    BR.config(text="")
    for button in buttons:
        button.config(text="")
    buttons.clear()
    root.focus_force()


root.mainloop()