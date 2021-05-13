from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from numpy import *
import thumbnail

window = Tk()
window.title('Narzędzie do rysowania wykresów.')
window.resizable(width = False, height = False)

plot_canvas = Canvas(window, width = 375, height = 375, bg = "white")
plot_canvas.grid(row = 0, column = 0, columnspan = 16, rowspan = 16)

recepy_label = ttk.Label(window, width = 15, text = "Wzór funkcji: ", anchor = CENTER, padding = 4)
recepy_label.grid(row = 0, column = 16, columnspan = 3)

write_recepy = Entry(window, width = 85)
write_recepy.grid(row = 0, column = 19, columnspan = 17)

nothing_label_1 = ttk.Label(window, width = 100).grid(row = 4, column = 16, columnspan = 20)
nothing_label_2 = ttk.Label(window, width = 100).grid(row = 8, column = 16, columnspan = 20)
nothing_label_3 = ttk.Label(window, width = 100).grid(row = 13, column = 16, columnspan = 20)

def keyboard(text):
    place = len(write_recepy.get())
    write_recepy.insert(place, text)
    
sin_button = Button(window, width = 10, text = "sin", anchor = CENTER, command = lambda:keyboard("sin"))
sin_button.grid(row = 1, column = 20, columnspan = 2, pady = 2, padx = 2)

cos_button = Button(window, width = 10, text = "cos", anchor = CENTER, command = lambda:keyboard("cos"))
cos_button.grid(row = 1, column = 22, columnspan = 2, pady = 2, padx = 2)

tan_button = Button(window, width = 10, text = "tan", anchor = CENTER, command = lambda:keyboard("tan"))
tan_button.grid(row = 1, column = 24, columnspan = 2, pady = 2, padx = 2)

exp_button = Button(window, width = 10, text = "exp", anchor = CENTER, command = lambda:keyboard("exp"))
exp_button.grid(row = 1, column = 26, columnspan = 2, pady = 2, padx = 2)

division_button = Button(window, width = 10, text = "/", anchor = CENTER, command = lambda:keyboard("/"))
division_button.grid(row = 2, column = 20, columnspan = 2, pady = 2, padx = 2)

mul_button = Button(window, width = 10, text = "*", anchor = CENTER, command = lambda:keyboard("*"))
mul_button.grid(row = 2, column = 22, columnspan = 2, pady = 2, padx = 2)

plus_button = Button(window, width = 10, text = "+", anchor = CENTER, command = lambda:keyboard("+"))
plus_button.grid(row = 2, column = 24, columnspan = 2, pady = 2, padx = 2)

minus_button = Button(window, width = 10, text = "-", anchor = CENTER, command = lambda:keyboard("-"))
minus_button.grid(row = 2, column = 26, columnspan = 2, pady = 2, padx = 2)

open_button = Button(window, width = 10, text = "(", anchor = CENTER, command = lambda:keyboard("("))
open_button.grid(row = 3, column = 20, columnspan = 2, pady = 2, padx = 2)

close_button = Button(window, width = 10, text = ")", anchor = CENTER, command = lambda:keyboard(")"))
close_button.grid(row = 3, column = 22, columnspan = 2, pady = 2, padx = 2)

pi_button = Button(window, width = 10, text = "**", anchor = CENTER, command = lambda:keyboard("**"))
pi_button.grid(row = 3, column = 24, columnspan = 2, pady = 2, padx = 2)

equal_button = Button(window, width = 10, text = "=", anchor = CENTER, command = lambda:keyboard("="))
equal_button.grid(row = 3, column = 26, columnspan = 2, pady = 2, padx = 2)


x_axis_label = ttk.Label(window, width = 15, text = "Zakres osi x:", anchor = CENTER, padding = 4).grid(row = 5, column = 16, columnspan = 3)
x_from_label = ttk.Label(window, width = 5, text = "od:", anchor = E).grid(row = 5, column = 19)
x_from_entry = Entry(window, width = 15)
x_from_entry.grid(row = 5, column = 20, columnspan = 3)

x_to_label = ttk.Label(window, width = 5, text = "do:", anchor = E).grid(row = 5, column = 23)
x_to_entry = Entry(window, width = 15)
x_to_entry.grid(row = 5, column = 24, columnspan = 3)

x_label_label = ttk.Label(window, width = 10, text = "Etykieta osi x:", anchor = E).grid(row = 5, column = 27, columnspan = 2)
x_label_entry = Entry(window, width = 35)
x_label_entry.grid(row = 5, column = 29, columnspan = 7, padx = 4)
x_label_entry.insert(0, "x")

y_label_label = ttk.Label(window, width = 10, text = "Etykieta osi y:", anchor = E).grid(row = 6, column = 27, columnspan = 2)
y_label_entry = Entry(window, width = 35)
y_label_entry.grid(row = 6, column = 29, columnspan = 7, padx = 4)
y_label_entry.insert(0, "y")



title_label = ttk.Label(window, width = 15, text = "Tytuł wykresu:", anchor = CENTER, padding = 4).grid(row = 6, column = 16, columnspan = 3)
title_entry = Entry(window, width = 40)
title_entry.grid(row = 6, column = 19, columnspan = 8)
title_entry.insert(0, "Wykres")

legend_button = Checkbutton(window, width = 20, text = "Pokaż legendę")
legend_button.grid(row = 7, column = 28, columnspan = 4)



message_label = Label(window, width = 60, bg = 'white')
message_label.grid(row = 14, column = 16, columnspan = 12)

# WORKING PART

def function_definition():

    banned_list = ['?', '"', "<", ">", "@", "#", "$", "%", "&", "_"]
    function = list(write_recepy.get())
    print(function)
    for i in function:
        if i == ' ':
            function.remove(i)

    print(function)
            
    for i in range(0, len(function)-1):       
        if function[i] == '[' or function[i]=='{':
            function[i] = '('
        elif function[i] == ']' or function[i] == '}':
            function[i] = ')'
        elif function[i] == ':':
            function[i] = '/'
        elif function[i] == ',':
            function[i] = '.'
        elif function[i] == '^':
            function[i] = '**'
        elif function[i] == '|':
            message_label.config(text = "A co to za moduł?")
        elif function[i] in banned_list:
            message_label.config(text = "Proszę nie wpisywać takich znaków.")
        
            
    index_list = [0]
    for index in range(2,len(function)):
        if function[index] == ';':
            index_list.append(index + 1)
    index_list.append(len(function)+1)

    fun = []
    for i in range(0,len(index_list)-1):
        if function[index_list[i] : index_list[i] + 2] == ['y', '=']:
            string_function = ''
            for i in function[index_list[i] + 2 : index_list[i+1]-1]:
                string_function += i
            fun.append(string_function)
        elif function[index_list[i] : index_list[i] + 5] == ['f', '(', 'x', ')', '=']:
            string_function = ''
            for i in function[index_list[i] + 5 : index_list[i+1]-1]:
                string_function += i
            fun.append(string_function)
        else:
            message_label.config(text = "Proszę zdefiniować funkcję jako y = ... lub f(x) = ... .")
            
    return fun

def save_plot():
    
    functions = function_definition()
    if len(functions) == 0:
        message_label.config(text = "Proszę zdefiniować funkcję jako y = ... lub f(x) = ... .")
        return False
    try:
        float(x_from_entry.get())
        float(x_to_entry.get())
    except:
        message_label.config(text = "Proszę podać prawidłowy zakres na osi x.")
        return False
    
    x = arange(float(x_from_entry.get()), float(x_to_entry.get()), 0.01)

    for function in functions:
        y = eval(function)
        plt.scatter(x,y)

    plt.xlabel(x_label_entry.get())
    plt.ylabel(y_label_entry.get())
    plt.title(title_entry.get())
    plt.savefig('plot.png')
    plt.show()

def show_plot():
    save_plot()
    plot_image = Image.open("plot.png")
    plot_image.resize((375, 375))
    img = ImageTk.PhotoImage(plot_image)
    plot_canvas.create_image(375, 375, image = img)
    plot_canvas.grid(row = 0, column = 0, columnspan = 16, rowspan = 16)
    

def close():
    """
    Closes a window.
    """
    window.destroy()
    

draw_button = Button(window, width = 35, height = 8, text = "RYSUJ", command = save_plot)
draw_button.grid(row = 8, column = 28, rowspan = 4, columnspan = 7)

q_button = Button(window, width = 35, text = "WYJDŹ", command = close)
q_button.grid(row = 14, column = 28, columnspan = 7)

window.mainloop()
