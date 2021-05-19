from tkinter import *

size_of_board = 600
number_of_dots = 6
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
dot_color = '#7BC043'
player1_color = '#0492CF'
player1_color_light = '#67B0CF'
player2_color = '#EE4035'
player2_color_light = '#EE7E77'
Green_color = '#7BC043'
distance_between_dots = size_of_board / number_of_dots 
dot_width = .25 * distance_between_dots
edge_width = .1 * distance_between_dots

window = Tk()
window.title("Dots and Line Game")
canvas = Canvas(window, width=size_of_board, height=size_of_board)
canvas.pack() #Geometry manager. 
window.mainloop(30)

# First Row and Column
#x = 0 * distance_between_dots+distance_between_dots/2
canvas.create_line(50, 50, 550, 50, fill='gray', dash = (2,2)) #row1
canvas.create_line(50, 150, 550, 150, fill='gray', dash = (2,2)) #row2
canvas.create_line(50, 250, 550, 250, fill='gray', dash = (2,2)) #row3
canvas.create_line(50, 350, 550, 350, fill='gray', dash = (2,2)) #row4
canvas.create_line(50, 450, 550, 450, fill='gray', dash = (2,2)) #row5
canvas.create_line(50, 550, 550, 550, fill='gray', dash = (2,2)) #row6

canvas.create_line(50, 50, 50, 550, fill='gray', dash = (2,2)) #col1
canvas.create_line(150, 50, 150, 550, fill='gray', dash = (2,2)) #col2
canvas.create_line(250, 50, 250, 550, fill='gray', dash = (2,2)) #col3
canvas.create_line(350, 50, 350, 550, fill='gray', dash = (2,2)) #col4
canvas.create_line(450, 50, 450, 550, fill='gray', dash = (2,2)) #col5
canvas.create_line(550, 50, 550, 550, fill='gray', dash = (2,2)) #col5


