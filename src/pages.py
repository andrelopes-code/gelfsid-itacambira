from src.backend.template import render
from src.config import CONFIG


class Pages:
    def index(self, **context):
        return render('index.html', **{**CONFIG.BASE_CONTEXT, **context})


pages = Pages()
