from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Truot file text")
        self.geometry('480x560')
        self.text = Text(self, font=('Times New Roman', 14),
                         width=50, wrap=WORD)

        self.btn_open = Button(self, text="Open file text",
                               command=self.btn_open_click)
        self.btn_open.place(x=5, y=5)
        self.text.place(x=5, y=40)

        # scrollbar
        scroll_y = ttk.Scrollbar(
            self, orient=VERTICAL, command=self.text.yview)
        self.text.config(yscrollcommand=scroll_y.set)
        scroll_y.place(x=450, y=40, height=510, width=25)
        style = ttk.Style()
        style.theme_use('classic')
        style.configure("Vertical.TScrollbar", background="green",
                        bordercolor="red", arrowcolor="white")

    def btn_open_click(self):
        file = open('Ho_Alphonse_de_Lamartine.txt', 'r', encoding='utf-8')
        content = file.read()
        file.close()
        self.text.insert(INSERT, content)
        self.text.configure(state=DISABLED)
        self.btn_open.configure(state=DISABLED)


if __name__ == "__main__":
    app = App()
    app.mainloop()
