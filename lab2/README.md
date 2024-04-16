Предполагается, что запуск jenskins будет из Docker

### Сборка Docker образа
docker build -t jenkins-ml .

### Запуск Jenkins в Docker контейнере
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins-ml
