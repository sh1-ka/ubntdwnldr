import time
import random
import subprocess

def download_large_files(url : str,  limit : int):
    cmd = [
        "curl",
        "-L",
        "--limit-rate", f"{limit}M",
        "-o", "/dev/null",
        "-s",
        url
    ]

    try:
        subprocess.run(cmd)
    except Exception as e:
        print(e)

    
urls = [
    "https://releases.ubuntu.com/24.04/ubuntu-24.04.1-desktop-amd64.iso",
    "https://releases.ubuntu.com/22.04/ubuntu-22.04.5-desktop-amd64.iso",
    "https://releases.ubuntu.com/24.04/ubuntu-24.04.4-desktop-amd64.iso",
    "https://releases.ubuntu.com/24.04/ubuntu-24.04.4-live-server-amd64.iso",
    "https://releases.ubuntu.com/24.04/ubuntu-24.04.4-wsl-amd64.wsl",
    "https://releases.ubuntu.com/22.04/ubuntu-22.04.5-desktop-amd64.iso"
]

if __name__ == "__main__":
    while True:
        wait = random.randint(3000, 5000)
        id = random.randint(0, len(urls) - 1)
        spd = random.randint(40, 100)
        download_large_files(urls[id], spd)
        time.sleep(wait)
