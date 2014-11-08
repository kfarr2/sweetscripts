.PHONY: run clean

# run the traaaaap
run:
	./manage.py runserver 0.0.0.0:8000

# remove that .pyc garbage
clean:
	find -iname "*.pyc" -delete
	find -iname "__pycache__" -delete
