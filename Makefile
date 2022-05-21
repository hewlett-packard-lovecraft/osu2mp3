init:
	pip install -r requirements.txt

test:
	python -m unittest tests/test_osu2mp3.py

.PHONY: init test
