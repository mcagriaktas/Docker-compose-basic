# Docker-compose-basic
In this project, we'll build mini calculator app with docker-compose.
![Untitled](https://github.com/mcagriaktas/Docker-compose-basic/assets/52080028/f1564414-24a4-4cec-8dc8-3b1494b93ebe)
If you want to Dockerize a application you must need to 4 file like that:
1. Dockerfile 
2. app.py
3. requirements.txt
4. docker-compose.yml

   1. Dockerfile:
      Dockerfile name must be same Dockerfile. This file is meaning, "Image". Basicly, Dockerfile is runnig command line to line.
   2. app.py:
      app.py typly classic app file.
   3. requirements.txt:
      requirements file is typly, what's need to our app, so we're putting our requirements to in our requirements.txt
   4. docker-compose.yml:
      docker-compose.yml for build. We can start the app like "flask run -h 0.0.0.0" but A Docker image is a lightweight, standalone, and executable software package that includes everything needed to run a piece of       
      software, including the code, runtime, libraries, environment variables, and system tools. 
      ![docker-compose-build](https://github.com/mcagriaktas/Docker-compose-basic/assets/52080028/a9994e6e-82bd-48dd-9bc8-c269799b47f8)



