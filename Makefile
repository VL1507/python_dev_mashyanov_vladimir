# app
runapp:
	uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

format:
	uv run ruff format .

testapp:
	uv run pytest


# docker
run:
	docker run -it -d --env-file ./app/.env --restart=unless-stopped --name backend_docker

stop:
	docker stop backend_docker

attach:
	docker attach backend_docker

dell:
	docker rm backend_docker

alldocker:
	docker ps -a