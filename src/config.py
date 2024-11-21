from pathlib import Path

import webview

from src.backend.utils import is_frozen, resource_path

webview.settings['OPEN_DEVTOOLS_IN_DEBUG'] = True
TEMPLATES_DIR = Path(resource_path('frontend'))


class CONFIG:
    """Application configuration"""

    title = 'Contracts'
    width = 800
    height = 600
    resizable = True
    frameless = True
    min_size = 800, 600
    debug = False if is_frozen() else True
    watch = True
    templates_dir = TEMPLATES_DIR
    static_dir = TEMPLATES_DIR / 'static'

    background_color = '#f0f2f2'

    BASE_CONTEXT = {
        'resizable': resizable,
        'title': title,
    }
