Tekhnical project for Inforce
to use this project you need 
1) docker must be installed - https://www.docker.com/;
2) clone thisa git repo and run docker-compose up from folder with this file;
3) to check all api endpoints use short postman collection :
https://go.postman.co/workspace/new~ec0dc50a-9b82-45ea-a322-3c8a2cf3c898/collection/14225093-e998ce1c-88d6-4d17-80a7-a021e86304a7?action=share&creator=14225093;
4) also you can check base endpoints at http://localhost:8000/api/ after running app;
5) all endpoints are locked and needed token so fist of all create user with 'http://127.0.0.1:8000/api/register/' ;
6) after sing in with 'http://127.0.0.1:8000/api/auth/', take your token to use else endpoints in drf-view or like api;
