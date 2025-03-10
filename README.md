# Тестовое задание на практику в FarPost на Python-разработчика

[Тестовое задание](terms_of_reference/description.txt)

## Установка

```bash
git clone https://github.com/VL1507/python_dev_mashyanov_vladimir.git
cd python_dev_mashyanov_vladimir
pip install uv
uv sync
```

Создайте .env файл. Используйте .env.example как шаблон.

## Запуск

```bash
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

или

```bash
make runapp
```

## Изменения (нестыковки/несоответствия)

### Нет связи между комментариями и постом

#### Проблема

Нет связи между комментарием и постом, поэтому нельзя получить количество оставленных пользователем комментариев под постом для comments датасета

#### Решение

В db1 добавил таблицу comments c полями

- id: int
- user_id: int - внешние ключи с users.id
- post_id: int - внешние ключи с post.id
- text: varchar
- created_at: datetime
- updated_at: datetime - пусть можно редактировать комментарии

## Другие комментарии

- хотел использовать репозитории, но не придумал как
- UnitOfWork не используется, т.к. нет репозиториев
- тестов в папке tests нет
- специально загрузил .env, db1.sqlite3 и db2.sqlite3, чтобы было проще проверить работу
