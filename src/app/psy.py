# Setup psychopy functions
from psychopy import visual, event, core, sound, monitors, gui, data

# Prepare psychopy and window
def setup(conf: dict) -> None: 
  from psychopy import prefs
  # Apply config
  prefs.hardware['audioLib'] = conf['audioLib']
  prefs.general['winType'] = conf['winType']


def get_window(conf: dict) -> visual.Window:
  setup(conf)
  return visual.Window(
    size=conf.winsize
    )
def display_text_stimulus(image):
  visual.TextBox2()




