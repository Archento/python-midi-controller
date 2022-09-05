import time
import src.midi_in as m_in
import src.midi_out as m_out

midi_in, in_port_name = m_in.get_midi_in()

# Einbettung des MIDI-Monitorings in try-except-Block
try:
    while True:
        # Rückgabewert von get_message ist: (<Die Note>, <vergangene Zeit seit letztem Befehl>)
        msg = midi_in.get_message()
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
# Loop kann per ctrl+C gestoppt werden
except KeyboardInterrupt:
    pass
# MIDI-Port wieder schließen und Variable aus dem Speicher entfernen
finally:
    midi_in.close_port()
    del midi_in


# MIDI OUT

# EXAMPLE: destructured assignment of "open_midioutput"-tuple
midi_output, out_port_name = m_out.get_midi_out()

with midi_output:
    m_out.play_chord(midi_output, [60, 64, 67, 71], hold_time=3)
    time.sleep(0.1)

midi_output.close_port()
del midi_output
