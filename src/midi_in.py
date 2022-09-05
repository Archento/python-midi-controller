"""
Dieses Modul soll MIDI eingaben verarbeiten
"""
import time

import rtmidi.midiutil as midi


# Methode open_midiinput wird ausgeführt und in zwei Variablen destrukturiert, die den jew. Werten des Tuples (= Rückgabewert von open_midiinput) zugewiesen werden
def get_midi_in(port = None) -> tuple:
    """Generates MIDI input object using rtmidi-library

    Returns:
        tuple: rtmidi-object, port name
    """
    return midi.open_midiinput(port)


# midi_in, port_name = get_midi_in()


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

# Einbettung des MIDI-Monitorings in try-except-Block
# try:
#     while True:
#         # Rückgabewert von get_message ist: (<Die Note>, <vergangene Zeit seit letztem Befehl>)
#         msg = midi_in.get_message()
#         if msg:
#             # Destrukturierung, weil wir nur einen Teil davon benutzen wollen
#             message, delta = msg
#             # Zugriff auf einzelne Parameter möglich (weitere Destrukturierung)
#             [event, note, velocity] = message
#             # keine Ausgabe, falls nicht im dict
#             if event not in channel_events:
#                 continue
#             # 'channel_events' wird  benutzt, so dass statt Zahlen die jew. Bedeutungen angezeigt werden
#             print(f"channel: {channel_events[event]}, note: {note}, velocity: {velocity}")
#         # Polling-Intervall (Abfragen pro Sekunde werden begrenzt, um Ressourcen zu sparen) 
#         time.sleep(0.1)
# # Loop kann per ctrl+C gestoppt werden
# except KeyboardInterrupt: 
#     pass
# # MIDI-Port wieder schließen und Variable aus dem Speicher entfernen
# finally:    
#     midi_in.close_port()
#     del midi_in
