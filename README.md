# Тестовое задание на практику в [название компании удалено] на Python-разработчика

[Тестовое задание](terms_of_reference/description.txt)

## Установка

```bash
git clone https://github.com/VL1507/python_dev_mashyanov_vladimir.git
cd python_dev_mashyanov_vladimir
pip install uv
uv sync
```

## Запуск

```bash
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

или

```bash
make runapp
```

## Изменения (нестыковки/несоответствия)

### Нет связи между комментариаем и постом

Нет связи между комментарием и постом, поэтому нельзя получить количество оставленных пользователем комментариев под постом для comments датасета

## Другие комментарии

- хотел использовать репозитории, но не придумал как
- UnitOfWork не используется, т.к. нет репозиториев
- тестов в папке tests нет
