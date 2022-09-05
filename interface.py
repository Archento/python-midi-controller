import time
from tkinter import *

import src.midi_in as m_in
import src.midi_out as m_out

app = Tk()
app.title("Python MIDI Tool")
app.geometry("400x350+200+200")

label = Label(text = "Test Label")
label.pack()


midi_input, input_port_name = m_in.get_midi_in(0)
midi_output, output_port_name = m_out.get_midi_out(2)


def button_pressed():
    print('The button was pressed')
    m_out.play_chord(midi_output, [60, 64, 67, 71], velocity=100, hold_time=3)


button1 = Button(text = "Test chord", command = button_pressed) 
button1.pack()


def press_listen():
    print('Listen was pressed')
    while True:
        # Rückgabewert von get_message ist: (<Die Note>, <vergangene Zeit seit letztem Befehl>)
        msg = midi_input.get_message()
        if msg:
            # Destrukturierung, weil wir nur einen Teil davon benutzen wollen
            message, delta = msg
            # Zugriff auf einzelne Parameter möglich (weitere Destrukturierung)
            [event, note, velocity] = message
            # keine Ausgabe, falls nicht im dict
            if event not in m_in.channel_events:
                continue
            # 'channel_events' wird  benutzt, so dass statt Zahlen die jew. Bedeutungen angezeigt werden
            print(f"channel: {m_in.channel_events[event]}, note: {note}, velocity: {velocity}")
        # Polling-Intervall (Abfragen pro Sekunde werden begrenzt, um Ressourcen zu sparen) 
        time.sleep(0.1)


btn_listen = Button(text = "Listen", command = press_listen)
btn_listen.pack()



app.mainloop()
