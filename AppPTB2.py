import tkinter as tk
from tkinter import messagebox as msg
from tkinter.constants import NSEW, SUNKEN


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bai thuc hanh so 2")

        # label
        lbl_a = tk.Label(self, text="Nhap a")
        lbl_b = tk.Label(self, text="Nhap b")
        lbl_c = tk.Label(self, text="Nhap c")
        lbl_nghiem = tk.Label(self, text="Nghiem")
        self.lbl_ketqua = tk.Label(self, bg='white', relief=SUNKEN)

        # tao bien
        self.a = tk.StringVar()
        self.b = tk.StringVar()
        self.c = tk.StringVar()

        # input
        entry_a = tk.Entry(self, justify=tk.RIGHT, textvariable=self.a)
        entry_a.focus_set()
        entry_b = tk.Entry(self, justify=tk.RIGHT, textvariable=self.b)
        entry_c = tk.Entry(self, justify=tk.RIGHT, textvariable=self.c)

        # button
        btn_giai = tk.Button(self, text="Giai", width=6,
                             command=self.btn_giai_click)
        btn_xoa = tk.Button(self, text="Xoa", width=6)
        btn_thoat = tk.Button(self, text="Thoat", width=6)

        # grid
        lbl_a.grid(row=0, column=0, padx=10, pady=10)
        lbl_b.grid(row=1, column=0, padx=10, pady=10)
        lbl_c.grid(row=2, column=0, padx=10, pady=10)
        lbl_nghiem.grid(row=3, column=0, padx=10, pady=10)
        self.lbl_ketqua.grid(row=3, column=1, columnspan=2,
                             padx=10, pady=10, sticky=NSEW)

        entry_a.grid(row=0, column=1, padx=10, pady=10)
        entry_b.grid(row=1, column=1, padx=10, pady=10)
        entry_c.grid(row=2, column=1, padx=10, pady=10)

        btn_giai.grid(row=0, column=2, padx=10, pady=10)
        btn_xoa.grid(row=1, column=2, padx=10, pady=10)
        btn_thoat.grid(row=2, column=2, padx=10, pady=10)

    # functions
    def btn_giai_click(self):
        a = float(self.a.get())
        b = float(self.b.get())
        c = float(self.c.get())
        d = a+b+c
        s = '%.2f' % d
        self.lbl_ketqua.configure(text=s)


if __name__ == "__main__":
    app = App()
    app.mainloop()
