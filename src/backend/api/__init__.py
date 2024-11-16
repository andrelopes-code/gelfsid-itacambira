from src.backend.api.clipboard import ClipboardAPI
from src.backend.api.files import FilesAPI
from src.backend.api.pdf import PDFAPI
from src.backend.api.window import WindowAPI


class API:
    def __init__(self, window):
        self.pdf = PDFAPI(window)
        self.files = FilesAPI(window)
        self.window = WindowAPI(window)
        self.clipboard = ClipboardAPI()
