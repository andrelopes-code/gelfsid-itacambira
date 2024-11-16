from dataclasses import dataclass
from src.backend.utils import resource_path
from pathlib import Path
import webview

TEMPLATES_DIR = Path(resource_path('frontend'))
webview.settings['OPEN_DEVTOOLS_IN_DEBUG'] = False


@dataclass
class Config:
    title: str
    width: int
    height: int
    debug: bool
    watch: bool
    port: int
    resizable: bool
    frameless: bool
    min_size: tuple[int, int]
    static_dir: Path
    static_port: int
    templates_dir: Path


CONFIG = Config(
    title='Contracts',
    width=800,
    height=600,
    resizable=False,
    frameless=True,
    min_size=(800, 600),
    debug=True,
    watch=True,
    port=9876,
    templates_dir=TEMPLATES_DIR,
    static_dir=TEMPLATES_DIR / 'static',
    static_port=6789,
)

BASE_CONTEXT = {
    'resizable': CONFIG.resizable,
}
