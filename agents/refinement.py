import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def load_refiner():
    """Возвращает функцию-уточнитель."""
    def refine(query: str) -> str:
        prompt = (
            f"Переформулируй поисковый запрос, чтобы он был максимально точным. "
            f"Верни **одну** строку без кавычек и без пояснений. "
            f"Исходный запрос: \"{query}\"\nУточнённый:"
        )
        response = model.generate_content(prompt)
        return response.text.strip()

    return refine