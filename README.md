export FLASK_APP=app.py
export FLASK_RUN_PORT=5555
flask db init
flask db revision --autogenerate -m "test"
flask db upgrade head
pipenv install && pipenv shell
python app.py (to start flask server)