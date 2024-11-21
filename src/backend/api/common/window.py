import webview

from src.backend.api.common.base import BaseAPI
from src.backend.utils import handle_api_errors
from src.backend.watcher import WatchData, watcher
from src.config import CONFIG
from src.pages import pages


def create_window(
    page_name,
    *,
    context,
    title=None,
    width=None,
    height=None,
    resizable=None,
    frameless=None,
    min_size=None,
    background_color=None,
    api=None,
):
    """
    Creates a new PyWebView window for the given page.
    It uses the parameters provided or the ones from the config.
    """

    page = getattr(pages, page_name, None)
    if not page:
        raise ValueError(f'Page {page_name} not found')

    if api is None:
        from src.backend.api import API

        api = API()

    window = webview.create_window(
        title=title or CONFIG.title,
        width=width or CONFIG.width,
        height=height or CONFIG.height,
        resizable=resizable or CONFIG.resizable,
        frameless=frameless or CONFIG.frameless,
        min_size=min_size or CONFIG.min_size,
        background_color=background_color or CONFIG.background_color,
        html=page(**context),
        js_api=api,
    )

    api.start(window)

    watcher.add_window(
        WatchData(
            window.uid,
            window.title,
            page_name,
            page,
            context,
            window,
        )
    )

    return window


@handle_api_errors
class WindowAPI(BaseAPI):
    """API for window related functions"""

    def __init__(self, window):
        super().__init__(window)
        self.children = {self._window.uid: []}
        self.maximized = False

    def minimize(self):
        self._window.minimize()

    def toggle_maximize(self):
        if self.maximized:
            self._window.restore()
            self.maximized = False
        else:
            self._window.maximize()
            self.maximized = True

        return self.maximized

    def destroy(self):
        for child in self.children.get(self._window.uid, []):
            child.destroy()

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
        self._window.resize(
            width,
            height,
        )

    def min_size(self):
        return {
            'width': self._window.min_size[0],
            'height': self._window.min_size[1],
        }

    def goto(self, page_name):
        if page := getattr(pages, page_name, None):
            self._window.load_html(page())

    def new(self, page_name, kwargs):
        window = create_window(page_name, **kwargs)

        if self.children.get(self._window.uid):
            self.children[self._window.uid].append(window)
        else:
            self.children[self._window.uid] = [window]
