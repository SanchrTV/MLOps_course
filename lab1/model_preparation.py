import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Загружаем предобработанные данные
train_data = pd.read_csv('data/train/scaled_train_data.csv')

# Обучаем модель
model = LinearRegression()
model.fit(train_data[['day']], train_data['scaled_temperature'])

# Сохраняем модель
joblib.dump(model, 'model.joblib')
