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

if __name__ == '__main__':
    subprocess.run(command, check=True)
