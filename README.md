# Docker-compose-build-basic-a-calculator
In this project, we will build a mini calculator app using Docker Compose. To Dockerize an application, you need four files:
1. Dockerfile 
2. app.py
3. requirements.txt
4. docker-compose.yml
   
![Untitled](https://github.com/mcagriaktas/Docker-compose-basic/assets/52080028/f1564414-24a4-4cec-8dc8-3b1494b93ebe)

   1. Dockerfile: The Dockerfile is a text file that defines the steps to create a Docker image. It specifies the base image, sets the working directory, defines environment variables, copies files, installs dependencies, 
      exposes ports, and sets the command to run the application.
      Dockerfile's steps:
      
      ---------------------------------------------------
         1. FROM python:3.9 << This line sets the base image for your Docker image. It specifies that you want to start with a base image that has Python 3.9 installed. This base image will provide the runtime environment                                for your application.

         2. WORKDIR /code   << This line sets the working directory inside the container to /code. Any subsequent instructions will be executed in this directory. It is a best practice to set the working directory to an                                  appropriate location for your application code.
         
         3. ENV FLASK_APP app.py << This line sets an environment variable named FLASK_APP to the value app.py. This environment variable is used by the Flask framework to identify the main application file.
         
         4. ENV FLASK_RUN_HOST 0.0.0.0 << This line sets the FLASK_RUN_HOST environment variable to 0.0.0.0, which means that the Flask development server should bind to all network interfaces in the container. This allows                                          the server to accept connections from outside the container.
         
         5. COPY requirements.txt requirements.txt << This line copies the requirements.txt file from your local directory to the /code directory inside the container. This file typically lists the Python dependencies                                                           required by your application.
         
         6. RUN pip install --upgrade pip && pip install -r requirements.txt << This line runs the pip command inside the container to install the necessary Python packages. It upgrades pip itself and then installs the                                                                                    packages listed in the requirements.txt file.
         
         7. EXPOSE 5000 << This line specifies that the container will listen on port 5000. Please be carrefuly this because if you using 5000 port, you can't build clearly Dockerfile.
         
         8. COPY . . << This line copies all the files and directories from your local directory to the current directory (/code) inside the container. It includes your Flask application code and any other necessary files.
      
         9. CMD ["flask", "run"] << This line specifies the command that will be executed when the container starts. It runs the flask run command, which starts the Flask development server to run your application.
   
   2. app.py: This file contains the code for the calculator application. It is a typical application file.
       
   3. requirements.txt: The requirements.txt file lists the Python dependencies required by the application. It specifies the packages that need to be installed for the application to run properly.
   4. docker-compose.yml: The docker-compose.yml file is used to define and configure the Docker services. It specifies how the Docker containers should be built and run. It includes information about the Docker image, 
      ports to expose, and any additional configuration.
  
      When we run "docker-compose build", the instructions in the Dockerfile are executed to build the Docker image.
      
      ![docker-compose-build](https://github.com/mcagriaktas/Docker-compose-basic/assets/52080028/a9994e6e-82bd-48dd-9bc8-c269799b47f8)

      If everything is set up correctly, we can start the containers using "docker-compose up". To run the 
      containers in the background, we can use "docker-compose up -d" where the "-d" flag means to run in detached mode.
      
      ![image](https://github.com/mcagriaktas/Docker-compose-basic/assets/52080028/ac7267ec-2d8c-4370-b026-6e73b837f72c)

      So you can start the app in any browser " localhost:5000 "
      
      ![appin](https://github.com/mcagriaktas/Docker-compose-basic/assets/52080028/a7f2d6cd-6d9b-4f6e-bb4b-e24d1bdecdd6)

      ![appinn2](https://github.com/mcagriaktas/Docker-compose-basic/assets/52080028/58fcec22-3294-4a27-b313-6d6355333ba0)


PS: I'll soon add the calculation history to the application. "Redis" exists in the application because of that!

      

      



