import pandas as pd
from catboost.datasets import titanic

def main():
    # Загрузка датасета
    train, _ = titanic()

    # Сохранение интересующих столбцов
    train = train[['Pclass', 'Sex', 'Age']]
    train.to_csv('titanic_v1.csv', index=False)

    # Заполнение пропущенных значений возраста средним значением
    train['Age'].fillna(train['Age'].mean(), inplace=True)
    train.to_csv('titanic_v2.csv', index=False)

    # Добавление one-hot-encoding для признака "Sex"
    train = pd.get_dummies(train, columns=['Sex'])
    train.to_csv('titanic_v3.csv', index=False)

if __name__ == "__main__":
    main()
