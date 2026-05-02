import requests
import time
import random
import os

def download_large_files(url : str,  dest : str):
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(dest, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        pass
    except:
        print("FAILED")

urls = [
    "https://releases.ubuntu.com/24.04/ubuntu-24.04.4-desktop-amd64.iso",
    "https://releases.ubuntu.com/24.04/ubuntu-24.04.4-live-server-amd64.iso",
    "https://releases.ubuntu.com/24.04/ubuntu-24.04.4-wsl-amd64.wsl",
    "https://releases.ubuntu.com/22.04/ubuntu-22.04.5-desktop-amd64.iso"
]

if __name__ == "__main__":
    while True:
        wait = random.randint(1000, 2000)
        id = random.randint(0, len(urls) - 1)
        download_large_files(urls[id], "tmpfile")
        os.remove("tmpfile")
        time.sleep(wait)
