from tkinter import *
import tkinter.ttk as ttk
import math
import matplotlib.pyplot as plt
from math import *

window = Tk()
window.title('Narzędzie do rysowania wykresów.')
window.resizable(width = False, height = False)

plot_canvas = Canvas(window, width = 400, height = 400, bg = "white")
plot_canvas.grid(row = 0, column = 0, columnspan = 16, rowspan = 16)

recepy_label = ttk.Label(window, width = 15, text = "Wzór funkcji: ", anchor = CENTER, padding = 4)
recepy_label.grid(row = 0, column = 16, columnspan = 3)

write_recepy = Entry(window, width = 85)
write_recepy.grid(row = 0, column = 19, columnspan = 17)

nothing_label_1 = ttk.Label(window, width = 100).grid(row = 4, column = 16, columnspan = 20)
nothing_label_2 = ttk.Label(window, width = 100).grid(row = 8, column = 16, columnspan = 20)
nothing_label_3 = ttk.Label(window, width = 100).grid(row = 13, column = 16, columnspan = 20)
    
sin_button = Button(window, width = 10, text = "sin", anchor = CENTER)
sin_button.grid(row = 1, column = 20, columnspan = 2, pady = 2, padx = 2)

cos_button = Button(window, width = 10, text = "cos", anchor = CENTER)
cos_button.grid(row = 1, column = 22, columnspan = 2, pady = 2, padx = 2)

tan_button = Button(window, width = 10, text = "tan", anchor = CENTER)
tan_button.grid(row = 1, column = 24, columnspan = 2, pady = 2, padx = 2)

exp_button = Button(window, width = 10, text = "exp", anchor = CENTER)
exp_button.grid(row = 1, column = 26, columnspan = 2, pady = 2, padx = 2)

division_button = Button(window, width = 10, text = "/", anchor = CENTER)
division_button.grid(row = 2, column = 20, columnspan = 2, pady = 2, padx = 2)

mul_button = Button(window, width = 10, text = "*", anchor = CENTER)
mul_button.grid(row = 2, column = 22, columnspan = 2, pady = 2, padx = 2)

plus_button = Button(window, width = 10, text = "+", anchor = CENTER)
plus_button.grid(row = 2, column = 24, columnspan = 2, pady = 2, padx = 2)

minus_button = Button(window, width = 10, text = "-", anchor = CENTER)
minus_button.grid(row = 2, column = 26, columnspan = 2, pady = 2, padx = 2)

open_button = Button(window, width = 10, text = "(", anchor = CENTER)
open_button.grid(row = 3, column = 20, columnspan = 2, pady = 2, padx = 2)

close_button = Button(window, width = 10, text = ")", anchor = CENTER)
close_button.grid(row = 3, column = 22, columnspan = 2, pady = 2, padx = 2)

pi_button = Button(window, width = 10, text = "**", anchor = CENTER)
pi_button.grid(row = 3, column = 24, columnspan = 2, pady = 2, padx = 2)

equal_button = Button(window, width = 10, text = "=", anchor = CENTER)
equal_button.grid(row = 3, column = 26, columnspan = 2, pady = 2, padx = 2)


x_axis_label = ttk.Label(window, width = 15, text = "Zakres osi x:", anchor = CENTER, padding = 4).grid(row = 5, column = 16, columnspan = 3)
x_from_label = ttk.Label(window, width = 5, text = "od:", anchor = E).grid(row = 5, column = 19)
x_from_entry = Entry(window, width = 15).grid(row = 5, column = 20, columnspan = 3)
x_to_label = ttk.Label(window, width = 5, text = "do:", anchor = E).grid(row = 5, column = 23)
x_to_entry = Entry(window, width = 15).grid(row = 5, column = 24, columnspan = 3)
x_label_label = ttk.Label(window, width = 10, text = "Etykieta:", anchor = E).grid(row = 5, column = 27, columnspan = 2)
x_label_entry = Entry(window, width = 35)
x_label_entry.grid(row = 5, column = 29, columnspan = 7, padx = 4)
x_label_entry.insert(0, "x")

y_axis_label = ttk.Label(window, width = 15, text = "Zakres osi y:", anchor = CENTER, padding = 4).grid(row = 6, column = 16, columnspan = 3)
y_from_label = ttk.Label(window, width = 5, text = "od:", anchor = E).grid(row = 6, column = 19)
y_from_entry = Entry(window, width = 15).grid(row = 6, column = 20, columnspan = 3)
y_to_label = ttk.Label(window, width = 5, text = "do:", anchor = E).grid(row = 6, column = 23)
y_to_entry = Entry(window, width = 15).grid(row = 6, column = 24, columnspan = 3)
y_label_label = ttk.Label(window, width = 10, text = "Etykieta:", anchor = E).grid(row = 6, column = 27, columnspan = 2)
y_label_entry = Entry(window, width = 35)
y_label_entry.grid(row = 6, column = 29, columnspan = 7, padx = 4)
y_label_entry.insert(0, "y")

title_label = ttk.Label(window, width = 15, text = "Tytuł wykresu:", anchor = CENTER, padding = 4).grid(row = 7, column = 16, columnspan = 3)
title_entry = Entry(window, width = 40)
title_entry.grid(row = 7, column = 19, columnspan = 8)
title_entry.insert(0, "Wykres")

legend_button = Checkbutton(window, width = 20, text = "Pokaż legendę")
legend_button.grid(row = 7, column = 28, columnspan = 4)



message_label = Label(window, width = 60, bg = 'white')
message_label.grid(row = 14, column = 16, columnspan = 12)

# WORKING PART

def function_definition(string):
    function = list(string)
    num_of_functions = function.count(';') + 1
    for i in function:
        if i == ' ':
            function.remove(i)
    if function[0:2] == ['y', '=']:
        string_function = ''
        for i in function[2:]:
            string_function += i
    elif function[0:5] == ['f', '(', 'x', ')', '=']:
        string_function = ''
        for i in function[5:]:
            string_function += i 
    else:
        message_label.config(text = "Proszę zdefiniować funkcję jako y = ... lub f(x) = ...")
    if num_of_functions = 1:
        fun = []
        fun.append(string_function)
        return fun
    else:
        index
        for index in range(1:length(function)):
            

def close():
    """
    Closes a root window.
    """
    window.destroy()
    

draw_button = Button(window, width = 35, height = 8, text = "RYSUJ", command = function_definition)
draw_button.grid(row = 8, column = 28, rowspan = 4, columnspan = 7)

q_button = Button(window, width = 35, text = "WYJDŹ", command = close)
q_button.grid(row = 14, column = 28, columnspan = 7)

window.mainloop()
