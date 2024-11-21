import webview

from src.backend.api import API
from src.backend.api.common.window import create_window
from src.backend.static import static_server
from src.backend.utils import setup_cleanup_functions
from src.backend.watcher import watcher
from src.config import CONFIG


class App:
    """Application class to start the application"""

    def start(self):
        try:
            api = API()

            setup_cleanup_functions(
                watcher.stop,
                static_server.stop,
            )

            window = create_window('index', context=CONFIG.BASE_CONTEXT, api=api)
            api.start(window)

            if CONFIG.debug and CONFIG.watch:
                watcher.start(dir_to_watch=CONFIG.templates_dir)

            webview.start(debug=CONFIG.debug, http_server=True)

        except Exception:
            import traceback

            traceback.print_exc()


if __name__ == '__main__':
    app = App()
    app.start()
