from pathlib import Path
import sys


def is_freezed():
    return getattr(sys, '_MEIPASS', None)


def resource_path(relative_path):
    bundler_dir = Path(getattr(sys, '_MEIPASS', Path(__file__).parent.parent))
    return bundler_dir / relative_path
