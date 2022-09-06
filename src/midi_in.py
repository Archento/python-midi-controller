"""
This module processes MIDI inputs
"""
import rtmidi.midiutil as midi
import rtmidi

# Method ".open_midiinput" is executed and destructured into 2 variables, which are assigned to the respective values of the tuple (= return values from open_midiinput)
def get_midi_in(port = None) -> tuple:
    """Generates MIDI input object using rtmidi-library

    Returns:
        tuple: rtmidi-object, port name
    """
    return midi.open_midiinput(port)


def get_in_ports():
    """Creates function to get MIDI IN port information from OS MIDI module

    Returns:
        function: obtain MIDI Input port information from OS
    """
    midiin = rtmidi.MidiIn(midi.get_api_from_environment())
    return midiin.get_ports()

# Dictionary of keys for different MIDI events
channel_events = {
  144: "NOTE_ON",
  128: "NOTE_OFF",
  160: "POLY",
  176: "CTRL_CNG",
  192: "PGR_CNG",
  208: "AFTERTOUCH",
  224: "PITCH"
}
