"""
Dieses Modul soll MIDI eingaben verarbeiten
"""
import time

import rtmidi.midiutil as midi

midi_in, port_name = midi.open_midiinput(0)

channel_events = {
  144: 'NOTE_ON',
  128: 'NOTE_OFF',
  160: 'POLY',
  176: 'CTRL_CNG',
  192: 'PGR_CNG',
  208: 'AFTERTOUCH',
  224: 'PITCH'
}

try:
    while True:
        # Rückgabewert von get_message ist: (<Die Note>, <vergangene Zeit seit letztem Befehl>)
        msg = midi_in.get_message()
        if msg:
            message, delta = msg
            [event, note, velocity] = message # Zugriff auf einzelne Parameter möglich
            if event not in channel_events:
                continue
            print(f"channel: {channel_events[event]}, note: {note}, velocity: {velocity}")
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    midi_in.close_port()
    del midi_in
