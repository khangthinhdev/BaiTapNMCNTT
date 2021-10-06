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
        self.entry_a = tk.Entry(self, justify=tk.RIGHT, textvariable=self.a)
        self.entry_a.focus_set()
        self.entry_b = tk.Entry(self, justify=tk.RIGHT, textvariable=self.b)
        self.entry_c = tk.Entry(self, justify=tk.RIGHT, textvariable=self.c)

        # button
        btn_giai = tk.Button(self, text="Giai", width=6,
                             command=self.btn_giai_click)
        btn_xoa = tk.Button(self, text="Xoa", width=6,
                            command=self.btn_xoa_click)
        btn_thoat = tk.Button(self, text="Thoat", width=6)

        # grid
        lbl_a.grid(row=0, column=0, padx=10, pady=10)
        lbl_b.grid(row=1, column=0, padx=10, pady=10)
        lbl_c.grid(row=2, column=0, padx=10, pady=10)
        lbl_nghiem.grid(row=3, column=0, padx=10, pady=10)
        self.lbl_ketqua.grid(row=3, column=1, columnspan=2,
                             padx=10, pady=10, sticky=NSEW, ipady=2)

        self.entry_a.grid(row=0, column=1, padx=10, pady=10, ipady=2)
        self.entry_b.grid(row=1, column=1, padx=10, pady=10, ipady=2)
        self.entry_c.grid(row=2, column=1, padx=10, pady=10, ipady=2)

        btn_giai.grid(row=0, column=2, padx=10, pady=10)
        btn_xoa.grid(row=1, column=2, padx=10, pady=10)
        btn_thoat.grid(row=2, column=2, padx=10, pady=10)

    # functions
    def btn_giai_click(self):
        def isFloat(value):
            value_num = 0.0
            try:
                value_num = float(value)
                return True, value_num
            except ValueError:
                return False, value_num

        value_a = self.a.get()
        value_b = self.b.get()
        value_c = self.c.get()

        result, a = isFloat(value_a)
        if result == False:
            msg.showerror('Error', 'Ban phai nhap chu so')
            self.entry_a.focus_set()
            return
        result, b = isFloat(value_b)
        if result == False:
            msg.showerror('Error', 'Ban phai nhap chu so')
            self.entry_b.focus_set()
            return
        result, c = isFloat(value_c)
        if result == False:
            msg.showerror('Error', 'Ban phai nhap chu so')
            self.entry_c.focus_set()
            return

        d = a+b+c
        s = '%.2f' % d
        self.lbl_ketqua.configure(text=s)

    def btn_xoa_click(self):
        self.entry_a.delete(0, tk.END)
        self.entry_b.delete(0, tk.END)
        self.entry_c.delete(0, tk.END)
        self.lbl_ketqua.configure(text='')
        self.entry_a.focus_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()