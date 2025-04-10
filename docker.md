[![Tutorial for beginners ](https://img.youtube.com/vi/b0HMimUb4f0/0.jpg)](
https://www.youtube.com/watch?v=b0HMimUb4f0)


- **docker:**
	- ultralytics, yolo, python 10
	- puppeteer
	- django
	- XMPP

### Utiles
- docker-compose up -d --build	# cuando tocamos Dockerfile o docker-compose
- docker-compose restart		# cuando solo tocamos codigo



### BASIC COMMANDS
- docker run hello-world
- docker pull hello-world

- docker image ls 				# muestra imagenes
- docker ps -a 					# muestra containers

- docker run -p 5000:80 -d --name my-nginx nginx:1.27.0-bookworm		
	- -d 						# detach
	- -p 						# puerto
	- -v mydata:/docker_path	# crea Volumen y copia ./mydata -> /docker_path				
	- --name					# nombre
	- --rm						# borrar contenedor despues de su uso
	- -e ABC=123				# variables de environment

	- nginx:1.27				# si sale version 1.27.1 se actualiza y quizas no queremos esto
	- nginx:1.27.0-bookworm		# nombre especifico, dificil que cambie
	- nginx@sha256:6af79ae5...  #DIGEST no cambia nunca



#### small images
- docker pull python:3.12  				# 1.02 GB (debian)
- docker pull python:3.12-slim			# 133 MB (reduced debian)
- docker pull python:3.12-alpine		# 55 MB (alpine linux), no tiene bash

#### DEBUG container
- docker exec -it 13ecad... /bin/bash	# terminal interactivo del docker


#### Volumes
- 

#### Dockerfile build & run
- docker build -t mysite .
- docker run -p 80:80 -t mysite


#### Docker Compose
- docker compose run			# crea los contenedores
- docker compose start			# arranca los contenedores
- docker compose stop			# para los contenedores
- docker compose up
- docker compose down			# borra los contenedores


