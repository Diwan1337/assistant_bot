# Multi-Agent LLM Assistant Bot
## [Мультиагентный LLM-ассистент через Telegram](https://github.com/Diwan1337/assistant_bot/blob/main/Архитектура_системы_Резинкин_Дмитрий_Владимирович.pdf)

---
> ⚡ **Status:** In Development  
> ⚡ **Статус:** В разработке

---

## 1. Introduction / Введение  

**English:**  
This repository implements a modular, multi-agent assistant that processes user queries in several stages—planning, query refinement, information retrieval, quality evaluation, and summarization—leveraging Google Gemini (LLM) and the Google Custom Search API. The final interface is a Telegram bot delivering concise, human-readable answers.

**Русский:**  
Этот репозиторий реализует модульного, мультиагентного ассистента, который обрабатывает пользовательские запросы в несколько этапов: планирование, уточнение запроса, поиск информации, оценка качества и суммаризация. Для этого используются Google Gemini (LLM) и Google Custom Search API. Итоговый интерфейс — Telegram-бот, который выдаёт краткие, понятные человеку ответы.

---

## 2. Architecture Overview / Обзор архитектуры  

1. **Manager Agent (Coordinator)**  
   - **EN:** Orchestrates the workflow: calls Planner → Refiner → Search → Evaluator → Summarizer → returns final answer.  
   - **RU:** Оркестрирует весь поток: вызывает Планировщика → Уточнитель → Поисковика → Оценщика → Сумматор → возвращает итоговый ответ.

2. **Planner Agent**  
   - **EN:** Splits the user’s raw query into a JSON array of logical “tasks”/steps via Google Gemini.  
   - **RU:** Разбивает исходный запрос пользователя на JSON-массив логических «задач»/шагов через Google Gemini.

3. **Query Refinement Agent**  
   - **EN:** Takes a single “task” and reforms it into a precise search query.  
   - **RU:** Берёт каждый «шаг» и переформулирует его в точный поисковый запрос.

4. **Retrieval Agent**  
   - **EN:** Uses Google Custom Search API to retrieve a small set of relevant links/snippets for each refined query.  
   - **RU:** Использует Google Custom Search API для получения набора релевантных ссылок/сниппетов по каждому уточнённому запросу.

5. **Evaluation Agent**  
   - **EN:** Compares previous vs. current search results; if no new links appear, halts further refinements.  
   - **RU:** Сравнивает предыдущие и текущие результаты поиска; если новых ссылок нет, прекращает дальнейшее уточнение.

6. **Summarization Agent**  
   - **EN:** Aggregates all steps, refined queries, and retrieved links into a single prompt to Google Gemini, producing a coherent answer.  
   - **RU:** Собирает все шаги, уточнённые запросы и найденные ссылки в один промпт для Google Gemini, формируя связный ответ.

7. **User Interface Agent (Telegram Bot)**  
   - **EN:** Receives user messages, calls the Manager, and sends back the final reply.  
   - **RU:** Принимает сообщения от пользователя, вызывает Менеджера и отправляет обратно итоговый ответ.

---

## 3. Current Progress / Текущий прогресс  

| Component                       | Status      | Details / Детали                                      |
|---------------------------------|-------------|-------------------------------------------------------|
| Manager Agent                   | ✅ Complete  | `core/orchestrator.py` orchestrates the full pipeline. |
| Planner Agent                   | ✅ Complete  | `agents/planner.py` returns a JSON list of tasks.      |
| Query Refinement Agent          | ✅ Complete  | `agents/refinement.py` refines each “task” to a query. |
| Retrieval Agent (Google CSE)    | ✅ Complete  | `agents/search.py` fetches top 3–5 links via CSE.       |
| Evaluation Agent                | ✅ Complete  | `agents/evaluation.py` checks for new links per step.  |
| Summarization Agent             | ✅ Complete  | `agents/summarization.py` synthesizes final answer.    |
| Telegram UI Agent               | ✅ Complete  | `bot/telegram_handler.py` handles incoming/outgoing.   |
| **Parallel Retrieval Agents**   | ❌ Pending   | Additional sources (arXiv, PubMed, Wiki, etc.).        |
| **Verifier Agent (Fact-Check)** | ❌ Pending   | LLM-based verification of summary accuracy.           |
| **Caching / Knowledge Base**    | ❌ Pending   | SQLite/Redis cache for repeated queries.               |
| **User Feedback Mechanism**     | ❌ Pending   | Inline buttons (“Helpful/Not helpful”) and metrics.    |
| **Ontology Integration**        | ❌ Pending   | WordNet/DBpedia/Wikidata for better query refinements. |

---

## 4. Roadmap / План развития  

### Phase 1: Core Pipeline (Completed)  
- **EN:**  
  - Implement Manager orchestrator (Planner → Refiner → Search → Evaluator → Summarizer).  
  - Set up Google Gemini (LLM) and Google Custom Search integration.  
  - Build Telegram bot interface for user interaction.  
- **RU:**  
  - Реализован Менеджер (Оркестратор) последовательности (Планировщик → Уточнитель → Поисковик → Оценщик → Сумматор).  
  - Настроена интеграция с Google Gemini (LLM) и Google Custom Search.  
  - Создан Telegram-бот для взаимодействия с пользователями.

### Phase 2: Expand Retrieval Sources  
- **EN:**  
  - Add additional Retrieval Agents: arXiv API, PubMed E-utilities, Wikipedia API, Stack Exchange API, etc.  
  - Implement parallel fetching and merging of results from multiple sources.  
- **RU:**  
  - Добавить дополнительные агенты поиска: arXiv, PubMed, Wikipedia, Stack Exchange и др.  
  - Реализовать параллельную (асинхронную) выборку и объединение результатов из разных источников.

### Phase 3: Verification & QA Agent  
- **EN:**  
  - Develop a Verifier Agent that reviews the Summarizer’s output for factual consistency using LLM checks.  
  - Track and log summary accuracy metrics (e.g., factual correctness, hallucination rate).  
- **RU:**  
  - Реализовать «Агента-верификатора», который проверяет сводку на корректность фактов через LLM.  
  - Вести логи и метрики точности («фактопоиск», уровень выдумок).

### Phase 4: Caching & Knowledge Base  
- **EN:**  
  - Introduce a caching layer (SQLite or Redis) to store previously executed refined queries and search results.  
  - Build a mini knowledge base or ontology (WordNet/DBpedia/Wikidata) to support smarter refinements.  
- **RU:**  
  - Добавить кэширование (SQLite или Redis) для хранения ранее выполненных уточнённых запросов и результатов поиска.  
  - Построить собственную базу знаний или онтологию (WordNet/DBpedia/Wikidata) для более продвинутого уточнения запросов.

### Phase 5: User Feedback & Iterative Improvement  
- **EN:**  
  - Embed “Helpful / Not helpful” buttons in Telegram responses to collect user feedback.  
  - Use feedback to adjust future query refinements and summarization quality.  
  - Display basic analytics dashboard for user satisfaction and system performance.  
- **RU:**  
  - Включить в ответы Telegram-бота кнопки «Полезно / Не полезно» для сбора обратной связи.  
  - На основе фидбэка корректировать будущие уточнения запросов и качество суммаризации.  
  - Отображать простую аналитику удовлетворённости пользователей и производительности системы.

---

## 5. Installation / Установка  

1. **Clone the repository / Клонирование репозитория**  
   ```bash
   git clone https://github.com/yourusername/multiagent-llm-bot.git  
   cd multiagent-llm-bot

2. **Create & activate a virtual environment / Создание виртуального окружения**

    ```
    python3 -m venv .venv 
    ```
    ```
    source .venv/bin/activate      # Linux/macOS  
    .venv\Scripts\activate         # Windows (PowerShell)
    ```
3. **Copy .env and fill in your keys / Скопировать .env и заполнить ключи**
    ````
    GEMINI_API_KEY=AIzaSyYourGeminiKey...
    GOOGLE_SEARCH_API_KEY=AIzaSyYourSearchKey...
    GOOGLE_SEARCH_CX=0123456789:abcdefghij
    TELEGRAM_BOT_TOKEN=123456789:ABCDefGhIjK
    ````
4. **Install dependencies / Установка зависимостей**
    ````
    pip install -r requirements.txt
    ````
## 6. Usage / Использование
1. **Run the bot / Запуск бота**
    ````
    python main.py
    ````
   `EN: The console should print: Bot started. Waiting for messages…`\
   `RU: В консоли появится: Бот запущен. Ожидание сообщений…`

2. **Open Telegram & chat with the bot / Откройте Telegram и напишите боту**\
3. **Receive the final answer / Получите окончательный ответ**

## 7. Contributing / Сотрудничество
**EN:**
I welcome contributions! Steps to contribute:
1) Fork this repository
2) Create a new feature branch (```git checkout -b feature/YourFeature```)
3) Implement your changes, commit and push to your fork
4) Open a Pull Request with a clear description of what you implemented or fixed

**RU:**
Я рад вкладчикам! Шаги для участия:
1) Форкните этот репозиторий
2) Создайте новую ветку для фичи (git checkout -b feature/YourFeature)
3) Реализуйте изменения, закоммитьте и запушьте в свой форк
4) Откройте Pull Request с подробным описанием того, что вы сделали или исправили

## 8. License / Лицензия
**MIT License** © 2025 Diwan1337\
See LICENSE for details.\
MIT Лицензия © 2025 Diwan1337\
См. LICENSE для подробностей.


<details>
<summary>🔍 Localization Notes / Заметки по русификации</summary>

- Каждый раздел содержит сначала **английскую версию**, затем **русскую**.  
- Все ключевые термины (Planner, Refiner, Evaluator, Summarizer) оставлены на английском для ясности, с пояснениями на русском.  
- «Status», «Roadmap», «Installation», «Usage», «Contributing», «License» оформлены двуязычно.  
- В таблице прогресса указаны метки `✅`/`❌` и краткие комментарии на английском и русском.  
- Примеры команд `bash` и `.env` одинаковы для обеих локалей, с пояснением, как заполнять.  

</details>
