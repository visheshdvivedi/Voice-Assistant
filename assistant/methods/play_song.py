import webbrowser
from assistant.utils.google_search import google_search

def main(song_name):
    song_name = song_name.lower()
    if "song" in song_name:
        song_name.replace("song", "")
    search_term = song_name + " song lyrical"
    results = google_search(search_term, num=1)
    youtube_link = results[0]['link']
    webbrowser.open(youtube_link)