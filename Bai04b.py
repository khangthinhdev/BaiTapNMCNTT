import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('420x420')
        self.cvs_figure = tk.Canvas(
            self, bg='white', relief=tk.SUNKEN, bd=1, width=600, height=600)
        self.cvs_figure.bind("<Button-1>", self.print_event)
        self.cvs_figure.place(x=0, y=0)

    def print_event(self, event):
        position = "(x={}, y={})".format(event.x, event.y)
        print(event.type, "event", position)


if __name__ == "__main__":
    app = App()
    app.mainloop()
