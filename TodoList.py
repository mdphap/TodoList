#! python3
# please install tkcalendar and babel (if needed) before using.

from datetime import datetime
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from tkcalendar import Calendar, DateEntry

# convert string to date with multiple formats
def str_to_date(date_text):
    for fmt in ('%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y', '%d/%m/%Y'):
        try:
            date = datetime.strptime(date_text, fmt).date()
            return date
        except ValueError:
            pass
    raise ValueError('No valid date format found, see the list below for valid date formats:\n 1. %Y-%m-%d\n 2. %Y/%m/%d\n 3. %d-%m-%Y\n 4. %d/%m/%Y')

class Todo():
    __TodoList = []
    __IDcount = []

    def __init__(self, work_name, start_date, end_date, status):
        self.ID = 'ID_' + str(len(Todo.__IDcount) + 1)
        self.work_name = work_name
        self.start_date = str_to_date(start_date)
        self.end_date = str_to_date(end_date)
        if status in ['Planning', 'Doing', 'Complete']:
            self.status = status
        else:
            print('The status can only be: Planning, Doing or Complete')
            return
        Todo.__TodoList.append(self)
        Todo.__IDcount.append(len(Todo.__IDcount) + 1)
        Todo.__sort()

    def __sort():
        Todo.__TodoList.sort(key = lambda x: x.start_date)

    def __edit(ID, **kwargs):
        for job in Todo.__TodoList:
            if job.ID == ID:
                for k,w in kwargs.items():
                    if (k == 'start_date') | (k == 'end_date'):
                        w = str_to_date(w)
                    job.__dict__[k] = w
        Todo.__sort()

    def __delete(ID):
        for job in Todo.__TodoList:
            if job.ID == ID:
                Todo.__TodoList.remove(job)
        Todo.__sort()

# Controller functions
def TDL_add(work_name, start_date, end_date, status):
    Todo(work_name, start_date, end_date, status)
    print('Your job is added.')

def TDL_edit(ID, **kwargs):
    Todo._Todo__edit(ID, **kwargs)
    print('Your job is edited.')

def TDL_delete(ID):
    Todo._Todo__delete(ID)
    print('Your job is deleted.')

def TDL_view():
    TDL = Todo._Todo__TodoList.copy()
    root = tk.Tk()
    root.title('To do list viewer')
    cal = Calendar(root)
    for job in TDL:
        cal.calevent_create(job.start_date, job.work_name, job.status)
    view_config(cal)
    root.lift()
    root.attributes('-topmost', True)
    root.attributes('-topmost', False)
    root.mainloop()

def TDL_print():
    TDL = Todo._Todo__TodoList.copy()
    for i in range(len(TDL)):
        print('{}. {}'.format(i + 1, TDL[i].work_name))
        print('Job\'s ID: {} (use this to refer to the job)'.format(TDL[i].ID))
        print('Start Date: ' + str(TDL[i].start_date))
        print('End Date: ' + str(TDL[i].end_date))
        print('Status: ' + TDL[i].status)

# View configurations
def view_config(cal_obj):
    cal_obj.tag_config('Planning', background = 'blue')
    cal_obj.tag_config('Doing', background = 'red')
    cal_obj.tag_config('Complete', background = 'green')
    cal_obj.pack(fill = 'both')
                    

    
