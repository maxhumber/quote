import sys
from itertools import cycle
from threading import Event, Thread
from time import sleep
from typing import Any


class Spinner:
    phases: Any = cycle(["⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻", "⣽"])

    def __init__(self) -> None:
        self.stop_running: Any = Event()
        self.spin_thread: Any = Thread(target=self.init_spin)

    def start(self) -> None:
        sys.stderr.write("\033[32m")  # Set the color to green
        self.spin_thread.start()

    def stop(self) -> None:
        self.stop_running.set()
        self.spin_thread.join()
        sys.stderr.write("\r \r")  # Clear the spinner character by overwriting
        sys.stderr.write("\033[0m")  # Reset color

    def init_spin(self) -> None:
        while not self.stop_running.is_set():
            sys.stderr.write(next(self.phases))
            sys.stderr.flush()
            sleep(0.1)
            sys.stderr.write("\b")  # Move back to overwrite next time
