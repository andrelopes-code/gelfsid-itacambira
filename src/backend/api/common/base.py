from webview import Window


class BaseAPI:
    """Base class for all APIs that use the window object"""

    def __init__(self, window: Window):
        self._window = window
