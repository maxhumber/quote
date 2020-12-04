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
        sys.stdout.write("\033[32m")
        self.spin_thread.start()

    def stop(self) -> None:
        self.stop_running.set()
        self.spin_thread.join()
        sys.stdout.write("\033[0m")

    def init_spin(self) -> None:
        while not self.stop_running.is_set():
            sys.stdout.write(next(self.phases))
            sys.stdout.flush()
            sleep(0.1)
            sys.stdout.write("\b")
