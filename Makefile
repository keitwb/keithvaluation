tag := $(shell git describe --abbrev=0 --tags)

.PHONY: images
images:
	docker build -t keithvaluation/public-site:$(tag) -f docker/app/Dockerfile .
	docker build -t keithvaluation/reverse-proxy-http:$(tag) --build-arg PROTOCOL=http docker/nginx
	docker build -t keithvaluation/reverse-proxy-https:$(tag) --build-arg PROTOCOL=https docker/nginx

.PHONY: push-images
push-images:
	docker push keithvaluation/public-site:$(tag)
	docker push keithvaluation/reverse-proxy-http:$(tag)
	docker push keithvaluation/reverse-proxy-https:$(tag)

.PHONY: run-app-dev
run-app-dev:
	./dc exec app ./manage.py runserver 0.0.0.0:8000

.PHONY: run-admin-dev
run-admin-dev:
	./dc exec admin ./manage.py runserver 0.0.0.0:8000
