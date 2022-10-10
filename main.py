import tkinter as tk
from tkinter import ttk

def main():
    window = tk.Tk()

    ciudades = ['Medellín', 'Bogotá', 'Cali', 'Pereira', 'Armenia', 'Bucaramanga', 'Pasto']
    ciudades = tk.StringVar(value=ciudades)
    lbl_inicio = ttk.Label(window, text='Ciudades:')
    lbl_inicio.grid(column=0, row=0)

    lst_bx = tk.Listbox(window, height=10, listvariable=ciudades)
    lst_bx.grid(column=0, row=1, sticky=tk.W)

    window.mainloop()

if __name__ == '__main__':
    main()