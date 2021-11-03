import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bai Thuc Hanh So 3')

        # chuyển kích thước từ cố định thành biến
        self.width = 445
        self.height = 325
        self.geometry(f'{self.width}x{self.height}')

        # đặt kích thước nhỏ nhất để app không bị vỡ
        self.minsize(445, 325)

        self.figure = tk.StringVar()
        self.figure.set('Tam Giac')

        # nơi chứa các shape
        self.cvs_figure = tk.Canvas(self, bg='white', bd=1, relief=tk.SUNKEN,
                                    width=0.67*self.width, height=0.67*self.width)

        # frame figure
        self.lfrm_figure = tk.LabelFrame(self, text='Figure')
        self.rbtn_tam_giac = tk.Radiobutton(self.lfrm_figure, text='Tam Giac', width=8,
                                            anchor=tk.W, value='Tam Giac', variable=self.figure, command=self.xu_ly)
        self.rbtn_tron = tk.Radiobutton(self.lfrm_figure, text='Tron', width=8,
                                        anchor=tk.W, value='Tron', variable=self.figure, command=self.xu_ly)
        self.rbtn_chu_nhat = tk.Radiobutton(self.lfrm_figure, text='Chu Nhat', width=8,
                                            anchor=tk.W, value='Chu Nhat', variable=self.figure, command=self.xu_ly)

        self.red = tk.IntVar()
        self.green = tk.IntVar()
        self.blue = tk.IntVar()

        # frame color
        self.lfrm_color = tk.LabelFrame(
            self, text='Color', width=200)
        self.chk_red = tk.Checkbutton(self.lfrm_color, text='Red', width=8, height=1, anchor=tk.W,
                                      variable=self.red, command=self.xu_ly)
        self.chk_green = tk.Checkbutton(self.lfrm_color, text='Green', width=8, height=1, anchor=tk.W,
                                        variable=self.green, command=self.xu_ly)
        self.chk_blue = tk.Checkbutton(self.lfrm_color, text='Blue', width=8, height=1, anchor=tk.W,
                                       variable=self.blue, command=self.xu_ly)
        self.chk_red.select()

        self.cvs_figure.place(x=10, y=10)
        self.lfrm_figure.place(x=self.height+1, y=4)
        self.rbtn_tam_giac.grid(row=0, padx=10, pady=5)
        self.rbtn_tron.grid(row=1, padx=10, pady=5)
        self.rbtn_chu_nhat.grid(row=2, padx=10, pady=5)

        self.lfrm_color.place(x=self.height+1, y=self.height/2)
        self.chk_red.grid(row=0, padx=10, pady=5)
        self.chk_green.grid(row=1, padx=10, pady=5)
        self.chk_blue.grid(row=2, padx=10, pady=5)

        self.cvs_figure.update()

        W = self.cvs_figure.winfo_width() - 2
        H = self.cvs_figure.winfo_height() - 2
        #     R    G    B
        #    FF   00   00
        #    color = '#FF0000'
        R = 255
        G = 0
        B = 0
        color = '#%02X%02X%02X' % (R, G, B)
        # cvs_figure.create_oval(10, 10, W-10, H-10, outline = color, fill = color)
        # cvs_figure.create_rectangle(10, 10, W-10, H-10, outline = color, fill = color)
        points = [10, H-10, W // 2, 10, W-10, H-10]
        self.cvs_figure.create_polygon(points, outline=color, fill=color)

        # kiểm tra sự thay đổi của kích thước màn hình
        self.bind("<Configure>", self.configure)
        # lấy chính xác kích thước của container
        self.update_idletasks()

    def configure(self, event):
        if ((event.width != self.width) or (event.height != self.height)):

            # xóa canvas cũ
            self.cvs_figure.delete("all")
            # cập nhật lại kích thước cho canvas
            self.cvs_figure.config(
                width=self.winfo_width()-150, height=self.winfo_height()-30)

            self.lfrm_figure.place(x=self.winfo_width()-120, y=4)
            self.lfrm_color.place(x=self.winfo_width() -
                                  120, y=self.winfo_height()/2)
            # vẽ lại các hình
            color = '#'
            if self.red.get() == 1:
                color = color + 'FF'
            else:
                color = color + '00'

            if self.green.get() == 1:
                color = color + 'FF'
            else:
                color = color + '00'

            if self.blue.get() == 1:
                color = color + 'FF'
            else:
                color = color + '00'

            W = self.cvs_figure.winfo_width() - 2
            H = self.cvs_figure.winfo_height() - 2
            if self.figure.get() == 'Tam Giac':
                points = [10, H-10, W // 2, 10, W-10, H-10]
                self.cvs_figure.create_polygon(
                    points, outline=color, fill=color)
            elif self.figure.get() == 'Tron':
                self.cvs_figure.create_oval(
                    10, 10, W-10, H-10, outline=color, fill=color)
            else:
                self.cvs_figure.create_rectangle(
                    10, 10, W-10, H-10, outline=color, fill=color)

    def xu_ly(self):
        self.cvs_figure.delete('all')
        self.cvs_figure.update()
        color = '#'
        if self.red.get() == 1:
            color = color + 'FF'
        else:
            color = color + '00'

        if self.green.get() == 1:
            color = color + 'FF'
        else:
            color = color + '00'

        if self.blue.get() == 1:
            color = color + 'FF'
        else:
            color = color + '00'

        W = self.cvs_figure.winfo_width() - 2
        H = self.cvs_figure.winfo_height() - 2
        if self.figure.get() == 'Tam Giac':
            points = [10, H-10, W // 2, 10, W-10, H-10]
            self.cvs_figure.create_polygon(points, outline=color, fill=color)
        elif self.figure.get() == 'Tron':
            self.cvs_figure.create_oval(
                10, 10, W-10, H-10, outline=color, fill=color)
        else:
            self.cvs_figure.create_rectangle(
                10, 10, W-10, H-10, outline=color, fill=color)


if __name__ == "__main__":
    app = App()
    app.mainloop()
