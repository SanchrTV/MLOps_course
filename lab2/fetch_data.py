import os

# URL для скачивания датасета Титаник из репозитория на GitHub
data_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Путь к сохранению данных
data_path = "data/raw/titanic.csv"

# Создаем директорию если она не существует
os.makedirs(os.path.dirname(data_path), exist_ok=True)

# Скачивание данных
os.system(f"wget -O {data_path} {data_url}")
