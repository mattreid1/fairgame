from cli import cli
from signal import signal, SIGINT
from utils.logger import log

def handler(signal, frame):
    log.info("Caught a ctrl-c, exiting...")
    exit(0)

if __name__ == "__main__":
    signal(SIGINT, handler)
    cli.main()
