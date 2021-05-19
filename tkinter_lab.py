from tkinter import *
window = Tk()
window.title("Stick Figure Drawing")
canvas = Canvas(window, width=300, height=300)
canvas.pack()
window.mainloop(30)
canvas.create_oval(100, 50, 180, 130) #head
canvas.create_oval(114, 80, 124, 84) #left eye
canvas.create_oval(160, 80, 170, 84) #right eye
canvas.create_arc(115, 95, 165, 115, start=160, extent=200, width=2, outline="red", style="chord") #smile
canvas.create_line(140, 130, 140, 220) #body
canvas.create_line(140, 220, 105, 270) #left leg
canvas.create_line(140, 220, 175, 270) #right leg
canvas.create_line(140, 175, 105, 200) #left arm
canvas.create_line(140, 175, 175, 200) #right arm

