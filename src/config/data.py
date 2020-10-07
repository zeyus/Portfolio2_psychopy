# Where to save the participant data
DATA_PATH = '../data'

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