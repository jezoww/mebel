mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser


udb:
	rm -rf db.sqlite3
	rm -rf mebel/migrations/*
	touch mebel/migrations/__init__.py
	python3 manage.py makemigrations
	python3 manage.py migrate

celery:
	celery -A root worker --loglevel=info


