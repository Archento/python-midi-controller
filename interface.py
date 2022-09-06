import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import src.midi_in as m_in
import src.midi_out as m_out

###############################
########## VARIABLES ##########
###############################

app = tk.Tk()
app.title("Python MIDI Tool")
app.geometry("560x350")

midi_input = None
midi_output = None

###############################
########## FUNCTIONS ##########
###############################

def format_name(port_name, port_list):
    """Remove index digits from port names

    Args:
        port_name (str): name of MIDI port
        port_list (list): array of MIDI ports

    Returns:
        str: formatted MIDI port name
    """
    return port_name[:-2] if len(port_list) > 1 else port_name # ternary operator instead of simple if-else


def set_midi_in_port():
    """Sets selected MIDI IN port via "get_midi_in()" and enables "Listen"-button
    """
    global midi_input
    chosen_in_port = in_ports[midi_in_menu.get()]
    midi_input, portname = m_in.get_midi_in(chosen_in_port)
    showinfo(
        title="Result",
        message=f"You selected {format_name(portname, in_list)} as your IN port."
    )
    btn_set_midi_in.state(["disabled"])
    btn_listen.state(["!disabled"])


def set_midi_out_port():
    """Sets selected MIDI OUT port via "get_midi_out()" and enables "Chord"-button
    """
    global midi_output
    chosen_out_port = out_ports[midi_out_menu.get()]
    midi_output, portname = m_out.get_midi_out(chosen_out_port)
    showinfo(
        title="Result",
        message=f"You selected {format_name(portname, out_list)} as your OUT port."
    )
    btn_set_midi_out.state(["disabled"])
    btn_play.state(["!disabled"])


def midi_listen():
    """Catch and display incoming MIDI notes
    """
    msg = midi_input.get_message()
    if msg:
        message, delta = msg
        [event, note, velocity] = message
        if event not in m_in.channel_events:
            pass
        field_onoff.config(text=f"{m_in.channel_events[event]}")
        field_note.config(text=f"{note}")
        field_velocity.config(text=f"{velocity}")
    app.after(100, midi_listen)


def test_chord():
    """Outputs a set of MIDI notes to test MIDI OUT functionality
    """
    m_out.play_chord(midi_output, [60, 64, 67, 71], velocity=100, hold_time=3)


###############################
########## INTERFACE ##########
###############################

########## MIDI IN PORT SELECTION ##########
# Label for MIDI IN port menu 
label_in_port = tk.Label(text = "MIDI In port:")
label_in_port.grid(row = 0, column = 1, sticky = "E", pady = 20)
# Create dictionary for MIDI IN port names
in_ports = {}
in_list = m_in.get_in_ports()
# get port names into "in_ports"; remove index digits from port names via "format_name()"
for portno, name in enumerate(in_list):
    in_ports[format_name(name, in_list)] = portno
# Create and place MIDI IN port dropdown menu
midi_in_menu = ttk.Combobox(app)
midi_in_menu["state"] = "readonly"
midi_in_menu["values"] = list(in_ports.keys()) # use keys of "in_ports" dictionary as menu options
midi_in_menu.set(list(in_ports.keys())[0])
midi_in_menu.grid(row = 0, column = 2)
# Create and place button for setting selected MIDI IN port
btn_set_midi_in = ttk.Button(text="Set", command=set_midi_in_port)
btn_set_midi_in.grid(row = 0, column = 3)

########## MIDI OUT PORT SELECTION ##########
# Label for MIDI OUT port menu 
label_out_port = tk.Label(text = "MIDI Out port:")
label_out_port.grid(row = 1, column = 1, sticky = tk.E) # constant E as part of tk
# Create dict for MIDI OUT port names
out_ports = {}
out_list = m_out.get_out_ports()
for portno, name in enumerate(out_list):
    out_ports[format_name(name, out_list)] = portno
# Create and place MIDI OUT port dropdown menu
midi_out_menu = ttk.Combobox(app)
midi_out_menu["state"] = "readonly" # change default setting of combobox from read/write
midi_out_menu["values"] = list(out_ports.keys())
midi_out_menu.set(list(out_ports.keys())[0])
midi_out_menu.grid(row = 1, column = 2)
# Create and place button for setting selected MIDI OUT port
btn_set_midi_out = ttk.Button(text = "Set", command = set_midi_out_port)
btn_set_midi_out.grid(row = 1, column = 3)

########## SEPARATOR ##########
sep = ttk.Separator(app, orient=tk.HORIZONTAL)
sep.grid(row = 2, column = 1, pady = 20, columnspan = 3, sticky=tk.EW)

########## LABELS FOR "MIDI IN"-MONITOR GRID ##########
# Create headings for displayed MIDI
label_onoff = tk.Label(text = "Event")
label_note = tk.Label(text = "Note")
label_velocity = tk.Label(text = "Velocity")
# Place labels
label_onoff.grid(row = 3, column = 1, padx = 20, pady = 20, ipadx = 20)
label_note.grid(row = 3, column = 2, padx = 20)
label_velocity.grid(row = 3, column = 3, padx = 20)
# Create labels for displaying recorded MIDI values
field_onoff = tk.Label()
field_note = tk.Label()
field_velocity = tk.Label()
# Place labels
field_onoff.grid(row = 4, column = 1, padx = 20, pady = 10)
field_note.grid(row = 4, column = 2, padx = 20)
field_velocity.grid(row = 4, column = 3, padx = 20)

########## LISTEN-BUTTON ##########
btn_listen = ttk.Button(text = "Listen", command = midi_listen)
btn_listen.grid(row = 4, column = 0, padx = 20, sticky = "W")
btn_listen.state(["disabled"])

########## CHORD-BUTTON ##########
btn_play = ttk.Button(text = "Chord", command = test_chord)
btn_play.grid(row = 5, column = 0, pady = 50)
btn_play.state(["disabled"])


#############################
########## RUN APP ##########
#############################

app.mainloop()
