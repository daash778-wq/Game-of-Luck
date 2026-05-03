import tkinter as tk
import random

root = tk.Tk()
root.geometry("500x320")
root.title("Game of Luck!")

player1 = tk.StringVar()
player2 = tk.StringVar()
cbtnplayer1 = tk.StringVar()
cbtnplayer2 = tk.StringVar()
output = tk.StringVar()
result = tk.StringVar()
turncounterplayer1 = 0
turncounterplayer2 = 0
player1val = 0
player2val = 0
player1.set("Player1: ")
player2.set("Player2: ")
output.set("Player 1 Turn")
cbtnplayer1.set("Player1 Roll")
cbtnplayer2.set("Player2 Roll")
result.set("Here, The result will show")


def rolling():
    global turncounterplayer1, turncounterplayer2, player1val, player2val
    if(player1btn['state'] == "normal"):
        player1btn["state"] = "disabled"
        player2btn["state"] = "normal"
        output.set("Player 2 Turn")
        randnum = random.randint(0, 10)
        player1val = player1val + randnum
        player1sum = player1.get()
        player1sum = "{} + {}".format(player1sum, randnum)
        player1.set(player1sum)
        turncounterplayer1 += 1
        cbtnplayer1.set("Player1 - Turn# {}".format(turncounterplayer1))
    else:
        player2btn["state"] = "disabled"
        player1btn["state"] = "normal"
        output.set("Player 1 Turn")
        randnum = random.randint(0, 10)
        player2val = player2val + randnum
        player2sum = player2.get()
        player2sum = "{} + {}".format(player2sum, randnum)
        player2.set(player2sum)
        turncounterplayer2 += 1
        cbtnplayer2.set("Player2 - Turn# {}".format(turncounterplayer2))

    if turncounterplayer1 >= 3:
        player1btn["state"] = "disabled"
    if turncounterplayer2 >= 3:
        player2btn["state"] = "disabled"
    
    if turncounterplayer1 == 3 and turncounterplayer2 == 3:
        if player1val > player2val:
            result.set("PLAYER#1 WINS.")
        elif player1val < player2val:
            result.set("PLAYER#2 WINS.")
        else:
            result.set("THIS IS DRAW")

def playagain():
    global turncounterplayer1, turncounterplayer2, player1val, player2val
    turncounterplayer1 = 0
    turncounterplayer2 = 0
    player1val = 0
    player2val = 0
    player1.set("Player1: ")
    player2.set("Player2: ")
    player1btn["state"] = "normal"
    output.set("Player 1 Turn")
    cbtnplayer1.set("Player1 Roll")
    cbtnplayer2.set("Player2 Roll")
    result.set("Here, The result will show")

headinglbl = tk.Label(root, font=("Helvetica", "16", "bold"), width="498", wraplength="400", underline="10", text="GAME OF LUCK")
instructionlbl = tk.Label(root, font=("Helvetica", "8", "bold"), width="498", wraplength="400", text="INSTRUCTIONS \nEach Player will have three chances to click and after 3 clicks button will be disabled. Each click will give a random value between 0 to 10 and after 3 clicks all the values will be added for each player and \n 'THE PLAYER WHO GETS HIGHER SUM WILL WIN.' ")
player1labl = tk.Label(root, font=("Helvetica", "10", "bold"), anchor="w", textvariable=player1, bg="#01761C", fg="#FFFFFF")
player2labl = tk.Label(root, font=("Helvetica", "10", "bold"), anchor="w", textvariable=player2, bg="#01761C", fg="#FFFFFF")
outputbox = tk.Label(root, font=("Helvetica", "10", "bold"), textvariable=output, bg="#FFFFFF", fg="#01761C")
player1btn = tk.Button(root, command=rolling, font=("Helvetica", "10", "bold"), textvariable=cbtnplayer1,  bg="#DEFEE6", fg="#01761C")
player2btn = tk.Button(root, command=rolling, font=("Helvetica", "10", "bold"), textvariable=cbtnplayer2, state="disabled", bg="#DEFEE6", fg="#01761C")
resultbox = tk.Label(root, font=("Helvetica", "12", "bold"),textvariable=result, bg="#1549CE", fg="#FFFFFF")
againbtn = tk.Button(root, command=playagain,  font=("Helvetica", "10", "bold"), text="Play Again")
exitbtn = tk.Button(root, command=root.destroy, font=("Helvetica", "10", "bold"), text = "Exit")               


headinglbl.place(x=1, y=5, bordermode="outside", height=35, width=498)
instructionlbl.place(x=1, y=41, bordermode="outside", height=75, width=498)
player1labl.place(x=10, y=120, bordermode="outside", height=30, width=150)
outputbox.place(x=170, y=120,  bordermode="outside", height=30, width=150)
player2labl.place(x=330, y=120, bordermode="outside", height=30, width=150)
player1btn.place(x=80, y=160, height=30, width=150)
player2btn.place(x=260, y=160, height=30, width=150)
resultbox.place(x=0, y=220,  bordermode="outside", height=40, width=500)
againbtn.place(x=150, y=275, height=30, width=100)
exitbtn.place(x=250, y=275, height=30, width=100)

root.mainloop()


