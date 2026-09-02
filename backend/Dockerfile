# Stage 1: собираем фронтенд
FROM node:20-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: backend + собранный фронтенд как статика
FROM python:3.12-slim
WORKDIR /app/backend

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .
COPY --from=frontend-build /app/frontend/dist /app/frontend/dist

EXPOSE 8000

# Применяем миграции при каждом старте контейнера, затем запускаем сервер
CMD alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000