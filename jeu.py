from tkinter import *
import random

class WaltersGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mon jeu")
        self.root.resizable(False, False)
        self.root.configure(bg="black")
        self.taille = 15
        self.board = self.newBoard()
        self.tailleCellule = 60
        self.marginX = 30
        self.marginY = 30
        self.height = self.marginY * 2 + self.tailleCellule
        self.width = self.marginX * 2 + self.tailleCellule * self.taille

        self.canvas = Canvas(self.root, height=self.height, width=self.width, bg="black", highlightbackground="black")
        self.canvas.pack()

        self.label = Label(self.root, text="Player 1", bg="black", fg="white",  font=("Courier", 18, "bold"))
        self.label.pack()

        self.drawBoard()
        self.player = 1
        self.pion = None

        self.canvas.bind("<Button-1>", self.onclick)
        

    def newBoard(self):
        return [(random.randint(0, 1)) for _ in range(self.taille)]

    def drawBoard(self):
        self.canvas.delete("all")
        for index, case in enumerate(self.board):
            Canvas.create_rectangle(self.canvas, index * self.tailleCellule + self.marginX, self.marginY, index * self.tailleCellule + self.marginY + self.tailleCellule, self.tailleCellule + self.marginY, outline='white')

            if case == 1:
                Canvas.create_oval(self.canvas, index * self.tailleCellule + self.marginX + 10, self.marginY + 10, index * self.tailleCellule + self.marginY + self.tailleCellule - 10, self.tailleCellule + self.marginY - 10, fill="red")

    def updateDisplay(self):
        self.label.config(text= f"Player {self.player}")
        self.drawBoard()

    def onclick(self, event):
        if self.marginY < event.y < self.marginY + self.tailleCellule and self.marginX < event.x < self.marginX + self.tailleCellule * self.taille:
            pos = (event.x - self.marginX) // self.tailleCellule
            self.gameTurn(pos)

    def possiblePawn(self, pos):
        if self.board[pos] != 1:
            return

        return any(self.board[i] == 0 for i in range(pos))

    def possibleDestination(self, x1, x2):
        return x2 < x1 and self.board[x2] == 0

    def again(self):
        self.board = self.newBoard()
        self.player = 1
        self.drawBoard()
        self.pion = None

    def put(self, x1, x2):
        self.board[x1] = 0
        self.board[x2] = 1
        
    def fin(self):
        return not any(self.board[i] == 0 for i in range(self.taille))

    def gameTurn(self, position):
        pass



app_root = Tk()
app = WaltersGame(app_root)
app.root.mainloop()



