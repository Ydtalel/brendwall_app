IMAGE_NAME = my-django-app
CONTAINER_NAME = my-container
PORT = 8000

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -d -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

migrate:
	docker exec -it $(CONTAINER_NAME) python manage.py makemigrations products
	docker exec -it $(CONTAINER_NAME) python manage.py migrate

stop:
	docker stop $(CONTAINER_NAME)
