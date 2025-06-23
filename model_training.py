from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    # Загрузка данных
    X_train = joblib.load('X_train.joblib')
    y_train = joblib.load('y_train.joblib')
    
    # Обучение модели
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Сохранение модели
    joblib.dump(model, 'model.pkl')
    print("Модель успешно обучена и сохранена!")

if __name__ == "__main__":
    train_model()