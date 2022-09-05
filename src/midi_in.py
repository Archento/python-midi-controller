"""
Dieses Modul soll MIDI eingaben verarbeiten
"""
import rtmidi.midiutil as midi
import rtmidi

# Methode open_midiinput wird ausgeführt und in zwei Variablen destrukturiert, die den jew. Werten des Tuples (= Rückgabewert von open_midiinput) zugewiesen werden
def get_midi_in(port = None) -> tuple:
    """Generates MIDI input object using rtmidi-library

    Returns:
        tuple: rtmidi-object, port name
    """
    return midi.open_midiinput(port)

def get_in_ports():
    midiin = rtmidi.MidiIn(midi.get_api_from_environment(rtmidi.API_UNSPECIFIED))
    return midiin.get_ports()

# Schlüssel für Eventtypen
channel_events = {
  144: 'NOTE_ON',
  128: 'NOTE_OFF',
  160: 'POLY',
  176: 'CTRL_CNG',
  192: 'PGR_CNG',
  208: 'AFTERTOUCH',
  224: 'PITCH'
}
