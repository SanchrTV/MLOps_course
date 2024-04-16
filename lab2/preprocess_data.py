import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Загрузка данных
df = pd.read_csv('data/raw/titanic.csv')

# Очистка данных и импутация отсутствующих значений для Age
imputer = SimpleImputer(strategy='mean')
df['Age'] = imputer.fit_transform(df[['Age']])

# Кодирование категориальных переменных
df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})

# Выбираем релевантные колонки
features = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Fare']
X = df[features]
y = df['Age']

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Сохранение данных
X_train.join(y_train).to_csv('data/train/train.csv', index=False)
X_test.join(y_test).to_csv('data/test/test.csv', index=False)
