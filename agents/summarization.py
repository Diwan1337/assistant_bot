import google.generativeai as genai
from config import GEMINI_API_KEY

# Настраиваем ключ Gemini (через VPN или из доступного региона)
genai.configure(api_key=GEMINI_API_KEY)
# Инициализируем модель. Можно оставить "gemini-2.0-flash" или сменить на более новую версию.
model = genai.GenerativeModel("gemini-2.0-flash")

def load_summarizer():
    """
    Возвращает функцию summarizer(user_query, tasks, refined_queries, search_results),
    которая на основе всех найденных данных формирует финальный ответ.
    """
    def summarizer(
        user_query: str,
        tasks: list[str],
        refined_queries: list[str],
        search_results: list[str],
    ) -> str:
        # Собираем «контекст» — для каждого шага:
        blocks = []
        for step, rq, sr in zip(tasks, refined_queries, search_results):
            block = (
                f"Шаг: {step}\n"
                f"Уточнённый запрос: {rq}\n"
                f"Ссылки/результаты:\n{sr}"
            )
            blocks.append(block)

        context = "\n\n".join(blocks)

        # Подготавливаем итоговый промпт для Gemini
        prompt = (
            f"Пользователь задал вопрос:\n\"{user_query}\"\n\n"
            "Ниже приведены результаты поиска и промежуточные шаги:\n\n"
            f"{context}\n\n"
            "На основе этих данных сформируй полный и развернутый ответ на исходный вопрос. "
            "Не выдавай список шагов, а объясни позиции и факты в связном тексте. "
            "Если информации недостаточно для полного ответа — сообщи об этом."
        )

        try:
            # Генерируем ответ
            response = model.generate_content(prompt)
        except Exception as e:
            msg = str(e)
            if "User location is not supported" in msg:
                return (
                    "ОШИБКА: ваш регион не поддерживается Gemini API. "
                    "Попробуйте VPN или другую LLM для получения ответов."
                )
            return f"Ошибка при суммаризации: {msg}"

        return response.text.strip()

    return summarizer
