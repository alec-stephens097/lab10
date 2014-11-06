##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
rectangle = drawpad.create_rectangle(310,450,410,600, fill= 'red')
line1 = drawpad.create_line(310,450,360,400, fill= 'red')
line2 = drawpad.create_line(410,450,360,400, fill= 'red')
# What makes the windows and doors
rectangle = drawpad.create_rectangle(340,490,320,470, fill= 'white')
rectangle = drawpad.create_rectangle(380,470,400,490, fill= 'white')
rectangle = drawpad.create_rectangle(350,570,370,600, fill= 'white')
rectangle = drawpad.create_rectangle(340,500,320,520, fill= 'white')
rectangle = drawpad.create_rectangle(380,500,400,520, fill= 'white')
#Fireplace and door knob
line1 = drawpad.create_line(400,400,400,440, fill= 'green')
line2 = drawpad.create_line(410,400,410,450, fill= 'green')
line3 = drawpad.create_line(400,400,410,400, fill= 'green')
line4 = drawpad.create_line(360,590,360,580, fill= 'green')


root.mainloop()


