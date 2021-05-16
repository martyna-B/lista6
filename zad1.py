from tkinter import *
import tkinter.ttk as ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import *

window = Tk()
window.title('Narzędzie do rysowania wykresów.')
window.resizable(width = False, height = False)

#Canvas

plot_canvas = Canvas(window, width = 375, height = 375, bg = "white")
plot_canvas.grid(row = 0, column = 0, columnspan = 16, rowspan = 16)

#Backgrounds

backround_label_0 = Label(window, width = 95, bg = '#da7f8f', borderwidth = 5).grid(row = 0, column = 16, columnspan = 19) 
background_label_1 = Label(window, width = 50, bg = '#a7bbc7', text = "\n\n\n\n\n").grid(row = 1, column = 19, rowspan = 3, columnspan = 10)
background_label_2 = Label(window, width = 105, bg = '#e1e5ea', borderwidth = 10, text = "\t\n\n").grid(row = 5, column = 16, rowspan = 2, columnspan = 20)
background_label_3 = Label(window, width = 15, bg = '#da7f8f', borderwidth = 5).grid(row = 0, column = 16, columnspan = 3)
bg_message_label = Label(window, width = 60, bg = '#da7f8f', borderwidth = 4).grid(row = 14, column = 16, columnspan = 12)

nothing_label_1 = Label(window, width = 100).grid(row = 4, column = 16, columnspan = 20)
nothing_label_2 = Label(window, width = 100).grid(row = 8, column = 16, columnspan = 20)
nothing_label_3 = Label(window, width = 100).grid(row = 13, column = 16, columnspan = 20)

#Place to write in functions

recepy_label = Label(window, width = 15, text = "Wzór funkcji", anchor = CENTER, background = 'white')
recepy_label.grid(row = 0, column = 16, columnspan = 3, pady=4, padx=4)
write_recepy = Entry(window, width = 85)
write_recepy.grid(row = 0, column = 19, columnspan = 17)

#Calculator buttons

def keyboard(text):
    place = len(write_recepy.get())
    write_recepy.insert(place, text)
    
sin_button = Button(window, bg = '#e1e5ea', width = 10, text = "sin", anchor = CENTER, command = lambda:keyboard("sin"))
sin_button.grid(row = 1, column = 20, columnspan = 2, pady = 2, padx = 2)

cos_button = Button(window, bg = '#e1e5ea',width = 10, text = "cos", anchor = CENTER, command = lambda:keyboard("cos"))
cos_button.grid(row = 1, column = 22, columnspan = 2, pady = 2, padx = 2)

tan_button = Button(window, bg = '#e1e5ea',width = 10, text = "tan", anchor = CENTER, command = lambda:keyboard("tan"))
tan_button.grid(row = 1, column = 24, columnspan = 2, pady = 2, padx = 2)

exp_button = Button(window, bg = '#e1e5ea',width = 10, text = "exp", anchor = CENTER, command = lambda:keyboard("exp"))
exp_button.grid(row = 1, column = 26, columnspan = 2, pady = 2, padx = 2)

division_button = Button(window, bg = '#e1e5ea',width = 10, text = ":", anchor = CENTER, command = lambda:keyboard("/"))
division_button.grid(row = 2, column = 20, columnspan = 2, pady = 2, padx = 2)

mul_button = Button(window, bg = '#e1e5ea',width = 10, text = "*", anchor = CENTER, command = lambda:keyboard("*"))
mul_button.grid(row = 2, column = 22, columnspan = 2, pady = 2, padx = 2)

plus_button = Button(window, bg = '#e1e5ea',width = 10, text = "+", anchor = CENTER, command = lambda:keyboard("+"))
plus_button.grid(row = 2, column = 24, columnspan = 2, pady = 2, padx = 2)

minus_button = Button(window, bg = '#e1e5ea',width = 10, text = "-", anchor = CENTER, command = lambda:keyboard("-"))
minus_button.grid(row = 2, column = 26, columnspan = 2, pady = 2, padx = 2)

open_button = Button(window, bg = '#e1e5ea',width = 10, text = "(", anchor = CENTER, command = lambda:keyboard("("))
open_button.grid(row = 3, column = 20, columnspan = 2, pady = 2, padx = 2)

close_button = Button(window, bg = '#e1e5ea',width = 10, text = ")", anchor = CENTER, command = lambda:keyboard(")"))
close_button.grid(row = 3, column = 22, columnspan = 2, pady = 2, padx = 2)

pi_button = Button(window, bg = '#e1e5ea',width = 10, text = "^", anchor = CENTER, command = lambda:keyboard("**"))
pi_button.grid(row = 3, column = 24, columnspan = 2, pady = 2, padx = 2)

equal_button = Button(window, bg = '#e1e5ea',width = 10, text = "=", anchor = CENTER, command = lambda:keyboard("="))
equal_button.grid(row = 3, column = 26, columnspan = 2, pady = 2, padx = 2)

# Places to write in function range.

x_axis_label = Label(window, width = 15, text = "Zakres osi x:", anchor = CENTER, bg = '#e1e5ea')
x_axis_label.grid(row = 5, column = 16, columnspan = 3)

x_from_label = Label(window, width = 5, text = "od:", bg = '#e1e5ea', anchor = E)
x_from_label.grid(row = 5, column = 19)
x_from_entry = Entry(window, width = 15)
x_from_entry.grid(row = 5, column = 20, columnspan = 3)

x_to_label = Label(window, width = 5, text = "do:", anchor = E, bg = '#e1e5ea')
x_to_label.grid(row = 5, column = 23)
x_to_entry = Entry(window, width = 15)
x_to_entry.grid(row = 5, column = 24, columnspan = 3)

#Places to choose labels.

x_label_label = Label(window, width = 10, text = "Etykieta osi x:", bg = '#e1e5ea', anchor = E).grid(row = 5, column = 27, columnspan = 2)

x_label_entry = Entry(window, width = 35)
x_label_entry.grid(row = 5, column = 29, columnspan = 7, padx = 4)
x_label_entry.insert(0, "x")

y_label_label = Label(window, width = 10, text = "Etykieta osi y:", bg = '#e1e5ea', anchor = E).grid(row = 6, column = 27, columnspan = 2)

y_label_entry = Entry(window, width = 35)
y_label_entry.grid(row = 6, column = 29, columnspan = 7, padx = 4)
y_label_entry.insert(0, "y")

#Place to choose plot title.

title_label = Label(window, width = 15, text = "Tytuł wykresu:", anchor = CENTER, bg = '#e1e5ea').grid(row = 6, column = 16, columnspan = 3)
title_entry = Entry(window, width = 40)
title_entry.grid(row = 6, column = 19, columnspan = 8)
title_entry.insert(0, "Wykres")

#Place to choose legend.

is_legend = IntVar()
legend_button = Checkbutton(window, width = 20, text = "Pokaż legendę", variable = is_legend)
legend_button.grid(row = 7, column = 28, columnspan = 4)

#Place to show messages.

message_label = Label(window, width = 60, bg = 'white')
message_label.grid(row = 14, column = 16, columnspan = 12)
 
# WORKING PART

def function_definition(for_label = False):
    """
    Converts given function definition so that Python is able to draw its plot and collects them
    in a list named "fun". Returns it.
    
    Returns false if function definition contains unconvertable sign or is difined incorrect
    and informs about it through message_label.

    Parameters
    ----------
    for_label(bool): determinates if returned functions definitions will be used to create a plot(false)
                     or to be shown in legend(true).
    """

    banned_list = ['?', '"', "<", ">", "@", "#", "$", "%", "&", "_", "|"]
    convert_dic = {'[':'(', '{':'(', ']':')', '}':')', ':':'/', ",":".", "^":"**"}      
    function = list(write_recepy.get())
    
    for i in function:
        if i == ' ':
            function.remove(i)

    if for_label:
        label_function = seperate_out_fun(function)
        return label_function
    
    for i in range(0, len(function)):
        if function[i] in convert_dic:
            function[i] = convert_dic[function[i]]
        elif function[i] in banned_list:
            message_label.config(text = "Proszę nie wpisywać takich znaków jak '%s's." % function[i])
            return False

    return seperate_out_fun(function)
                  

def seperate_out_fun(function_list):
    """
    Seperates out functions from function_list. Functions are divided by sign ";".
    Returns list with functions.

    Arguments
    ---------
    function_list(list): list with chars which correctly splited are functions
    """

    if type(function_list) == list:
        index_list = [0]
        for index in range(2,len(function_list)):
            if function_list[index] == ';':
                index_list.append(index + 1)
        index_list.append(len(function_list)+1)

        fun = []
        for i in range(0,len(index_list)-1):
            if function_list[index_list[i] : index_list[i] + 2] == ['y', '=']:
                string_function = ''
                for i in function_list[index_list[i] + 2 : index_list[i+1]-1]:
                    string_function += i
                fun.append(string_function)
            elif function_list[index_list[i] : index_list[i] + 5] == ['f', '(', 'x', ')', '=']:
                string_function = ''
                for i in function_list[index_list[i] + 5 : index_list[i+1]-1]:
                    string_function += i
                fun.append(string_function)
            else:
                message_label.config(text = "Proszę zdefiniować funkcję jako y = ... lub f(x) = ... .")

        return fun
    
    else:
        raise TypeError
        
def draw_plot():
    """
    Creates a plot using functions from the list returned by function "function_definition".
    Shows it on the canvas.

    Returns False if the list is empty or if Python is unable to create their plots or if function range is incorrect.
    Informs about it through message_label.
    """

    if function_definition():
        functions = function_definition()
    else:
        return False
    
    if len(functions) == 0:
        message_label.config(text = "Proszę zdefiniować funkcję poprawnie.")
        return False

    try:
        float(x_from_entry.get())
        float(x_to_entry.get())
    except:
        message_label.config(text = "Proszę podać prawidłowy zakres na osi x.")
        x_axis_label.config(bg = '#a7bbc7')
        return False
    
    if x_from_entry.get() >= x_to_entry.get():
        message_label.config(text = "Wartość 'od' zakresu na osi x powinna być mniejsza niż wartość 'do'.")
        return False

    x_axis_label.config(bg = '#e1e5ea')
    x = arange(float(x_from_entry.get()), float(x_to_entry.get()), 0.001)
    figure = Figure(figsize=(3.7, 4), dpi=100)
    plot = figure.add_subplot(1, 1, 1)

    sus_functions = ['tan', 'cot', 'log', 'arcsin', 'arccos']
    sus_signs = ['**', '/']
    
    for function in functions:
        try:
            y = eval(function)
        except:
            message_label.config(text = "Proszę zdefiniować funkcję poprawnie.")
            return False
        for f in sus_functions:
            if f in function:
                message_label.config(text = "Proszę zwrócić uwagę, czy funkcja '%s' jest określona na zakresie." % f)
        for sign in sus_signs:
            if sign in function:
                message_label.config(text = "Proszę zwrócić uwagę, czy operator '%s' będzie działał prawidłowo." % sign)
        plot.plot(x,y)

    if is_legend.get() == 1:   
        plot.legend(function_definition(True))
        
    plot.set(title = title_entry.get(), xlabel = x_label_entry.get(), ylabel = y_label_entry.get())
    canvas = FigureCanvasTkAgg(figure, window)
    canvas.get_tk_widget().grid(row = 0, column = 0, columnspan = 16, rowspan = 16)

    
def close():
    """
    Closes a window.
    """
    window.destroy()
    

draw_button = Button(window, width = 25, height = 6, text = "RYSUJ", command = draw_plot, bg = '#a7bbc7')
draw_button.grid(row = 1, column = 29, rowspan = 3, columnspan = 5)

q_button = Button(window, width = 35, text = "WYJDŹ", command = close)
q_button.grid(row = 14, column = 28, columnspan = 7)

window.mainloop()
