import time

import rtmidi
from rtmidi.midiconstants import NOTE_ON, NOTE_OFF

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
# print(available_ports)


def play_note(note, velocity=127, hold_time=1):
    midiout.send_message([NOTE_ON, note, velocity]) # note ON
    time.sleep(hold_time)
    midiout.send_message([NOTE_OFF, note, 0]) # note OFF


def play_chord(notes, velocity=127, hold_time=1):
    for note in notes:
        midiout.send_message([NOTE_ON, note, velocity]) # note ON
    time.sleep(hold_time)
    for note in notes:
        midiout.send_message([NOTE_OFF, note, 0]) # note OFF


midiout.open_port(2)

with midiout:
    play_chord([60, 64, 67, 71], hold_time=3)
    time.sleep(0.1)

del midiout
