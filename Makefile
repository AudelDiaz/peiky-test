migrate:
	docker-compose exec app ./manage.py makemigrations
	docker-compose exec app ./manage.py migrate
requirements:
	docker-compose exec app pip install -r requirements.txt
statics:
	docker-compose exec app ./manage.py collectstatic --no-input
superuser:
	docker-compose exec app ./manage.py createsuperuser
loaddata:
	docker-compose exec app ./manage.py loaddata ubicaciones
	docker-compose exec app ./manage.py loaddata initial
	docker-compose exec app ./manage.py loaddata auth
clean:
	rm -rf src/*/migrations/00**.py
	find . -name "*.pyc" -exec rm -- {} +
	rm -rf src/*/migrations/__pycache__/*
reset:
	docker-compose down -v
	sudo rm -rf .pgdata/
test:
	docker-compose exec app ./manage.py test
dump:
	docker-compose exec app ./manage.py dumpdata --format=json Auth > /usr/src/app/fixtures/initial_data_auth.json
load:
	docker-compose exec app ./manage.py loaddata fixtures/initial_data_auth.json
	docker-compose exec app ./manage.py loaddata fixtures/initial_data_vehiculos.json
