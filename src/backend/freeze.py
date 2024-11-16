import subprocess

command = [
    'pyinstaller',
    'main.py',
    '--windowed',
    '--add-data',
    'src/frontend:frontend',
    '--onefile',
    '--icon',
    'src/frontend/static/assets/icon.ico',
]

subprocess.run(command, check=True)
