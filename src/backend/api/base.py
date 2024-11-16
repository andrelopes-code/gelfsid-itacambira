from webview import Window


class BaseAPI:
    def __init__(self, window: Window):
        self._window = window
