import pyperclip

from src.backend.utils import handle_api_errors


@handle_api_errors
class ClipboardAPI:
    """API for clipboard functions"""

    def get(self):
        return pyperclip.paste()

    def set(self, value):
        pyperclip.copy(value)
