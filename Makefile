install: install_python install_project

install_python:
	pyenv install 3.10.5 --skip-existing
	pyenv local 3.10.5

install_project:
	poetry env use 3.10.5
	poetry install

update:
	poetry update