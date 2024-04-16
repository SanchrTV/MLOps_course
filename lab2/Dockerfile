# Dockerfile
FROM jenkins/jenkins:lts
USER root

# Установка Python и необходимых библиотек
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    python3 -m pip install --upgrade pip && \
    pip3 install numpy pandas scikit-learn joblib

# Переключение обратно на пользователя jenkins
USER jenkins
