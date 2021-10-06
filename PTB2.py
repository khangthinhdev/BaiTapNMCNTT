import tkinter as tk
from tkinter import messagebox as msg


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello bai 1")
        lbl_chao = tk.Label(self, text="KhoaCNTTABCCCCCCCCCCCCCC", bg="white",
                            fg="blue", relief=tk.SUNKEN, font=("calibri", 20))
        lbl_chao.grid(row=1, column=1, padx=10, pady=10)

        btn_thoat = tk.Button(self, text="Thoat", width=10,
                              command=self.btn_thoat_click)
        btn_thoat.grid(row=2, column=1, padx=10, pady=10)
        self.protocol('WM_DELETE_WINDOW', self.btn_thoat_click)

    def btn_thoat_click(self):
        tra_loi = msg.askquestion('Question', 'Ban co muon thoat khong?')
        if tra_loi == 'yes':
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
