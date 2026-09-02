# Faceit Tracker 

Трекер игроков Faceit: добавляешь ник или ссылку на профиль, а фоновый процесс раз в 10 секунд опрашивает Faceit API и обновляет статус игрока (в поиске, в матче, недавно играл, оффлайн).

## Возможности

- Добавление игрока по нику или ссылке на профиль Faceit
- Список отслеживаемых игроков с живым статусом
- Удаление игрока из трекера
- Фоновая асинхронная задача опрашивает Faceit API параллельно по всем игрокам (`asyncio.gather`)
- Лимит на количество одновременно отслеживаемых игроков

## Стек

**Backend:** FastAPI, SQLAlchemy, PostgreSQL, Pydantic, Alembic, httpx
**Frontend:** React, Vite, Tailwind CSS

## Установка и запуск

Нужен PostgreSQL, запущенный локально, и API-ключ Faceit ([faceit.com/developers](https://developers.faceit.com/)).

### Backend

```bash
git clone https://github.com/chaitos/faceitTracker.git
cd faceitTracker/backend

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

# создать .env на основе .env.example:
# DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/faceitTrackerDB
# FACEIT_API_KEY=ваш_ключ

alembic upgrade head
uvicorn main:app --reload
```

Backend поднимется на `http://localhost:8000`.

### Frontend

```bash
cd ../frontend
npm install
npm run dev
```

Frontend поднимется на `http://localhost:5173` (Vite проксирует запросы `/api` на бекенд).

## Возможные улучшения

- [ ] Тесты
- [ ] Docker Compose для БД + backend + frontend одной командой
- [ ] Детальная статистика по матчам, а не только текущий статус