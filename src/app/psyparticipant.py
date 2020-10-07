"""
Display the dialogue for the psychopy participant ID

This is seperated from the `psy.py` to avoid a fullscreen
window covering the dialogue box.
"""
from psychopy import gui, core

def display_participant_dialogue() -> list:
    """
    Show participant information dialogue box
    """

    # Standard psychopy dialogue box
    dlg = gui.Dlg(title="Please enter participant information")
    dlg.addField(label='ID')
    participant = dlg.show()
    # Do not continue if no ID is entered
    if participant is None:
        core.quit()
    return participant
