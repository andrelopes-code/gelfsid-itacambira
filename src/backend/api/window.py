from src.backend.api.base import BaseAPI


class WindowAPI(BaseAPI):
    def __init__(self, window):
        super().__init__(window)
        self._is_maximized = False

    def minimize(self):
        self._window.minimize()

    def toggle_maximize(self):
        if self._is_maximized:
            self._window.restore()
            self._is_maximized = False
        else:
            self._window.maximize()
            self._is_maximized = True

    def destroy(self):
        self._window.destroy()

    def size(self):
        return {
            'width': self._window.width,
            'height': self._window.height,
        }

    def position(self):
        return {
            'x': self._window.x,
            'y': self._window.y,
        }

    def resize(self, width, height, x, y):
        self._window.move(x, y)
        self._window.resize(width, height)

    def min_size(self):
        return {
            'width': self._window.min_size[0],
            'height': self._window.min_size[1],
        }
