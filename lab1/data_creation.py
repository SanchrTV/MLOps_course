import numpy as np
import pandas as pd
import os

# Создаем каталоги, если они не существуют
os.makedirs('data/train', exist_ok=True)
os.makedirs('data/test', exist_ok=True)

# Генерируем данные
np.random.seed(0)
days = 365
data = {
    'day': range(days),
    'temperature': np.random.normal(loc=20, scale=5, size=days)  # Средняя температура 20, стандартное отклонение 5
}

# Добавляем шумы/аномалии
for _ in range(10):  # 10 аномальных дней
    idx = np.random.randint(days)
    data['temperature'][idx] += np.random.randint(15, 25)

df = pd.DataFrame(data)

# Разделяем данные на train и test
train = df.sample(frac=0.8, random_state=200)  # 80% данных на обучение
test = df.drop(train.index)

# Сохраняем данные
train.to_csv('data/train/train_data.csv', index=False)
test.to_csv('data/test/test_data.csv', index=False)
