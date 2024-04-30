from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

# Загрузка и подготовка данных
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Обучение модели логистической регрессии
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Сохранение модели для дальнейшего использования
pickle.dump(model, open("iris_model.pkl", "wb"))

# Загрузка модели
model = pickle.load(open("iris_model.pkl", "rb"))

# Определение API для получения предсказаний
@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_data = request.get_json(force=True)
        prediction = model.predict([json_data['features']])
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
