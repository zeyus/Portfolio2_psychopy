"""Main word-by-word experiment script"""
import sys
import os
import glob
import random
import time
import pandas as pd

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
    # Ensure data directory exists and is writeable
    if not os.path.exists(config.data.DATA_PATH):
        try:
            os.mkdir(config.data.DATA_PATH)
        except Exception:
            raise SystemError('Cannot write to {}'.format(os.path.abspath(config.data.DATA_PATH)))       
    return psy.Psypy(config.psy.PREFS)

def get_condition() -> dict:
    experimental_results = len(glob.glob(config.data.DATA_PATH + os.path.sep + '*_experimental.csv'))
    control_results = len(glob.glob(config.data.DATA_PATH + os.path.sep + '*_control.csv'))
    if experimental_results == control_results:
        condition = random.choice(('control', 'experimental'))
    elif experimental_results < control_results:
        condition = 'experimental'
    else:
        condition = 'experimental'
    return {
        'condition': condition,
        'story': config.story.TEXT.get('main').format(cond_word = config.exp.CONDS.get(condition))
    }


def write_experiment_data(timing_data: dict, participant: list, condition: str):
    d_f = pd.DataFrame(columns=config.data.COLS)
    for row in timing_data:
        d_f = d_f.append({
            # Timestamp YYYY-MM-DD HH:MM:SS
            'timestamp': row.get('timestamp'),
            # Participant ID
            'id': participant[0],
            # Current word
            'word': row.get('word'),
            # Display time
            'time': row.get('time'),
            # Which condition: (control, experimental)
            'condition': condition.get('condition'),
            # Integer: The nth word displayed of the story
            'sequence': row.get('sequence'),
        }, ignore_index = True)
    d_f.to_csv(
        config.data.DATA_PATH + os.path.sep +
        config.data.LOG_FORMAT.format(timestamp = time.strftime('%Y-%m-%d %H_%M_%S'), id=participant[0], condition=condition.get('condition')))

def run_experiment():
    """
    Step by step script for the experiment
    """
    psypy = setup()
    condition = get_condition()
    participant = psypy.display_participant_dialogue()
    psypy.display_text_message(config.exp.MESSAGES.get('instructions'))
    psypy.display_text_sequence(config.story.TEXT.get('practice'))
    psypy.display_text_message(config.exp.MESSAGES.get('post_practice'))
    timing_data = psypy.display_text_sequence(condition.get('story'))
    psypy.display_text_message('Please wait...', wait = False)
    write_experiment_data(timing_data, participant, condition)
    psypy.display_text_message(config.exp.MESSAGES.get('complete'))
