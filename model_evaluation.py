from sklearn.metrics import accuracy_score, classification_report
import joblib

def evaluate_model():
    # Загрузка данных и модели
    X_test = joblib.load('X_test.joblib')
    y_test = joblib.load('y_test.joblib')
    model = joblib.load('model.pkl')
    
    # Предсказание и оценка
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    # Сохранение метрик
    with open('metrics.txt', 'w') as f:
        f.write(f"Accuracy: {accuracy:.4f}\n\nClassification Report:\n{report}")
    
    print("Оценка модели завершена!")

if __name__ == "__main__":
    evaluate_model()