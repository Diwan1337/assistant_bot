import os
from googleapiclient.discovery import build

API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
CX_ID   = os.getenv("GOOGLE_SEARCH_CX")      # идентификатор поискового движка

if not API_KEY or not CX_ID:
    raise ValueError("Нужны GOOGLE_SEARCH_API_KEY и GOOGLE_SEARCH_CX в .env")

service = build("customsearch", "v1", developerKey=API_KEY)

def load_search():
    def search(query: str) -> str:
        res = service.cse().list(q=query, cx=CX_ID, num=3).execute()
        items = res.get("items", [])
        if not items:
            return "нет результатов"
        return "\n".join(f"- {it['title']} — {it['link']}" for it in items)
    return search
