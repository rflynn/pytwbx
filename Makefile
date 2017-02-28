# vim: set ts=8 noet:

test:
	ext 1

venv: requirements.txt
	virtualenv -p python3.5 venv
	venv/bin/pip install -r requirements.txt
