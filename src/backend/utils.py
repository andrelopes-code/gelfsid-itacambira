import atexit
import functools
import sys
import traceback
from pathlib import Path

from src.backend import swal


def is_frozen():
    """Check if app is frozen"""

    return True if getattr(sys, '_MEIPASS', None) else False


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""

    bundler_dir = Path(getattr(sys, '_MEIPASS', Path(__file__).parent.parent))
    return bundler_dir / relative_path


def setup_cleanup_functions(*functions):
    """Function to register cleanup/stop functions"""

    for function in functions:
        atexit.register(function)


def handle_api_errors(cls):
    """Decorator to handle API errors using the sweetalert2 library"""

    for name, method in cls.__dict__.items():
        if callable(method) and not name.startswith('_'):

            @functools.wraps(method)
            def wrapper(self, *args, method=method, **kwargs):
                try:
                    return method(self, *args, **kwargs)

                except Exception as e:
                    print(traceback.format_exc())

                    if window := getattr(self, '_window', None):
                        swal.error(
                            window,
                            str(e),
                            f'{self.__class__.__name__}.{method.__name__} error:',
                        )
                    else:
                        raise

            setattr(cls, name, wrapper)

    return cls
