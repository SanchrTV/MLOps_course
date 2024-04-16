import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Загрузка обучающих данных
data = pd.read_csv('data/train/train.csv')
X_train = data[['Pclass', 'Sex', 'SibSp', 'Parch', 'Fare']]
y_train = data['Age']

# Создание и обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Сохранение модели
joblib.dump(model, 'model/model.joblib')
