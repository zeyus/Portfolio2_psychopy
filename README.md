# Portfolio 2 - Experiment in Psychopy

## Description

This experiment in psychopy uses a short story displayed to the participant word-by-word.
The timings between the display of the word and the participant proceding to the next word is recorded.
There are two conditions, one - the control condition - with a word near the end of the text 
(the second last sentence) that is congruent to the story context. The experimental condition
changes that word for one that is a common property of the inanimate object (in this case "metallic")
but is incongruent to the story context.

## Requirements

* Python >= 3.5
* psychopy
* pandas

the required modules can be installed by using `pip install -r requirements.txt`

## Running

From project root directry, run `python experiment.py`

## Data

Data is stored by default in `./data` and the default format is:
```python
# Data columns
COLS = [
    # Timestamp YYYY-MM-DD HH:MM:SS
    'timestamp',
    # Participant ID
    'id',
    # Current word
    'word',
    # Display time
    'time',
    # Which condition: (control, experimental)
    'condition',
    # Integer: The nth word displayed of the story
    'sequence',
]
```

## Configuration

All project configuration lives in `./src/config`

* `data.py`: where and how data is stored
* `experiment.py`: experimental conditions and messages for the user
* `psy.py`: psychopy options
* `story.py`: text for experimental story and practice story

## Scripts

* `./src/app/storytime.py`: the main experiment runner, sets up psychopy, runs the experiment and saves the data
