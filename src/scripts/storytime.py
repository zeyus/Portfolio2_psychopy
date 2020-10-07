"""
Main word-by-word experiment script
"""

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
    """
    Prepare psychopy environment and settings
    """

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
        except Exception as ex:
            raise SystemError(
                'Cannot write to {}'.format(os.path.abspath(config.data.DATA_PATH))) from ex
    return psy.Psypy(config.psy.PREFS)

def get_condition() -> dict:
    """
    Choose the condition for the next participant.
    """

    # Get number of participants so far in each condition
    experimental_results = len(glob.glob(
        config.data.DATA_PATH + os.path.sep + '*_experimental.csv'))
    control_results = len(glob.glob(
        config.data.DATA_PATH + os.path.sep + '*_control.csv'))

    # Try to balance the numbers, but if they're already balanced, randonly select one
    if experimental_results == control_results:
        condition = random.choice(('control', 'experimental'))
    elif experimental_results < control_results:
        condition = 'experimental'
    else:
        condition = 'control'
    # Return the condition, with the completed story text
    return {
        'condition': condition,
        'story': config.story.TEXT.get('main').format(cond_word = config.exp.CONDS.get(condition))
    }


def write_experiment_data(timing_data: dict, participant: list, condition: str):
    """
    Save the experimental results
    """

    # Prepare dataframe using configured columns
    d_f = pd.DataFrame(columns=config.data.COLS)

    # Loop through the results for this participant
    for row in timing_data:
        d_f = d_f.append({
            'timestamp': row.get('timestamp'),
            'id': participant[0],
            'word': row.get('word'),
            'time': row.get('time'),
            'condition': condition.get('condition'),
            'sequence': row.get('sequence'),
        }, ignore_index = True)
    # Write the data to a csv file in the data directory
    d_f.to_csv(
        config.data.DATA_PATH + os.path.sep +
        config.data.LOG_FORMAT.format(
            timestamp = time.strftime('%Y-%m-%d_%H_%M_%S'),
            id=participant[0],
            condition=condition.get('condition')))

def run_experiment():
    """
    Step by step script for the experiment
    """

    # Prepare psychopy
    psypy = setup()
    # Get the participants condition
    condition = get_condition()
    # Ask for participant ID
    participant = psypy.display_participant_dialogue()
    # Show instructions
    psypy.display_text_message(config.exp.MESSAGES.get('instructions'))
    # Run practice experiment
    psypy.display_text_sequence(config.story.TEXT.get('practice'))
    # Get ready
    psypy.display_text_message(config.exp.MESSAGES.get('post_practice'))
    # Run experiment and get time per displayed word
    timing_data = psypy.display_text_sequence(condition.get('story'))
    # We can't accept input until the data saves
    psypy.display_text_message('Please wait...', wait = False)
    # Save the data
    write_experiment_data(timing_data, participant, condition)
    # Byeeeeeeeee
    psypy.display_text_message(config.exp.MESSAGES.get('complete'))
