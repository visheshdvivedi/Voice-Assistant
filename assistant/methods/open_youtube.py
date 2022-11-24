import webbrowser

YOUTUBE_SEARCH_URL = "https://www.youtube.com/results?search_query={search_query}"

def main(search_query: str):
    url = YOUTUBE_SEARCH_URL.replace("{search_query}", search_query)
    webbrowser.open(url)
    return True