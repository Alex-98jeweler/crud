
configure:
	. ./setenv.sh
	python3 -m venv env
	. ./env/bin/activate
	pip install -r requirements.txt

migrations:
	./manage.py makemigrations crud
	./manage.py migrate

run:
	./manage.py runserver




