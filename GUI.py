# Mert Gulmus / 211ADB070

from tkinter import *
from Game import Game

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Number Multiplication Game - 211ADB070")
        self.canvas = Canvas(master, width=300, height=100)
        self.canvas.pack(side=TOP)
        self.check_var = IntVar()
        self.check_var.set(1)
        self.check = Checkbutton(master, text="Player starts", variable=self.check_var)
        self.check.pack()
        self.start_button = Button(master, text="Start", command=self.startGame)
        self.start_button.pack()

    def computerMove(self):
        self.computer_move_button.pack_forget()

        self.game.computerMove()
        self.current_number_label.config(text="Current number: " + str(self.game.currentNumber))
        if self.game.currentNumber >= self.game.lowerBound:
            self.completeGame()
            return

        self.button1.pack(side=LEFT, padx=10)
        self.button2.pack(side=LEFT, padx=10)
        self.button3.pack(side=LEFT, padx=10)
        self.waiting_label.config(text="Waiting for player move...")

    def playerMove(self, move):
        self.game.playerMove(move)
        self.current_number_label.config(text="Current number: " + str(self.game.currentNumber))

        if self.game.currentNumber >= self.game.lowerBound:
            self.completeGame()
            return

        if hasattr(self, 'computer_move_button'):
            self.computer_move_button.pack(side=TOP)
        else:
            self.computer_move_button = Button(self.master, text="Computer move", command=self.computerMove)
            self.computer_move_button.pack(side=TOP)

        self.waiting_label.config(text="Please click on the computer move button")
        self.button1.pack_forget()
        self.button2.pack_forget()
        self.button3.pack_forget()

    def completeGame(self):
        self.current_number_label.config(text="Final number: " + str(self.game.currentNumber) + " - Winner: " + str(self.game.determineWinner()))
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.lower_bound_label.destroy()
        self.upper_bound_label.destroy()
        self.waiting_label.destroy()
        self.start_button = Button(self.master, text="Start", command=self.startGame)
        self.start_button.pack()
        self.check_var = IntVar()
        self.check_var.set(1)
        self.check = Checkbutton(self.master, text="Player starts", variable=self.check_var)
        self.check.pack()

    def startGame(self):
        if hasattr(self, 'current_number_label'):
            self.current_number_label.destroy()

        self.start_button.destroy()
        self.check.destroy()

        self.game = Game(self.check_var.get())

        self.frame = Frame(self.master)
        self.frame.pack(side=BOTTOM)
        self.button1 = Button(self.frame, text="2", command=lambda: self.playerMove(2), padx=10)
        self.button2 = Button(self.frame, text="3", command=lambda: self.playerMove(3), padx=10)
        self.button3 = Button(self.frame, text="4", command=lambda: self.playerMove(4), padx=10)

        self.current_number_label = Label(self.master, text="Current number: " + str(self.game.currentNumber), font=("Helvetica", 16))
        self.lower_bound_label = Label(self.master, text="Lower bound: " + str(self.game.lowerBound), font=("Helvetica", 12))
        self.upper_bound_label = Label(self.master, text="Upper bound: " + str(self.game.upperBound), font=("Helvetica", 12))
        self.waiting_label = Label(self.master, text="Waiting for player to move...", font=("Helvetica", 12))
        self.current_number_label.pack(side=TOP)
        self.lower_bound_label.pack(side=TOP)
        self.upper_bound_label.pack(side=TOP)
        self.waiting_label.pack(side=TOP)

        if self.check_var.get() == 0:
            self.computer_move_button = Button(self.master, text="Computer move", command=self.computerMove)
            self.computer_move_button.pack(side=TOP)
            self.waiting_label.config(text="Please click on the computer move button")
        else:
            self.button1.pack(side=LEFT, padx=10)
            self.button2.pack(side=LEFT, padx=10)
            self.button3.pack(side=LEFT, padx=10)
            

root = Tk()
my_gui = GUI(root)
root.mainloop()
