import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello World')
        self.geometry('400x400')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        reset_button = tk.Label(self, text='Reset')
        run_button = tk.Label(self, text='Run')

        reset_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        run_button.grid(row=0, column=1, sticky=tk.W+tk.E)


if __name__ == '__main__':
    app = App()
    app.mainloop()
