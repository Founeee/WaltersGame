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

        self.canvas = Canvas(self.root, height=self.height, width=self.width, bg="black")
        self.canvas.pack()

        self.drawBoard()

    def newBoard(self):
        return [(random.randint(0, 1)) for _ in range(self.taille)]

    def drawBoard(self):
        self.canvas.delete("all")
        for index, case in enumerate(self.board):
            Canvas.create_rectangle(self.canvas, index * self.tailleCellule + self.marginX, self.marginY, index * self.tailleCellule + self.marginY + self.tailleCellule, self.tailleCellule + self.marginY, outline='white')

            if case == 1:
                Canvas.create_oval(self.canvas, index * self.tailleCellule + self.marginX + 10, self.marginY + 10, index * self.tailleCellule + self.marginY + self.tailleCellule - 10, self.tailleCellule + self.marginY - 10, fill="red")
            


    def possiblePawn(self):
        pass

    def possibleDestination(self):
        pass

    def again(self):
        pass

    def put(self):
        pass

    def fin(self):
        pass

    def gameTurn(self):
        pass



app_root = Tk()
app = WaltersGame(app_root)
print(app.newBoard())
app.root.mainloop()



