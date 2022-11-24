import webbrowser

def main(search_term):
    URL = f"https://www.google.com/search?q={search_term}"
    webbrowser.open(URL)