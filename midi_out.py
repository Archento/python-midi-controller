"""
This module is an example for generating MIDI output.
"""
import time
# Only modules 'midiutil' and 'midiconstants' are imported and assigned to var 'midi'
import rtmidi.midiutil as midi
# variables imported from midiconstants for better readability of code
from rtmidi.midiconstants import NOTE_OFF, NOTE_ON

# function for one single note
def play_note(note, velocity=127, hold_time=1):
    midi_out.send_message([NOTE_ON, note, velocity]) # note ON
    time.sleep(hold_time)
    midi_out.send_message([NOTE_OFF, note, 0]) # note OFF

# function for multiple notes (notes = list)
def play_chord(notes, velocity=127, hold_time=1):
    for note in notes:
        midi_out.send_message([NOTE_ON, note, velocity]) # note ON
    time.sleep(hold_time)
    for note in notes:
        midi_out.send_message([NOTE_OFF, note, 0]) # note OFF

# destructured assignment of "open_midioutput"-tuple
midi_out, portname = midi.open_midioutput()

with midi_out:
    play_chord([60, 64, 67, 71], hold_time=3)
    time.sleep(0.1)

midi_out.close_port()
del midi_out
