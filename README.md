# Тестовое задание на стажировку/практику в farpost на python

## Установка

```bash
git clone https://github.com/VL1507/python_dev_mashyanov_vladimir.git
pip install uv
uv sync
```

## Запуск

`uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`

или

`make runapp`

## Изменения (нестыковки/несоответствия)

### Нет связи между комментариаем и постом

#### Нет связи между комментарием и постом, поэтому нельзя получить количество оставленных пользователем комментариев под постом для comments датасета
