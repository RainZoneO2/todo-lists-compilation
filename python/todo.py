from dataclasses import dataclass, field
from datetime import date
from itertools import count
from sys import version
from queue import PriorityQueue

from tkinter import *
from tkinter.ttk import *


@dataclass
class todo: #Individual Todo Item
    name: str
    description: str
    deadline: date # Year, Month, Day
    itemid: int = field(default_factory=count().__next__, init=False)

@dataclass
class todo_list: #List of Todos
    name: str
    description: str
    todos = PriorityQueue()

    def add_item(self, item: todo):
        '''Adds item into todo list.'''

        self.todos.put((item.itemid, item))


    def remove_item(id: int):
        '''Removes item with id from todo list.'''

        pass

    def empty(self):
        '''Empties the todo list.'''

        while len(self.todos.queue) != 0:
            self.todos.get()
        print("Queue has been emptied!")

    def change_priority(from_id: int, to_id: int):
        '''Changes priority of item with id to another id.'''

        pass


    def list(self):
        '''Lists all items in todo list.'''

        for item in self.todos.queue:
            print(item)


def info_print():
    '''Returns general info.'''

    _version = 'Python Todo List using Python: {}'.format(version)
    _today = 'Todays Date: {}'.format(date.today())
    #print(_version)
    #print(_today)

    return _version, _today

def init_gui():
    '''GUI is initialized here.'''

    #Creates Window
    window = Tk() 

    #GUI Frames
    frm_info = Frame(master=window, relief=SUNKEN)
    frm_input = Frame(master=window)

    #General Info
    _version, _today = info_print()
    Label(master=frm_info, text= _version).pack()
    Label(master=frm_info, text = _today).pack()

    #Task Info
    Label(master=frm_input, text= "Input task name: ").pack()

    ent_name = Entry(master=frm_input)
    ent_name.pack()

    Label(master=frm_input, text= "Input task description: ").pack()

    txt_description = Text(master=frm_input)
    txt_description.pack()

    task_description = txt_description.get("1.0", END)

    #deadline = input('Input deadline in the format (Year,Month,Day): ')
    #Use tkCalender for this ^

    frm_info.pack()
    frm_input.pack()

    window.mainloop()




def main():
    '''Where it all begins..'''

    init_gui()

    #item = todo(name, description, deadline)
    #print(item)
    #todos = todo_list('List', 'Work')
    
    #todos.add_item(item)
    #todos.list()
    

if __name__ == "__main__":
    main()
