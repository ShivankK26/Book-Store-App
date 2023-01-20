'''
Title, Author
ISBN, Year

view all records
search any entry
add any entry
update any entry
delete
close
'''

from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete.view(0,END)
    for row in backend.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)


def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))


window = Tk()
window.wm_title('BookStore')#used to write the title


l1 = Label(window,text = 'Title')
l1.grid(row=0,column=0)

l2 = Label(window,text = 'Author')
l2.grid(row=0,column=2)

l3 = Label(window,text = 'Year')
l3.grid(row=1,column=0)

l4 = Label(window,text = 'ISBN') #label is a function used to store the value like a container does.
l4.grid(row=1,column=2)

title_text = StringVar() #stringvar helps you manage the value of a widget
e1 = Entry(window,textvariable = title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable = author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window,textvariable = year_text)#entry is a textbox which accepts value in a single line from the user.
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4 = Entry(window,textvariable = isbn_text)#textvariable : In order to be able to retrieve the current text from your entry widget
e4.grid(row=1,column=3)

list1 = Listbox(window, height=6,width=35)#The ListBox widget is used to display different types of items
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)#scrollbar widget is used to scroll down the content of the other widgets
sb1.grid(row=1,column=3,rowspan=6)

list1.configure(yscrollcommand=sb1.set)#in y axis
sb1.configure(command=list1.yview)#yview is the vertical view of widget in tkinter..
list1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window,text='View All',width=12,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text='Search Entry',width=12,command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text='Add Entry',width=12,command=add_command)#Button displays info in the form of a button..
b3.grid(row=4,column=3)


b6 = Button(window,text='Close',width=12,command=window.destroy)#window.destroy destroys a widget..
b6.grid(row=7,column=3)

window.mainloop() #window. mainloop() tells Python to run the Tkinter event loop