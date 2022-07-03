import math

length = float(input("Enter the length of the room"))
width = float(input("Enter the Width of the room"))
height = float(input("Enter the Height of the room"))

#variable used to calculate the area of the floor
area = (length * length) + (width * width)

#variable to calculate the paint needed is this
paint_needed = area / 350


#the variable that is used to declare the value of pi
pi = math.pi 

#variable to calculte the volume of the room 

volume = length * width * height

# below are the print statments that are used to print the values
print(area,  "is the area of the Floor")
print(f'the amount of paint neeeded is {paint_needed:.2f}')
print(volume, "this is the volume of the room")

if area in area:
    area = length * length + width *width
    print('all good')
    
else:
    print('wrong input')