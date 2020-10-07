"""
Psychopy middleware. Provides display / stimulus functionality for the experiment.
"""
from psychopy import visual, event, monitors

class Psypy:
    """Wrapper class for reusable psychopy activities"""
    conf: dict
    mon: monitors.Monitor
    win: visual.Window
    wait_keys: list = ['space']

    def __init__(self, conf: dict) -> None:
        self.conf = conf
        self.mon = self.prepare_monitor()
        self.win = self.get_window()

    def prepare_monitor(self) -> monitors.Monitor:
        """Set up psychopy monitor"""
        mon = monitors.Monitor(self.conf.get('monitorName'))
        mon.setSizePix(self.conf.get('winSize'))
        mon.setWidth(self.conf.get('monitorWidth'))
        return mon

    def get_window(self) -> visual.Window:
        """Return a window for drawing stimuli"""
        return visual.Window(size=self.conf.get('winSize'), fullscr=self.conf.get('fullScreen'), monitor=self.mon)

    def display_text_message(self, txt: str, wait: bool = True) -> None:
        """Display message / instructions"""
        msg = visual.TextStim(self.win, text=txt)
        msg.draw()
        self.win.flip()
        if wait:
            event.waitKeys(keyList=self.wait_keys)

    def display_text_sequence(self, txt: str) -> dict:
        """Display word by word text sequence"""
        for word in txt.strip():
            msg = visual.TextStim(self.win, text=word)
            msg.draw()
            self.win.flip()
            event.waitKeys(keyList=self.wait_keys)
            return {}
