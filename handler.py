import os
import requests
import subprocess

def download_file(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)

def handler(event):
    video_url = event['input']['video_url']
    audio_url = event['input']['audio_url']
    command = event['input']['command']

    # Télécharger les fichiers
    download_file(video_url, 'video.mp4')
    download_file(audio_url, 'audio.mp3')

    # Exécuter la commande FFmpeg
    subprocess.run(command, shell=True)

    # Retourne un message simple (le fichier est dans le container)
    return {
        "message": "Fusion terminée.",
        "output_file": "output.mp4"
    }
