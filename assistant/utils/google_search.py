from googleapiclient.discovery import build
from pprint import pprint

API_KEY = "AIzaSyBbkVjR-j6EvYGa_rCUFGkcux8FNcEWrd0"
CSE_ID = "f378c3bdf27be4161"

def google_search(search_term, **kwargs):
    service = build("customsearch", "v1", developerKey=API_KEY)
    res = service.cse().list(q=search_term, cx=CSE_ID, **kwargs).execute()
    return res['items']