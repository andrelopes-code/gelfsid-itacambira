from fpdf import FPDF
import os
import re
from dataclasses import dataclass
from typing import List
from src.backend.utils import resource_path


@dataclass
class Delivery:
    plate: str
    ticket: str
    date: str
    images: List[str]


class PDFGenerator:
    MARGIN = 5
    ORIENT = 'L'
    UNIT = 'mm'
    FORMAT = 'A4'
    FONT = ('Arial', 'B', 14)
    MAX_HEIGHT = 125
    TEXT_HEIGHT = 55
    IMAGE_COLUMNS = 3

    def __init__(self, images_dir, output_dir='./out'):
        self.images_dir = images_dir
        self.output_dir = output_dir
        self.pdf = FPDF(orientation=self.ORIENT, unit=self.UNIT, format=self.FORMAT)
        self.page_width = self.pdf.w - (2 * self.MARGIN)
        self.image_width = self.page_width / self.IMAGE_COLUMNS
        self.pdf.set_font(*self.FONT)
        self.pdf.set_text_color(70, 70, 70)
        os.makedirs(output_dir, exist_ok=True)

    def get_images(self) -> List[str]:
        if not os.path.exists(self.images_dir):
            raise FileNotFoundError(f'O diretório {self.images_dir} não existe!')

        images = [
            os.path.join(self.images_dir, img)
            for img in sorted(os.listdir(self.images_dir), key=self.natural_sort_key)
        ]

        if not images:
            raise FileNotFoundError('Nenhuma imagem foi encontrada!')
        if len(images) % self.IMAGE_COLUMNS != 0:
            raise ValueError('O número de imagens deve ser múltiplo de 3!')

        return images

    @staticmethod
    def natural_sort_key(text):
        return [
            int(part) if part.isdigit() else part
            for part in re.split(r'(\d+)', text.lower())
        ]

    def parse_deliveries(self, data: str) -> List[Delivery]:
        deliveries = []

        for line in data.strip().split('\n'):
            if not line.strip():
                continue

            items = list(filter(bool, line.split('\t')))
            if len(items) < 4:
                raise ValueError(f'dados invalidos para a linha: {line}')

            date, plate, _, ticket = items[:4]
            deliveries.append(
                Delivery(
                    date=date.strip(),
                    plate=plate.strip(),
                    ticket=ticket.strip(),
                    images=[],
                )
            )

        images = self.get_images()
        chunked_images = [
            images[i : i + self.IMAGE_COLUMNS]
            for i in range(0, len(images), self.IMAGE_COLUMNS)
        ]
        if len(chunked_images) != len(deliveries):
            raise ValueError(
                'O número de imagens não corresponde ao número de entregas!'
            )

        for i, delivery in enumerate(deliveries):
            delivery.images = chunked_images[i]

        if len(set(d.date for d in deliveries)) != 1:
            raise ValueError('Todas as entregas devem ter a mesma data!')

        return deliveries

    def add_delivery_to_pdf(self, delivery: Delivery):
        self.pdf.add_page()
        self.add_header(delivery)
        self.add_images(delivery.images)

    def add_header(self, delivery: Delivery):
        self.pdf.image(
            resource_path('logo.jpeg'),
            x=10,
            y=-12,
            w=50,
            h=50,
        )

        self.pdf.set_font('Arial', style='B', size=14)
        self.pdf.cell(
            0,
            10,
            f'INFORMAÇÕES DA ENTREGA DE CARVÃO - {delivery.date}',
            ln=True,
            align='C',
        )
        self.pdf.ln(5)
        self.pdf.set_line_width(0.5)
        self.pdf.set_draw_color(200, 200, 200)
        self.pdf.line(
            10, self.pdf.get_y(), self.pdf.w - 2 * self.MARGIN, self.pdf.get_y()
        )
        self.pdf.ln(10)

        info_w = 60
        info_h = 7
        font_size = 13

        self.pdf.set_font('Arial', size=font_size)
        self.pdf.cell(info_w, info_h, 'PLACA DO VEÍCULO: ', align='L', ln=False)
        self.pdf.set_font('Arial', style='B', size=font_size)
        self.pdf.cell(0, info_h, f'{delivery.plate}', ln=True)

        self.pdf.set_font('Arial', size=font_size)
        self.pdf.cell(info_w, info_h, 'TÍQUETE DE ENTRADA: ', align='L', ln=False)
        self.pdf.set_font('Arial', style='B', size=font_size)
        self.pdf.cell(0, info_h, f'{delivery.ticket}', ln=True)

    def add_images(self, images: List[str]):
        y = self.TEXT_HEIGHT + self.MARGIN
        x = self.MARGIN
        for image in images:
            if not os.path.exists(image):
                raise FileNotFoundError(f'Imagem inexistente: {image}')
            self.pdf.image(image, x=x, y=y, w=self.image_width, h=self.MAX_HEIGHT)
            x += self.image_width

    def create_pdf(self, data: str) -> str:
        deliveries = self.parse_deliveries(data)
        for delivery in deliveries:
            self.add_delivery_to_pdf(delivery)

        output_pdf = os.path.join(
            self.output_dir, f"{deliveries[0].date.replace('/', '.')}.pdf"
        )

        self.pdf.output(output_pdf)
        print(f'PDF criado com sucesso: {output_pdf}')

        output_dir = os.path.dirname(output_pdf)
        os.startfile(os.path.abspath(output_dir))
        return output_pdf
