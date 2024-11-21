from src.backend import pdfgen, swal
from src.backend.api.common.base import BaseAPI
from src.backend.utils import handle_api_errors


@handle_api_errors
class PDFAPI(BaseAPI):
    def generate(self, images_dir, data):
        try:
            generator = pdfgen.PDFGenerator(images_dir=images_dir)
            generator.create_pdf(data=data)
        except Exception as e:
            swal.error(self._window, str(e), 'ERRO AO GERAR PDF')
