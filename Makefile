# Makefile for managing the project
.PHONY: 
	install run clean lint test

# Define the target to install dependencies
install:`
	poetry install --no-root
	poetry lock
	poetry env activate

# Define the target to run the project
run:
<<<<<<< HEAD
<<<<<<< HEAD
	poetry run python src/main.py
=======
	poetry run python src/main_cluster.py
>>>>>>> 19ac1c0b568b3fbe961d1a7d9904b8272c460efc
=======
	poetry run python src/main_ts.py
>>>>>>> parent of 170f1f0 (added framework)

# Define the target to clean the build directory
clean:
	rmdir /s /q .venv
	rmdir /s /q build
	rmdir /s /q dist
	rmdir /s /q *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} \+

# Define the target to lint the code
lint:
	poetry run flake8 .

# Define the target to test the code
test:
	poetry run pytest