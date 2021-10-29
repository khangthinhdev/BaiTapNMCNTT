import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bai Thuc Hanh Mouse')

        # chuyển width và height từ cố định thành biến
        self.width = 405
        self.height = 405
        self.geometry(f'{self.width}x{self.height}')

        # đặt kích thước nhỏ nhất để app không bị vỡ
        self.minsize(405, 405)

        self.DIVISION = 5
        self.state = []
        for i in range(0, self.DIVISION):
            line = []
            for j in range(0, self.DIVISION):
                line.append(False)
            self.state.append(line)

        self.cvs_figure = tk.Canvas(self, bg='white', relief=tk.SUNKEN,
                                    bd=1, width=(self.width-5), height=(self.height-5))
        self.cxBlock = (self.width-9) // self.DIVISION
        self.cyBlock = (self.height-9) // self.DIVISION
        dx = 4
        dy = 4
        for i in range(0, self.DIVISION):
            for j in range(0, self.DIVISION):
                self.cvs_figure.create_rectangle(dx + i*self.cxBlock, dy + j*self.cyBlock,
                                                 dx + (i+1)*self.cxBlock, dy +
                                                 (j+1)*self.cyBlock,
                                                 fill='white', outline='black', width=3)

        self.cvs_figure.bind("<Button-1>", self.print_event)
        # tracking sự thay đổi của kích thước cửa sổ
        self.bind("<Configure>", self.configure)
        self.update_idletasks()
        self.cvs_figure.place(x=0, y=0, width=self.width, height=self.height)
        self.cvs_figure.update()

    def configure(self, event):
        # nếu size của cửa sổ khác với size hiện tại
        if (event.width != self.width) or (event.height != self.height):
            # xóa canvas cũ
            self.cvs_figure.delete("all")
            self.width = event.width
            self.height = event.height
            # cập nhật kích thước cho canvas mới
            self.cvs_figure.config(width=self.width, height=self.height)
            self.cvs_figure.place(
                x=0, y=0, width=self.width, height=self.height)
            self.cxBlock = (self.width-9) // self.DIVISION
            self.cyBlock = (self.height-9) // self.DIVISION
            dx = 4
            dy = 4

            # in lại các hình chữ nhật
            for i in range(0, self.DIVISION):
                for j in range(0, self.DIVISION):
                    self.cvs_figure.create_rectangle(dx + i*self.cxBlock, dy + j*self.cyBlock,
                                                     dx + (i+1)*self.cxBlock, dy +
                                                     (j+1)*self.cyBlock,
                                                     fill='white', outline='black', width=3)

            # in lại các chữ X đã lưu trong state[][]
            for i in range(0, self.DIVISION):
                for j in range(0, self.DIVISION):
                    self.cvs_figure.create_rectangle(dx + i*self.cxBlock, dy + j*self.cyBlock,
                                                     dx +
                                                     (i+1)*self.cxBlock, dy +
                                                     (j+1)*self.cyBlock,
                                                     fill='white', outline='black', width=3)
                    if self.state[i][j] == True:
                        self.cvs_figure.create_line(dx + i*self.cxBlock, dy + j*self.cyBlock,
                                                    dx +
                                                    (i+1)*self.cxBlock, dy +
                                                    (j+1)*self.cyBlock,
                                                    fill='black', width=3)
                        self.cvs_figure.create_line(dx + (i+1)*self.cxBlock, dy + j*self.cyBlock,
                                                    dx + i*self.cxBlock, dy +
                                                    (j+1)*self.cyBlock,
                                                    fill='black', width=3)

    def print_event(self, event):
        x = event.x // self.cxBlock
        y = event.y // self.cyBlock
        if x < self.DIVISION and y < self.DIVISION:
            self.state[x][y] = not self.state[x][y]
            dx = 4
            dy = 4
            for i in range(0, self.DIVISION):
                for j in range(0, self.DIVISION):
                    self.cvs_figure.create_rectangle(dx + i*self.cxBlock, dy + j*self.cyBlock,
                                                     dx +
                                                     (i+1)*self.cxBlock, dy +
                                                     (j+1)*self.cyBlock,
                                                     fill='white', outline='black', width=3)
                    if self.state[i][j] == True:
                        self.cvs_figure.create_line(dx + i*self.cxBlock, dy + j*self.cyBlock,
                                                    dx +
                                                    (i+1)*self.cxBlock, dy +
                                                    (j+1)*self.cyBlock,
                                                    fill='black', width=3)
                        self.cvs_figure.create_line(dx + (i+1)*self.cxBlock, dy + j*self.cyBlock,
                                                    dx + i*self.cxBlock, dy +
                                                    (j+1)*self.cyBlock,
                                                    fill='black', width=3)


if __name__ == "__main__":
    app = App()
    app.mainloop()
