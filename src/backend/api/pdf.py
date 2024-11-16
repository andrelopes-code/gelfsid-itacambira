from src.backend import pdfgen
from src.backend.api.base import BaseAPI


class PDFAPI(BaseAPI):
    def generate(self, images_dir, data):
        generator = pdfgen.PDFGenerator(images_dir=images_dir)

        try:
            generator.create_pdf(data=data)
        except Exception as e:
            self._window.evaluate_js(
                f"""
                SwalUtils.error(
                    "{str(e)}",
                    "UM ERRO OCORREU"
                );
                """
            )
