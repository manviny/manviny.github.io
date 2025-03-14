[![Tutorial for beginners ](https://img.youtube.com/vi/b0HMimUb4f0/0.jpg)](
https://www.youtube.com/watch?v=b0HMimUb4f0)

- **docker:**
	- ultralytics, yolo, python 10
	- puppeteer
	- django
	- XMPP

### COMMANDS
- docker ps -a
- docker run -p 5000:80 -d nginx:1.27.0-bookworm


#### small images
- docker pull python:3.12-slim			# debian 100 mg
- docker pull python:3.12-alpine		# 


#### ejecutar comandos interactivos
- docker run -d nginx
- docker exec -it 13ecad89cd4a6db7a1e339db7eb1b0c3c078e1ac393f710cc6db400df150737a /bin/bash

#### Volumes


#### Dockerfile build & run
- docker build -t mysite .
- docker run -p 80:80 -t mysite
