from tkinter import *

def change():
    but2.configure(text='Utile')

def nom():
    tex1.configure(text="Welcome "+ent1.get()+" to Battle of the Clicks.")

fen = Tk()

fen.title('Battle of the clicks')

tex1 = Label(fen, text = 'Welcome to Battle of the Clicks.')
tex1.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)

tex2 = Label(fen, text = 'Dessin.')
tex2.grid(row = 1, column=0, rowspan=5, padx=20, pady=20)

ent1 = Label(fen, text = 'Nom : ')
ent1.grid(row = 1, column=1, sticky = W)
but4 = Button(fen, text = 'Valider ')
but4.grid(row = 4, column=1, sticky = W)

but1 = Button(fen, text = 'Change', command=change)
but2 = Button(fen, text = 'Inutile')
but3 = Button(fen, text = 'Quitter', command = fen.destroy)

but1.grid(row = 2, column=1, columnspan=2)
but2.grid(row = 3, column=1, columnspan=2)
but3.grid(row = 4, column=2, sticky=E)

fen.mainloop()
