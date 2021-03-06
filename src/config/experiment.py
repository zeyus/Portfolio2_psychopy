"""
Specific configuration for the experiment / interface.
"""

# Define the context congruent and incongruent condition words
CONDS = {
  # Context congruent
  'control': 'delighted',
  # Context incongruent
  'experimental': 'metallic',
}

# Informational messages for the participants
MESSAGES = {
    # Initial instructions before the experiment starts
    'instructions': """
        In the following experiment you will be presented a short story one word at a time. In order to advance to the next word in the story, press the space bar. You will be notified once the story has been completely presented. 
        
        Before the experiment commences, you will complete a practice sentence.
        
        Press [space] to begin the practice sentence. 
        """,
    # Break after the practice to prevent accidental start of the experiment
    'continue': """
        Press [space] to continue...
        """,
    # Displayed after the practice is complete
    'post_practice' : """
        The practice sentence has been completed. Once you are ready, press [space] to begin the experiment.
        """,
    # Transient message while data is writing (hopefully very quick)
    'wait': """
        Please wait...
        """,
    # Final message at the end of the experiment
    'complete': """
        The experiment is over. Thank you for your participation!
        
        Have a wonderful day :)
        """
}
