import atexit

import webview

from src.backend import static
from src.backend.api import API
from src.backend.template import render
from src.backend.utils import is_freezed
from src.backend.watcher import start_watch_thread, stop_watch_thread
from src.config import BASE_CONTEXT, CONFIG


def setup_cleanup():
    cleanup = static.serve()
    atexit.register(cleanup)
    atexit.register(stop_watch_thread)


def main():
    setup_cleanup()

    window = webview.create_window(
        title=CONFIG.title,
        width=CONFIG.width,
        height=CONFIG.height,
        resizable=CONFIG.resizable,
        frameless=CONFIG.frameless,
        min_size=CONFIG.min_size,
        background_color='#f4f6f6',
        html=render('index.html', **BASE_CONTEXT),
    )

    api = API(window)
    window._js_api = api

    if CONFIG.debug and CONFIG.watch:
        start_watch_thread(
            dir_to_watch=CONFIG.templates_dir,
            callback=lambda: window.load_html(render('index.html', **BASE_CONTEXT)),
        )

    webview.start(
        debug=False if is_freezed() else CONFIG.debug,
        http_port=CONFIG.port,
    )


if __name__ == '__main__':
    main()
