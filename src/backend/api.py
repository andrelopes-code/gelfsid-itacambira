from webview import Window
import webview


class WindowControl:
    _is_maximized = False

    def minimize_window(self):
        self._window.minimize()

    def toggle_maximize_window(self):
        if self._is_maximized:
            self._window.restore()
            self._is_maximized = False
        else:
            self._window.maximize()
            self._is_maximized = True

    def close_window(self):
        self._window.destroy()

    def window_size(self):
        return {'width': self._window.width, 'height': self._window.height}

    def window_position(self):
        return {'x': self._window.x, 'y': self._window.y}

    def resize_window(self, width, height, x, y):
        self._window.move(x, y)
        self._window.resize(width, height)

    def window_min_size(self):
        return {'width': self._window.min_size[0], 'height': self._window.min_size[1]}


class API(WindowControl):
    def __init__(self, window: Window):
        self._window = window

    def select_directory(self):
        result = self._window.create_file_dialog(
            webview.FOLDER_DIALOG,
            directory='.',
        )
        return result[0] if result else None
