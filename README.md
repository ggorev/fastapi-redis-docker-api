## Установка

- Клонируйте репозиторий
- Установите pdm `pip install pdm`
- Установите зависимости `pdm install`
- В папке docker создайте `.env` файл на основе `example.env`

## Использование

Для запуска web API через docker перейдите в папку docker:
```bash
cd docker
```
и выполните команды:
```bash
docker compose -f docker-compose.yaml build 
```
```bash
docker compose -f docker-compose.yaml up 
```
Перейдите по адресу:
`http://localhost:8000/docs`

Для запуска web API локально, введите команду:

```bash
uvicorn src.app.web.api.app:app
```
так же необходимо будет поднять redis.

Перейдите по адресу:
`http://localhost:8000/docs`

