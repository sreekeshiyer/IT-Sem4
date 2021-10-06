from tkinter import *

def checkered(canvas, line_distance):
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")

canvas_width = 450
canvas_height =400
master = Tk()
canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

#drawing a checkered pattern on the canvas
checkered(canvas,10)

#drawing a star-shaped polygon on the canvas
points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
canvas.create_polygon(points, outline='black', fill='grey', width=3)

#draw gif iamge on the canvas
img = PhotoImage(file="027-face.gif")
canvas.create_image(160,160, anchor=NW, image=img)
mainloop()
