import re
import subprocess
import threading
import time

# Comanda pe care o vom rula
cmd = ['./spotifyd', '--no-daemon']

def ms_to_min_sec(ms):
    total_seconds = ms // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:02}"

def extract_song_info(output):
    match = re.search(r'<(.*?)>\s\((\d+)\sms\)', output)
    if match:
        song_name = match.group(1)
        duration = ms_to_min_sec(int(match.group(2)))
        return song_name, duration
    return None

def read_output(process_spotifyd):
    while True:
        for line in iter(process_spotifyd.stdout.readline, b''):
            song_info = extract_song_info(line.decode())
            if song_info:
                song_name, duration = song_info
                print(f"Now Playing: {song_name} {duration}")

# Rulează comanda și începe firul de execuție pentru a citi output-ul
process_spotifyd = subprocess.Popen(cmd, stdout=subprocess.PIPE)

# Începe firul de execuție pentru a citi output-ul procesului Spotifyd
threading.Thread(target=read_output, args=(process_spotifyd,)).start()

# Firul de execuție pentru lansarea în buclă a comenzii "python ./volume.py"
def launch_volume_command():
    while True:
        subprocess.call(['python', './volume.py'])
        #time.sleep(1)

# Începe firul de execuție pentru a lansa comanda "python ./volume.py" în buclă
threading.Thread(target=launch_volume_command).start()

# Păstrăm programul principal în execuție folosind o buclă infinită aici
while True:
    # Poți adăuga alte instrucțiuni sau să lași bucla goală, în funcție de nevoile tale
    time.sleep(1)
