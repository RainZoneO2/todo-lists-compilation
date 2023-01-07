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
        '''Adds item into todo list'''
        self.todos.put((item.itemid, item))


    def remove_item(id: int):
        '''Removes item with id from todo list'''
        pass

    def empty():
        '''Empties the todo list'''
        pass

    def change_priority(from_id: int, to_id: int):
        '''Changes priority of item with id to another id'''
        pass

    def list(self):
        '''Lists all items in todo list'''
        for item in self.todos.queue:
            print(item)


def info_print():
    '''Prints general info'''
    _version = 'Python Todo List using Python: {}'.format(version)
    _today = 'Todays Date: {}'.format(date.today())
    #print(_version)
    #print(_today)

    return _version, _today

def init_gui():
    window = Tk() #Creates Window
    _version, _today = info_print()
    _ver = Label(text= _version)
    _tod = Label(text = _today)

    _ver.pack()
    _tod.pack()
    window.mainloop()



def main():
    init_gui()

    print("Input Information related to Task:")
    name = input('Input task name: ')
    description = input('Input task description: ')
    deadline = input('Input deadline in the format (Year,Month,Day): ')

    item = todo(name, description, deadline)
    print(item)
    todos = todo_list('List', 'Work')
    
    todos.add_item(item)
    todos.list()
    

if __name__ == "__main__":
    main()
