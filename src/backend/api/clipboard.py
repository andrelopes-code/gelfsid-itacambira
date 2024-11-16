import pyperclip


class ClipboardAPI:
    def get(self):
        return pyperclip.paste()

    def set(self, value):
        pyperclip.copy(value)
