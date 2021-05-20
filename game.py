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
for n in range(50, 650, 100):
  canvas.create_line(50, n, 550, n, fill='gray', dash = (2,2)) # create 6 rows
  canvas.create_line(n, 50, n, 550, fill='gray', dash = (2,2)) #col1



