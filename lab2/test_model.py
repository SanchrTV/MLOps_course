import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error

# Загрузка модели
model = joblib.load('model/model.joblib')

# Загрузка тестовых данных
data = pd.read_csv('data/test/test.csv')
X_test = data[['Pclass', 'Sex', 'SibSp', 'Parch', 'Fare']]
y_test = data['Age']

# Предсказание
predictions = model.predict(X_test)

# Расчет MSE
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
