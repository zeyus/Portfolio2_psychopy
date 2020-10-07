"""Main word-by-word experiment script"""
import sys
import os
# Add src directory to path for module loading
sys.path.append(os.path.abspath(os.path.dirname(
    os.path.abspath(__file__)) + os.path.sep + '..' + os.path.sep))

#pylint: disable=wrong-import-position
import config
#pylint: enable=wrong-import-position

def setup():
    """Prepare psychopy environment and settings"""
    #pylint: disable=import-outside-toplevel
    from psychopy import prefs
    #pylint: enable=import-outside-toplevel
    prefs.hardware['audioLib'] = config.psy.PREFS.get('audioLib')
    prefs.general['winType'] = config.psy.PREFS.get('winType')
    prefs.hardware['highDPI'] = config.psy.PREFS.get('highDPI')
    prefs.saveUserPrefs()
    #pylint: disable=import-outside-toplevel
    import app.psy as psy
    #pylint: enable=import-outside-toplevel
    return psy.Psypy(config.psy.PREFS)


def run_experiment():
    """
    Step by step script for the experiment
    """
    psypy = setup()
    psypy.display_text_message(config.exp.MESSAGES.get('instructions'))
    psypy.display_text_sequence(config.story.TEXT.get('practice'))
