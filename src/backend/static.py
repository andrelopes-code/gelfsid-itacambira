import subprocess
from threading import Thread

import psutil

from src.config import CONFIG


def serve():
    def run_server():
        command = [
            'python',
            '-m',
            'http.server',
            str(CONFIG.static_port),
            '-d',
            str(CONFIG.static_dir),
        ]

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE

        process = subprocess.Popen(
            command,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            startupinfo=startupinfo,
        )

        run_server.process = process

    def cleanup():
        if hasattr(run_server, 'process'):
            try:
                parent = psutil.Process(run_server.process.pid)
                for child in parent.children(recursive=True):
                    child.terminate()
                parent.terminate()

            except (psutil.NoSuchProcess, ProcessLookupError):
                pass

    thread = Thread(target=run_server, daemon=True)
    thread.start()

    return cleanup
