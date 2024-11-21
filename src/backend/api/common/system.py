import webview

from src.backend.api.common.base import BaseAPI
from src.backend.utils import handle_api_errors


@handle_api_errors
class SystemAPI(BaseAPI):
    """API for system related functions"""

    def select_directory(self):
        result = self._window.create_file_dialog(
            webview.FOLDER_DIALOG,
            directory='.',
        )
        return result[0] if result else None

    def select_file(self, file_types=None):
        result = self._window.create_file_dialog(
            webview.OPEN_DIALOG,
            directory='.',
            file_types=file_types or tuple(),
        )
        return result[0] if result else None
