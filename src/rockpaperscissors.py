import tkinter as tk
import random


class RockPaperScissorsGUI():

    def __init__(self, master):
        self.master = master
        self.user_select = ""

        sizex = 400
        sizey = 400
        posx = 40
        posy = 20
        self.master.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
        self.master.title('RockPaperScissors.exe')

        self.frame = tk.Frame(self.master)
        tk.Label(text='Rock, Paper, Scissors Game').pack()
        self.user_entry = tk.Listbox(self.master)

        for x in selection_list:
            self.user_entry.insert(tk.END, x)

        self.user_select_display = tk.Label(text="")
        self.user_select_display.pack()

        self.user_entry.pack()
        self.user_entry.bind("<<ListboxSelect>>", self.on_select)

        self.result = tk.StringVar()
        tk.Button(master=self.master,
                  text='Play',
                  command=self.play).place(x=180,
                                           y=210)

        tk.Button(master=self.master,
                  text='Exit',
                  command=self.exit).place(x=205,
                                           y=270)

        tk.Button(master=self.master,
                  text='Reset',
                  command=self.reset).place(x=155,
                                            y=270)

        tk.Entry(master=self.master,
                 width=55,
                 textvariable=self.result).place(x=25, y=250)

    def on_select(self, event):
        widget = event.widget
        selection = widget.curselection()
        self.user_select = widget.get(selection[0])

        self.user_select_display.destroy()
        self.user_select_display = tk.Label(text=f'You are about to play {self.user_select}')
        self.user_select_display.pack()

    def computer_select(self):
        computer_select = random.choice(selection_list)
        return computer_select

    def play(self):
        computer_select = self.computer_select()

        if computer_select == self.user_select:
            self.result.set("It's a tie!")
        elif (computer_select == 'rock') and (self.user_select == 'paper'):
            self.result.set(f"You win, the computer selected {computer_select}!")
        elif (computer_select == 'rock') and (self.user_select == 'scissor'):
            self.result.set(f"You win, the computer selected {computer_select}!")
        elif (computer_select == 'scissor') and (self.user_select == 'paper'):
            self.result.set(f"You Lose, the computer selected {computer_select}!")
        elif (computer_select == 'scissor') and (self.user_select == 'rock'):
            self.result.set(f"You win, the computer selected {computer_select}!")
        elif (computer_select == 'paper') and (self.user_select == 'scissor'):
            self.result.set(f"You win, the computer selected {computer_select}!")
        elif (computer_select == 'paper') and (self.user_select == 'rock'):
            self.result.set(f"You lose, the computer selected {computer_select}!")

    def exit(self):
        self.master.destroy()

    def reset(self):
        self.result.set('')
        self.user_select_display.destroy()


def main():
    global selection_list
    selection_list = ['rock', 'paper', 'scissor']

    window = tk.Tk()
    RockPaperScissorsGUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
