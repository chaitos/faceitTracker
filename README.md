# Faceit Tracker

Простой и удобный трекер игроков Faceit с возможностью добавления, удаления и отслеживания статистики.

---

## 🔹 Технологии

**Бэкенд:**  
- FastAPI  
- SQLAlchemy / PostgreSQL  
- Pydantic для валидации данных  
- Alembic для миграций базы данных  

**Фронтенд:**  
- React  
- Tailwind CSS  
- Axios для API-запросов  

---

## 🔹 Функционал

- Добавление игроков по Faceit ID  
- Просмотр списка отслеживаемых игроков  
- Удаление игроков из трекера  
- Просмотр детальной информации об игроке (статистика, рейтинги)  
- Адаптивный и простой интерфейс  

---

## 🔹 Установка

### Бэкенд

Клонируем репозиторий:
git clone https://github.com/yourusername/faceit-tracker.git
cd faceit-tracker/backend

Устанавливаем зависимости:
pip install -r requirements.txt

Настраиваем переменные окружения в файле .env:
DATABASE_URL=postgresql://user:password@localhost:5432/faceit_db
FACEIT_API_KEY=your_faceit_api_key

Применяем миграции:
alembic upgrade head

Запускаем сервер:
uvicorn main:app --reload
Фронтенд

Переходим в папку фронтенда:
cd ../frontend

Устанавливаем зависимости:
npm install

Запускаем приложение:
npm start

Открываем в браузере:
http://localhost:5174/






