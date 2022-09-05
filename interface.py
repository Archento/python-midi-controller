import src.midi_out as m_out

from tkinter import *


app = Tk()
app.title("Python MIDI Tool")
app.geometry("400x350+200+200")

label = Label(text = "Test Label")
label.pack()


midi_output, portname = m_out.get_midi_out(2)


def button_pressed():
    print('The button was pressed')
    m_out.play_chord(midi_output, [60, 64, 67, 71], velocity=100, hold_time=3)


button1 = Button(text = "Drück mir", command = button_pressed) 
button1.pack()


app.mainloop()