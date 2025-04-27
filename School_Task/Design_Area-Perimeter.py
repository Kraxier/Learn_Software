from tkinter import *
import tkinter as tk
root = tk.Tk()
root.title("Area and Perimeter Activity")
root.geometry("500x350")
root.configure(bg='#ADD8E6')
custom_font = ('Times New Roman', 11)
'''
Kristian M. Biñas
Activity Area and Perimeter
'''
label_length = Label(root, bg='#ADD8E6',text="Enter the Length of rectangular", font=custom_font)
label_length.pack()
length = tk.Entry(root, width=50)
length.pack(pady=20)

label_width = Label(root,bg='#ADD8E6' ,text="Enter the width of rectangular", font=custom_font)
label_width.pack()
width = Entry(root, width=50)
width.pack(pady=20)

display_area = None
display_perimeter = None
error_message = None

def area_perimeter():
    length_value = length.get()
    width_value = width.get()
    global display_area, display_perimeter
    if not length_value.isdigit() or not width_value.isdigit():
        global error_message
        if error_message:
            error_message.pack_forget()
        error_message = Label(root, bg='#ADD8E6', text="Please enter a valid number", font=custom_font)
        error_message.pack(pady=10)
        return

    if width_value == length_value:
        area = int(length_value) * int(width_value)
        formatted_area = "{:,}".format(area)
        display_area = Label(root, bg='#FF7F50',text="The Area is " + str(formatted_area))
        display_area.pack(pady=20)

    if width_value != length_value:
        perimeter = (int(length_value) + int(width_value)) * 2
        formatted_perimeter = "{:,}".format(perimeter)
        display_perimeter = Label(root,bg='#FF7F50', text="The Perimeter is " + str(formatted_perimeter))
        display_perimeter.pack(pady=20)
def clear_fields():
    length.delete(0, 'end')
    width.delete(0, 'end')
    if display_area:
        display_area.pack_forget()
    if display_perimeter:
        display_perimeter.pack_forget()

myButton = Button(root, text="Submit",bg='#FF7F50' ,command=area_perimeter, font=custom_font)
myButton.pack(pady=10)
myClear = Button(root, text="Clear", bg= '#FF7F50',command=clear_fields, font=custom_font)
myClear.pack()



root.mainloop()