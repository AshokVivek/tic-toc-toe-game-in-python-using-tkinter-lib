from tkinter import Frame, Canvas, Label, Button, LEFT, RIGHT, ALL, Tk
from random import randint


class main:


    def x(self,m1,m2):
        self.canvas.create_rectangle(m1 - 50, m2 - 50, m1 + 50, m2 + 50, fill="red", width=4, outline="black")
        self.canvas.create_line(m1 + 20, m2 + 20, m1 - 20, m2 - 20, width=4, fill="black")
        self.canvas.create_line(m1 - 20, m2 + 20, m1 + 20, m2 - 20, width=4, fill="black")

    def y(self,m1,m2):
        self.canvas.create_rectangle(m1-50, m2-50, m1+50, m2+50, fill="red", width=4, outline="black")
        self.canvas.create_oval(m1 + 25, m2 + 25, m1 - 25, m2 - 25, width=4, outline="black")


    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.label = Label(self.frame, text='Tic Tac Toe Game',font="Tic, 40", height=3, bg='green', fg='black')
        self.label.pack(fill="both", expand=True)
        self.frameb = Frame(self.frame)
        self.frameb.pack(fill="both", expand=True)
        self.Start1 = Button(self.frameb, text='Click here to start\ndouble player',font="Click, 15", height=4, command=self.start1,
                             bg='purple', fg='white')
        self.Start1.pack(fill="both", expand=True, side=RIGHT)

    def start1(self):
        self.canvas.delete(ALL)
        self.label['text'] = ('Tic Tac Toe Game')
        self.canvas.bind("<ButtonPress-1>", self.sgplayer)
        self._board()
        self.TTT = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.i = 0
        self.j = False


    def _board(self):
        self.canvas.create_rectangle(0, 0, 300, 300,fill="yellow",width=4, outline="black")
        self.canvas.create_rectangle(100, 300, 200, 0, outline="black")
        self.canvas.create_rectangle(0, 100, 300, 200, outline="black")

    def sgplayer(self, event):
        for k in range(0, 300, 100):
            for j in range(0, 300, 100):
                if event.x in range(k, k + 100) and event.y in range(j, j + 100):
                    if self.canvas.find_enclosed(k, j, k + 100, j + 100) == ():
                        if self.i % 2 == 0:
                            X = (2 * k + 100) / 2
                            Y = (2 * j + 100) / 2
                            X1 = int(k / 100)
                            Y1 = int(j / 100)
                            self.canvas.create_oval(X + 25, Y + 25, X - 25, Y - 25, width=4, outline="black")
                            self.TTT[Y1][X1] += 1
                            self.i += 1
                        else:
                            X = (2 * k + 100) / 2
                            Y = (2 * j + 100) / 2
                            X1 = int(k / 100)
                            Y1 = int(j / 100)
                            self.canvas.create_line(X + 20, Y + 20, X - 20, Y - 20, width=4, fill="black")
                            self.canvas.create_line(X - 20, Y + 20, X + 20, Y - 20, width=4, fill="black")
                            self.TTT[Y1][X1] += 9
                            self.i += 1
        self.check()

    def check(self):
        # horizontal check
        for i in range(0, 3):
            if sum(self.TTT[i]) == 27:
                if self.TTT[0][0] + self.TTT[0][1] + self.TTT[0][2] == 27:
                    self.x(50, 50)
                    self.x(150, 50)
                    self.x(250, 50)
                if self.TTT[1][0]+self.TTT[1][1]+self.TTT[1][2] == 27:
                    self.x(50, 150)
                    self.x(150, 150)
                    self.x(250, 150)
                if self.TTT[2][0] + self.TTT[2][1] + self.TTT[2][2] == 27:
                    self.x(50, 250)
                    self.x(150, 250)
                    self.x(250, 250)
                self.label['text'] = ('2nd player wins!')
                self.end()
            if sum(self.TTT[i]) == 3:
                if self.TTT[0][0]+self.TTT[0][1]+self.TTT[0][2] == 3:
                    self.y(50, 50)
                    self.y(150, 50)
                    self.y(250, 50)
                if self.TTT[1][0]+self.TTT[1][1]+self.TTT[1][2] == 3:
                    self.y(50, 150)
                    self.y(150, 150)
                    self.y(250, 150)
                if self.TTT[2][0] + self.TTT[2][1] + self.TTT[2][2] == 3:
                    self.y(50, 250)
                    self.y(150, 250)
                    self.y(250, 250)
                self.label['text'] = ('1st player wins!')
                self.end()
        # vertical check
        # the matrix below transposes self.TTT so that it could use the sum fucntion again
        self.ttt = [[row[i] for row in self.TTT] for i in range(3)]
        for i in range(0, 3):
            if sum(self.ttt[i]) == 27:
                if self.ttt[0][0] + self.ttt[0][1] + self.ttt[0][2] == 27:
                    self.x(50, 50)
                    self.x(50, 150)
                    self.x(50, 250)
                if self.ttt[1][0]+self.ttt[1][1]+self.ttt[1][2] == 27:
                    self.x(150, 50)
                    self.x(150, 150)
                    self.x(150, 250)
                if self.ttt[2][0] + self.ttt[2][1] + self.ttt[2][2] == 27:
                    self.x(250, 50)
                    self.x(250, 150)
                    self.x(250, 250)
                self.label['text'] = ('2nd player wins!')
                self.end()
            if sum(self.ttt[i]) == 3:
                if self.ttt[0][0] + self.ttt[0][1] + self.ttt[0][2] == 3:
                    self.y(50, 50)
                    self.y(50, 150)
                    self.y(50, 250)
                if self.ttt[1][0]+self.ttt[1][1]+self.ttt[1][2] == 3:
                    self.y(150, 50)
                    self.y(150, 150)
                    self.y(150, 250)
                if self.ttt[2][0] + self.ttt[2][1] + self.ttt[2][2] == 3:
                    self.y(250, 50)
                    self.y(250, 150)
                    self.y(250, 250)
                self.label['text'] = ('1st player wins!')
                self.end()
        # check for diagonal wins
        if self.TTT[1][1] == 9:
            if self.TTT[0][0] == self.TTT[1][1] and self.TTT[2][2] == self.TTT[1][1]:
                self.x(50,50)
                self.x(150,150)
                self.x(250,250)
                self.label['text'] = ('2nd player wins!')
                self.end()
            if self.TTT[0][2] == self.TTT[1][1] and self.TTT[2][0] == self.TTT[1][1]:
                self.x(250,50)
                self.x(150,150)
                self.x(50,250)
                self.label['text'] = ('2nd player wins!')
                self.end()
        if self.TTT[1][1] == 1:
            if self.TTT[0][0] == self.TTT[1][1] and self.TTT[2][2] == self.TTT[1][1]:
                self.y(50, 50)
                self.y(150, 150)
                self.y(250, 250)
                self.label['text'] = ('1st player wins!')
                self.end()
            if self.TTT[0][2] == self.TTT[1][1] and self.TTT[2][0] == self.TTT[1][1]:
                self.y(250, 50)
                self.y(150, 150)
                self.y(50, 250)
                self.label['text'] = ('1st player wins!')
                self.end()
        # check for draws
        if self.j == False:
            a = 0
            for i in range(0, 3):
                a += sum(self.TTT[i])
            if a == 41:
                self.label['text'] = ("It's a Draw!")
                self.end()

    def end(self):
        self.canvas.unbind("<ButtonPress-1>")
        self.j = True


root = Tk()
app = main(root)
root.mainloop()





