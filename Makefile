init:
	pip install -r requirements.txt
build_assets:
	grunt coffee
	grunt less
run:
	nodemon --exec python main.py
