from tkinter import *
root = Tk()
root.title("Area and Perimeter Activity")
root.geometry("500x300")

'''
Kristian M. Biñas
Activity Area and Perimeter
'''
label_length = Label(root, text="Enter the Length of rectangular")
label_length.pack()
length = Entry(root, width=50)
length.pack()

label_width = Label(root, text="Enter the width of rectangular")
label_width.pack()
width = Entry(root, width=50)
width.pack()

def area_perimeter():
    length_value = length.get()
    width_value = width.get()

    if width_value == length_value:
        area = int(length_value) * int(width_value)
        formatted_area = "{:,}".format(area)
        display_area = Label(root, text="The Area is " + str(formatted_area))
        display_area.pack()

    if width_value != length_value:
        perimeter = (int(length_value) + int(width_value)) * 2
        formatted_perimeter = "{:,}".format(perimeter)
        display_perimeter = Label(root, text="The Perimeter is " + str(formatted_perimeter))
        display_perimeter.pack()
def clear_fields():
    length.delete(0, 'end')
    width.delete(0, 'end')
myButton = Button(root, text="Submit", command=area_perimeter)
myButton.pack()
myClear = Button(root, text="Clear", command=clear_fields)
myClear.pack()


root.mainloop()