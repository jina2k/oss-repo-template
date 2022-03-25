## Example 00
![image](https://user-images.githubusercontent.com/66571652/160159355-6eb30118-ae77-4832-9638-f1046d61a50c.png)

Testing installation with Docker, works well when testing with a remote sample container.

## Example 01
![image](https://user-images.githubusercontent.com/66571652/160160824-51e5b3e1-6d60-477a-8272-c095d2c29e56.png) </br>
Testing vim in Ubuntu which is hosted by a docker container, created a test file.

![image](https://user-images.githubusercontent.com/66571652/160161228-b4fabfa4-816c-4fbd-965d-2710c2814568.png) </br>
Testing cowsay in same bash terminal, cowsay "moo!" prints properly.

## Example 02
![image](https://user-images.githubusercontent.com/66571652/160162067-7eb13b5a-dbc6-4128-be76-a895b998b04b.png) </br>
Downloaded mongo:3.2 and rocket.chat:0.62, can be shown using docker ps.

![image](https://user-images.githubusercontent.com/66571652/160162224-6799325c-a012-42bc-822e-bf7dcfa22ebc.png) </br>
Here we see RocketChat running in localhost.

![image](https://user-images.githubusercontent.com/66571652/160162807-7a46201a-8794-46c0-ba47-a07a336b62e4.png) </br>
Removed containers for rocket chat and mongo, and removed images for both of them using:
```
docker stop <container-name>
docker rm <container-name>
docker rmi <images-id>
```

## Example 03
![image](https://user-images.githubusercontent.com/66571652/160170623-1465f2f7-ec3b-4d33-aa4e-3e5b00efe227.png)
Edited [Dockerfile](https://github.com/jina2k/oss-repo-template/blob/master/labs/lab-09/Dockerfile) to use python3 instead, ran a Flask app that uses the provided hello.py, hosting it on localhost:5000.

## Example 04
