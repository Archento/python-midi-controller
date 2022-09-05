"""
This module is an example for generating MIDI output.
"""
import time
# Only modules 'midiutil' and 'midiconstants' are imported and assigned to var 'midi'
import rtmidi.midiutil as midi
# variables imported from midiconstants for better readability of code
from rtmidi.midiconstants import NOTE_OFF, NOTE_ON

# function for one single note
def play_note(midi_obj, note, velocity=0, hold_time=1) -> None:
    """Plays single notes from given rtmidi object.
    Interaction is based on the rtmidi library.

    Args:
        midi_obj (Object): rtmidi created Object
        note (int): MIDI note number (0-127)
        velocity (int, optional): MIDI velocity signal. Defaults to 0.
        hold_time (int, optional): Nr of seconds for the note to hold. Defaults to 1.
    """
    midi_obj.send_message([NOTE_ON, note, velocity]) # note ON
    time.sleep(hold_time)
    midi_obj.send_message([NOTE_OFF, note, 0]) # note OFF

# function for multiple notes (notes = list)
def play_chord(midi_obj, notes, velocity=0, hold_time=1) -> None:
    """Plays multiple notes from given rtmidi object.
    Interaction is based on the rtmidi library.

    Args:
        midi_obj (Object): rtmidi created Object
        notes (list): MIDI note number (0-127)
        velocity (int, optional): MIDI velocity signal. Defaults to 0.
        hold_time (int, optional): Nr of seconds for the note to hold. Defaults to 1.
    """
    for note in notes:
        midi_obj.send_message([NOTE_ON, note, velocity]) # note ON
    time.sleep(hold_time)
    for note in notes:
        midi_obj.send_message([NOTE_OFF, note, 0]) # note OFF

def get_midi_out() -> tuple:
    """Creates outbound rtmidi object for further use

    Returns:
        tuple: rtmidi object, port name
    """
    return midi.open_midioutput()

# EXAMPLE: destructured assignment of "open_midioutput"-tuple
# midi_output, portname = get_midi_out()

# with midi_output:
#     play_chord(midi_output, [60, 64, 67, 71], hold_time=3)
#     time.sleep(0.1)

# midi_output.close_port()
# del midi_output
