.PHONY: clean venv play net py

clean_venv:
	rm -fr venv

venv:
	virtualenv -p python3 venv
	source venv/bin/activate

build:
	pip install -r requirements.txt

play: 
	./venv/bin/python3 tic_tac_toe/play.py

net: 
	./venv/bin/python3 tic_tac_toe/neural_net.py

py:
	./venv/bin/python3

