install:
	pip install -r requirements.txt
test:
	pytest test_cases.py
build:
	docker build -t sample .
images:
	docker images
delete:

	docker rmi sample:latest
container:
	docker run -d -p 5000:5000 --name my_app_container sample 
stop:
	docker stop $(cont_id)
remove_cont:
	docker rm $(cont_id)