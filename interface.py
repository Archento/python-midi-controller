import tkinter as tk
from tkinter import ttk

import src.midi_in as m_in
import src.midi_out as m_out

app = tk.Tk()
app.title("Python MIDI Tool")
app.geometry("400x300+200+200")

sep = ttk.Separator(app, orient='horizontal')
sep.grid(row=5, column=0, ipadx=150, pady=20, columnspan = 5)


# midi_input, input_port_name = m_in.get_midi_in(0)
# midi_output, output_port_name = m_out.get_midi_out(2)



# INPUT #

midi_input, input_port_name = m_in.get_midi_in(0)

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


btn_listen = tk.Button(text = "Listen", command = press_listen)
btn_listen.grid(row = 7, column = 0, padx = 20, sticky = "W")


def button_pressed():
    print('The button was pressed')
    # m_out.play_chord(midi_output, [60, 64, 67, 71], velocity=100, hold_time=3)

button1 = tk.Button(text = "Test chord", command = button_pressed)
button1.grid(row = 8, column = 3, pady = 50)



### LAYOUT ###
# MIDI IN-PORT MENU #
label_in_port = tk.Label(text = "MIDI In port:")
label_in_port.grid(row = 0, column = 1, sticky = "E", pady = 20)

midi_in_menu = ttk.Combobox(app)
midi_in_menu["values"] = [1, 2, 3]
midi_in_menu.grid(row=0, column=2)

btn_set_midi_in = tk.Button(text="Set")
btn_set_midi_in.grid(row = 0, column = 3)


# MIDI OUT-PORT MENU #

label_out_port = tk.Label(text = "MIDI Out port:")
label_out_port.grid(row = 1, column = 1)

midi_out_menu = ttk.Combobox(app)
midi_out_menu["values"] = [1, 2, 3]
midi_out_menu.grid(row=1, column=2)

btn_set_midi_out = tk.Button(text="Set")
btn_set_midi_out.grid(row = 1, column = 3)


label_onoff = tk.Label(text = "Event")
label_note = tk.Label(text = "Note")
label_velocity = tk.Label(text = "Velocity")

label_onoff.grid(row = 6, column = 2, padx = 20, pady = 20, ipadx = 20)
label_note.grid(row = 6, column = 3, padx = 20)
label_velocity.grid(row = 6, column = 4, padx = 20)

field_onoff = tk.Label()
field_note = tk.Label()
field_velocity = tk.Label()

field_onoff.grid(row = 7, column = 2, padx = 20, pady = 10)
field_note.grid(row = 7, column = 3, padx = 20)
field_velocity.grid(row = 7, column = 4, padx = 20)

app.mainloop()
