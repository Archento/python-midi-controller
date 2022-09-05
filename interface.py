import time
from tkinter import *

import src.midi_in as m_in
import src.midi_out as m_out

app = Tk()
app.title("Python MIDI Tool")
app.geometry("400x350+200+200")

label = Label(text = "Test Label")
label.pack()

# midi_input, input_port_name = m_in.get_midi_in(0)
# midi_output, output_port_name = m_out.get_midi_out(2)


def button_pressed():
    print('The button was pressed')
    m_out.play_chord(midi_output, [60, 64, 67, 71], velocity=100, hold_time=3)

button1 = Button(text = "Test chord", command = button_pressed)
button1.pack()

midi_input, input_port_name = m_in.get_midi_in(0)

def press_listen():
    msg = midi_input.get_message()
    if msg:
        message, delta = msg
        [event, note, velocity] = message
        if event not in m_in.channel_events:
            pass
        label.config(text=f"channel: {m_in.channel_events[event]}, note: {note}, velocity: {velocity}")
    app.after(100, press_listen)

btn_listen = Button(text = "Listen", command = press_listen)
btn_listen.pack()

app.mainloop()
