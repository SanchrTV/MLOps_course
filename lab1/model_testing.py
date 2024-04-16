import pandas as pd
from sklearn.metrics import mean_squared_error
import joblib

# Загружаем модель
model = joblib.load('model.joblib')

# Загружаем тестовые данные
test_data = pd.read_csv('data/test/test_data.csv')

# Прогнозирование
predictions = model.predict(test_data[['day']])

# Оцениваем модель
mse = mean_squared_error(test_data['temperature'], predictions)
print(f'Mean Squared Error: {mse}')
