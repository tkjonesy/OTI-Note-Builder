import tkinter as tk
from tkinter import *
from tkcalendar import *
from classes import *


# ------------------------------Main Menu Functions---------------------------------------------------------------------


def clear_textbox(event=None):
    textbox.delete('1.0', END)


def new_date(event=None):
    def ordinal_suffix(number):

        last_digit = number % 10

        if number in [11, 12, 13]:
            suffix = 'th'

        elif last_digit == 1:
            suffix = 'st'
        elif last_digit == 2:
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'

        return suffix

    def date_submit(*args):
        day = cal.get_date()
        suffix = ordinal_suffix(int(day.strftime('%d')))
        day = day.strftime('%A %B %d{}, %Y'.format(suffix))

        if textbox.index('end -1 chars') == '1.0':
            textbox.insert(END, day)
            start_index = textbox.index('end -9 chars')
            end_index = textbox.index('end -7 chars')
            textbox.tag_add('sup', start_index, end_index)

        else:
            textbox.insert(END, '\n\n' + day)
            start_index = textbox.index('end -9 chars')
            end_index = textbox.index('end -7 chars')
            textbox.tag_add('sup', start_index, end_index)

        container.destroy()

    def close_date(*args):
        container.destroy()

    container = tk.Canvas(root, highlightthickness=0)
    container.place(relwidth=.5, relheight=0.35, relx=0.5, rely=0.25, anchor=CENTER)

    cal = DateEntry(container, font='Lucida 16', selectmode='day')
    cal.pack(padx=50, pady=50)

    submit = tk.Button(container, text='Submit (Enter)', padx=10, pady=5, command=date_submit)
    submit.pack(padx=5, pady=5)

    close = tk.Button(container, text='Close (Esc)', padx=10, pady=5, command=close_date)
    close.pack(padx=5, pady=5)

    cal.bind('<Return>', date_submit)
    cal.bind('<Escape>', close_date)


def new_timestamp(event=None):
    def time_submit(*args):
        time = timeentry.get()
        textbox.insert('end', '\n\n' + time)
        timestamp.destroy()

    def close_timestamp(*args):
        timestamp.destroy()

    timestamp = tk.Canvas(root, highlightthickness=0)
    timestamp.place(relwidth=.5, relheight=0.35, relx=0.5, rely=0.25, anchor=CENTER)

    timelabel = tk.Label(timestamp, text='Enter 24-Hour Time\n(ex. "1351" for 1:51 PM)', font=('Lucida', 16))
    timelabel.pack(padx=5, pady=10)

    timeentry = Entry(timestamp, width=6, font=('Lucida', 20), justify=CENTER)
    timeentry.pack(padx=5, pady=10)
    timeentry.focus()

    submit = tk.Button(timestamp, text='Submit (Enter)', padx=10, pady=5, command=time_submit)
    submit.pack(padx=5, pady=5)

    close = tk.Button(timestamp, text='Close (Esc)', padx=10, pady=5, command=close_timestamp)
    close.pack(padx=5, pady=5)

    timeentry.bind('<Return>', time_submit)
    timeentry.bind('<Escape>', close_timestamp)


# --------------------------Active Window Functions---------------------------------------------------------------------


def time_cap(event=None):
    textbox.insert(END, '\nTime caption.')


def suspend_surveillance(event=None):
    def for_day():
        lastchar = textbox.get('end -2 chars')
        if lastchar.isdigit():
            textbox.insert(END,
                           '\nThe Investigator elected to suspend surveillance and resume handling at a later date.')
        elif lastchar == ' ':
            textbox.insert(END, 'The Investigator elected to suspend surveillance and resume handling at a later date.')
        else:
            textbox.insert(END,
                           ' The Investigator elected to suspend surveillance and resume handling at a later date.')
        background.destroy()

    def for_now():
        lastchar = textbox.get('end -2 chars')
        if lastchar.isdigit():
            textbox.insert(END,
                           '\nThe Investigator elected to suspend surveillance and resume handling at a later time.')
        elif lastchar == ' ':
            textbox.insert(END, 'The Investigator elected to suspend surveillance and resume handling at a later time.')
        else:
            textbox.insert(END,
                           ' The Investigator elected to suspend surveillance and resume handling at a later time.')
        background.destroy()

    def last_day():
        lastchar = textbox.get('end -2 chars')
        if lastchar.isdigit():
            textbox.insert(END, '\nThe Investigator elected to suspend surveillance.')
        elif lastchar == ' ':
            textbox.insert(END, 'The Investigator elected to suspend surveillance.')
        else:
            textbox.insert(END, ' The Investigator elected to suspend surveillance.')
        background.destroy()

    background = tk.Canvas(root, highlightthickness=0)
    background.place(relwidth=.5, relheight=0.35, relx=0.5, rely=0.25, anchor='center')

    later_date = tk.Button(background, text='For The Day', padx=10, pady=5, command=for_day)
    later_date.pack(pady=5)

    final_day = tk.Button(background, text='Final Suspend', padx=10, pady=5, command=last_day)
    final_day.pack(pady=5)

    later_time = tk.Button(background, text='Returning Same Day', padx=10, pady=5, command=for_now)
    later_time.pack(pady=5)


def investigator_arrives(event=None):
    background = tk.Canvas(root, highlightthickness=0)
    frame = tk.Frame(background)
    background.place(relwidth=.75, relheight=0.35, relx=0.5, rely=0.25, anchor='center')
    frame.pack(expand=True)

    def close_arrival(*args):
        background.destroy()

    def clear_frame():
        for widget in frame.winfo_children():
            widget.destroy()

    def inv_ari_house(x):

        def is_sub_home():
            x.subjects_house()
            lastchar = textbox.get('end -2 chars')
            if lastchar.isdigit():
                textbox.insert(END,
                               f"\nThe Investigator arrived at the Subject's residence located at {x.address} in {x.city}")
            elif lastchar == ' ':
                textbox.insert(END,
                               f"The Investigator arrived at the Subject's residence located at {x.address} in {x.city}")
            else:
                textbox.insert(END,
                               f" The Investigator arrived at the Subject's residence located at {x.address} in {x.city}")
            clear_frame()
            select_vehicles()

        def not_sub_home():
            lastchar = textbox.get('end -2 chars')
            if lastchar.isdigit():
                textbox.insert(END, f'\nThe Investigator arrived at a residence located at {x.address} in {x.city}')
            elif lastchar == ' ':
                textbox.insert(END, f'The Investigator arrived at a residence located at {x.address} in {x.city}')
            else:
                textbox.insert(END, f' The Investigator arrived at a residence located at {x.address} in {x.city}')
            clear_frame()
            select_vehicles()

        clear_frame()

        if not x.subject_house:
            is_sub_house = tk.Button(frame, text='Yes', padx=10, pady=5, command=is_sub_home)
            not_sub_house = tk.Button(frame, text='No', padx=10, pady=5, command=not_sub_home)
            is_sub_house.pack(side=LEFT, padx=5)
            not_sub_house.pack(side=LEFT, padx=5)
        else:
            is_sub_home()
            select_vehicles()

    def select_vehicles():

        vehicles_present = []

        def post_vehicles():
            textbox.insert(END, ' and observed')

            if len(vehicles_present) == 1:
                textbox.insert(END, f' a {vehicles_present[0].get_label()} present.')

            elif len(vehicles_present) == 2:
                textbox.insert(END, f' a {vehicles_present[0].get_label()} and a {vehicles_present[-1].get_label()} present.')

            else:
                for i, v in enumerate(vehicles_present):
                    if i == 0:
                        textbox.insert(END, f' a {v.get_label()}')
                    elif i == len(vehicles_present) - 1:
                        textbox.insert(END, f', and a {v.get_label()} present.')

                    else:
                        textbox.insert(END, f', a {v.get_label()}')

        def click(v, cb):
            if cb.get() == 1:
                vehicles_present.append(v)
            if cb.get() == 0 and v in vehicles_present:
                vehicles_present.remove(v)

        if len(Vehicle.all_vehicles) > 0:

            for vehicle in Vehicle.all_vehicles:
                var = IntVar()
                vehicle_cb = tk.Checkbutton(frame, text=vehicle.get_label(), variable=var, padx=10, pady=5)
                vehicle_cb.config(command=lambda v=vehicle, cb=var: click(v, cb))
                vehicle_cb.pack(pady=5)

            submit = tk.Button(frame, text='Submit', padx=10, pady=5, command=post_vehicles)
            submit.pack(padx=5, pady=5)

    if len(House.all_houses) > 0:

        for house in House.all_houses:
            house_button = tk.Button(frame, text=house.get_label(), padx=10, pady=5, command=lambda x=house: inv_ari_house(x))
            house_button.pack(padx=5, pady=5)

    close = tk.Button(background, text='Close (Esc)', padx=10, pady=5, command=close_arrival)
    close.pack(padx=5, pady=5)

    root.bind('<Escape>', close_arrival)


# -------------------------------Root-----------------------------------------------------------------------------------

root = tk.Tk()
root.geometry('900x700')
root.title('On Track Investigations Note Builder')
root.iconbitmap('images/OTI.ico')

canvas = tk.Canvas(root, bg='#EDF5F8', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

button_container = tk.Frame(canvas, bg='#bacbcf')
button_container.place(relwidth=.95, relheight=0.45, relx=0.025, rely=0.01)

# ----------------------------Main Menu---------------------------------------------------------------------------------

main_menu = tk.Frame(button_container, bg='#bacbcf')
main_menu.pack(fill='x')

new_case = tk.Button(main_menu, text='New Case', padx=10, pady=5, command=clear_textbox)
new_case.pack(side='left', anchor='n', padx=5)

new_day = tk.Button(main_menu, text='New Day', padx=10, pady=5, command=new_date)
new_day.pack(side='left', anchor='n')

new_time = tk.Button(main_menu, text='New Timestamp (Ctrl+N)', padx=10, pady=5, command=new_timestamp)
new_time.pack(side='left', anchor='n', padx=5)

root.bind('<Control-n>', new_timestamp)

# ----------------------------Active Window-----------------------------------------------------------------------------

active_window = tk.Frame(button_container, bg='#bacbcf', pady=40)
active_window.pack(fill='x')

time_caption = tk.Button(active_window, text='Time Caption (Ctrl+T)', padx=10, pady=5, command=time_cap)
time_caption.pack(pady=5)

root.bind('<Control-t>', time_cap)

suspend_surv = tk.Button(active_window, text='Suspend Surveillance', padx=10, pady=5, command=suspend_surveillance)
suspend_surv.pack(pady=5)

inv_arrive = tk.Button(active_window, text='Investigator Arrived', padx=10, pady=5, command=investigator_arrives)
inv_arrive.pack(pady=5)

# -------------------------------Textbox and Scrollbar------------------------------------------------------------------

scroll = Scrollbar(canvas)
scroll.pack(side=RIGHT, fill=Y)
textbox = Text(canvas, font=('Lucida', 12), undo=True, yscrollcommand=scroll.set)
textbox.place(relwidth=.95, relheight=0.46, relx=0.025, rely=0.53)
scroll.config(command=textbox.yview)
textbox.tag_config('sup', offset=6, font=('Lucida', 9))

root.mainloop()
