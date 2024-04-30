## Установка и запуск

### Предварительные требования
Убедитесь, что на вашей машине установлен Docker.

### Сборка и запуск Docker контейнера

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SanchrTV/MLOps_course.git
   cd MLOps_course/lab3
   ```
2. Соберите Docker образ:
   ```bash
   docker build -t iris-classifier .
   ```
3. Запустите контейнер:
   ```bash
   docker run -p 5000:5000 iris-classifier
   ```

После выполнения этих шагов, сервис будет доступен по адресу http://localhost:5000/.

## Использование

Для получения предсказаний отправьте POST запрос на /predict с JSON содержащим признаки ириса. Пример использования с помощью curl:
```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

Вы получите ответ в формате JSON, например:
```json
{"prediction": 0}
```
