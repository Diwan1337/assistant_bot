from typing import List

def eval_results(previous_links: List[str], current_links: List[str]) -> bool:
    """
    Сравнивает два списка URL: previous_links и current_links.
    Если в current_links есть хотя бы один URL, которого не было в previous_links,
    возвращает True (т. е. нашли «новую» информацию).
    Иначе возвращает False (новых ссылок нет).
    """
    for link in current_links:
        if link not in previous_links:
            return True
    return False


def extract_links(search_result: str) -> List[str]:
    """
    Парсит строку search_result в формате:
      "- Заголовок — https://пример.ru/..."
      "- Ещё заголовок — https://другой-сайт.com/..."
    Возвращает список просто URL, без заголовков.
    Если нет ни одной строки с «—», возвращает пустой список.
    """
    links: List[str] = []
    for line in search_result.splitlines():
        # Ожидаем, что каждая строка начинается с "- " и содержит " — "
        if line.strip().startswith("-") and "—" in line:
            parts = line.split("—")
            url = parts[-1].strip()
            # Если URL валидного вида (начинается с http), добавляем
            if url.startswith("http"):
                links.append(url)
    return links
