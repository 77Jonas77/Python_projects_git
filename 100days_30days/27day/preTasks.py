import tkinter


def add(*args):
    """Wczyta dowolnie duzo wart jako tuple"""
    print(args)


def xd(**kwargs):
    """Wczyta dowolnie duzo wart jako tuple"""
    print(kwargs)


xd(a=1, b=2, c=3)

window = tkinter.Tk()
window.title("Janek to grubas")
window.minsize(500, 500)

my_label = tkinter.Label(window, text="Janek to grubas", font=("Helvetica", 20))
my_label.pack()

window.mainloop()
