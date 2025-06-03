import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")  # можно сменить на gemini-pro

def load_planner():
    """Возвращает функцию-планировщик."""
    def planner(query: str) -> str:
        prompt = (
            f"Ты планировщик. Верни **только** JSON-массив строк (без пояснений) "
            f"с шагами, на которые надо разбить запрос пользователя.\n"
            f"Пример вывода:\n[\"Шаг 1\", \"Шаг 2\", \"Шаг 3\"]\n\n"
            f"Запрос: {query}\nJSON:"
        )
        response = model.generate_content(prompt)
        return response.text.strip()

    return planner