from sklearn.preprocessing import StandardScaler
import pandas as pd

# Загружаем данные
train_data = pd.read_csv('data/train/train_data.csv')

# Предобработка данных
scaler = StandardScaler()
train_data['scaled_temperature'] = scaler.fit_transform(train_data[['temperature']])

# Сохраняем обработанные данные
train_data.to_csv('data/train/scaled_train_data.csv', index=False)
