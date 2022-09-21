import random
from tkinter import *
root = Tk(className = "猜数游戏")
maxNo = 10
score = 0
rounds = 0

def buttonClick():
    global score
    global rounds
    try:
        guess = int(guessBox.get())
        if 0 < guess <= maxNo:
            result = random.randrange(1,maxNo + 1)
            if guess == result:
                score = score + 1
            rounds = rounds + 1
        else:
            result = "请输入有效数字!"
    except:
        result = "请输入有效数字!"
    resultLabel.config(text = result)
    scoreLabel.config(text = str(score) + "/" + str(rounds))
    guessBox.delete(0,END)
    
guessLabel = Label(root,text = "请输入一个数(1~"+ str(maxNo) + ")")
guessBox = Entry(root)
resultLabel = Label(root)
scoreLabel = Label(root)
button = Button(root,text = "猜 数",command = buttonClick)

guessLabel.pack()
guessBox.pack()
resultLabel.pack()
scoreLabel.pack()
button.pack()

root.mainloop()
