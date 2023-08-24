import atexit
import os
import platform
import subprocess
import tempfile
import zipfile
from pathlib import Path
from threading import Thread

import requests


def get_command():
    system = platform.system()
    if system == 'Darwin':
        command = 'ngrok'
    elif system == 'Windows':
        command = 'ngrok.exe'
    elif system == 'Linux':
        command = 'ngrok'
    else:
        raise Exception(f'{system} is not supported')
    return command


def run_ngrok(port: str | int) -> str:
    command = get_command()
    ngrok_path = str(Path(tempfile.gettempdir(), 'ngrok'))
    download_ngrok(ngrok_path)
    executable = str(Path(ngrok_path, command))
    os.chmod(executable, 0o777)
    ngrok = subprocess.Popen([executable, 'http', str(port)])
    atexit.register(ngrok.terminate)
    localhost_url = 'http://localhost:4040/api/tunnels'  # Url with tunnel details

    return requests.get(localhost_url).json()['tunnels'][0]['public_url']


def download_ngrok(ngrok_path):
    if Path(ngrok_path).exists():
        return

    print(f'Going to try to download ngrok to this folder: {ngrok_path}')

    system = platform.system()
    if system == 'Darwin':
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip'
    elif system == 'Windows':
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip'
    elif system == 'Linux':
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'
    else:
        raise Exception(f'{system} is not supported')
    download_path = download_file(url)
    with zipfile.ZipFile(download_path, 'r') as zip_ref:
        zip_ref.extractall(ngrok_path)


def download_file(url):
    local_filename = url.split('/')[-1]
    download_path = str(Path(tempfile.gettempdir(), local_filename))

    r = requests.get(url, stream=True)
    with open(download_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=10240):
            if chunk:
                f.write(chunk)

    return download_path


def start_ngrok(port):
    ngrok_address = run_ngrok(port)
    print(f' * Running on {ngrok_address}')
    print(f' * Traffic stats available on http://127.0.0.1:4040')


def patch_to_run_with_ngrok(app):
    """
    :param app: a Flask application object
    """
    old_run = app.run

    def new_run(*args, **kwargs):
        port = kwargs.get('port')
        if port is None:
            if len(args) >= 2:
                port = args[1]
            else:
                port = 3000
                kwargs['port'] = 3000
        thread = Thread(target=start_ngrok, args=(port,), daemon=True)
        thread.start()
        old_run(*args, **kwargs)

    app.run = new_run

