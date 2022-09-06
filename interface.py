import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import src.midi_in as m_in
import src.midi_out as m_out

app = tk.Tk()
app.title("Python MIDI Tool")
app.geometry("560x350")

midi_input = None
midi_output = None

########## MIDI LISTEN ##########

def press_listen():
    msg = midi_input.get_message()
    if msg:
        message, delta = msg
        [event, note, velocity] = message
        if event not in m_in.channel_events:
            pass
        field_onoff.config(text=f"{m_in.channel_events[event]}")
        field_note.config(text=f"{note}")
        field_velocity.config(text=f"{velocity}")
    app.after(100, press_listen)


btn_listen = ttk.Button(text = "Listen", command = press_listen)
btn_listen.grid(row = 4, column = 0, padx = 20, sticky = "W")
btn_listen.state(['disabled'])

########## PLAY SOUND ########## 
def play_sound():
    print('The button was pressed')
    # m_out.play_chord(midi_output, [60, 64, 67, 71], velocity=100, hold_time=3)

button1 = ttk.Button(text = "Test chord", command = play_sound)
button1.grid(row = 5, column = 0, pady = 50)


########## MIDI IN-PORT MENU ##########
label_in_port = tk.Label(text = "MIDI In port:")
label_in_port.grid(row = 0, column = 1, sticky = "E", pady = 20)

in_ports = {}
for portno, name in enumerate(m_in.get_in_ports()):
    in_ports[name] = portno

midi_in_menu = ttk.Combobox(app)
midi_in_menu['state'] = 'readonly'
midi_in_menu["values"] = list(in_ports.keys())
midi_in_menu.set(list(in_ports.keys())[0])
midi_in_menu.grid(row = 0, column = 2)


def set_midi_in_port():
    global midi_input
    chosen_in_port = in_ports[midi_in_menu.get()]
    midi_input, portname = m_in.get_midi_in(chosen_in_port)
    showinfo(
        title='Result',
        message=f'You selected {portname} as your IN port.'
    )
    btn_set_midi_in.state(['disabled'])
    btn_listen.state(['!disabled'])

btn_set_midi_in = ttk.Button(text="Set", command=set_midi_in_port)
btn_set_midi_in.grid(row = 0, column = 3)


########## MIDI OUT-PORT MENU ##########
label_out_port = tk.Label(text = "MIDI Out port:")
label_out_port.grid(row = 1, column = 1, sticky = "E")

# Get dict of MIDI Out ports
out_ports = {}
for portno, name in enumerate(m_out.get_out_ports()):
    out_ports[name] = portno

midi_out_menu = ttk.Combobox(app)
midi_out_menu['state'] = 'readonly'
midi_out_menu["values"] = list(out_ports.keys())
midi_out_menu.set(list(out_ports.keys())[0])
midi_out_menu.grid(row = 1, column = 2)


def set_midi_out_port():
    global midi_output
    chosen_out_port = out_ports[midi_out_menu.get()]
    midi_output, portname = m_out.get_midi_out(chosen_out_port)
    showinfo(
        title='Result',
        message=f'You selected {portname} as your OUT port.'
    )
    btn_set_midi_out.state(['disabled'])
    btn_listen.state(['!disabled'])
    print(btn_listen.state)

# Assign "set_midi_out_port" function to button
btn_set_midi_out = ttk.Button(text = "Set", command = set_midi_out_port)
btn_set_midi_out.grid(row = 1, column = 3)


########## SEPARATOR ##########
sep = ttk.Separator(app, orient=tk.HORIZONTAL)
sep.grid(row = 2, column = 0, pady = 20, columnspan = 4, sticky=tk.EW)


########## LABELS FOR MIDI IN MONITOR GRID ##########
label_onoff = tk.Label(text = "Event")
label_note = tk.Label(text = "Note")
label_velocity = tk.Label(text = "Velocity")

label_onoff.grid(row = 3, column = 1, padx = 20, pady = 20, ipadx = 20)
label_note.grid(row = 3, column = 2, padx = 20)
label_velocity.grid(row = 3, column = 3, padx = 20)

field_onoff = tk.Label()
field_note = tk.Label()
field_velocity = tk.Label()

field_onoff.grid(row = 4, column = 1, padx = 20, pady = 10)
field_note.grid(row = 4, column = 2, padx = 20)
field_velocity.grid(row = 4, column = 3, padx = 20)



app.mainloop()
