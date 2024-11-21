import threading
from dataclasses import dataclass
from typing import Callable

import watchfiles
from webview import Window


@dataclass
class WatchData:
    uid: str
    title: str
    page_name: str
    page_function: Callable
    context: dict
    window: Window


class Watcher:
    """Class to watch for changes in a directory in a separate thread"""

    def __init__(self):
        self.watch_event = threading.Event()
        self.windows_to_watch: dict[str, WatchData] = {}
        self.windows_lock = threading.Lock()

        self._watch_thread = None

    def start(self, dir_to_watch):
        if self._watch_thread and self._watch_thread.is_alive():
            return

        self._watch_thread = threading.Thread(
            target=self._watch_for_changes,
            args=(dir_to_watch,),
            daemon=True,
        )
        self._watch_thread.start()

    def add_window(self, window_data: WatchData):
        with self.windows_lock:
            self.windows_to_watch[window_data.uid] = window_data

    def remove_window(self, window_data: WatchData):
        if window_data.uid in self.windows_to_watch:
            del self.windows_to_watch[window_data.uid]

    def stop(self):
        self.watch_event.set()
        if self._watch_thread:
            self._watch_thread.join(timeout=1)

    def _watch_for_changes(self, dir_to_watch):
        for changes in watchfiles.watch(dir_to_watch):
            if self.watch_event.is_set():
                break

            for _ in changes:
                with self.windows_lock:
                    windows_to_watch_copy = self.windows_to_watch.copy()

                for data in windows_to_watch_copy.values():
                    data.window.load_html(data.page_function(**data.context))


watcher = Watcher()
