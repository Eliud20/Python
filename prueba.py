from tkinter import *
import time as tm
import threading as th

raiz = Tk()
raiz.title("Hola mundo")
raiz.resizable(True, False)
raiz.geometry("650x450")
bot = Button(raiz, text="Hola")
bot.place(x=100, y=50)

# raiz.mainloop()


def worker():
    """funcion que realiza el trabajo en el thread"""
    for i in range(5):
        print("i =", i)
        tm.sleep(1)
    return


t = th.Thread(target=worker)
t1 = th.Thread(target=raiz.mainloop())

t1.run()
t.run()
