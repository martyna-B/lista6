from tkinter import *
import tkinter.ttk as ttk
import math

window = Tk()
window.title('Narzędzie rysowania wykresów.')
window.resizable(width = False, height = False)

recepy_label = ttk.Label(window, width = 15, text = "Wzór funkcji: ", anchor = CENTER, padding = 4)
recepy_label.grid(row = 0, column = 0, columnspan = 3)

write_recepy = Entry(window, width = 90).grid(row = 0, column = 3, columnspan = 19)

nothing_label_1 = ttk.Label(window, width = 100).grid(row = 4, column = 0, columnspan = 20)
nothing_label_2 = ttk.Label(window, width = 100).grid(row = 8, column = 0, columnspan = 20)
nothing_label_3 = ttk.Label(window, width = 100).grid(row = 9, column = 0, columnspan = 20)

plot_canvas = Canvas(window, width = 400, height = 400, bg = "blue")
plot_canvas.grid(row = 0, column = 0, columnspan = 16, rowspan = 16)
    
sin_button = Button(window, width = 10, text = "sin", anchor = CENTER)
sin_button.grid(row = 1, column = 4, columnspan = 2, pady = 2, padx = 2)

cos_button = Button(window, width = 10, text = "cos", anchor = CENTER)
cos_button.grid(row = 1, column = 6, columnspan = 2, pady = 2, padx = 2)

tan_button = Button(window, width = 10, text = "tan", anchor = CENTER)
tan_button.grid(row = 1, column = 8, columnspan = 2, pady = 2, padx = 2)

exp_button = Button(window, width = 10, text = "exp", anchor = CENTER)
exp_button.grid(row = 1, column = 10, columnspan = 2, pady = 2, padx = 2)

division_button = Button(window, width = 10, text = "/", anchor = CENTER)
division_button.grid(row = 2, column = 4, columnspan = 2, pady = 2, padx = 2)

mul_button = Button(window, width = 10, text = "*", anchor = CENTER)
mul_button.grid(row = 2, column = 6, columnspan = 2, pady = 2, padx = 2)

plus_button = Button(window, width = 10, text = "+", anchor = CENTER)
plus_button.grid(row = 2, column = 8, columnspan = 2, pady = 2, padx = 2)

minus_button = Button(window, width = 10, text = "-", anchor = CENTER)
minus_button.grid(row = 2, column = 10, columnspan = 2, pady = 2, padx = 2)

open_button = Button(window, width = 10, text = "(", anchor = CENTER)
open_button.grid(row = 3, column = 4, columnspan = 2, pady = 2, padx = 2)
close_button = Button(window, width = 10, text = ")", anchor = CENTER)
close_button.grid(row = 3, column = 6, columnspan = 2, pady = 2, padx = 2)

pi_button = Button(window, width = 10, text = "**", anchor = CENTER)
pi_button.grid(row = 3, column = 8, columnspan = 2, pady = 2, padx = 2)

equal_button = Button(window, width = 10, text = "=", anchor = CENTER)
equal_button.grid(row = 3, column = 10, columnspan = 2, pady = 2, padx = 2)


x_axis_label = ttk.Label(window, width = 15, text = "Zakres osi x:", anchor = CENTER, padding = 4).grid(row = 5, column = 0, columnspan = 3)
x_from_label = ttk.Label(window, width = 5, text = "od:", anchor = E).grid(row = 5, column = 3)
x_from_entry = Entry(window, width = 15).grid(row = 5, column = 4, columnspan = 3)
x_to_label = ttk.Label(window, width = 5, text = "do:", anchor = E).grid(row = 5, column = 7)
x_to_entry = Entry(window, width = 15).grid(row = 5, column = 8, columnspan = 3)
x_label_label = ttk.Label(window, width = 10, text = "Etykieta:", anchor = E).grid(row = 5, column = 11, columnspan = 2)
x_label_entry = Entry(window, width = 35)
x_label_entry.grid(row = 5, column = 13, columnspan = 7, padx = 4)
x_label_entry.insert(0, "x")

y_axis_label = ttk.Label(window, width = 15, text = "Zakres osi y:", anchor = CENTER, padding = 4).grid(row = 6, column = 0, columnspan = 3)
y_from_label = ttk.Label(window, width = 5, text = "od:", anchor = E).grid(row = 6, column = 3)
y_from_entry = Entry(window, width = 15).grid(row = 6, column = 4, columnspan = 3)
y_to_label = ttk.Label(window, width = 5, text = "do:", anchor = E).grid(row = 6, column = 7)
y_to_entry = Entry(window, width = 15).grid(row = 6, column = 8, columnspan = 3)
y_label_label = ttk.Label(window, width = 10, text = "Etykieta:", anchor = E).grid(row = 6, column = 11, columnspan = 2)
y_label_entry = Entry(window, width = 35)
y_label_entry.grid(row = 6, column = 13, columnspan = 7, padx = 4)
y_label_entry.insert(0, "y")

title_label = ttk.Label(window, width = 15, text = "Tytuł wykresu:", anchor = CENTER, padding = 4).grid(row = 7, column = 0, columnspan = 3)
title_entry = Entry(window, width = 40)
title_entry.grid(row = 7, column = 3, columnspan = 8)
title_entry.insert(0, "Wykres")

legend_button = Checkbutton(window, width = 20, text = "Pokaż legendę")
legend_button.grid(row = 7, column = 11, columnspan = 4)
#nothing_label_2 = ttk.Label(window, width = 100).grid(row = 4, column = 0, columnspan = 20)

window.mainloop()
