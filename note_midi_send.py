import time

import rtmidi.midiutil as midi
from rtmidi.midiconstants import NOTE_ON, NOTE_OFF

def play_note(note, velocity=127, hold_time=1):
    midi_out.send_message([NOTE_ON, note, velocity]) # note ON
    time.sleep(hold_time)
    midi_out.send_message([NOTE_OFF, note, 0]) # note OFF


def play_chord(notes, velocity=127, hold_time=1):
    for note in notes:
        midi_out.send_message([NOTE_ON, note, velocity]) # note ON
    time.sleep(hold_time)
    for note in notes:
        midi_out.send_message([NOTE_OFF, note, 0]) # note OFF


midi_out, portname = midi.open_midioutput()

with midi_out:
    play_chord([60, 64, 67, 71], hold_time=3)
    time.sleep(0.1)

midi_out.close_port()
del midi_out
